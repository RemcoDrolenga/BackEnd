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
    return "<h1>De ingevulde gegevens zijn:</h1> <br> <p>Naam: " + name + "</p> <br> <p>Email: " + email + "</p>"
