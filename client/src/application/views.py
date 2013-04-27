# -*- coding: latin-1 -*-
"""
URL-reititykset ja sivut OAuth-toimintoja lukuunottamatta.
"""

from application import app
from urlparse import parse_qs
from flask import render_template, session, redirect, request
from settings import REQUEST_TOKEN_URL, ACCESS_TOKEN_URL, AUTHORIZE_URL
from settings import CALLBACK_URL, API_URL
from utils import fetch_from_api, fetch_from_api_signed

### SIVUT ###


@app.route("/")
def index():
    """Viimeisimmät ottelutilastot, sarjataulukko ja pelaajien pistekärki.
    käyttäjää kehotetaan kirjautumaan sisään.
    """
    if "oauth_token" in session:
        return render_template("start.html",authorized=True)

    else:
        return render_template("start.html",authorized=True)  # TODO false


@app.route("/player")
def player():
    return render_template("player.html")

@app.route("/game/<int:game_id>")
def game(game_id):
    # TODO:Hae pelin tiedot apilta

    # Muuta json python-olioksi

    # Build list of goal-objects

    # Build list of players
    game = {"away_team": "njd", "home_score": "6", "shootout": [], "goals": [{"period": 1, "desc": "Dustin Brown 8 (power play) (Assists: Drew Doughty 11, Mike Richards 10)", "team": "los", "time": "11:03", "score": "0 - 1"}, {"period": 1, "desc": "Jeff Carter 7 (power play) (Assists: Dustin Brown 11, Mike Richards 11)", "team": "los", "time": "12:45", "score": "0 - 2"}, {"period": 1, "desc": "Trevor Lewis 2 (power play) (Assists: Dwight King 2, Drew Doughty 12)", "team": "los", "time": "15:01", "score": "0 - 3"}, {"period": 2, "desc": "Jeff Carter 8 (Assists: Dustin Brown 12, Anze Kopitar 12)", "team": "los", "time": "1:30", "score": "0 - 4"}, {"period": 2, "desc": "Adam Henrique 5 (Assists: Petr Sykora 3, Alexei Ponikarovsky 8)", "team": "njd", "time": "18:45", "score": "1 - 4"}, {"period": 3, "desc": "Trevor Lewis 3 (empty net) (Assists: Dwight King 3, Jarret Stoll 3)", "team": "los", "time": "16:15", "score": "1 - 5"}, {"period": 3, "desc": "Matt Greene 2 (Unassisted)", "team": "los", "time": "16:30", "score": "1 - 6"} ], "home_team": "los", "skaters": {"3990": {"pts": "2", "team": "home", "fo%": "1.000", "fl": "0", "name": "T. Lewis", "fw": "1", "s": "2", "toi": "14:54", "+/-": "+1", "hits": "4", "pim": "0", "g": "2", "bs": "0", "a": "0", "shifts": "25"}, "3972": {"pts": "0", "team": "away", "fo%": ".000", "fl": "2", "name": "R. Carter", "fw": "0", "s": "0", "toi": "08:20", "+/-": "-1", "hits": "0", "pim": "12", "g": "0", "bs": "0", "a": "0", "shifts": "12"}, "1333": {"pts": "1", "team": "away", "fo%": "-", "fl": "0", "name": "P. Sykora", "fw": "0", "s": "1", "toi": "11:53", "+/-": "+1", "hits": "0", "pim": "2", "g": "0", "bs": "0", "a": "1", "shifts": "20"}, "2121": {"pts": "0", "team": "home", "fo%": "-", "fl": "0", "name": "W. Mitchell", "fw": "0", "s": "2", "toi": "24:29", "+/-": "+2", "hits": "0", "pim": "0", "g": "0", "bs": "0", "a": "0", "shifts": "31"}, "3871": {"pts": "0", "team": "away", "fo%": "-", "fl": "0", "name": "A. Greene", "fw": "0", "s": "2", "toi": "19:29", "+/-": "0", "hits": "1", "pim": "0", "g": "0", "bs": "2", "a": "0", "shifts": "29"}, "3657": {"pts": "0", "team": "away", "fo%": ".412", "fl": "10", "name": "T. Zajac", "fw": "7", "s": "1", "toi": "18:47", "+/-": "-2", "hits": "4", "pim": "0", "g": "0", "bs": "0", "a": "0", "shifts": "29"}, "5190": {"pts": "0", "team": "away", "fo%": "-", "fl": "0", "name": "M. Fayne", "fw": "0", "s": "0", "toi": "16:20", "+/-": "+1", "hits": "1", "pim": "0", "g": "0", "bs": "2", "a": "0", "shifts": "26"}, "4424": {"pts": "0", "team": "home", "fo%": "-", "fl": "0", "name": "A. Martinez", "fw": "0", "s": "0", "toi": "15:03", "+/-": "+1", "hits": "3", "pim": "0", "g": "0", "bs": "0", "a": "0", "shifts": "21"}, "4549": {"pts": "0", "team": "home", "fo%": "-", "fl": "0", "name": "S. Voynov", "fw": "0", "s": "2", "toi": "20:00", "+/-": "+2", "hits": "1", "pim": "0", "g": "0", "bs": "2", "a": "0", "shifts": "26"}, "3249": {"pts": "0", "team": "away", "fo%": "-", "fl": "0", "name": "M. Zidlicky", "fw": "0", "s": "2", "toi": "20:20", "+/-": "-1", "hits": "3", "pim": "2", "g": "0", "bs": "2", "a": "0", "shifts": "28"}, "2557": {"pts": "1", "team": "away", "fo%": "-", "fl": "0", "name": "A. Ponikarovsky", "fw": "0", "s": "0", "toi": "15:17", "+/-": "0", "hits": "1", "pim": "0", "g": "0", "bs": "1", "a": "1", "shifts": "19"}, "3565": {"pts": "0", "team": "home", "fo%": "1.000", "fl": "0", "name": "C. Fraser", "fw": "3", "s": "0", "toi": "07:16", "+/-": "0", "hits": "2", "pim": "0", "g": "0", "bs": "0", "a": "0", "shifts": "10"}, "1389": {"pts": "0", "team": "away", "fo%": ".250", "fl": "9", "name": "P. Elias", "fw": "3", "s": "1", "toi": "17:13", "+/-": "0", "hits": "4", "pim": "0", "g": "0", "bs": "1", "a": "0", "shifts": "26"}, "2944": {"pts": "0", "team": "away", "fo%": "-", "fl": "0", "name": "I. Kovalchuk", "fw": "0", "s": "2", "toi": "18:19", "+/-": "-2", "hits": "1", "pim": "0", "g": "0", "bs": "0", "a": "0", "shifts": "24"}, "1920": {"pts": "0", "team": "home", "fo%": "-", "fl": "0", "name": "S. Gagne", "fw": "0", "s": "0", "toi": "08:38", "+/-": "0", "hits": "0", "pim": "0", "g": "0", "bs": "0", "a": "0", "shifts": "11"}, "1753": {"pts": "0", "team": "away", "fo%": "-", "fl": "0", "name": "B. Salvador", "fw": "0", "s": "1", "toi": "20:49", "+/-": "-1", "hits": "3", "pim": "4", "g": "0", "bs": "1", "a": "0", "shifts": "25"}, "5238": {"pts": "1", "team": "away", "fo%": ".500", "fl": "7", "name": "A. Henrique", "fw": "7", "s": "3", "toi": "16:37", "+/-": "+1", "hits": "1", "pim": "0", "g": "1", "bs": "0", "a": "0", "shifts": "25"}, "2528": {"pts": "1", "team": "home", "fo%": ".625", "fl": "6", "name": "J. Stoll", "fw": "10", "s": "3", "toi": "17:43", "+/-": "+1", "hits": "7", "pim": "0", "g": "0", "bs": "1", "a": "1", "shifts": "29"}, "1485": {"pts": "0", "team": "away", "fo%": ".000", "fl": "1", "name": "D. Zubrus", "fw": "0", "s": "1", "toi": "16:41", "+/-": "0", "hits": "6", "pim": "0", "g": "0", "bs": "0", "a": "0", "shifts": "27"}, "3351": {"pts": "3", "team": "home", "fo%": ".000", "fl": "1", "name": "D. Brown", "fw": "0", "s": "2", "toi": "19:23", "+/-": "+1", "hits": "4", "pim": "4", "g": "1", "bs": "1", "a": "2", "shifts": "26"}, "2151": {"pts": "0", "team": "away", "fo%": "-", "fl": "0", "name": "H. Tallinder", "fw": "0", "s": "0", "toi": "18:39", "+/-": "-1", "hits": "2", "pim": "0", "g": "0", "bs": "1", "a": "0", "shifts": "25"}, "3355": {"pts": "0", "team": "away", "fo%": "-", "fl": "0", "name": "Z. Parise", "fw": "0", "s": "1", "toi": "19:12", "+/-": "-2", "hits": "5", "pim": "0", "g": "0", "bs": "1", "a": "0", "shifts": "29"}, "3354": {"pts": "0", "team": "away", "fo%": "-", "fl": "0", "name": "S. Bernier", "fw": "0", "s": "0", "toi": "01:56", "+/-": "0", "hits": "1", "pim": "15", "g": "0", "bs": "0", "a": "0", "shifts": "3"}, "3788": {"pts": "1", "team": "home", "fo%": ".500", "fl": "9", "name": "A. Kopitar", "fw": "9", "s": "2", "toi": "20:15", "+/-": "+1", "hits": "2", "pim": "0", "g": "0", "bs": "2", "a": "1", "shifts": "27"}, "2564": {"pts": "0", "team": "away", "fo%": "-", "fl": "0", "name": "A. Volchenkov", "fw": "0", "s": "0", "toi": "21:28", "+/-": "-2", "hits": "7", "pim": "2", "g": "0", "bs": "4", "a": "0", "shifts": "24"}, "3587": {"pts": "0", "team": "home", "fo%": "-", "fl": "0", "name": "D. Penner", "fw": "0", "s": "2", "toi": "13:36", "+/-": "0", "hits": "2", "pim": "2", "g": "0", "bs": "0", "a": "0", "shifts": "23"}, "4559": {"pts": "2", "team": "home", "fo%": "-", "fl": "0", "name": "D. King", "fw": "0", "s": "2", "toi": "15:36", "+/-": "+1", "hits": "0", "pim": "0", "g": "0", "bs": "0", "a": "2", "shifts": "23"}, "2468": {"pts": "0", "team": "home", "fo%": "-", "fl": "0", "name": "J. Williams", "fw": "0", "s": "2", "toi": "20:24", "+/-": "0", "hits": "2", "pim": "0", "g": "0", "bs": "0", "a": "0", "shifts": "26"}, "3271": {"pts": "1", "team": "home", "fo%": "-", "fl": "0", "name": "M. Greene", "fw": "0", "s": "1", "toi": "14:10", "+/-": "+1", "hits": "2", "pim": "0", "g": "1", "bs": "0", "a": "0", "shifts": "22"}, "4472": {"pts": "2", "team": "home", "fo%": "-", "fl": "0", "name": "D. Doughty", "fw": "0", "s": "1", "toi": "27:31", "+/-": "-1", "hits": "2", "pim": "0", "g": "0", "bs": "1", "a": "2", "shifts": "32"}, "3349": {"pts": "2", "team": "home", "fo%": "1.000", "fl": "0", "name": "J. Carter", "fw": "1", "s": "3", "toi": "16:39", "+/-": "+1", "hits": "0", "pim": "0", "g": "2", "bs": "0", "a": "0", "shifts": "26"}, "3361": {"pts": "2", "team": "home", "fo%": ".769", "fl": "3", "name": "M. Richards", "fw": "10", "s": "1", "toi": "16:55", "+/-": "0", "hits": "0", "pim": "0", "g": "0", "bs": "1", "a": "2", "shifts": "25"}, "4744": {"pts": "0", "team": "away", "fo%": ".333", "fl": "4", "name": "S. Gionta", "fw": "2", "s": "2", "toi": "14:17", "+/-": "-1", "hits": "3", "pim": "0", "g": "0", "bs": "0", "a": "0", "shifts": "20"}, "3741": {"pts": "0", "team": "away", "fo%": ".000", "fl": "1", "name": "D. Clarkson", "fw": "0", "s": "1", "toi": "09:59", "+/-": "-1", "hits": "5", "pim": "10", "g": "0", "bs": "1", "a": "0", "shifts": "14"}, "2837": {"pts": "0", "team": "home", "fo%": "-", "fl": "0", "name": "R. Scuderi", "fw": "0", "s": "0", "toi": "17:01", "+/-": "-1", "hits": "0", "pim": "0", "g": "0", "bs": "1", "a": "0", "shifts": "24"}, "5221": {"pts": "0", "team": "home", "fo%": "-", "fl": "0", "name": "J. Nolan", "fw": "0", "s": "0", "toi": "06:33", "+/-": "0", "hits": "3", "pim": "0", "g": "0", "bs": "0", "a": "0", "shifts": "9"} }, "goalies": {"4147": {"sv%": ".944", "name": "J. Quick", "team": "home", "toi": "59:54", "ga": "1", "sv": "17", "pim": "0", "sa": "18"}, "686": {"sv%": ".792", "name": "M. Brodeur", "team": "away", "toi": "59:24", "ga": "5", "sv": "19", "pim": "0", "sa": "24"} }, "away_score": "1"}

    home_team = "JYP"
    home_score = 99
    away_team = "BOS"
    away_score = 4
    goals = [{"period": 1,
              "desc": "Dustin Brown 8 (power play) (Assists: Drew Doughty 11, Mike Richards 10)",
              "team": "los",
              "time": "11:03",
              "score": "0 - 1"},
             {
               "period": 2,
               "desc": "Adam Henrique 5 (Assists: Petr Sykora 3, Alexei Ponikarovsky 8)",
               "team": "njd",
               "time": "18:45",
               "score": "1 - 4"
             },
             {
               "period": 3,
               "desc": "Trevor Lewis 3 (empty net) (Assists: Dwight King 3, Jarret Stoll 3)",
               "team": "los",
               "time": "16:15",
               "score": "1 - 5"
             }]

    skaters = [{"3990": {"pts": "2", "team": "home", "fo%": "1.000", "fl": "0", "name": "T. Lewis", "fw": "1", "s": "2", "toi": "14:54", "+/-": "+1", "hits": "4", "pim": "0", "g": "2", "bs": "0", "a": "0", "shifts": "25"}, "3972": {"pts": "0", "team": "away", "fo%": ".000", "fl": "2", "name": "R. Carter", "fw": "0", "s": "0", "toi": "08:20", "+/-": "-1", "hits": "0", "pim": "12", "g": "0", "bs": "0", "a": "0", "shifts": "12"}, "1333": {"pts": "1", "team": "away", "fo%": "-", "fl": "0", "name": "P. Sykora", "fw": "0", "s": "1", "toi": "11:53", "+/-": "+1", "hits": "0", "pim": "2", "g": "0", "bs": "0", "a": "1", "shifts": "20"}, "2121": {"pts": "0", "team": "home", "fo%": "-", "fl": "0", "name": "W. Mitchell", "fw": "0", "s": "2", "toi": "24:29", "+/-": "+2", "hits": "0", "pim": "0", "g": "0", "bs": "0", "a": "0", "shifts": "31"}, "3871": {"pts": "0", "team": "away", "fo%": "-", "fl": "0", "name": "A. Greene", "fw": "0", "s": "2", "toi": "19:29", "+/-": "0", "hits": "1", "pim": "0", "g": "0", "bs": "2", "a": "0", "shifts": "29"},"3657": {"pts": "0", "team": "away", "fo%": ".412", "fl": "10", "name": "T. Zajac", "fw": "7", "s": "1", "toi": "18:47", "+/-": "-2", "hits": "4", "pim": "0", "g": "0", "bs": "0", "a": "0", "shifts": "29"}, "5190": {"pts": "0", "team": "away", "fo%": "-", "fl": "0", "name": "M. Fayne", "fw": "0", "s": "0", "toi": "16:20", "+/-": "+1", "hits": "1", "pim": "0", "g": "0", "bs": "2", "a": "0", "shifts": "26"}, "4424": {"pts": "0", "team": "home", "fo%": "-", "fl": "0", "name": "A. Martinez", "fw": "0", "s": "0", "toi": "15:03", "+/-": "+1", "hits": "3", "pim": "0", "g": "0", "bs": "0", "a": "0", "shifts": "21"}}]

    # Poistetaan pelaaja-lista-dictionary -rakenteesta yksi dictionary-taso, jotta
    # Jinja template-engine osaa loopata tietorakenteen läpi ilman ongelmaa.
    skater_list = []
    for k,v in game['skaters'].iteritems():
        v[id] = k
        skater_list.append(v)

    return render_template("game.html", home_team=home_team ,
                                        home_score=home_score ,
                                        away_team=away_team ,
                                        away_score=away_score,
                                        goals=goals,
                                        skaters=skater_list )


@app.route("/team")
def team():
    return render_template("team.html")

@app.route("/search")
def search():
    return render_template("search.html")
