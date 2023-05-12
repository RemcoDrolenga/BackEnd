from flask import *

app = Flask(__name__)


@app.route("/")
def connectie():
    return render_template("formulier_onkunde.html")


@app.route("/resultaat_onkunde", methods=["POST"])
def submit():
    willen_kunnen = request.form.get("willen_kunnen")
    persoon_opschieten = request.form.get("persoon_opschieten")
    favoriete_getal = request.form.get("favoriete_getal")
    vakantie_gaan = request.form.get("vakantie_gaan")
    beste_eigenschap = request.form.get("beste_eigenschap")
    slechtste_eigenschap = request.form.get("slechtste_eigenschap")
    ergste_overkomen = request.form.get("ergste_overkomen")
    print(willen_kunnen, persoon_opschieten, favoriete_getal, vakantie_gaan,
          beste_eigenschap, slechtste_eigenschap, ergste_overkomen)
    return render_template("resultaat_onkunde.html", willen_kunnen=willen_kunnen, persoon_opschieten=persoon_opschieten, favoriete_getal=favoriete_getal, vakantie_gaan=vakantie_gaan, beste_eigenschap=beste_eigenschap, slechtste_eigenschap=slechtste_eigenschap, ergste_overkomen=ergste_overkomen)


@app.route("/formulier_paniek")
def connectie2():
    return render_template("formulier_paniek.html")


@app.route("/resultaat_paniek", methods=["POST"])
def submit2():
    huisdier = request.form.get("huisdier")
    persoon = request.form.get("persoon")
    land = request.form.get("land")
    verveelt = request.form.get("verveelt")
    speelgoed = request.form.get("speelgoed")
    spijbel = request.form.get("spijbel")
    kopen = request.form.get("kopen")
    bezigheid = request.form.get("bezigheid")
    print(huisdier, persoon, land, verveelt,
          speelgoed, spijbel, kopen, bezigheid)
    return render_template("resultaat_paniek.html", huisdier=huisdier, persoon=persoon, land=land, verveelt=verveelt, speelgoed=speelgoed, spijbel=spijbel, kopen=kopen, bezigheid=bezigheid)
