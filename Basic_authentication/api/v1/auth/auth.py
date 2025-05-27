#!/usr/bin/env python3
"""
Auth module
"""


from typing import List, TypeVar
from flask import Request


class Auth:
    """
    Manage API authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Checks if authentication is required
        """
        return False

    def authorization_header(self, request: Request = None) -> str:
        """ Gets the authentication from the header
        """
        return None

    def current_user(self, request: Request = None) -> User:
        """ Gets the current authenticated user
        """
        return None
