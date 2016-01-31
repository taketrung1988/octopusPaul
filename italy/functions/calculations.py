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
        name="EmptyTeam"
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


		
        
        
