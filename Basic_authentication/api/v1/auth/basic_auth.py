#!/usr/bin/env python3
"""
BasicAuth module
"""

from api.v1.auth.auth import Auth
from typing import List, TypeVar, Tuple
import base64
import binascii

User = TypeVar('User')

class BasicAuth(Auth):
    """
    BasicAuth authenication
    """

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """
        Extract the Base64 part of the Authorization header for Basic Authentication.
        """
        if authorization_header is None:
            return None
        
        if not isinstance(authorization_header, str):
            return None
        
        if not authorization_header.startswith("Basic "):
            return None
        
        return authorization_header.split(" ")[1]
    
    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        """
        Decode the Base64 string in the authorization header.
        """

        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            decoded_string = decoded_bytes.decode("utf-8")
        except (binascii.Error, UnicodeDecodeError):
            return
        
    def extract_user_credentials(self, decoded_base64_authorization_header: str) -> Tuple[str, str]:
        """
        Extract the user email and password from the decoded Base64 string.
        """
        if decoded_base64_authorization_header is None:
            return None, None
        
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        
        parts = decoded_base64_authorization_header.split(":")
        if len(parts) != 2:
            return None, None
        
        return parts[0], parts[1]
    
    def user_object_from_credentials(self, user_email: str, user_pwd: str) -> User:
        """
        Create a User instance based on email and password.
        """

        if not isinstance(user_email, str):
            return None
        
        if not isinstance(user_pwd, str):
            return None
        

        users = User.search(email=user_email)
        
        if not users:
            return None
        
        if not users[0].is_valid_password(user_pwd):
            return None
        
        return users[0]
    
    def current_user(self, request=None) -> User:
        """
        Get the current authenticated user based on the Authorization header.
        """

        if request is None:
            return None
        
        auth_header = self.authorization_header(request)
        if auth_header is None:
            return None
        
        base64_auth = self.extract_base64_authorization_header(auth_header)
        if base64_auth is None:
            return None
        
        decoded_auth = self.decode_base64_authorization_header(base64_auth)
        if decoded_auth is None:
            return None
        
        email, pwd = self.extract_user_credentials(decoded_auth)
        if email is None or pwd is None:
            return None
        
        return self.user_object_from_credentials(email, pwd)
