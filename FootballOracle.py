#!/usr/bin/python3

from italy.functions.calculations import *

homeTeam = ItalyTeam()
awayTeam = ItalyTeam()

homeData=0
awayData=0

country=""

nationalTeam = input("Enter first team name: ")
country = checkNames(nationalTeam)


homeTeam.name = setName(nationalTeam)
awayTeam.name = input("Enter second team name: ")
if country == "Italy":
    awayTeam.name = setName(awayTeam.name)

if country == "Italy":
    homeData = findName(homeTeam.name)
    awayData = findName(awayTeam.name)
    populateData(homeTeam)
    populateData(awayTeam)

first_team_name = homeTeam.name
second_team_name = awayTeam.name
             
# Current season stats
first_team_current_season_games = int(input("Enter " + homeTeam.name + " current season number of games: "))
first_team_current_season_wins = float(input("Enter " + homeTeam.name + " current season wins: "))
first_team_current_season_draws = float(input("Enter " + homeTeam.name + " current season draws: "))
first_team_current_season_loses = float(input("Enter " + homeTeam.name + " current season loses: "))

second_team_current_season_games = int(input("Enter " + awayTeam.name + " current season number of games: "))
second_team_current_season_wins = float(input("Enter " + awayTeam.name + " current season wins: "))
second_team_current_season_draws = float(input("Enter " + awayTeam.name + " current season draws: "))
second_team_current_season_loses = float(input("Enter " + awayTeam.name + " current season loses: "))

first_team_current_season_percent_wins = (first_team_current_season_wins*100)/first_team_current_season_games
first_team_current_season_percent_draws = (first_team_current_season_draws*100)/first_team_current_season_games
first_team_current_season_percent_loses = (first_team_current_season_loses*100)/first_team_current_season_games

second_team_current_season_percent_wins = (second_team_current_season_wins*100)/second_team_current_season_games
second_team_current_season_percent_draws = (second_team_current_season_draws*100)/second_team_current_season_games
second_team_current_season_percent_loses = (second_team_current_season_loses*100)/second_team_current_season_games

season_percent_home = (first_team_current_season_percent_wins + second_team_current_season_percent_loses)/2
season_percent_draw = (first_team_current_season_percent_draws + second_team_current_season_percent_draws)/2
season_percent_away = (first_team_current_season_percent_loses + second_team_current_season_percent_wins)/2



# Last 5 games 
first_team_last5games_wins = int(input("Enter " + homeTeam.name + " last 5 games wins: "))
first_team_last5games_draws = int(input("Enter " + homeTeam.name + " last 5 games draws: "))
first_team_last5games_loses = int(input("Enter " + homeTeam.name + " last 5 games loses: "))

if first_team_last5games_wins > 5 :
    print("Error")
if first_team_last5games_draws > 5 :
    print("Error")
if first_team_last5games_loses > 5 :
    print("Error")
    
second_team_last5games_wins = int(input("Enter " + awayTeam.name + " last 5 games wins: "))
second_team_last5games_draws = int(input("Enter " + awayTeam.name + " last 5 games draws: "))
second_team_last5games_loses = int(input("Enter " + awayTeam.name + " last 5 games loses: "))

if second_team_last5games_wins > 5 :
    print("Error")
if second_team_last5games_draws > 5 :
    print("Error")
if second_team_last5games_loses > 5 :
    print("Error")

last5games_percent_home = (((first_team_last5games_wins + second_team_last5games_loses)/2)*100)/5
last5games_percent_draw = (((first_team_last5games_draws + second_team_last5games_draws)/2)*100)/5
last5games_percent_away = (((first_team_last5games_loses + second_team_last5games_loses)/2)*100)/5  


# Last 5 meetings

if homeData ==1 and awayData ==1:
    first_team_5meetings_wins = get5meetingswins(homeTeam.name, awayTeam.name)
    meetings_draws = get5meetingsdraws(homeTeam.name, awayTeam.name)
    second_team_5meetings_wins = get5meetingsloses(homeTeam.name, awayTeam.name)
else:    
    first_team_5meetings_wins = int(input("Enter " + homeTeam.name + " wins in last 5 meetings: "))
    meetings_draws = int(input("Enter number of draws last 5 meetings: "))
    second_team_5meetings_wins = int(input("Enter " + awayTeam.name + " wins in last 5 meetings: "))

if first_team_5meetings_wins > 5 :
    print("Error")
if meetings_draws > 5 :
    print("Error")
if second_team_5meetings_wins > 5 :
    print("Error")


meetings_percent_home = (first_team_5meetings_wins*100)/5
meetings_percent_draw = (meetings_draws*100)/5
meetings_percent_away = (second_team_5meetings_wins*100)/5


#Last 3years home-away percents

if homeData == 1 and awayData ==1 :
    first_team_last3years_home_wins_percent = homeWins3years(homeTeam.name)
    first_team_last3years_home_draws_percent = homeDraws3years(homeTeam.name)
    first_team_last3years_home_loses_percent = homeLoses3years(homeTeam.name)
    second_team_last3years_away_wins_percent = awayWins3years(awayTeam.name)
    second_team_last3years_away_draws_percent = awayDraws3years(awayTeam.name) 
    second_team_last3years_away_loses_percent = awayLoses3years(awayTeam.name)
else :
    first_team_last3years_home_wins_percent = float(input("Enter last 3 years " + first_team_name + " home wins percent: "))
    first_team_last3years_home_draws_percent = float(input("Enter last 3 years " + first_team_name + " home draws percent: "))
    first_team_last3years_home_loses_percent = float(input("Enter last 3 years " + first_team_name + " home loses percent: "))

    second_team_last3years_away_wins_percent = float(input("Enter last 3 years " + second_team_name + " away wins percent: "))
    second_team_last3years_away_draws_percent = float(input("Enter last 3 years " + second_team_name + " away draws percent: "))
    second_team_last3years_away_loses_percent = float(input("Enter last 3 years " + second_team_name + " away loses percent: "))

home_away_percent1 = (first_team_last3years_home_wins_percent + second_team_last3years_away_loses_percent)/2
home_away_percentX = (first_team_last3years_home_draws_percent + second_team_last3years_away_draws_percent)/2
home_away_percent2 = (first_team_last3years_home_loses_percent + second_team_last3years_away_wins_percent)/2

#Calculated percents
	
calculated_home = (home_away_percent1 + season_percent_home + last5games_percent_home + meetings_percent_home)/4
calculated_draw = (home_away_percentX + season_percent_draw + last5games_percent_draw + meetings_percent_draw)/4
calculated_away = (home_away_percent2 + season_percent_away + last5games_percent_away + meetings_percent_away)/4

print("calculated percents home: ")
print(calculated_home)
print("calculated percents draw: ")
print(calculated_draw)
print("calculated percents away: ")
print(calculated_away)

# bet365 percents

bet1 = float(input("Enter bet365 coefficient for 1: "))
print(bet1)
betx = float(input("Enter bet365 coefficient for x: "))
print(betx)
bet2 = float(input("Enter bet365 coefficient for 2: "))
print(bet2)
bet_base = bet1+betx+bet2

bet_home = (bet2*100)/bet_base
bet_draw = (betx*100)/bet_base
bet_away = (bet1*100)/bet_base

print("bet percents home: ")
print(bet_home)
print("bet percents draw: ")
print(bet_draw)
print("bet percents away: ")
print(bet_away)

if bet_home + 10 < calculated_home :
    print("Bet 1")
    if calculated_home < 25 :
        print("WARNING! Chanse to hit under 25%")
if bet_draw + 10 < calculated_draw :
    print("Bet X")
    if calculated_draw < 25 :
        print("WARNING! Chanse to hit under 25%")
if bet_away + 10 < calculated_away :
    print("Bet 2")
    if calculated_away < 25 :
        print("WARNING! Chanse to hit under 25%")
theend = input("done")