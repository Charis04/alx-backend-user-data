#!/usr/bin/env python3
"""Auth class for api"""
from flask import request
from typing import List, TypeVar


class Auth:
    """A class to manage the API authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Requires auth
        Returns: False
        """
        if excluded_paths is None:
            return True

        if path[-1] != '/':
            path += '/'

        if path in excluded_paths:
            return False

        return True

    def authorization_header(self, request=None) -> str:
        """Don't know man"""

        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Still don't know. Just writing what i'm told for now"""

        return None
