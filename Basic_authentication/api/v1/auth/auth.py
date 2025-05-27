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
        """ Flask request object
        """
        return False

    def authorization_header(self, request: Request = None) -> str:
        """ Flask request objevt
        """
        return None

    def current_user(self, request: Request = None) -> User:
        """ Flask request object
        """
        return None
