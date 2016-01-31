#!/usr/bin/python3

from ..teams import atalanta
from ..teams import chievo
from ..teams import fiorentina
from ..teams import genoa
from ..teams import inter
from ..teams import juventus
from ..teams import lazio
from ..teams import milan
from ..teams import napoli
from ..teams import roma
from ..teams import sampdoria
from ..teams import torino
from ..teams import udinese

class ItalyTeam:
        name=""
        homeWins3Years=0
        homeDraws3Years=0
        homeLoses3Years=0
        awayWins3Years=0
        awayDraws3Years=0
        awayLoses3Years=0

        home1milan=0
        homexmilan=0
        home2milan=0

        home1inter=0
        homexinter=0
        home2inter=0

        home1juventus=0
        homexjuventus=0
        home2juventus=0

        home1lazio=0
        homexlazio=0
        home2lazio=0

        home1roma=0
        homexroma=0
        home2roma=0

        home1napoli=0
        homexnapoli=0
        home2napoli=0

        home1fiorentina=0
        homexfiorentina=0
        home2fiorentina=0

        home1udinese=0
        homexudinese=0
        home2udinese=0

        home1genoa=0
        homexgenoa=0
        home2genoa=0

        home1sampdoria=0
        homexsampdoria=0
        home2sampdoria=0

        home1chievo=0
        homexchievo=0
        home2chievo=0

        home1atalanta=0
        homexatalanta=0
        home2atalanta=0

        home1torino=0
        homextorino=0
        home2torino=0

def checkNames( team ) :
        if team == "milan" or team == "ACM" or team == "acm" or team == "Milan" \
           or team == "atalanta" or team == "Atalanta" \
           or team == "chievo" or team == "Chievo" \
           or team == "fiorentina" or team == "Fiorentina" \
           or team == "genoa" or team == "Genoa" \
           or team == "inter" or team =="internazionale" or team == "Internazionale" or team == "Inter" \
           or team == "juventus" or team == "juve" or team == "Juve" or team == "Juventus" \
           or team == "lazio" or team == "Lazio" \
           or team == "napoli" or team == "Napoli" \
           or team == "roma" or team == "Roma" \
           or team == "sampdoria" or team == "samp" or team == "Samp" or team == "Sampdoria" \
           or team == "torino" or team == "toro" or team == "Toro" or team == "Torino" \
           or team == "udinese" or team == "udine" or team == "Udine" or team == "Udinese" :
                return "Italy"
        else :
                return "Country"
                        
def setName( team ):
        if team == "milan" or team == "ACM" or team == "acm" :
                team = "Milan"
        if team == "atalanta" :
                team = "Atalanta"
        if team == "chievo" :
                team = "Chievo"
        if team == "fiorentina" :
                team = "Fiorentina"
        if team == "genoa" :
                team = "Genoa"
        if team == "inter" or team =="internazionale" or team == "Internazionale" :
                team = "Inter"
        if team == "juventus" or team == "juve" or team == "Juve" :
                team = "Juventus"
        if team == "lazio" :
                team = "Lazio"
        if team == "napoli" :
                team = "Napoli"
        if team == "roma" :
                team = "Roma"
        if team == "sampdoria" or team == "samp" or team == "Samp" :
                team = "Sampdoria"
        if team == "torino" or team == "toro" or team == "Toro" :
                team = "Torino"
        if team == "udinese" or team == "udine" or team == "Udine":
                team = "Udinese"
        return team

def findName ( name ):
        if name == "Atalanta" or name == "Chievo" or name == "Fiorentina" or \
        name == "Genoa" or name == "Inter" or name == "Juventus" or \
        name == "Lazio" or name == "Milan" or name == "Napoli" or \
        name == "Roma" or name == "Sampdoria" or name == "Torino" or \
        name == "Udinese" :
                return 1
        else:
                return 0

def populateData( team ):
	if team.name == "Atalanta" :
		team.homeWins3Years=atalanta.homeWins3Years
		team.homeDraws3Years=atalanta.homeDraws3Years
		team.homeLoses3Years=atalanta.homeLoses3Years
		team.awayWins3Years=atalanta.awayWins3Years
		team.awayDraws3Years=atalanta.awayDraws3Years
		team.awayLoses3Years=atalanta.awayLoses3Years
		team.home1milan=atalanta.home1milan
		team.homexmilan=atalanta.homexmilan
		team.home2milan=atalanta.home2milan
		team.home1inter=atalanta.home1inter
		team.homexinter=atalanta.homexinter
		team.home2inter=atalanta.home2inter
		team.home1juventus=atalanta.home1juventus
		team.homexjuventus=atalanta.homexjuventus
		team.home2juventus=atalanta.home2juventus
		team.home1lazio=atalanta.home1lazio
		team.homexlazio=atalanta.homexlazio
		team.home2lazio=atalanta.home2lazio
		team.home1roma=atalanta.home1roma
		team.homexroma=atalanta.homexroma
		team.home2roma=atalanta.home2roma
		team.home1napoli=atalanta.home1napoli
		team.homexnapoli=atalanta.homexnapoli
		team.home2napoli=atalanta.home2napoli
		team.home1fiorentina=atalanta.home1fiorentina
		team.homexfiorentina=atalanta.homexfiorentina
		team.home2fiorentina=atalanta.home2fiorentina
		team.home1udinese=atalanta.home1udinese
		team.homexudinese=atalanta.homexudinese
		team.home2udinese=atalanta.home2udinese
		team.home1genoa=atalanta.home1genoa
		team.homexgenoa=atalanta.homexgenoa
		team.home2genoa=atalanta.home2genoa
		team.home1sampdoria=atalanta.home1sampdoria
		team.homexsampdoria=atalanta.homexsampdoria
		team.home2sampdoria=atalanta.home2sampdoria
		team.home1chievo=atalanta.home1chievo
		team.homexchievo=atalanta.homexchievo
		team.home2chievo=atalanta.home2chievo
		team.home1atalanta=atalanta.home1atalanta
		team.homexatalanta=atalanta.homexatalanta
		team.home2atalanta=atalanta.home2atalanta
		team.home1torino=atalanta.home1torino
		team.homextorino=atalanta.homextorino
		team.home2torino=atalanta.home2torino
	if team.name == "Chievo" :
		team.homeWins3Years=chievo.homeWins3Years
		team.homeDraws3Years=chievo.homeDraws3Years
		team.homeLoses3Years=chievo.homeLoses3Years
		team.awayWins3Years=chievo.awayWins3Years
		team.awayDraws3Years=chievo.awayDraws3Years
		team.awayLoses3Years=chievo.awayLoses3Years
		team.home1milan=chievo.home1milan
		team.homexmilan=chievo.homexmilan
		team.home2milan=chievo.home2milan
		team.home1inter=chievo.home1inter
		team.homexinter=chievo.homexinter
		team.home2inter=chievo.home2inter
		team.home1juventus=chievo.home1juventus
		team.homexjuventus=chievo.homexjuventus
		team.home2juventus=chievo.home2juventus
		team.home1lazio=chievo.home1lazio
		team.homexlazio=chievo.homexlazio
		team.home2lazio=chievo.home2lazio
		team.home1roma=chievo.home1roma
		team.homexroma=chievo.homexroma
		team.home2roma=chievo.home2roma
		team.home1napoli=chievo.home1napoli
		team.homexnapoli=chievo.homexnapoli
		team.home2napoli=chievo.home2napoli
		team.home1fiorentina=chievo.home1fiorentina
		team.homexfiorentina=chievo.homexfiorentina
		team.home2fiorentina=chievo.home2fiorentina
		team.home1udinese=chievo.home1udinese
		team.homexudinese=chievo.homexudinese
		team.home2udinese=chievo.home2udinese
		team.home1genoa=chievo.home1genoa
		team.homexgenoa=chievo.homexgenoa
		team.home2genoa=chievo.home2genoa
		team.home1sampdoria=chievo.home1sampdoria
		team.homexsampdoria=chievo.homexsampdoria
		team.home2sampdoria=chievo.home2sampdoria
		team.home1chievo=chievo.home1chievo
		team.homexchievo=chievo.homexchievo
		team.home2chievo=chievo.home2chievo
		team.home1atalanta=chievo.home1atalanta
		team.homexatalanta=chievo.homexatalanta
		team.home2atalanta=chievo.home2atalanta
		team.home1torino=chievo.home1torino
		team.homextorino=chievo.homextorino
		team.home2torino=chievo.home2torino
	if team.name == "Fiorentina" :
		team.homeWins3Years=fiorentina.homeWins3Years
		team.homeDraws3Years=fiorentina.homeDraws3Years
		team.homeLoses3Years=fiorentina.homeLoses3Years
		team.awayWins3Years=fiorentina.awayWins3Years
		team.awayDraws3Years=fiorentina.awayDraws3Years
		team.awayLoses3Years=fiorentina.awayLoses3Years
		team.home1milan=fiorentina.home1milan
		team.homexmilan=fiorentina.homexmilan
		team.home2milan=fiorentina.home2milan
		team.home1inter=fiorentina.home1inter
		team.homexinter=fiorentina.homexinter
		team.home2inter=fiorentina.home2inter
		team.home1juventus=fiorentina.home1juventus
		team.homexjuventus=fiorentina.homexjuventus
		team.home2juventus=fiorentina.home2juventus
		team.home1lazio=fiorentina.home1lazio
		team.homexlazio=fiorentina.homexlazio
		team.home2lazio=fiorentina.home2lazio
		team.home1roma=fiorentina.home1roma
		team.homexroma=fiorentina.homexroma
		team.home2roma=fiorentina.home2roma
		team.home1napoli=fiorentina.home1napoli
		team.homexnapoli=fiorentina.homexnapoli
		team.home2napoli=fiorentina.home2napoli
		team.home1fiorentina=fiorentina.home1fiorentina
		team.homexfiorentina=fiorentina.homexfiorentina
		team.home2fiorentina=fiorentina.home2fiorentina
		team.home1udinese=fiorentina.home1udinese
		team.homexudinese=fiorentina.homexudinese
		team.home2udinese=fiorentina.home2udinese
		team.home1genoa=fiorentina.home1genoa
		team.homexgenoa=fiorentina.homexgenoa
		team.home2genoa=fiorentina.home2genoa
		team.home1sampdoria=fiorentina.home1sampdoria
		team.homexsampdoria=fiorentina.homexsampdoria
		team.home2sampdoria=fiorentina.home2sampdoria
		team.home1chievo=fiorentina.home1chievo
		team.homexchievo=fiorentina.homexchievo
		team.home2chievo=fiorentina.home2chievo
		team.home1atalanta=fiorentina.home1atalanta
		team.homexatalanta=fiorentina.homexatalanta
		team.home2atalanta=fiorentina.home2atalanta
		team.home1torino=fiorentina.home1torino
		team.homextorino=fiorentina.homextorino
		team.home2torino=fiorentina.home2torino
	if team.name == "Genoa" :
		team.homeWins3Years=genoa.homeWins3Years
		team.homeDraws3Years=genoa.homeDraws3Years
		team.homeLoses3Years=genoa.homeLoses3Years
		team.awayWins3Years=genoa.awayWins3Years
		team.awayDraws3Years=genoa.awayDraws3Years
		team.awayLoses3Years=genoa.awayLoses3Years
		team.home1milan=genoa.home1milan
		team.homexmilan=genoa.homexmilan
		team.home2milan=genoa.home2milan
		team.home1inter=genoa.home1inter
		team.homexinter=genoa.homexinter
		team.home2inter=genoa.home2inter
		team.home1juventus=genoa.home1juventus
		team.homexjuventus=genoa.homexjuventus
		team.home2juventus=genoa.home2juventus
		team.home1lazio=genoa.home1lazio
		team.homexlazio=genoa.homexlazio
		team.home2lazio=genoa.home2lazio
		team.home1roma=genoa.home1roma
		team.homexroma=genoa.homexroma
		team.home2roma=genoa.home2roma
		team.home1napoli=genoa.home1napoli
		team.homexnapoli=genoa.homexnapoli
		team.home2napoli=genoa.home2napoli
		team.home1fiorentina=genoa.home1fiorentina
		team.homexfiorentina=genoa.homexfiorentina
		team.home2fiorentina=genoa.home2fiorentina
		team.home1udinese=genoa.home1udinese
		team.homexudinese=genoa.homexudinese
		team.home2udinese=genoa.home2udinese
		team.home1genoa=genoa.home1genoa
		team.homexgenoa=genoa.homexgenoa
		team.home2genoa=genoa.home2genoa
		team.home1sampdoria=genoa.home1sampdoria
		team.homexsampdoria=genoa.homexsampdoria
		team.home2sampdoria=genoa.home2sampdoria
		team.home1chievo=genoa.home1chievo
		team.homexchievo=genoa.homexchievo
		team.home2chievo=genoa.home2chievo
		team.home1atalanta=genoa.home1atalanta
		team.homexatalanta=genoa.homexatalanta
		team.home2atalanta=genoa.home2atalanta
		team.home1torino=genoa.home1torino
		team.homextorino=genoa.homextorino
		team.home2torino=genoa.home2torino
	if team.name == "Inter" :
                team.homeWins3Years=inter.homeWins3Years
                team.homeDraws3Years=inter.homeDraws3Years
                team.homeLoses3Years=inter.homeLoses3Years
                team.awayWins3Years=inter.awayWins3Years
                team.awayDraws3Years=inter.awayDraws3Years
                team.awayLoses3Years=inter.awayLoses3Years
                team.home1milan=inter.home1milan
                team.homexmilan=inter.homexmilan
                team.home2milan=inter.home2milan
                team.home1inter=inter.home1inter
                team.homexinter=inter.homexinter
                team.home2inter=inter.home2inter
                team.home1juventus=inter.home1juventus
                team.homexjuventus=inter.homexjuventus
                team.home2juventus=inter.home2juventus
                team.home1lazio=inter.home1lazio
                team.homexlazio=inter.homexlazio
                team.home2lazio=inter.home2lazio
                team.home1roma=inter.home1roma
                team.homexroma=inter.homexroma
                team.home2roma=inter.home2roma
                team.home1napoli=inter.home1napoli
                team.homexnapoli=inter.homexnapoli
                team.home2napoli=inter.home2napoli
                team.home1fiorentina=inter.home1fiorentina
                team.homexfiorentina=inter.homexfiorentina
                team.home2fiorentina=inter.home2fiorentina
                team.home1udinese=inter.home1udinese
                team.homexudinese=inter.homexudinese
                team.home2udinese=inter.home2udinese
                team.home1genoa=inter.home1genoa
                team.homexgenoa=inter.homexgenoa
                team.home2genoa=inter.home2genoa
                team.home1sampdoria=inter.home1sampdoria
                team.homexsampdoria=inter.homexsampdoria
                team.home2sampdoria=inter.home2sampdoria
                team.home1chievo=inter.home1chievo
                team.homexchievo=inter.homexchievo
                team.home2chievo=inter.home2chievo
                team.home1atalanta=inter.home1atalanta
                team.homexatalanta=inter.homexatalanta
                team.home2atalanta=inter.home2atalanta
                team.home1torino=inter.home1torino
                team.homextorino=inter.homextorino
                team.home2torino=inter.home2torino
	if team.name == "Lazio" :
		team.homeWins3Years=lazio.homeWins3Years
		team.homeDraws3Years=lazio.homeDraws3Years
		team.homeLoses3Years=lazio.homeLoses3Years
		team.awayWins3Years=lazio.awayWins3Years
		team.awayDraws3Years=lazio.awayDraws3Years
		team.awayLoses3Years=lazio.awayLoses3Years
		team.home1milan=lazio.home1milan
		team.homexmilan=lazio.homexmilan
		team.home2milan=lazio.home2milan
		team.home1inter=lazio.home1inter
		team.homexinter=lazio.homexinter
		team.home2inter=lazio.home2inter
		team.home1juventus=lazio.home1juventus
		team.homexjuventus=lazio.homexjuventus
		team.home2juventus=lazio.home2juventus
		team.home1lazio=lazio.home1lazio
		team.homexlazio=lazio.homexlazio
		team.home2lazio=lazio.home2lazio
		team.home1roma=lazio.home1roma
		team.homexroma=lazio.homexroma
		team.home2roma=lazio.home2roma
		team.home1napoli=lazio.home1napoli
		team.homexnapoli=lazio.homexnapoli
		team.home2napoli=lazio.home2napoli
		team.home1fiorentina=lazio.home1fiorentina
		team.homexfiorentina=lazio.homexfiorentina
		team.home2fiorentina=lazio.home2fiorentina
		team.home1udinese=lazio.home1udinese
		team.homexudinese=lazio.homexudinese
		team.home2udinese=lazio.home2udinese
		team.home1genoa=lazio.home1genoa
		team.homexgenoa=lazio.homexgenoa
		team.home2genoa=lazio.home2genoa
		team.home1sampdoria=lazio.home1sampdoria
		team.homexsampdoria=lazio.homexsampdoria
		team.home2sampdoria=lazio.home2sampdoria
		team.home1chievo=lazio.home1chievo
		team.homexchievo=lazio.homexchievo
		team.home2chievo=lazio.home2chievo
		team.home1atalanta=lazio.home1atalanta
		team.homexatalanta=lazio.homexatalanta
		team.home2atalanta=lazio.home2atalanta
		team.home1torino=lazio.home1torino
		team.homextorino=lazio.homextorino
		team.home2torino=lazio.home2torino
	if team.name == "Milan" :
		team.homeWins3Years=milan.homeWins3Years
		team.homeDraws3Years=milan.homeDraws3Years
		team.homeLoses3Years=milan.homeLoses3Years
		team.awayWins3Years=milan.awayWins3Years
		team.awayDraws3Years=milan.awayDraws3Years
		team.awayLoses3Years=milan.awayLoses3Years
		team.home1milan=milan.home1milan
		team.homexmilan=milan.homexmilan
		team.home2milan=milan.home2milan
		team.home1inter=milan.home1inter
		team.homexinter=milan.homexinter
		team.home2inter=milan.home2inter
		team.home1juventus=milan.home1juventus
		team.homexjuventus=milan.homexjuventus
		team.home2juventus=milan.home2juventus
		team.home1lazio=milan.home1lazio
		team.homexlazio=milan.homexlazio
		team.home2lazio=milan.home2lazio
		team.home1roma=milan.home1roma
		team.homexroma=milan.homexroma
		team.home2roma=milan.home2roma
		team.home1napoli=milan.home1napoli
		team.homexnapoli=milan.homexnapoli
		team.home2napoli=milan.home2napoli
		team.home1fiorentina=milan.home1fiorentina
		team.homexfiorentina=milan.homexfiorentina
		team.home2fiorentina=milan.home2fiorentina
		team.home1udinese=milan.home1udinese
		team.homexudinese=milan.homexudinese
		team.home2udinese=milan.home2udinese
		team.home1genoa=milan.home1genoa
		team.homexgenoa=milan.homexgenoa
		team.home2genoa=milan.home2genoa
		team.home1sampdoria=milan.home1sampdoria
		team.homexsampdoria=milan.homexsampdoria
		team.home2sampdoria=milan.home2sampdoria
		team.home1chievo=milan.home1chievo
		team.homexchievo=milan.homexchievo
		team.home2chievo=milan.home2chievo
		team.home1atalanta=milan.home1atalanta
		team.homexatalanta=milan.homexatalanta
		team.home2atalanta=milan.home2atalanta
		team.home1torino=milan.home1torino
		team.homextorino=milan.homextorino
		team.home2torino=milan.home2torino	
	if team.name == "Napoli" :
		team.homeWins3Years=napoli.homeWins3Years
		team.homeDraws3Years=napoli.homeDraws3Years
		team.homeLoses3Years=napoli.homeLoses3Years
		team.awayWins3Years=napoli.awayWins3Years
		team.awayDraws3Years=napoli.awayDraws3Years
		team.awayLoses3Years=napoli.awayLoses3Years
		team.home1milan=napoli.home1milan
		team.homexmilan=napoli.homexmilan
		team.home2milan=napoli.home2milan
		team.home1inter=napoli.home1inter
		team.homexinter=napoli.homexinter
		team.home2inter=napoli.home2inter
		team.home1juventus=napoli.home1juventus
		team.homexjuventus=napoli.homexjuventus
		team.home2juventus=napoli.home2juventus
		team.home1lazio=napoli.home1lazio
		team.homexlazio=napoli.homexlazio
		team.home2lazio=napoli.home2lazio
		team.home1roma=napoli.home1roma
		team.homexroma=napoli.homexroma
		team.home2roma=napoli.home2roma
		team.home1napoli=napoli.home1napoli
		team.homexnapoli=napoli.homexnapoli
		team.home2napoli=napoli.home2napoli
		team.home1fiorentina=napoli.home1fiorentina
		team.homexfiorentina=napoli.homexfiorentina
		team.home2fiorentina=napoli.home2fiorentina
		team.home1udinese=napoli.home1udinese
		team.homexudinese=napoli.homexudinese
		team.home2udinese=napoli.home2udinese
		team.home1genoa=napoli.home1genoa
		team.homexgenoa=napoli.homexgenoa
		team.home2genoa=napoli.home2genoa
		team.home1sampdoria=napoli.home1sampdoria
		team.homexsampdoria=napoli.homexsampdoria
		team.home2sampdoria=napoli.home2sampdoria
		team.home1chievo=napoli.home1chievo
		team.homexchievo=napoli.homexchievo
		team.home2chievo=napoli.home2chievo
		team.home1atalanta=napoli.home1atalanta
		team.homexatalanta=napoli.homexatalanta
		team.home2atalanta=napoli.home2atalanta
		team.home1torino=napoli.home1torino
		team.homextorino=napoli.homextorino
		team.home2torino=napoli.home2torino
	if team.name == "Sampdoria" :
		team.homeWins3Years=sampdoria.homeWins3Years
		team.homeDraws3Years=sampdoria.homeDraws3Years
		team.homeLoses3Years=sampdoria.homeLoses3Years
		team.awayWins3Years=sampdoria.awayWins3Years
		team.awayDraws3Years=sampdoria.awayDraws3Years
		team.awayLoses3Years=sampdoria.awayLoses3Years
		team.home1milan=sampdoria.home1milan
		team.homexmilan=sampdoria.homexmilan
		team.home2milan=sampdoria.home2milan
		team.home1inter=sampdoria.home1inter
		team.homexinter=sampdoria.homexinter
		team.home2inter=sampdoria.home2inter
		team.home1juventus=sampdoria.home1juventus
		team.homexjuventus=sampdoria.homexjuventus
		team.home2juventus=sampdoria.home2juventus
		team.home1lazio=sampdoria.home1lazio
		team.homexlazio=sampdoria.homexlazio
		team.home2lazio=sampdoria.home2lazio
		team.home1roma=sampdoria.home1roma
		team.homexroma=sampdoria.homexroma
		team.home2roma=sampdoria.home2roma
		team.home1napoli=sampdoria.home1napoli
		team.homexnapoli=sampdoria.homexnapoli
		team.home2napoli=sampdoria.home2napoli
		team.home1fiorentina=sampdoria.home1fiorentina
		team.homexfiorentina=sampdoria.homexfiorentina
		team.home2fiorentina=sampdoria.home2fiorentina
		team.home1udinese=sampdoria.home1udinese
		team.homexudinese=sampdoria.homexudinese
		team.home2udinese=sampdoria.home2udinese
		team.home1genoa=sampdoria.home1genoa
		team.homexgenoa=sampdoria.homexgenoa
		team.home2genoa=sampdoria.home2genoa
		team.home1sampdoria=sampdoria.home1sampdoria
		team.homexsampdoria=sampdoria.homexsampdoria
		team.home2sampdoria=sampdoria.home2sampdoria
		team.home1chievo=sampdoria.home1chievo
		team.homexchievo=sampdoria.homexchievo
		team.home2chievo=sampdoria.home2chievo
		team.home1atalanta=sampdoria.home1atalanta
		team.homexatalanta=sampdoria.homexatalanta
		team.home2atalanta=sampdoria.home2atalanta
		team.home1torino=sampdoria.home1torino
		team.homextorino=sampdoria.homextorino
		team.home2torino=sampdoria.home2torino
	if team.name == "Torino" :
		team.homeWins3Years=torino.homeWins3Years
		team.homeDraws3Years=torino.homeDraws3Years
		team.homeLoses3Years=torino.homeLoses3Years
		team.awayWins3Years=torino.awayWins3Years
		team.awayDraws3Years=torino.awayDraws3Years
		team.awayLoses3Years=torino.awayLoses3Years
		team.home1milan=torino.home1milan
		team.homexmilan=torino.homexmilan
		team.home2milan=torino.home2milan
		team.home1inter=torino.home1inter
		team.homexinter=torino.homexinter
		team.home2inter=torino.home2inter
		team.home1juventus=torino.home1juventus
		team.homexjuventus=torino.homexjuventus
		team.home2juventus=torino.home2juventus
		team.home1lazio=torino.home1lazio
		team.homexlazio=torino.homexlazio
		team.home2lazio=torino.home2lazio
		team.home1roma=torino.home1roma
		team.homexroma=torino.homexroma
		team.home2roma=torino.home2roma
		team.home1napoli=torino.home1napoli
		team.homexnapoli=torino.homexnapoli
		team.home2napoli=torino.home2napoli
		team.home1fiorentina=torino.home1fiorentina
		team.homexfiorentina=torino.homexfiorentina
		team.home2fiorentina=torino.home2fiorentina
		team.home1udinese=torino.home1udinese
		team.homexudinese=torino.homexudinese
		team.home2udinese=torino.home2udinese
		team.home1genoa=torino.home1genoa
		team.homexgenoa=torino.homexgenoa
		team.home2genoa=torino.home2genoa
		team.home1sampdoria=torino.home1sampdoria
		team.homexsampdoria=torino.homexsampdoria
		team.home2sampdoria=torino.home2sampdoria
		team.home1chievo=torino.home1chievo
		team.homexchievo=torino.homexchievo
		team.home2chievo=torino.home2chievo
		team.home1atalanta=torino.home1atalanta
		team.homexatalanta=torino.homexatalanta
		team.home2atalanta=torino.home2atalanta
		team.home1torino=torino.home1torino
		team.homextorino=torino.homextorino
		team.home2torino=torino.home2torino
	if team.name == "Udinese" :
		team.homeWins3Years=udinese.homeWins3Years
		team.homeDraws3Years=udinese.homeDraws3Years
		team.homeLoses3Years=udinese.homeLoses3Years
		team.awayWins3Years=udinese.awayWins3Years
		team.awayDraws3Years=udinese.awayDraws3Years
		team.awayLoses3Years=udinese.awayLoses3Years
		team.home1milan=udinese.home1milan
		team.homexmilan=udinese.homexmilan
		team.home2milan=udinese.home2milan
		team.home1inter=udinese.home1inter
		team.homexinter=udinese.homexinter
		team.home2inter=udinese.home2inter
		team.home1juventus=udinese.home1juventus
		team.homexjuventus=udinese.homexjuventus
		team.home2juventus=udinese.home2juventus
		team.home1lazio=udinese.home1lazio
		team.homexlazio=udinese.homexlazio
		team.home2lazio=udinese.home2lazio
		team.home1roma=udinese.home1roma
		team.homexroma=udinese.homexroma
		team.home2roma=udinese.home2roma
		team.home1napoli=udinese.home1napoli
		team.homexnapoli=udinese.homexnapoli
		team.home2napoli=udinese.home2napoli
		team.home1fiorentina=udinese.home1fiorentina
		team.homexfiorentina=udinese.homexfiorentina
		team.home2fiorentina=udinese.home2fiorentina
		team.home1udinese=udinese.home1udinese
		team.homexudinese=udinese.homexudinese
		team.home2udinese=udinese.home2udinese
		team.home1genoa=udinese.home1genoa
		team.homexgenoa=udinese.homexgenoa
		team.home2genoa=udinese.home2genoa
		team.home1sampdoria=udinese.home1sampdoria
		team.homexsampdoria=udinese.homexsampdoria
		team.home2sampdoria=udinese.home2sampdoria
		team.home1chievo=udinese.home1chievo
		team.homexchievo=udinese.homexchievo
		team.home2chievo=udinese.home2chievo
		team.home1atalanta=udinese.home1atalanta
		team.homexatalanta=udinese.homexatalanta
		team.home2atalanta=udinese.home2atalanta
		team.home1torino=udinese.home1torino
		team.homextorino=udinese.homextorino
		team.home2torino=udinese.home2torino
	if team.name == "Juventus" :
		team.homeWins3Years=juventus.homeWins3Years
		team.homeDraws3Years=juventus.homeDraws3Years
		team.homeLoses3Years=juventus.homeLoses3Years
		team.awayWins3Years=juventus.awayWins3Years
		team.awayDraws3Years=juventus.awayDraws3Years
		team.awayLoses3Years=juventus.awayLoses3Years
		team.home1milan=juventus.home1milan
		team.homexmilan=juventus.homexmilan
		team.home2milan=juventus.home2milan
		team.home1inter=juventus.home1inter
		team.homexinter=juventus.homexinter
		team.home2inter=juventus.home2inter
		team.home1juventus=juventus.home1juventus
		team.homexjuventus=juventus.homexjuventus
		team.home2juventus=juventus.home2juventus
		team.home1lazio=juventus.home1lazio
		team.homexlazio=juventus.homexlazio
		team.home2lazio=juventus.home2lazio
		team.home1roma=juventus.home1roma
		team.homexroma=juventus.homexroma
		team.home2roma=juventus.home2roma
		team.home1napoli=juventus.home1napoli
		team.homexnapoli=juventus.homexnapoli
		team.home2napoli=juventus.home2napoli
		team.home1fiorentina=juventus.home1fiorentina
		team.homexfiorentina=juventus.homexfiorentina
		team.home2fiorentina=juventus.home2fiorentina
		team.home1udinese=juventus.home1udinese
		team.homexudinese=juventus.homexudinese
		team.home2udinese=juventus.home2udinese
		team.home1genoa=juventus.home1genoa
		team.homexgenoa=juventus.homexgenoa
		team.home2genoa=juventus.home2genoa
		team.home1sampdoria=juventus.home1sampdoria
		team.homexsampdoria=juventus.homexsampdoria
		team.home2sampdoria=juventus.home2sampdoria
		team.home1chievo=juventus.home1chievo
		team.homexchievo=juventus.homexchievo
		team.home2chievo=juventus.home2chievo
		team.home1atalanta=juventus.home1atalanta
		team.homexatalanta=juventus.homexatalanta
		team.home2atalanta=juventus.home2atalanta
		team.home1torino=juventus.home1torino
		team.homextorino=juventus.homextorino
		team.home2torino=juventus.home2torino
	if team.name == "Roma" :
		team.homeWins3Years=roma.homeWins3Years
		team.homeDraws3Years=roma.homeDraws3Years
		team.homeLoses3Years=roma.homeLoses3Years
		team.awayWins3Years=roma.awayWins3Years
		team.awayDraws3Years=roma.awayDraws3Years
		team.awayLoses3Years=roma.awayLoses3Years
		team.home1milan=roma.home1milan
		team.homexmilan=roma.homexmilan
		team.home2milan=roma.home2milan
		team.home1inter=roma.home1inter
		team.homexinter=roma.homexinter
		team.home2inter=roma.home2inter
		team.home1juventus=roma.home1juventus
		team.homexjuventus=roma.homexjuventus
		team.home2juventus=roma.home2juventus
		team.home1lazio=roma.home1lazio
		team.homexlazio=roma.homexlazio
		team.home2lazio=roma.home2lazio
		team.home1roma=roma.home1roma
		team.homexroma=roma.homexroma
		team.home2roma=roma.home2roma
		team.home1napoli=roma.home1napoli
		team.homexnapoli=roma.homexnapoli
		team.home2napoli=roma.home2napoli
		team.home1fiorentina=roma.home1fiorentina
		team.homexfiorentina=roma.homexfiorentina
		team.home2fiorentina=roma.home2fiorentina
		team.home1udinese=roma.home1udinese
		team.homexudinese=roma.homexudinese
		team.home2udinese=roma.home2udinese
		team.home1genoa=roma.home1genoa
		team.homexgenoa=roma.homexgenoa
		team.home2genoa=roma.home2genoa
		team.home1sampdoria=roma.home1sampdoria
		team.homexsampdoria=roma.homexsampdoria
		team.home2sampdoria=roma.home2sampdoria
		team.home1chievo=roma.home1chievo
		team.homexchievo=roma.homexchievo
		team.home2chievo=roma.home2chievo
		team.home1atalanta=roma.home1atalanta
		team.homexatalanta=roma.homexatalanta
		team.home2atalanta=roma.home2atalanta
		team.home1torino=roma.home1torino
		team.homextorino=roma.homextorino
		team.home2torino=roma.home2torino


def get5meetingswins(home, away) :
        if home == "Atalanta":
                if away == "Atalanta":
                        return atalanta.home1atalanta
                if away == "Chievo":
                        return atalanta.home1chievo
                if away == "Fiorentina":
                        return atalanta.home1fiorentina
                if away == "Genoa":
                        return atalanta.home1genoa
                if away == "Inter":
                        return atalanta.home1inter
                if away == "Juventus":
                        return atalanta.home1juventus
                if away == "Lazio":
                        return atalanta.home1lazio
                if away == "Milan":
                        return atalanta.home1milan
                if away == "Napoli":
                        return atalanta.home1napoli
                if away == "Roma":
                        return atalanta.home1roma
                if away == "Sampdoria":
                        return atalanta.home1sampdoria
                if away == "Torino":
                        return atalanta.home1torino
                if away == "Udinese":
                        return atalanta.home1udinese
        if home == "Chievo":
                if away == "Atalanta":
                        return chievo.home1atalanta
                if away == "Chievo":
                        return chievo.home1chievo
                if away == "Fiorentina":
                        return chievo.home1fiorentina
                if away == "Genoa":
                        return chievo.home1genoa
                if away == "Inter":
                        return chievo.home1inter
                if away == "Juventus":
                        return chievo.home1juventus
                if away == "Lazio":
                        return chievo.home1lazio
                if away == "Milan":
                        return chievo.home1milan
                if away == "Napoli":
                        return chievo.home1napoli
                if away == "Roma":
                        return chievo.home1roma
                if away == "Sampdoria":
                        return chievo.home1sampdoria
                if away == "Torino":
                        return chievo.home1torino
                if away == "Udinese":
                        return chievo.home1udinese
        if home == "Fiorentina":
                if away == "Atalanta":
                        return fiorentina.home1atalanta
                if away == "Chievo":
                        return fiorentina.home1chievo
                if away == "Fiorentina":
                        return fiorentina.home1fiorentina
                if away == "Genoa":
                        return fiorentina.home1genoa
                if away == "Inter":
                        return fiorentina.home1inter
                if away == "Juventus":
                        return fiorentina.home1juventus
                if away == "Lazio":
                        return fiorentina.home1lazio
                if away == "Milan":
                        return fiorentina.home1milan
                if away == "Napoli":
                        return fiorentina.home1napoli
                if away == "Roma":
                        return fiorentina.home1roma
                if away == "Sampdoria":
                        return fiorentina.home1sampdoria
                if away == "Torino":
                        return fiorentina.home1torino
                if away == "Udinese":
                        return fiorentina.home1udinese
        if home == "Genoa":
                if away == "Atalanta":
                        return genoa.home1atalanta
                if away == "Chievo":
                        return genoa.home1chievo
                if away == "Fiorentina":
                        return genoa.home1fiorentina
                if away == "Genoa":
                        return genoa.home1genoa
                if away == "Inter":
                        return genoa.home1inter
                if away == "Juventus":
                        return genoa.home1juventus
                if away == "Lazio":
                        return genoa.home1lazio
                if away == "Milan":
                        return genoa.home1milan
                if away == "Napoli":
                        return genoa.home1napoli
                if away == "Roma":
                        return genoa.home1roma
                if away == "Sampdoria":
                        return genoa.home1sampdoria
                if away == "Torino":
                        return genoa.home1torino
                if away == "Udinese":
                        return genoa.home1udinese
        if home == "Inter":
                if away == "Atalanta":
                        return inter.home1atalanta
                if away == "Chievo":
                        return inter.home1chievo
                if away == "Fiorentina":
                        return inter.home1fiorentina
                if away == "Genoa":
                        return inter.home1genoa
                if away == "Inter":
                        return inter.home1inter
                if away == "Juventus":
                        return inter.home1juventus
                if away == "Lazio":
                        return inter.home1lazio
                if away == "Milan":
                        return inter.home1milan
                if away == "Napoli":
                        return inter.home1napoli
                if away == "Roma":
                        return inter.home1roma
                if away == "Sampdoria":
                        return inter.home1sampdoria
                if away == "Torino":
                        return inter.home1torino
                if away == "Udinese":
                        return inter.home1udinese
        if home == "Juventus":
                if away == "Atalanta":
                        return juventus.home1atalanta
                if away == "Chievo":
                        return juventus.home1chievo
                if away == "Fiorentina":
                        return juventus.home1fiorentina
                if away == "Genoa":
                        return juventus.home1genoa
                if away == "Inter":
                        return juventus.home1inter
                if away == "Juventus":
                        return juventus.home1juventus
                if away == "Lazio":
                        return juventus.home1lazio
                if away == "Milan":
                        return juventus.home1milan
                if away == "Napoli":
                        return juventus.home1napoli
                if away == "Roma":
                        return juventus.home1roma
                if away == "Sampdoria":
                        return juventus.home1sampdoria
                if away == "Torino":
                        return juventus.home1torino
                if away == "Udinese":
                        return juventus.home1udinese
        if home == "Lazio":
                if away == "Atalanta":
                        return lazio.home1atalanta
                if away == "Chievo":
                        return lazio.home1chievo
                if away == "Fiorentina":
                        return lazio.home1fiorentina
                if away == "Genoa":
                        return lazio.home1genoa
                if away == "Inter":
                        return lazio.home1inter
                if away == "Juventus":
                        return lazio.home1juventus
                if away == "Lazio":
                        return lazio.home1lazio
                if away == "Milan":
                        return lazio.home1milan
                if away == "Napoli":
                        return lazio.home1napoli
                if away == "Roma":
                        return lazio.home1roma
                if away == "Sampdoria":
                        return lazio.home1sampdoria
                if away == "Torino":
                        return lazio.home1torino
                if away == "Udinese":
                        return lazio.home1udinese
        if home == "Milan":
                if away == "Atalanta":
                        return milan.home1atalanta
                if away == "Chievo":
                        return milan.home1chievo
                if away == "Fiorentina":
                        return milan.home1fiorentina
                if away == "Genoa":
                        return milan.home1genoa
                if away == "Inter":
                        return milan.home1inter
                if away == "Juventus":
                        return milan.home1juventus
                if away == "Lazio":
                        return milan.home1lazio
                if away == "Milan":
                        return milan.home1milan
                if away == "Napoli":
                        return milan.home1napoli
                if away == "Roma":
                        return milan.home1roma
                if away == "Sampdoria":
                        return milan.home1sampdoria
                if away == "Torino":
                        return milan.home1torino
                if away == "Udinese":
                        return milan.home1udinese
        if home == "Napoli":
                if away == "Atalanta":
                        return napoli.home1atalanta
                if away == "Chievo":
                        return napoli.home1chievo
                if away == "Fiorentina":
                        return napoli.home1fiorentina
                if away == "Genoa":
                        return napoli.home1genoa
                if away == "Inter":
                        return napoli.home1inter
                if away == "Juventus":
                        return napoli.home1juventus
                if away == "Lazio":
                        return napoli.home1lazio
                if away == "Milan":
                        return napoli.home1milan
                if away == "Napoli":
                        return napoli.home1napoli
                if away == "Roma":
                        return napoli.home1roma
                if away == "Sampdoria":
                        return napoli.home1sampdoria
                if away == "Torino":
                        return napoli.home1torino
                if away == "Udinese":
                        return napoli.home1udinese
        if home == "Roma":
                if away == "Atalanta":
                        return roma.home1atalanta
                if away == "Chievo":
                        return roma.home1chievo
                if away == "Fiorentina":
                        return roma.home1fiorentina
                if away == "Genoa":
                        return roma.home1genoa
                if away == "Inter":
                        return roma.home1inter
                if away == "Juventus":
                        return roma.home1juventus
                if away == "Lazio":
                        return roma.home1lazio
                if away == "Milan":
                        return roma.home1milan
                if away == "Napoli":
                        return roma.home1napoli
                if away == "Roma":
                        return roma.home1roma
                if away == "Sampdoria":
                        return roma.home1sampdoria
                if away == "Torino":
                        return roma.home1torino
                if away == "Udinese":
                        return roma.home1udinese
        if home == "Sampdoria":
                if away == "Atalanta":
                        return sampdoria.home1atalanta
                if away == "Chievo":
                        return sampdoria.home1chievo
                if away == "Fiorentina":
                        return sampdoria.home1fiorentina
                if away == "Genoa":
                        return sampdoria.home1genoa
                if away == "Inter":
                        return sampdoria.home1inter
                if away == "Juventus":
                        return sampdoria.home1juventus
                if away == "Lazio":
                        return sampdoria.home1lazio
                if away == "Milan":
                        return sampdoria.home1milan
                if away == "Napoli":
                        return sampdoria.home1napoli
                if away == "Roma":
                        return sampdoria.home1roma
                if away == "Sampdoria":
                        return sampdoria.home1sampdoria
                if away == "Torino":
                        return sampdoria.home1torino
                if away == "Udinese":
                        return sampdoria.home1udinese
        if home == "Torino":
                if away == "Atalanta":
                        return torino.home1atalanta
                if away == "Chievo":
                        return torino.home1chievo
                if away == "Fiorentina":
                        return torino.home1fiorentina
                if away == "Genoa":
                        return torino.home1genoa
                if away == "Inter":
                        return torino.home1inter
                if away == "Juventus":
                        return torino.home1juventus
                if away == "Lazio":
                        return torino.home1lazio
                if away == "Milan":
                        return torino.home1milan
                if away == "Napoli":
                        return torino.home1napoli
                if away == "Roma":
                        return torino.home1roma
                if away == "Sampdoria":
                        return torino.home1sampdoria
                if away == "Torino":
                        return torino.home1torino
                if away == "Udinese":
                        return torino.home1udinese
        if home == "Udinese":
                if away == "Atalanta":
                        return udinese.home1atalanta
                if away == "Chievo":
                        return udinese.home1chievo
                if away == "Fiorentina":
                        return udinese.home1fiorentina
                if away == "Genoa":
                        return udinese.home1genoa
                if away == "Inter":
                        return udinese.home1inter
                if away == "Juventus":
                        return udinese.home1juventus
                if away == "Lazio":
                        return udinese.home1lazio
                if away == "Milan":
                        return udinese.home1milan
                if away == "Napoli":
                        return udinese.home1napoli
                if away == "Roma":
                        return udinese.home1roma
                if away == "Sampdoria":
                        return udinese.home1sampdoria
                if away == "Torino":
                        return udinese.home1torino
                if away == "Udinese":
                        return udinese.home1udinese

def get5meetingsdraws(home, away) :
        if home == "Atalanta":
                if away == "Atalanta":
                        return atalanta.homexatalanta
                if away == "Chievo":
                        return atalanta.homexchievo
                if away == "Fiorentina":
                        return atalanta.homexfiorentina
                if away == "Genoa":
                        return atalanta.homexgenoa
                if away == "Inter":
                        return atalanta.homexinter
                if away == "Juventus":
                        return atalanta.homexjuventus
                if away == "Lazio":
                        return atalanta.homexlazio
                if away == "Milan":
                        return atalanta.homexmilan
                if away == "Napoli":
                        return atalanta.homexnapoli
                if away == "Roma":
                        return atalanta.homexroma
                if away == "Sampdoria":
                        return atalanta.homexsampdoria
                if away == "Torino":
                        return atalanta.homextorino
                if away == "Udinese":
                        return atalanta.homexudinese
        if home == "Chievo":
                if away == "Atalanta":
                        return chievo.homexatalanta
                if away == "Chievo":
                        return chievo.homexchievo
                if away == "Fiorentina":
                        return chievo.homexfiorentina
                if away == "Genoa":
                        return chievo.homexgenoa
                if away == "Inter":
                        return chievo.homexinter
                if away == "Juventus":
                        return chievo.homexjuventus
                if away == "Lazio":
                        return chievo.homexlazio
                if away == "Milan":
                        return chievo.homexmilan
                if away == "Napoli":
                        return chievo.homexnapoli
                if away == "Roma":
                        return chievo.homexroma
                if away == "Sampdoria":
                        return chievo.homexsampdoria
                if away == "Torino":
                        return chievo.homextorino
                if away == "Udinese":
                        return chievo.homexudinese
        if home == "Fiorentina":
                if away == "Atalanta":
                        return fiorentina.homexatalanta
                if away == "Chievo":
                        return fiorentina.homexchievo
                if away == "Fiorentina":
                        return fiorentina.homexfiorentina
                if away == "Genoa":
                        return fiorentina.homexgenoa
                if away == "Inter":
                        return fiorentina.homexinter
                if away == "Juventus":
                        return fiorentina.homexjuventus
                if away == "Lazio":
                        return fiorentina.homexlazio
                if away == "Milan":
                        return fiorentina.homexmilan
                if away == "Napoli":
                        return fiorentina.homexnapoli
                if away == "Roma":
                        return fiorentina.homexroma
                if away == "Sampdoria":
                        return fiorentina.homexsampdoria
                if away == "Torino":
                        return fiorentina.homextorino
                if away == "Udinese":
                        return fiorentina.homexudinese
        if home == "Genoa":
                if away == "Atalanta":
                        return genoa.homexatalanta
                if away == "Chievo":
                        return genoa.homexchievo
                if away == "Fiorentina":
                        return genoa.homexfiorentina
                if away == "Genoa":
                        return genoa.homexgenoa
                if away == "Inter":
                        return genoa.homexinter
                if away == "Juventus":
                        return genoa.homexjuventus
                if away == "Lazio":
                        return genoa.homexlazio
                if away == "Milan":
                        return genoa.homexmilan
                if away == "Napoli":
                        return genoa.homexnapoli
                if away == "Roma":
                        return genoa.homexroma
                if away == "Sampdoria":
                        return genoa.homexsampdoria
                if away == "Torino":
                        return genoa.homextorino
                if away == "Udinese":
                        return genoa.homexudinese
        if home == "Inter":
                if away == "Atalanta":
                        return inter.homexatalanta
                if away == "Chievo":
                        return inter.homexchievo
                if away == "Fiorentina":
                        return inter.homexfiorentina
                if away == "Genoa":
                        return inter.homexgenoa
                if away == "Inter":
                        return inter.homexinter
                if away == "Juventus":
                        return inter.homexjuventus
                if away == "Lazio":
                        return inter.homexlazio
                if away == "Milan":
                        return inter.homexmilan
                if away == "Napoli":
                        return inter.homexnapoli
                if away == "Roma":
                        return inter.homexroma
                if away == "Sampdoria":
                        return inter.homexsampdoria
                if away == "Torino":
                        return inter.homextorino
                if away == "Udinese":
                        return inter.homexudinese
        if home == "Juventus":
                if away == "Atalanta":
                        return juventus.homexatalanta
                if away == "Chievo":
                        return juventus.homexchievo
                if away == "Fiorentina":
                        return juventus.homexfiorentina
                if away == "Genoa":
                        return juventus.homexgenoa
                if away == "Inter":
                        return juventus.homexinter
                if away == "Juventus":
                        return juventus.homexjuventus
                if away == "Lazio":
                        return juventus.homexlazio
                if away == "Milan":
                        return juventus.homexmilan
                if away == "Napoli":
                        return juventus.homexnapoli
                if away == "Roma":
                        return juventus.homexroma
                if away == "Sampdoria":
                        return juventus.homexsampdoria
                if away == "Torino":
                        return juventus.homextorino
                if away == "Udinese":
                        return juventus.homexudinese
        if home == "Lazio":
                if away == "Atalanta":
                        return lazio.homexatalanta
                if away == "Chievo":
                        return lazio.homexchievo
                if away == "Fiorentina":
                        return lazio.homexfiorentina
                if away == "Genoa":
                        return lazio.homexgenoa
                if away == "Inter":
                        return lazio.homexinter
                if away == "Juventus":
                        return lazio.homexjuventus
                if away == "Lazio":
                        return lazio.homexlazio
                if away == "Milan":
                        return lazio.homexmilan
                if away == "Napoli":
                        return lazio.homexnapoli
                if away == "Roma":
                        return lazio.homexroma
                if away == "Sampdoria":
                        return lazio.homexsampdoria
                if away == "Torino":
                        return lazio.homextorino
                if away == "Udinese":
                        return lazio.homexudinese
        if home == "Milan":
                if away == "Atalanta":
                        return milan.homexatalanta
                if away == "Chievo":
                        return milan.homexchievo
                if away == "Fiorentina":
                        return milan.homexfiorentina
                if away == "Genoa":
                        return milan.homexgenoa
                if away == "Inter":
                        return milan.homexinter
def meetings_draws(home, away) :
        if home == "Atalanta":
                if away == "Atalanta":
                        return atalanta.homexatalanta
                if away == "Chievo":
                        return atalanta.homexchievo
                if away == "Fiorentina":
                        return atalanta.homexfiorentina
                if away == "Genoa":
                        return atalanta.homexgenoa
                if away == "Inter":
                        return atalanta.homexinter
                if away == "Juventus":
                        return atalanta.homexjuventus
                if away == "Lazio":
                        return atalanta.homexlazio
                if away == "Milan":
                        return atalanta.homexmilan
                if away == "Napoli":
                        return atalanta.homexnapoli
                if away == "Roma":
                        return atalanta.homexroma
                if away == "Sampdoria":
                        return atalanta.homexsampdoria
                if away == "Torino":
                        return atalanta.homextorino
                if away == "Udinese":
                        return atalanta.homexudinese
        if home == "Chievo":
                if away == "Atalanta":
                        return chievo.homexatalanta
                if away == "Chievo":
                        return chievo.homexchievo
                if away == "Fiorentina":
                        return chievo.homexfiorentina
                if away == "Genoa":
                        return chievo.homexgenoa
                if away == "Inter":
                        return chievo.homexinter
                if away == "Juventus":
                        return chievo.homexjuventus
                if away == "Lazio":
                        return chievo.homexlazio
                if away == "Milan":
                        return chievo.homexmilan
                if away == "Napoli":
                        return chievo.homexnapoli
                if away == "Roma":
                        return chievo.homexroma
                if away == "Sampdoria":
                        return chievo.homexsampdoria
                if away == "Torino":
                        return chievo.homextorino
                if away == "Udinese":
                        return chievo.homexudinese
        if home == "Fiorentina":
                if away == "Atalanta":
                        return fiorentina.homexatalanta
                if away == "Chievo":
                        return fiorentina.homexchievo
                if away == "Fiorentina":
                        return fiorentina.homexfiorentina
                if away == "Genoa":
                        return fiorentina.homexgenoa
                if away == "Inter":
                        return fiorentina.homexinter
                if away == "Juventus":
                        return fiorentina.homexjuventus
                if away == "Lazio":
                        return fiorentina.homexlazio
                if away == "Milan":
                        return fiorentina.homexmilan
                if away == "Napoli":
                        return fiorentina.homexnapoli
                if away == "Roma":
                        return fiorentina.homexroma
                if away == "Sampdoria":
                        return fiorentina.homexsampdoria
                if away == "Torino":
                        return fiorentina.homextorino
                if away == "Udinese":
                        return fiorentina.homexudinese
        if home == "Genoa":
                if away == "Atalanta":
                        return genoa.homexatalanta
                if away == "Chievo":
                        return genoa.homexchievo
                if away == "Fiorentina":
                        return genoa.homexfiorentina
                if away == "Genoa":
                        return genoa.homexgenoa
                if away == "Inter":
                        return genoa.homexinter
                if away == "Juventus":
                        return genoa.homexjuventus
                if away == "Lazio":
                        return genoa.homexlazio
                if away == "Milan":
                        return genoa.homexmilan
                if away == "Napoli":
                        return genoa.homexnapoli
                if away == "Roma":
                        return genoa.homexroma
                if away == "Sampdoria":
                        return genoa.homexsampdoria
                if away == "Torino":
                        return genoa.homextorino
                if away == "Udinese":
                        return genoa.homexudinese
        if home == "Inter":
                if away == "Atalanta":
                        return inter.homexatalanta
                if away == "Chievo":
                        return inter.homexchievo
                if away == "Fiorentina":
                        return inter.homexfiorentina
                if away == "Genoa":
                        return inter.homexgenoa
                if away == "Inter":
                        return inter.homexinter
                if away == "Juventus":
                        return inter.homexjuventus
                if away == "Lazio":
                        return inter.homexlazio
                if away == "Milan":
                        return inter.homexmilan
                if away == "Napoli":
                        return inter.homexnapoli
                if away == "Roma":
                        return inter.homexroma
                if away == "Sampdoria":
                        return inter.homexsampdoria
                if away == "Torino":
                        return inter.homextorino
                if away == "Udinese":
                        return inter.homexudinese
        if home == "Juventus":
                if away == "Atalanta":
                        return juventus.homexatalanta
                if away == "Chievo":
                        return juventus.homexchievo
                if away == "Fiorentina":
                        return juventus.homexfiorentina
                if away == "Genoa":
                        return juventus.homexgenoa
                if away == "Inter":
                        return juventus.homexinter
                if away == "Juventus":
                        return juventus.homexjuventus
                if away == "Lazio":
                        return juventus.homexlazio
                if away == "Milan":
                        return juventus.homexmilan
                if away == "Napoli":
                        return juventus.homexnapoli
                if away == "Roma":
                        return juventus.homexroma
                if away == "Sampdoria":
                        return juventus.homexsampdoria
                if away == "Torino":
                        return juventus.homextorino
                if away == "Udinese":
                        return juventus.homexudinese
        if home == "Lazio":
                if away == "Atalanta":
                        return lazio.homexatalanta
                if away == "Chievo":
                        return lazio.homexchievo
                if away == "Fiorentina":
                        return lazio.homexfiorentina
                if away == "Genoa":
                        return lazio.homexgenoa
                if away == "Inter":
                        return lazio.homexinter
                if away == "Juventus":
                        return lazio.homexjuventus
                if away == "Lazio":
                        return lazio.homexlazio
                if away == "Milan":
                        return lazio.homexmilan
                if away == "Napoli":
                        return lazio.homexnapoli
                if away == "Roma":
                        return lazio.homexroma
                if away == "Sampdoria":
                        return lazio.homexsampdoria
                if away == "Torino":
                        return lazio.homextorino
                if away == "Udinese":
                        return lazio.homexudinese
        if home == "Milan":
                if away == "Atalanta":
                        return milan.homexatalanta
                if away == "Chievo":
                        return milan.homexchievo
                if away == "Fiorentina":
                        return milan.homexfiorentina
                if away == "Genoa":
                        return milan.homexgenoa
                if away == "Inter":
                        return milan.homexinter
                if away == "Juventus":
                        return milan.homexjuventus
                if away == "Lazio":
                        return milan.homexlazio
                if away == "Milan":
                        return milan.homexmilan
                if away == "Napoli":
                        return milan.homexnapoli
                if away == "Roma":
                        return milan.homexroma
                if away == "Sampdoria":
                        return milan.homexsampdoria
                if away == "Torino":
                        return milan.homextorino
                if away == "Udinese":
                        return milan.homexudinese
        if home == "Napoli":
                if away == "Atalanta":
                        return napoli.homexatalanta
                if away == "Chievo":
                        return napoli.homexchievo
                if away == "Fiorentina":
                        return napoli.homexfiorentina
                if away == "Genoa":
                        return napoli.homexgenoa
                if away == "Inter":
                        return napoli.homexinter
                if away == "Juventus":
                        return napoli.homexjuventus
                if away == "Lazio":
                        return napoli.homexlazio
                if away == "Milan":
                        return napoli.homexmilan
                if away == "Napoli":
                        return napoli.homexnapoli
                if away == "Roma":
                        return napoli.homexroma
                if away == "Sampdoria":
                        return napoli.homexsampdoria
                if away == "Torino":
                        return napoli.homextorino
                if away == "Udinese":
                        return napoli.homexudinese
        if home == "Roma":
                if away == "Atalanta":
                        return roma.homexatalanta
                if away == "Chievo":
                        return roma.homexchievo
                if away == "Fiorentina":
                        return roma.homexfiorentina
                if away == "Genoa":
                        return roma.homexgenoa
                if away == "Inter":
                        return roma.homexinter
                if away == "Juventus":
                        return roma.homexjuventus
                if away == "Lazio":
                        return roma.homexlazio
                if away == "Milan":
                        return roma.homexmilan
                if away == "Napoli":
                        return roma.homexnapoli
                if away == "Roma":
                        return roma.homexroma
                if away == "Sampdoria":
                        return roma.homexsampdoria
                if away == "Torino":
                        return roma.homextorino
                if away == "Udinese":
                        return roma.homexudinese
        if home == "Sampdoria":
                if away == "Atalanta":
                        return sampdoria.homexatalanta
                if away == "Chievo":
                        return sampdoria.homexchievo
                if away == "Fiorentina":
                        return sampdoria.homexfiorentina
                if away == "Genoa":
                        return sampdoria.homexgenoa
                if away == "Inter":
                        return sampdoria.homexinter
                if away == "Juventus":
                        return sampdoria.homexjuventus
                if away == "Lazio":
                        return sampdoria.homexlazio
                if away == "Milan":
                        return sampdoria.homexmilan
                if away == "Napoli":
                        return sampdoria.homexnapoli
                if away == "Roma":
                        return sampdoria.homexroma
                if away == "Sampdoria":
                        return sampdoria.homexsampdoria
                if away == "Torino":
                        return sampdoria.homextorino
                if away == "Udinese":
                        return sampdoria.homexudinese
        if home == "Torino":
                if away == "Atalanta":
                        return torino.homexatalanta
                if away == "Chievo":
                        return torino.homexchievo
                if away == "Fiorentina":
                        return torino.homexfiorentina
                if away == "Genoa":
                        return torino.homexgenoa
                if away == "Inter":
                        return torino.homexinter
                if away == "Juventus":
                        return torino.homexjuventus
                if away == "Lazio":
                        return torino.homexlazio
                if away == "Milan":
                        return torino.homexmilan
                if away == "Napoli":
                        return torino.homexnapoli
                if away == "Roma":
                        return torino.homexroma
                if away == "Sampdoria":
                        return torino.homexsampdoria
                if away == "Torino":
                        return torino.homextorino
                if away == "Udinese":
                        return torino.homexudinese
        if home == "Udinese":
                if away == "Atalanta":
                        return udinese.homexatalanta
                if away == "Chievo":
                        return udinese.homexchievo
                if away == "Fiorentina":
                        return udinese.homexfiorentina
                if away == "Genoa":
                        return udinese.homexgenoa
                if away == "Inter":
                        return udinese.homexinter
                if away == "Juventus":
                        return udinese.homexjuventus
                if away == "Lazio":
                        return udinese.homexlazio
                if away == "Milan":
                        return udinese.homexmilan
                if away == "Napoli":
                        return udinese.homexnapoli
                if away == "Roma":
                        return udinese.homexroma
                if away == "Sampdoria":
                        return udinese.homexsampdoria
                if away == "Torino":
                        return udinese.homextorino
                if away == "Udinese":
                        return udinese.homexudinese
                if away == "Juventus":
                        return milan.homexjuventus
                if away == "Lazio":
                        return milan.homexlazio
                if away == "Milan":
                        return milan.homexmilan
                if away == "Napoli":
                        return milan.homexnapoli
                if away == "Roma":
                        return milan.homexroma
                if away == "Sampdoria":
                        return milan.homexsampdoria
                if away == "Torino":
                        return milan.homextorino
                if away == "Udinese":
                        return milan.homexudinese
        if home == "Napoli":
                if away == "Atalanta":
                        return napoli.homexatalanta
                if away == "Chievo":
                        return napoli.homexchievo
                if away == "Fiorentina":
                        return napoli.homexfiorentina
                if away == "Genoa":
                        return napoli.homexgenoa
                if away == "Inter":
                        return napoli.homexinter
                if away == "Juventus":
                        return napoli.homexjuventus
                if away == "Lazio":
                        return napoli.homexlazio
                if away == "Milan":
                        return napoli.homexmilan
                if away == "Napoli":
                        return napoli.homexnapoli
                if away == "Roma":
                        return napoli.homexroma
                if away == "Sampdoria":
                        return napoli.homexsampdoria
                if away == "Torino":
                        return napoli.homextorino
                if away == "Udinese":
                        return napoli.homexudinese
        if home == "Roma":
                if away == "Atalanta":
                        return roma.homexatalanta
                if away == "Chievo":
                        return roma.homexchievo
                if away == "Fiorentina":
                        return roma.homexfiorentina
                if away == "Genoa":
                        return roma.homexgenoa
                if away == "Inter":
                        return roma.homexinter
                if away == "Juventus":
                        return roma.homexjuventus
                if away == "Lazio":
                        return roma.homexlazio
                if away == "Milan":
                        return roma.homexmilan
                if away == "Napoli":
                        return roma.homexnapoli
                if away == "Roma":
                        return roma.homexroma
                if away == "Sampdoria":
                        return roma.homexsampdoria
                if away == "Torino":
                        return roma.homextorino
                if away == "Udinese":
                        return roma.homexudinese
        if home == "Sampdoria":
                if away == "Atalanta":
                        return sampdoria.homexatalanta
                if away == "Chievo":
                        return sampdoria.homexchievo
                if away == "Fiorentina":
                        return sampdoria.homexfiorentina
                if away == "Genoa":
                        return sampdoria.homexgenoa
                if away == "Inter":
                        return sampdoria.homexinter
                if away == "Juventus":
                        return sampdoria.homexjuventus
                if away == "Lazio":
                        return sampdoria.homexlazio
                if away == "Milan":
                        return sampdoria.homexmilan
                if away == "Napoli":
                        return sampdoria.homexnapoli
                if away == "Roma":
                        return sampdoria.homexroma
                if away == "Sampdoria":
                        return sampdoria.homexsampdoria
                if away == "Torino":
                        return sampdoria.homextorino
                if away == "Udinese":
                        return sampdoria.homexudinese
        if home == "Torino":
                if away == "Atalanta":
                        return torino.homexatalanta
                if away == "Chievo":
                        return torino.homexchievo
                if away == "Fiorentina":
                        return torino.homexfiorentina
                if away == "Genoa":
                        return torino.homexgenoa
                if away == "Inter":
                        return torino.homexinter
                if away == "Juventus":
                        return torino.homexjuventus
                if away == "Lazio":
                        return torino.homexlazio
                if away == "Milan":
                        return torino.homexmilan
                if away == "Napoli":
                        return torino.homexnapoli
                if away == "Roma":
                        return torino.homexroma
                if away == "Sampdoria":
                        return torino.homexsampdoria
                if away == "Torino":
                        return torino.homextorino
                if away == "Udinese":
                        return torino.homexudinese
        if home == "Udinese":
                if away == "Atalanta":
                        return udinese.homexatalanta
                if away == "Chievo":
                        return udinese.homexchievo
                if away == "Fiorentina":
                        return udinese.homexfiorentina
                if away == "Genoa":
                        return udinese.homexgenoa
                if away == "Inter":
                        return udinese.homexinter
                if away == "Juventus":
                        return udinese.homexjuventus
                if away == "Lazio":
                        return udinese.homexlazio
                if away == "Milan":
                        return udinese.homexmilan
                if away == "Napoli":
                        return udinese.homexnapoli
                if away == "Roma":
                        return udinese.homexroma
                if away == "Sampdoria":
                        return udinese.homexsampdoria
                if away == "Torino":
                        return udinese.homextorino
                if away == "Udinese":
                        return udinese.homexudinese
def get5meetingsloses(home, away) :
        if home == "Atalanta":
                if away == "Atalanta":
                        return atalanta.home2atalanta
                if away == "Chievo":
                        return atalanta.home2chievo
                if away == "Fiorentina":
                        return atalanta.home2fiorentina
                if away == "Genoa":
                        return atalanta.home2genoa
                if away == "Inter":
                        return atalanta.home2inter
                if away == "Juventus":
                        return atalanta.home2juventus
                if away == "Lazio":
                        return atalanta.home2lazio
                if away == "Milan":
                        return atalanta.home2milan
                if away == "Napoli":
                        return atalanta.home2napoli
                if away == "Roma":
                        return atalanta.home2roma
                if away == "Sampdoria":
                        return atalanta.home2sampdoria
                if away == "Torino":
                        return atalanta.home2torino
                if away == "Udinese":
                        return atalanta.home2udinese
        if home == "Chievo":
                if away == "Atalanta":
                        return chievo.home2atalanta
                if away == "Chievo":
                        return chievo.home2chievo
                if away == "Fiorentina":
                        return chievo.home2fiorentina
                if away == "Genoa":
                        return chievo.home2genoa
                if away == "Inter":
                        return chievo.home2inter
                if away == "Juventus":
                        return chievo.home2juventus
                if away == "Lazio":
                        return chievo.home2lazio
                if away == "Milan":
                        return chievo.home2milan
                if away == "Napoli":
                        return chievo.home2napoli
                if away == "Roma":
                        return chievo.home2roma
                if away == "Sampdoria":
                        return chievo.home2sampdoria
                if away == "Torino":
                        return chievo.home2torino
                if away == "Udinese":
                        return chievo.home2udinese
        if home == "Fiorentina":
                if away == "Atalanta":
                        return fiorentina.home2atalanta
                if away == "Chievo":
                        return fiorentina.home2chievo
                if away == "Fiorentina":
                        return fiorentina.home2fiorentina
                if away == "Genoa":
                        return fiorentina.home2genoa
                if away == "Inter":
                        return fiorentina.home2inter
                if away == "Juventus":
                        return fiorentina.home2juventus
                if away == "Lazio":
                        return fiorentina.home2lazio
                if away == "Milan":
                        return fiorentina.home2milan
                if away == "Napoli":
                        return fiorentina.home2napoli
                if away == "Roma":
                        return fiorentina.home2roma
                if away == "Sampdoria":
                        return fiorentina.home2sampdoria
                if away == "Torino":
                        return fiorentina.home2torino
                if away == "Udinese":
                        return fiorentina.home2udinese
        if home == "Genoa":
                if away == "Atalanta":
                        return genoa.home2atalanta
                if away == "Chievo":
                        return genoa.home2chievo
                if away == "Fiorentina":
                        return genoa.home2fiorentina
                if away == "Genoa":
                        return genoa.home2genoa
                if away == "Inter":
                        return genoa.home2inter
                if away == "Juventus":
                        return genoa.home2juventus
                if away == "Lazio":
                        return genoa.home2lazio
                if away == "Milan":
                        return genoa.home2milan
                if away == "Napoli":
                        return genoa.home2napoli
                if away == "Roma":
                        return genoa.home2roma
                if away == "Sampdoria":
                        return genoa.home2sampdoria
                if away == "Torino":
                        return genoa.home2torino
                if away == "Udinese":
                        return genoa.home2udinese
        if home == "Inter":
                if away == "Atalanta":
                        return inter.home2atalanta
                if away == "Chievo":
                        return inter.home2chievo
                if away == "Fiorentina":
                        return inter.home2fiorentina
                if away == "Genoa":
                        return inter.home2genoa
                if away == "Inter":
                        return inter.home2inter
                if away == "Juventus":
                        return inter.home2juventus
                if away == "Lazio":
                        return inter.home2lazio
                if away == "Milan":
                        return inter.home2milan
                if away == "Napoli":
                        return inter.home2napoli
                if away == "Roma":
                        return inter.home2roma
                if away == "Sampdoria":
                        return inter.home2sampdoria
                if away == "Torino":
                        return inter.home2torino
                if away == "Udinese":
                        return inter.home2udinese
        if home == "Juventus":
                if away == "Atalanta":
                        return juventus.home2atalanta
                if away == "Chievo":
                        return juventus.home2chievo
                if away == "Fiorentina":
                        return juventus.home2fiorentina
                if away == "Genoa":
                        return juventus.home2genoa
                if away == "Inter":
                        return juventus.home2inter
                if away == "Juventus":
                        return juventus.home2juventus
                if away == "Lazio":
                        return juventus.home2lazio
                if away == "Milan":
                        return juventus.home2milan
                if away == "Napoli":
                        return juventus.home2napoli
                if away == "Roma":
                        return juventus.home2roma
                if away == "Sampdoria":
                        return juventus.home2sampdoria
                if away == "Torino":
                        return juventus.home2torino
                if away == "Udinese":
                        return juventus.home2udinese
        if home == "Lazio":
                if away == "Atalanta":
                        return lazio.home2atalanta
                if away == "Chievo":
                        return lazio.home2chievo
                if away == "Fiorentina":
                        return lazio.home2fiorentina
                if away == "Genoa":
                        return lazio.home2genoa
                if away == "Inter":
                        return lazio.home2inter
                if away == "Juventus":
                        return lazio.home2juventus
                if away == "Lazio":
                        return lazio.home2lazio
                if away == "Milan":
                        return lazio.home2milan
                if away == "Napoli":
                        return lazio.home2napoli
                if away == "Roma":
                        return lazio.home2roma
                if away == "Sampdoria":
                        return lazio.home2sampdoria
                if away == "Torino":
                        return lazio.home2torino
                if away == "Udinese":
                        return lazio.home2udinese
        if home == "Milan":
                if away == "Atalanta":
                        return milan.home2atalanta
                if away == "Chievo":
                        return milan.home2chievo
                if away == "Fiorentina":
                        return milan.home2fiorentina
                if away == "Genoa":
                        return milan.home2genoa
                if away == "Inter":
                        return milan.home2inter
                if away == "Juventus":
                        return milan.home2juventus
                if away == "Lazio":
                        return milan.home2lazio
                if away == "Milan":
                        return milan.home2milan
                if away == "Napoli":
                        return milan.home2napoli
                if away == "Roma":
                        return milan.home2roma
                if away == "Sampdoria":
                        return milan.home2sampdoria
                if away == "Torino":
                        return milan.home2torino
                if away == "Udinese":
                        return milan.home2udinese
        if home == "Napoli":
                if away == "Atalanta":
                        return napoli.home2atalanta
                if away == "Chievo":
                        return napoli.home2chievo
                if away == "Fiorentina":
                        return napoli.home2fiorentina
                if away == "Genoa":
                        return napoli.home2genoa
                if away == "Inter":
                        return napoli.home2inter
                if away == "Juventus":
                        return napoli.home2juventus
                if away == "Lazio":
                        return napoli.home2lazio
                if away == "Milan":
                        return napoli.home2milan
                if away == "Napoli":
                        return napoli.home2napoli
                if away == "Roma":
                        return napoli.home2roma
                if away == "Sampdoria":
                        return napoli.home2sampdoria
                if away == "Torino":
                        return napoli.home2torino
                if away == "Udinese":
                        return napoli.home2udinese
        if home == "Roma":
                if away == "Atalanta":
                        return roma.home2atalanta
                if away == "Chievo":
                        return roma.home2chievo
                if away == "Fiorentina":
                        return roma.home2fiorentina
                if away == "Genoa":
                        return roma.home2genoa
                if away == "Inter":
                        return roma.home2inter
                if away == "Juventus":
                        return roma.home2juventus
                if away == "Lazio":
                        return roma.home2lazio
                if away == "Milan":
                        return roma.home2milan
                if away == "Napoli":
                        return roma.home2napoli
                if away == "Roma":
                        return roma.home2roma
                if away == "Sampdoria":
                        return roma.home2sampdoria
                if away == "Torino":
                        return roma.home2torino
                if away == "Udinese":
                        return roma.home2udinese
        if home == "Sampdoria":
                if away == "Atalanta":
                        return sampdoria.home2atalanta
                if away == "Chievo":
                        return sampdoria.home2chievo
                if away == "Fiorentina":
                        return sampdoria.home2fiorentina
                if away == "Genoa":
                        return sampdoria.home2genoa
                if away == "Inter":
                        return sampdoria.home2inter
                if away == "Juventus":
                        return sampdoria.home2juventus
                if away == "Lazio":
                        return sampdoria.home2lazio
                if away == "Milan":
                        return sampdoria.home2milan
                if away == "Napoli":
                        return sampdoria.home2napoli
                if away == "Roma":
                        return sampdoria.home2roma
                if away == "Sampdoria":
                        return sampdoria.home2sampdoria
                if away == "Torino":
                        return sampdoria.home2torino
                if away == "Udinese":
                        return sampdoria.home2udinese
        if home == "Torino":
                if away == "Atalanta":
                        return torino.home2atalanta
                if away == "Chievo":
                        return torino.home2chievo
                if away == "Fiorentina":
                        return torino.home2fiorentina
                if away == "Genoa":
                        return torino.home2genoa
                if away == "Inter":
                        return torino.home2inter
                if away == "Juventus":
                        return torino.home2juventus
                if away == "Lazio":
                        return torino.home2lazio
                if away == "Milan":
                        return torino.home2milan
                if away == "Napoli":
                        return torino.home2napoli
                if away == "Roma":
                        return torino.home2roma
                if away == "Sampdoria":
                        return torino.home2sampdoria
                if away == "Torino":
                        return torino.home2torino
                if away == "Udinese":
                        return torino.home2udinese
        if home == "Udinese":
                if away == "Atalanta":
                        return udinese.home2atalanta
                if away == "Chievo":
                        return udinese.home2chievo
                if away == "Fiorentina":
                        return udinese.home2fiorentina
                if away == "Genoa":
                        return udinese.home2genoa
                if away == "Inter":
                        return udinese.home2inter
                if away == "Juventus":
                        return udinese.home2juventus
                if away == "Lazio":
                        return udinese.home2lazio
                if away == "Milan":
                        return udinese.home2milan
                if away == "Napoli":
                        return udinese.home2napoli
                if away == "Roma":
                        return udinese.home2roma
                if away == "Sampdoria":
                        return udinese.home2sampdoria
                if away == "Torino":
                        return udinese.home2torino
                if away == "Udinese":
                        return udinese.home2udinese
                
def homeWins3years( home ):
                if home == "Atalanta":
                        return atalanta.homeWins3Years
                if home == "Chievo":
                        return chievo.homeWins3Years
                if home == "Fiorentina":
                        return fiorentina.homeWins3Years
                if home == "Genoa":
                        return genoa.homeWins3Years
                if home == "Inter":
                        return inter.homeWins3Years
                if home == "Juventus":
                        return juventus.homeWins3Years
                if home == "Lazio":
                        return lazio.homeWins3Years
                if home == "Milan":
                        return milan.homeWins3Years
                if home == "Napoli":
                        return napoli.homeWins3Years
                if home == "Roma":
                        return roma.homeWins3Years
                if home == "Sampdoria":
                        return sampdoria.homeWins3Years
                if home == "Torino":
                        return torino.homeWins3Years
                if home == "Udinese":
                        return udinese.homeWins3Years

def homeDraws3years( home ):
                if home == "Atalanta":
                        return atalanta.homeDraws3Years
                if home == "Chievo":
                        return chievo.homeDraws3Years
                if home == "Fiorentina":
                        return fiorentina.homeDraws3Years
                if home == "Genoa":
                        return genoa.homeDraws3Years
                if home == "Inter":
                        return inter.homeDraws3Years
                if home == "Juventus":
                        return juventus.homeDraws3Years
                if home == "Lazio":
                        return lazio.homeDraws3Years
                if home == "Milan":
                        return milan.homeDraws3Years
                if home == "Napoli":
                        return napoli.homeDraws3Years
                if home == "Roma":
                        return roma.homeDraws3Years
                if home == "Sampdoria":
                        return sampdoria.homeDraws3Years
                if home == "Torino":
                        return torino.homeDraws3Years
                if home == "Udinese":
                        return udinese.homeDraws3Years
def homeLoses3years( home ):
                if home == "Atalanta":
                        return atalanta.homeLoses3Years
                if home == "Chievo":
                        return chievo.homeLoses3Years
                if home == "Fiorentina":
                        return fiorentina.homeLoses3Years
                if home == "Genoa":
                        return genoa.homeLoses3Years
                if home == "Inter":
                        return inter.homeLoses3Years
                if home == "Juventus":
                        return juventus.homeLoses3Years
                if home == "Lazio":
                        return lazio.homeLoses3Years
                if home == "Milan":
                        return milan.homeLoses3Years
                if home == "Napoli":
                        return napoli.homeLoses3Years
                if home == "Roma":
                        return roma.homeLoses3Years
                if home == "Sampdoria":
                        return sampdoria.homeLoses3Years
                if home == "Torino":
                        return torino.homeLoses3Years
                if home == "Udinese":
                        return udinese.homeLoses3Years

def awayWins3years( away ):
                if away == "Atalanta":
                        return atalanta.awayWins3Years
                if away == "Chievo":
                        return chievo.awayWins3Years
                if away == "Fiorentina":
                        return fiorentina.awayWins3Years
                if away == "Genoa":
                        return genoa.awayWins3Years
                if away == "Inter":
                        return inter.awayWins3Years
                if away == "Juventus":
                        return juventus.awayWins3Years
                if away == "Lazio":
                        return lazio.awayWins3Years
                if away == "Milan":
                        return milan.awayWins3Years
                if away == "Napoli":
                        return napoli.awayWins3Years
                if away == "Roma":
                        return roma.awayWins3Years
                if away == "Sampdoria":
                        return sampdoria.awayWins3Years
                if away == "Torino":
                        return torino.awayWins3Years
                if away == "Udinese":
                        return udinese.awayWins3Years

def awayDraws3years( away ):
                if away == "Atalanta":
                        return atalanta.awayDraws3Years
                if away == "Chievo":
                        return chievo.awayDraws3Years
                if away == "Fiorentina":
                        return fiorentina.awayDraws3Years
                if away == "Genoa":
                        return genoa.awayDraws3Years
                if away == "Inter":
                        return inter.awayDraws3Years
                if away == "Juventus":
                        return juventus.awayDraws3Years
                if away == "Lazio":
                        return lazio.awayDraws3Years
                if away == "Milan":
                        return milan.awayDraws3Years
                if away == "Napoli":
                        return napoli.awayDraws3Years
                if away == "Roma":
                        return roma.awayDraws3Years
                if away == "Sampdoria":
                        return sampdoria.awayDraws3Years
                if away == "Torino":
                        return torino.awayDraws3Years
                if away == "Udinese":
                        return udinese.awayDraws3Years
def awayLoses3years( away ):
                if away == "Atalanta":
                        return atalanta.awayLoses3Years
                if away == "Chievo":
                        return chievo.awayLoses3Years
                if away == "Fiorentina":
                        return fiorentina.awayLoses3Years
                if away == "Genoa":
                        return genoa.awayLoses3Years
                if away == "Inter":
                        return inter.awayLoses3Years
                if away == "Juventus":
                        return juventus.awayLoses3Years
                if away == "Lazio":
                        return lazio.awayLoses3Years
                if away == "Milan":
                        return milan.awayLoses3Years
                if away == "Napoli":
                        return napoli.awayLoses3Years
                if away == "Roma":
                        return roma.awayLoses3Years
                if away == "Sampdoria":
                        return sampdoria.awayLoses3Years
                if away == "Torino":
                        return torino.awayLoses3Years
                if away == "Udinese":
                        return udinese.awayLoses3Years
       
