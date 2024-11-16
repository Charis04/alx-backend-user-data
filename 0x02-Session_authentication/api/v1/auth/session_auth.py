#!/usr/bin/env python3
"""A class to handle session authentication"""
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """Handles Session Auth"""

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Creates a Session ID for a user_id"""

        if not user_id:
            return
        if type(user_id) != str:
            return

        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Rreturns a User ID based on a Session ID"""

        if not session_id or type(session_id) != str:
            return

        return self.user_id_by_session_id.get(session_id)
