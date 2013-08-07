
welcome_html = """
<!DOCTYPE html><html><head><meta charset="utf-8"><style>html { font-size: 100%; overflow-y: scroll; -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; }

body{
  color:#444;
  font-family:Georgia, Palatino, 'Palatino Linotype', Times, 'Times New Roman',
              "Hiragino Sans GB", "STXihei", "", serif;
  font-size:12px;
  line-height:1.5em;
  background:#fefefe;
  width: 45em;
  margin: 10px auto;
  padding: 1em;
  outline: 1300px solid #FAFAFA;
}

a{ color: #0645ad; text-decoration:none;}
a:visited{ color: #0b0080; }
a:hover{ color: #06e; }
a:active{ color:#faa700; }
a:focus{ outline: thin dotted; }
a:hover, a:active{ outline: 0; }

span.backtick {
  border:1px solid #EAEAEA;
  border-radius:3px;
  background:#F8F8F8;
  padding:0 3px 0 3px;
}

::-moz-selection{background:rgba(255,255,0,0.3);color:#000}
::selection{background:rgba(255,255,0,0.3);color:#000}

a::-moz-selection{background:rgba(255,255,0,0.3);color:#0645ad}
a::selection{background:rgba(255,255,0,0.3);color:#0645ad}

p{
margin:1em 0;
}

img{
max-width:100%;
}

h1,h2,h3,h4,h5,h6{
font-weight:normal;
color:#111;
line-height:1em;
}
h4,h5,h6{ font-weight: bold; }
h1{ font-size:2.5em; }
h2{ font-size:2em; border-bottom:1px solid silver; padding-bottom: 5px; }
h3{ font-size:1.5em; }
h4{ font-size:1.2em; }
h5{ font-size:1em; }
h6{ font-size:0.9em; }

blockquote{
color:#666666;
margin:0;
padding-left: 3em;
border-left: 0.5em #EEE solid;
}
hr { display: block; height: 2px; border: 0; border-top: 1px solid #aaa;border-bottom: 1px solid #eee; margin: 1em 0; padding: 0; }


pre , code, kbd, samp { 
  color: #000; 
  font-family: monospace; 
  font-size: 0.88em; 
  border-radius:3px;
  background-color: #F8F8F8;
  border: 1px solid #CCC; 
}
pre { white-space: pre; white-space: pre-wrap; word-wrap: break-word; padding: 5px 12px;}
pre code { border: 0px !important; padding: 0;}
code { padding: 0 3px 0 3px; }

b, strong { font-weight: bold; }

dfn { font-style: italic; }

ins { background: #ff9; color: #000; text-decoration: none; }

mark { background: #ff0; color: #000; font-style: italic; font-weight: bold; }

sub, sup { font-size: 75%; line-height: 0; position: relative; vertical-align: baseline; }
sup { top: -0.5em; }
sub { bottom: -0.25em; }

ul, ol { margin: 1em 0; padding: 0 0 0 2em; }
li p:last-child { margin:0 }
dd { margin: 0 0 0 2em; }

img { border: 0; -ms-interpolation-mode: bicubic; vertical-align: middle; }

table { border-collapse: collapse; border-spacing: 0; }
td { vertical-align: top; }

@media only screen and (min-width: 480px) {
body{font-size:14px;}
}

@media only screen and (min-width: 768px) {
body{font-size:16px;}
}

@media print {
  * { background: transparent !important; color: black !important; filter:none !important; -ms-filter: none !important; }
  body{font-size:12pt; max-width:100%; outline:none;}
  a, a:visited { text-decoration: underline; }
  hr { height: 1px; border:0; border-bottom:1px solid black; }
  a[href]:after { content: " (" attr(href) ")"; }
  abbr[title]:after { content: " (" attr(title) ")"; }
  .ir a:after, a[href^="javascript:"]:after, a[href^="#"]:after { content: ""; }
  pre, blockquote { border: 1px solid #999; padding-right: 1em; page-break-inside: avoid; }
  tr, img { page-break-inside: avoid; }
  img { max-width: 100% !important; }
  @page :left { margin: 15mm 20mm 15mm 10mm; }
  @page :right { margin: 15mm 10mm 15mm 20mm; }
  p, h2, h3 { orphans: 3; widows: 3; }
  h2, h3 { page-break-after: avoid; }
}
</style><title>WebService URI Expose</title></head><body><h1 id="webservice-uri-information">WebService URI Information</h1>

<p><strong>heroku</strong> : <a href="http://restdemo.herokuapp.com">restdemo.herokuapp.com</a> </br>
<strong>github</strong> : <a href="http://github.com/rahulgautam/rest-demo">github.com/rahulgautam/rest-demo</a></p>

<p><ul>
  <strong>Table of Contents</strong>
  <li><a href="#new-md-app-uri">New MD App URI</a></li>
  <li><a href="#android-app-uri">Android App URI</a></li>
</ul>
</p>

<h1 id="new-md-app-uri">New MD App URI</h1>

<p><strong>1. Check login credentials</strong></p>

<ul>
<li>Request Method: GET</li>
<li>URI: login.php</li>
<li>BasicAuth: username:password</li>
</ul>

<pre><code>Test using curl
----------------
# curl -u meta:123456 -i http://restdemo.herokuapp.com/login.php
</code></pre>

<p><strong>2. Get all data for a subscriber</strong></p>

<ul>
<li>Request Method: GET</li>
<li>URI: <code>/md/subscriber</code></li>
<li>BasicAuth: username:password</li>
</ul>

<pre><code>Test using curl
----------------
# curl -u meta:123456 -i http://restdemo.herokuapp.com/md/subscriber
</code></pre>

<p><strong>3. Get data for a particular account details from a subscriber</strong></p>

<ul>
<li>Request Method: GET</li>
<li>URI: <code>/md/subscriber/&lt;int:account_id&gt;</code></li>
<li>BasicAuth: username:password</li>
</ul>

<pre><code>Test using curl
----------------
# curl -u meta:123456 -i http://restdemo.herokuapp.com/md/subscriber/30312
</code></pre>

<p><strong>4. Get filters for a subscriber</strong></p>

<ul>
<li>Request Method: GET</li>
<li>URI: <code>/md/subscriber/filters</code></li>
<li>BasicAuth: username:password</li>
</ul>

<pre><code>Test using curl
----------------
# curl -u meta:123456 -i http://restdemo.herokuapp.com/md/subscriber/filters
</code></pre>

<p><strong>5. Search throgh all the data of a subscriber using filters</strong></p>

<ul>
<li>Request Method: GET</li>
<li>URI: <code>/md/subscriber/q?&lt;query_string&gt;</code></li>
<li>query_string : "Account Type=Hospital&amp;State=IL&amp;GPO=MEDASSETS"</li>
<li>BasicAuth: username:password</li>
</ul>

<pre><code>Test using curl
----------------
# curl -u meta:123456 -i http://restdemo.herokuapp.com/md/subscriber/q?Account Type=Hospital&amp;State=IL&amp;GPO=MEDASSETS
</code></pre>

<h1 id="android-app-uri">Android App URI</h1>

<p><code>Note: URIs' are an exact match of shared doc file</code></p>

<p><strong>1. Check login credentials</strong></p>

<ul>
<li>Request Method: GET</li>
<li>URI: login.php</li>
<li>BasicAuth: username:password</li>
</ul>

<pre><code>Test using curl
----------------
# curl -u meta:123456 -i http://restdemo.herokuapp.com/login.php
</code></pre>

<p><strong>2. Upload diary entry for a user</strong></p>

<ul>
<li>Request Method: POST</li>
<li>URI: uploaddiary.php</li>
<li>BasicAuth: username:password</li>
<li>Content-type: application/json</li>
</ul>

<pre><code>body-data
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
</code></pre>

<p><strong>3. Upload schedule visit</strong></p>

<ul>
<li>Request Method: POST</li>
<li>URI: visitdate.php</li>
<li>BasicAuth: username:password</li>
<li>Content-type: application/json</li>
</ul>

<pre><code>body-data
---------
{
    "username":"meta", 
    "visit_date" : "mm/dd/yyyy" , 
    "appoint_taken_date":"mm/dd/yyyy"
}

Test using curl
----------------
#  curl -u meta:123456 -i -H "Content-Type: application/json" -X POST -d '{"username":"meta","visit_date":"mm/dd/yyyy","appoint_taken_date":"mm/dd/yyyy"}' http://restdemo.herokuapp.com/visitdate.php
</code></pre>

<p><strong>4. Get Diary Enteries</strong></p>

<ul>
<li>Request Method: GET</li>
<li>URI: diary</li>
<li>BasicAuth: username:password</li>
</ul>

<pre><code>Test using curl
----------------
# curl -u meta:123456 -i http://restdemo.herokuapp.com/diary
</code></pre>

<p><strong>5. Get Visit Enteries</strong></p>

<ul>
<li>Request Method: GET</li>
<li>URI: visit</li>
<li>BasicAuth: username:password</li>
</ul>

<pre><code>Test using curl
----------------
# curl -u meta:123456 -i http://restdemo.herokuapp.com/visit
</code></pre>

<p><strong>6. Delete Diary Enteries</strong></p>

<ul>
<li>Request Method: DELETE</li>
<li>URI: diary</li>
<li>BasicAuth: username:password</li>
</ul>

<pre><code>Test using curl
----------------
# curl -u meta:123456 -i http://restdemo.herokuapp.com/diary
</code></pre>

<p><strong>7. Delete Visit Enteries</strong></p>

<ul>
<li>Request Method: DELETE</li>
<li>URI: visit</li>
<li>BasicAuth: username:password</li>
</ul>

<pre><code>Test using curl
----------------
# curl -u meta:123456 -i -X DELETE http://restdemo.herokuapp.com/visit
</code></pre>
</body></html>"""