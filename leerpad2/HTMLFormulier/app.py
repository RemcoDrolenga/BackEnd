from flask import *

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("welcome.html")


@app.route("/submit")
def submit():
    name = request.args.get("name")
    email = request.args.get("email")
    print(name, email)
    return render_template("input.html", name=name, email=email)
