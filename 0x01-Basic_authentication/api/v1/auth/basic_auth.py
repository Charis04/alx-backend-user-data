#!/usr/bin/env python3
"""a class BasicAuth that inherits from Auth"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Implements basic auuthorisation."""

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """
        Returns the Base64 part of the Authorization header for a Basic
        Authentication
        """

        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None

        if authorization_header[:6] == 'Basic ':
            return authorization_header[6:]
        else:
            return None
