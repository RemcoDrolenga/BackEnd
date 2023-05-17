import Minecraft as mc, RocketLeague as rl, Celeste as cel, CoD_Warzone as cod
from flask import *
from datetime import datetime


app = Flask(__name__, static_folder="static")


@app.route("/Minecraft")
def index():
    Minecraft_Titel = mc.Titel
    Minecraft_Beschrijving = mc.Beschrijving
    Date = datetime.now().strftime("%d-%m-%Y")
    return render_template(
        "Minecraft.html",
        Minecraft_Titel=Minecraft_Titel,
        Minecraft_Beschrijving=Minecraft_Beschrijving,
        Date=Date,
    )


@app.route("/RocketLeague")
def index2():
    RocketLeague_Titel = rl.Titel
    RocketLeague_Beschrijving = rl.Beschrijving
    Date = datetime.now().strftime("%d-%m-%Y")
    return render_template(
        "RocketLeague.html",
        RocketLeague_Titel=RocketLeague_Titel,
        RocketLeague_Beschrijving=RocketLeague_Beschrijving,
        Date=Date,
    )


@app.route("/")
def index3():
    Celeste_Titel = cel.Titel
    Celeste_Beschrijving = cel.Beschrijving
    Date = datetime.now().strftime("%d-%m-%Y")
    return render_template(
        "Celeste.html",
        Celeste_Titel=Celeste_Titel,
        Celeste_Beschrijving=Celeste_Beschrijving,
        Date=Date,
    )


@app.route("/CoD_Warzone")
def index4():
    CoD_Warzone_Titel = cod.Titel
    CoD_Warzone_Beschrijving = cod.Beschrijving
    Date = datetime.now().strftime("%d-%m-%Y")
    return render_template(
        "CoD_Warzone.html",
        CoD_Warzone_Titel=CoD_Warzone_Titel,
        CoD_Warzone_Beschrijving=CoD_Warzone_Beschrijving,
        Date=Date,
    )
