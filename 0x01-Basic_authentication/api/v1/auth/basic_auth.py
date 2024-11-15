#!/usr/bin/env python3
"""a class BasicAuth that inherits from Auth"""
from api.v1.auth.auth import Auth
import base64
from typing import TypeVar
from models.base import Base
from models.user import User


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

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """Decodes a Base64 string to a UTF-8 string.

        Args:
            base64_authorization_header (str): The Base64 encoded
            authorization header.

        Returns:
            str: The decoded value as a UTF-8 string, or None if decoding
            fails.
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None

        try:
            # Decode the Base64 string
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode('utf-8')
        except (base64.binascii.Error, UnicodeDecodeError):
            # Catch decoding errors
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """Returns the user email and password from the Base64 decoded value.
        """

        if decoded_base64_authorization_header is None:
            return (None, None)
        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        if ":" not in decoded_base64_authorization_header:
            return (None, None)

        credentials = decoded_base64_authorization_header.partition()(":")

        return (credentials[0], credentials[2])

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """Returns the User instance based on his email and password."""

        if user_email is None or user_pwd is None:
            return None
        if not isinstance(user_pwd, str) or not isinstance(user_email, str):
            return None

        attr = {'email': user_email}
        user_list = User.search(attr)
        if len(user_list) == 0:
            return None

        print(user_list)
        for user in user_list:
            if user.is_valid_password(user_pwd):
                return user

        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Overloads Auth and retrieves the User instance for a request"""

        auth_head = self.authorization_header(request)
        base64_auth_head = self.extract_base64_authorization_header(auth_head)
        decoded_auth_head = self.decode_base64_authorization_header(
            base64_auth_head)
        user_credents = self.extract_user_credentials(decoded_auth_head)

        return self.user_object_from_credentials(
            user_credents[0], user_credents[1])
