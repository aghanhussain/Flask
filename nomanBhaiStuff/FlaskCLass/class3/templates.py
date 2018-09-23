from flask import Flask, render_template
app = Flask(__name__)

@app.route("/test/<action>")
def index(action):
    args={}
    args['param']='noman'
    args['action']=action
    return render_template('index.html',args=args)

@app.route("/my_macro")
def index2():
    return render_template('macro.html',args=[0,3,2])



if __name__=="__main__":
    app.run(debug=True)