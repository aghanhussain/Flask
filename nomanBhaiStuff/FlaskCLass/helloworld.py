from flask import Flask, request, redirect
app = Flask(__name__)

@app.route("/Pakistan/<name>")

def pakistan(name):
    if name =="Karachi":
        return "Karachi is the biggest city of Pakistan "
    elif  name=="Lahore":
        return "Lahore Lahore hy"

@app.route("/India/<name>")
def india(name):
    if name =="Mumbai":
        return "Mumbai is the biggest city of India "
    elif  name=="Delhi":
        return "Delhi Delhi hy"
@app.route("/header")
def getHeader():
    accept=request.headers.get("accept")
    return accept
@app.route("/path")
def path():
    accept=request.headers.get("url")
    return accept

@app.route("/host")
def getHost():
    accept=request.headers.get("Host")
    return accept



@app.route("/redirect")
def redir():
    return redirect('http://www.youtube.com')


from flask import abort

users=["asad", "tahir", "kami", "jamil","hasan"]
@app.route('/user/<id>')
def get_user(id):
    # user = load_user(id)

    if id not in users:
        return "<h1>User not in list</h>",(404)
    return '<h1>Hello, {}</h1>'.format(id)

if __name__=="__main__":
    app.run(debug=True)