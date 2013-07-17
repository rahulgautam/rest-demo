"""
flask.ext.httpauth
==================

This module provides Basic and Digest HTTP authentication for Flask routes.

:copyright: (C) 2013 by Miguel Grinberg.
:license:   BSD, see LICENSE for more details.
"""

from functools import wraps
from hashlib import md5
from random import random
from flask import request, make_response

class HTTPAuth(object):
    def __init__(self):
        def default_get_password(username):
            return None
        def default_auth_error():
            return "Unauthorized Access"

        self.realm = "Authentication Required"
        self.get_password(default_get_password)
        self.error_handler(default_auth_error)
        self.username = None

    def get_password(self, f):
        self.get_password_callback = f

    def error_handler(self, f):
        @wraps(f)
        def decorated(*args, **kwargs):
            res = f(*args, **kwargs)
            if type(res) == str:
                res = make_response(res)
                res.status_code = 401
            if 'WWW-Authenticate' not in res.headers.keys():
                res.headers['WWW-Authenticate'] = self.authenticate_header()
            return res
        self.auth_error_callback = decorated
        return decorated

    def login_required(self, f):
        @wraps(f)
        def decorated(*args, **kwargs):
            self.username = None
            auth = request.authorization
            if not auth:
                return self.auth_error_callback()
            password = self.get_password_callback(auth.username)
            if not password:
                return self.auth_error_callback()
            if not self.authenticate(auth, password):
                return self.auth_error_callback()
            self.username = auth.username
            return f(*args, **kwargs)
        return decorated

class HTTPBasicAuth(HTTPAuth):
    def __init__(self):
        super(HTTPBasicAuth, self).__init__()
        self.hash_password(None)

    def hash_password(self, f):
        self.hash_password_callback = f

    def authenticate_header(self):
        return 'Basic realm="' + self.realm + '"'

    def authenticate(self, auth, password):
        client_password = auth.password
        if self.hash_password_callback:
            client_password = self.hash_password_callback(client_password)
        return client_password == password

class HTTPDigestAuth(HTTPAuth):
    def get_nonce(self):
        return md5(str(random())).hexdigest()
        
    def authenticate_header(self):
        return 'Digest realm="' + self.realm + '",nonce="' + self.get_nonce() + '",opaque="' + self.get_nonce() + '"'

    def authenticate(self, auth, password):
        if not auth.username or not auth.realm or not auth.uri or not auth.nonce or not auth.response:
            return False
        a1 = auth.username + ":" + auth.realm + ":" + password
        ha1 = md5(a1).hexdigest()
        a2 = request.method + ":" + auth.uri
        ha2 = md5(a2).hexdigest()
        a3 = ha1 + ":" + auth.nonce + ":" + ha2
        response = md5(a3).hexdigest()
        return response == auth.response
