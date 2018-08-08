from flask import Flask

app=Flask(__name__)

def index():
    return "Hello First Flask App"

app.add_url_rule('/', 'index', index)

app.run(debug=True, port=8080)