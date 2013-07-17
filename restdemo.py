"""

==================

This is a demo web service

:copyright: (C) 2013 by Rahul Gautam.
:license:   BSD, see LICENSE for more details.
"""

import os
from flask import Flask, jsonify, abort, request, make_response, url_for
import httpauth
from htmlfile import welcome_html

app = Flask(__name__)
auth = httpauth.HTTPBasicAuth()

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

@app.route('/', methods = ['GET'])
def restdemo():
    return welcome_html

@app.route('/login.php', methods = ['GET'])
@auth.login_required
def check_login():
    return jsonify( { 'description': 'OK' } )
    

@app.route('/diary', methods = ['GET'])
@auth.login_required
def get_diary():
    return jsonify( { 'diary': diary } )


@app.route('/visit', methods = ['GET'])
@auth.login_required
def get_visit():
    return jsonify( { 'visit': visit } )


@app.route('/uploaddiary.php', methods = ['POST'])
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


@app.route('/visitdate.php', methods = ['POST'])
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

@app.route('/diary', methods = ['DELETE'])
@auth.login_required
def delete_diary():
    if diary.get(auth.username):
        del diary[auth.username]
    else:
        abort(404)    # not found
    return jsonify( { 'description': 
        'All diary enteries for user %s is deleted'% auth.username} )

@app.route('/visit', methods = ['DELETE'])
@auth.login_required
def delete_visit():
    if visit.get(auth.username):
        del visit[auth.username]
    else:
        abort(404)    # not found
    return jsonify( { 'description': 
        'All visit enteries for user %s is deleted'% auth.username} )

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)
