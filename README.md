#rest-demo (Simple REST-API mock services using flask)

WebService URI Information
==========================

**heroku** : [restdemo.herokuapp.com](http://restdemo.herokuapp.com) </br>
**github** : [github.com/rahulgautam/rest-demo](http://github.com/rahulgautam/rest-demo)

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

[TOC]

New MD App URI
==============

**1. Check login credentials**
 - Request Method: GET
 - URI: login.php
 - BasicAuth: username:password

```
Test using curl
----------------
# curl -u meta:123456 -i http://restdemo.herokuapp.com/login.php
```

**2. Get all data for a subscriber**
 - Request Method: GET
 - URI: `/md/subscriber`
 - BasicAuth: username:password

```
Test using curl
----------------
# curl -u meta:123456 -i http://restdemo.herokuapp.com/md/subscriber
```

**3. Get data for a particular account details from a subscriber**
 - Request Method: GET
 - URI: `/md/subscriber/<int:account_id>`
 - BasicAuth: username:password

```
Test using curl
----------------
# curl -u meta:123456 -i http://restdemo.herokuapp.com/md/subscriber/30312
```

**4. Get filters for a subscriber**
 - Request Method: GET
 - URI: `/md/subscriber/filters`
 - BasicAuth: username:password

```
Test using curl
----------------
# curl -u meta:123456 -i http://restdemo.herokuapp.com/md/subscriber/filters
```

**5. Search throgh all the data of a subscriber using filters**
 - Request Method: GET
 - URI: `/md/subscriber/q?<query_string>`
 - query_string : "Account Type=Hospital&State=IL&GPO=MEDASSETS"
 - In support for search box (so that an entered search value will get filtered from results currently from AccountName and Address)
   user must specify like `Search=<search_value>` in query_string.
 - BasicAuth: username:password


```
Test using curl
----------------
# curl -u meta:123456 -i http://restdemo.herokuapp.com/md/subscriber/q?Account Type=Hospital&State=IL&GPO=MEDASSETS&Search=center
```


Android App URI
================

`Note: URIs' are an exact match of shared doc file`

**1. Check login credentials**
 - Request Method: GET
 - URI: login.php
 - BasicAuth: username:password

```
Test using curl
----------------
# curl -u meta:123456 -i http://restdemo.herokuapp.com/login.php
```


**2. Upload diary entry for a user**
 - Request Method: POST
 - URI: uploaddiary.php
 - BasicAuth: username:password
 - Content-type: application/json

```
body-data
---------
{
    "username": "meta",
    "entrydate": "mm/dd/yyyy",
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

Test using curl
----------------
# curl -u meta:123456 -i -H "Content-Type: application/json" -X POST -d '{"username":"meta","entrydate":"07/17/2013","data":{"muscle_weakness":"","child_activity_level":"","leg_cramp":"","leg_cramp_rating":"","low_blood_sugar":"","intervene_type":"","glucose_measurement":"","glucose_measurement_":"","total_daily_dose":"","dose_frequency":"","route_type":""}}'  http://restdemo.herokuapp.com/uploaddiary.php
```


**3. Upload schedule visit**
 - Request Method: POST
 - URI: visitdate.php
 - BasicAuth: username:password
 - Content-type: application/json

```
body-data
---------
{
	"username":"meta", 
	"visit_date" : "mm/dd/yyyy" , 
	"appoint_taken_date":"mm/dd/yyyy"
}

Test using curl
----------------
#  curl -u meta:123456 -i -H "Content-Type: application/json" -X POST -d '{"username":"meta","visit_date":"mm/dd/yyyy","appoint_taken_date":"mm/dd/yyyy"}' http://restdemo.herokuapp.com/visitdate.php
```


**4. Get Diary Enteries**
 - Request Method: GET
 - URI: diary
 - BasicAuth: username:password
 
```
Test using curl
----------------
# curl -u meta:123456 -i http://restdemo.herokuapp.com/diary
```


**5. Get Visit Enteries**
 - Request Method: GET
 - URI: visit
 - BasicAuth: username:password
 
```
Test using curl
----------------
# curl -u meta:123456 -i http://restdemo.herokuapp.com/visit
```

**6. Delete Diary Enteries**
 - Request Method: DELETE
 - URI: diary
 - BasicAuth: username:password
 
```
Test using curl
----------------
# curl -u meta:123456 -i http://restdemo.herokuapp.com/diary
```


**7. Delete Visit Enteries**
 - Request Method: DELETE
 - URI: visit
 - BasicAuth: username:password
 
```
Test using curl
----------------
# curl -u meta:123456 -i -X DELETE http://restdemo.herokuapp.com/visit
```
