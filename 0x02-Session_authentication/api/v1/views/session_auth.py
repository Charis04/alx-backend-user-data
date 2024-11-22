#!/usr/bin/env python3
""" Module of Session auth views
"""
from flask import jsonify, request
from api.v1.views import app_views
from models.user import User
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def session_auth_login():
    """View that handles all routes for the Session authentication.
    """

    email = request.form.get('email', '')
    if email == '':
        return jsonify({"error": "email missing"}), 400
    pwd = request.form.get('password', '')
    if pwd == '':
        return jsonify({"error": "password missing"}), 400

    attr = {'email': email}
    user_list = User.search(attr)
    if len(user_list) == 0:
        return jsonify({"error": "no user found for this email"}), 404

    for user in user_list:
        if user.is_valid_password(pwd):
            from api.v1.app import auth
            session_id = auth.create_session(user.id)
            resp = jsonify(user.to_json())
            cookie_name = getenv('SESSION_NAME')
            resp.set_cookie(cookie_name, session_id)

    return jsonify({"error": "wrong password"}), 401
