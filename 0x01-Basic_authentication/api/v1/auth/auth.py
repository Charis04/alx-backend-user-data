#!/usr/bin/env python3
"""Auth class for api"""
from flask import request
from typing import List, TypeVar


class Auth:
    """A class to manage the API authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Checks if a path requires authentication
        """
        if excluded_paths is None:
            return True

        for ex_path in excluded_paths:
            if ex_path[-1] == "*" and ex_path[:-1] in path:
                return False

        if path and path[-1] != '/':
            path += '/'

        if path in excluded_paths:
            return False

        return True

    def authorization_header(self, request=None) -> str:
        """Check if there's an authorisation header in the request"""

        if request is None:
            return None

        auth_header = request.headers.get('Authorization')
        if auth_header is None:
            return None

        return auth_header

    def current_user(self, request=None) -> TypeVar('User'):
        """Still don't know. Just writing what i'm told for now"""

        return None
