#!/usr/bin/env python3
"""
BasicAuth module
"""

from api.v1.auth.auth import Auth
from typing import List, TypeVar, Tuple
import base64
import binascii

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
