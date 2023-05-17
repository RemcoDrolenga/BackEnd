import content as content
from flask import *

app = Flask(__name__, static_folder="static")


@app.route("/")
def index():
    naam = content.naam
    return render_template("index.html", naam=naam)
