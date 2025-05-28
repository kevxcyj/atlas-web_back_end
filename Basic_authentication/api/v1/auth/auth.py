#!/usr/bin/env python3
"""
Auth module
"""


from typing import List, TypeVar
from flask import Request

"""
Flask Request class.

This class represents an HTTP request. It contains attributes and methods
to interact with the incoming request data.
"""

class Auth:
    """
    Class to manage API authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Checks if authentication is required
        """
        return False

    def authorization_header(self, request: Request = None) -> str:
        """ Gets the authentication from the header
        """
        return None

    def current_user(self, request = None) -> TypeVar("User"):
        """ Gets the current authenticated user
        """
        return None
