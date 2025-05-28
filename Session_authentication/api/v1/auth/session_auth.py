#!/usr/bin/env python3
""" Session module """

from api.v1.auth.auth import Auth
from api.v1.app import auth
from api.v1.app import app
import os
from flask import Flask, request, jsonify
import uuid
from models.user import User

class SessionAuth(Auth):
    """ Session auth module """
    
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ Create session function """
        if user_id is None or not isinstance(user_id, str):
            return None
        
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id
    
    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ User id function """
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)
    
    def __init__(self):
        """ initialization """
        self.session_name = os.environ.get('SESSION_NAME', '_my_session_id')

    def session_cookie(self, request=None):
        """ session cookie """
        if request is None:
            return None
        
        cookie_value = request.cookies.get(self.session_name)
        return cookie_value
    
    def current_user(self, request=None):
        """ current user """
        if request is None:
            return None
        
        session_id = request.cookies.get('_my_session_id')
        user_id = self.user_id_for_session_id(session_id)
        
        if user_id is None:
            return None
        
        try:
            return User.get(id=user_id)
        except Exception as e:
            print(f"Error fetching user: {e}")
            return None
        
    @app.route('/auth_session/login', methods=['POST'])
    def login():
        """ Get email and password from request """

        email = request.form.get('email')
        password = request.form.get('password')

        if not email or not password:
            return jsonify({"error": "missing parameter"}), 400

        user = User.search(email=email)
        if not user:
            return jsonify({"error": "no user found for this email"}), 404

        if not user.is_valid_password(password):
            return jsonify({"error": "wrong password"}), 401

        session_id = auth.create_session(user.id)

        response = jsonify(user.to_json())
        response.set_cookie(auth.session_name, session_id, path='/', httponly=True)

        return response
        

   