#!/usr/bin/env python3
"""A class to handle session authentication"""
from api.v1.auth.auth import Auth
import uuid
from models.user import User
from flask import request


class SessionAuth(Auth):
    """Handles Session Auth"""

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Creates a Session ID for a user_id"""

        if not user_id:
            return
        if type(user_id) is not str:
            return

        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Rreturns a User ID based on a Session ID"""

        if not session_id or type(session_id) is not str:
            return

        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """Returns a User instance based on a cookie value"""

        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)

        return User.get(user_id)
