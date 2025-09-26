#!/usr/bin/env python3
"""
Module for session authentication views.
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def session_login() -> str:
    """
    POST /api/v1/auth_session/login
    Handles the session login for a user.
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
        users = []

    if not users:
        return jsonify({"error": "no user found for this email"}), 404

    for user in users:
        if user.is_valid_password(password):
            # Import auth here to avoid circular dependency
            from api.v1.app import auth
            session_id = auth.create_session(user.id)
            response = jsonify(user.to_json())
            session_name = getenv('SESSION_NAME')
            response.set_cookie(session_name, session_id)
            return response

    return jsonify({"error": "wrong password"}), 401

