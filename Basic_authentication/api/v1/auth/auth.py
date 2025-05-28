#!/usr/bin/env python3
"""
Auth module
"""


from typing import List, TypeVar
from flask import request


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
        if path is None:
            return True

        if excluded_paths is None or not excluded_paths:
            return True


        if not path.endswith('/'):
            path += '/'

        for excluded_path in excluded_paths:
            if excluded_path == path:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """ Gets the authentication from the header
        Args:
            request

        Returns:
        - None
        """
        if request is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar("User"): # pyright: ignore
        """ Gets the current authenticated user
        Args:
            request

        Returns:
        - None
        """
        return None # pyright: ignore
