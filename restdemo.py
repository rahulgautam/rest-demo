from flask import Flask, jsonify, abort, request, make_response, url_for
from functools import wraps
from hashlib import md5
from random import random

"""
flask.ext.httpauth
==================

This module provides Basic and Digest HTTP authentication for Flask routes.

:copyright: (C) 2013 by Miguel Grinberg.
:license:   BSD, see LICENSE for more details.
"""
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


"""

==================

This is a demo web service

:copyright: (C) 2013 by Rahul Gautam.
:license:   BSD, see LICENSE for more details.
"""

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "meta": "123456"
}


@auth.error_handler
def unauthorized():
    return make_response(jsonify( { 'description': 'Unauthorized access' } ), 403)
    # return 403 instead of 401 to prevent browsers from displaying the default auth dialog
    
@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'description': 'Bad request' } ), 400)
 
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'description': 'Not found' } ), 404)


@auth.get_password
def get_pw(username):
    if username in users:
        return users[username]
    return None

#: client will send this json format to add a new diary
# {
#     "usermame": "",
#     "entrydate": "mm/dd/yyyy",
#     "data": {
#         "muscle_weakness": "",
#         "child_activity_level": "",
#         "leg_cramp": "",
#         "leg_cramp_rating": "",
#         "low_blood_sugar": "",
#         "intervene_type": "",
#         "glucose_measurement": "",
#         "glucose_measurement_": "",
#         "total_daily_dose": "",
#         "dose_frequency": "",
#         "route_type": ""
#     }
# }
#:

diary = {
    "username": {
        #entrydate
        "mm/dd/yyyy": { 
            "data": {
                "muscle_weakness": "",
                "child_activity_level": "",
                "leg_cramp": "",
                "leg_cramp_rating": "",
                "low_blood_sugar": "",
                "intervene_type": "",
                "glucose_measurement": "",
                "glucose_measurement_": "",
                "total_daily_dose": "",
                "dose_frequency": "",
                "route_type": ""
            }
        }
    }
}


#: client will send this json format to add a new visit
# {
#     "username":"", 
#     "visit_date" : "mm/dd/yyyy" , 
#     "appoint_taken_date":"mm/dd/yyyy"
# }

visit = {
    "username": {
        #visit_date
        "mm/dd/yyyy" : {
            "appoint_taken_date":"mm/dd/yyyy"
        }
    }
}

@app.route('/restdemo', methods = ['GET'])
def say_hello():
    return "Hi I am RestDemo Web Service"

@app.route('/restdemo/login.php', methods = ['GET'])
@auth.login_required
def check_login():
    return jsonify( { 'description': 'OK' } )
    

@app.route('/restdemo/diary', methods = ['GET'])
@auth.login_required
def get_diary():
    return jsonify( { 'diary': diary } )


@app.route('/restdemo/visit', methods = ['GET'])
@auth.login_required
def get_visit():
    return jsonify( { 'visit': visit } )


@app.route('/restdemo/uploaddiary.php', methods = ['POST'])
@auth.login_required
def create_diary():
    if not request.json or not 'entrydate' in request.json:
        abort(400)
    user_key = 'username'
    date_key = 'entrydate'
    key_data = 'data'
    if diary.get(request.json.get(user_key)):
        diary[request.json[user_key]
            ][request.json[date_key]] = { key_data : request.json[key_data] }
    else:
        diary[request.json[user_key]
            ] = {request.json[date_key] : { key_data : request.json[key_data] } }
    return jsonify( { 'description': 'Successfully uploaded' } ), 201


@app.route('/restdemo/visitdate.php', methods = ['POST'])
@auth.login_required
def create_visit():
    if not request.json or not 'visit_date' in request.json:
        abort(500)
    user_key = 'username'
    date_key = 'visit_date'
    key_data = 'appoint_taken_date'
    if visit.get(request.json.get(user_key)):
        visit[request.json[user_key]
            ][request.json[date_key]] = { key_data : request.json[key_data] }
    else:
        visit[request.json[user_key]
            ] = {request.json[date_key] : { key_data : request.json[key_data] } }
    return jsonify( { 'description': 'Successfully saved' } ), 201


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)
