from flask import Flask
from flask import redirect
from flask import make_response, request

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('http://www.google.com')

@app.route('/c1')
def index2():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('color', 'red')
    return response

@app.route('/c2')
def index3():
    color = request.cookies['color']
    response = make_response('<font color=' + color+'>this is based on my cookied value</font>')
    return response

 
app.run(debug=True, port=8080)