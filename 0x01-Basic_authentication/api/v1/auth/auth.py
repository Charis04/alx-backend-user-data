#!/usr/bin/env python3
"""Auth class for api"""
from flask import request


class Auth:
    """A class to manage the API authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Requires auth
        Returns: False
        """

        return False

    def authorization_header(self, request=None) -> str:
        """Don't know man"""

        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Still don't know. Just writing what i'm told for now"""

        return None
