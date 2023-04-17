from flask import *

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("welcome.html")


@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")
    email = request.form.get("email")
    print(name, email)
    return render_template("input.html", name=name, email=email)
