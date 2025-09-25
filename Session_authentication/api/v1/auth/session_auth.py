#!/usr/bin/env python3
""" Session module """

from api.v1.auth.auth import Auth
import os
from flask import Flask, request
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
