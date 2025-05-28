#!/usr/bin/env python3
"""
Auth module
"""

from typing import List, TypeVar
from flask import Request


class Auth:
    """
    Class to manage API authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Checks if authentication is required
        Args:
            request

        Returns:
        - False
        """
        if path in excluded_paths:
            return False
        return False


    def authorization_header(self, request: Request = None) -> str:
        """ Gets the authentication from the header
        Args:
            request

        Returns:
        - None
        """
        return None

    def current_user(self, request=None) -> TypeVar("User"): # pyright: ignore
        """ Gets the current authenticated user
        Args:
            request

        Returns:
        - None
        """
        return None # pyright: ignore
