from flask import Flask, request, render_template
app = Flask(__name__)
numbers=[1,2,3,4,5,6,7,8,9]
@app.route("/pakistan")
def pakistan():
    return render_template("pakistan.html", numbers=numbers)

@app.route("/india")
def india():
    return render_template("india.html")

@app.route("/china")
def china():
    return render_template("china.html")

app.run(debug=True)