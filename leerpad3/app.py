import variables as var
from flask import *

app = Flask(__name__)


@app.route("/")
def connectie():
    naam = var.naam
    return render_template("index.html", naam=naam)
