#!/usr/bin/env python3
""" Session auth module """

from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
from os import getenv
import json


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login() -> str:
    """ Login function
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if not email:
        return jsonify({"error": "email missing"}), 400
    if not password:
        return jsonify({"error": "password missing"}), 400

    try:
        users = User.search({'email': email})
    except Exception:
        return jsonify({"error": "no user found for this email"}), 404
    if len(users) == 0:
        return jsonify({"error": "no user found for this email"}), 404

    for user in users:
        if user.is_valid_password(password):
            from api.v1.app import auth

            sessionID = auth.create_session(user_id=user.id)
            response = jsonify(user.to_json())
            response.set_cookie(getenv('SESSION_NAME'), sessionID)
            return response
    return jsonify({"error": "wrong password"}), 401



@app_views.route('/auth_session/logout', methods=['DELETE'], strict_slashes=False)
def logout():
    """ Logout function """
    request = request
    if request is None:
        return False
    
    session_id = request.cookies.get(getenv('SESSION_NAME'))
    if not session_id:
        return False
    
    from api.v1.app import auth
    user_id = auth.user_id_for_session_id(session_id)
    if not user_id:
        return False
    
    auth.destroy_session(request)
    
    return jsonify({}), 200
