#!/usr/bin/env python3
""" Session auth module """

from flask import Blueprint, request, jsonify
from api.v1.views import app_views
from models.user import User


@app_views.route('/auth_session/login', methods=['POST'])
def login():
    """ POST /api/v1/auth_session/login
    Def login function 
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if not email:
        return jsonify({"error": "email missing"}), 400
    
    if not password:
        return jsonify({"error": "password missing"}), 400
    
    user = User.search(email=email)
    
    if not user:
        return jsonify({"error": "no user found for this email"}), 404
    
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401
    
    from api.v1.app import auth
    session_id = auth.create_session(user.id)
    
    response = jsonify(user.to_json())
    response.set_cookie('session', session_id, httponly=True)
    
    return response
