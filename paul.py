#!/usr/bin/python3
import datetime

debug=0

first_team_name = input("Enter first team name: ")
second_team_name = input("Enter second team name: ")
             
# Current season stats
first_team_current_season_games = int(input("Enter " + first_team_name + " current season number of games: "))
first_team_current_season_wins = float(input("Enter " + first_team_name + " current season wins: "))
first_team_current_season_draws = float(input("Enter " + first_team_name + " current season draws: "))
first_team_current_season_loses = first_team_current_season_games - (first_team_current_season_wins +first_team_current_season_draws)

if first_team_current_season_wins + first_team_current_season_draws >first_team_current_season_games:
    print("Error")

second_team_current_season_games = int(input("Enter " + second_team_name + " current season number of games: "))
second_team_current_season_wins = float(input("Enter " + second_team_name + " current season wins: "))
second_team_current_season_draws = float(input("Enter " + second_team_name + " current season draws: "))
second_team_current_season_loses = second_team_current_season_games - (second_team_current_season_wins + second_team_current_season_draws)

if second_team_current_season_wins + second_team_current_season_draws > second_team_current_season_games:
    print("Error")

first_team_current_season_percent_wins = (first_team_current_season_wins*100)/first_team_current_season_games
first_team_current_season_percent_draws = (first_team_current_season_draws*100)/first_team_current_season_games
first_team_current_season_percent_loses = (first_team_current_season_loses*100)/first_team_current_season_games

second_team_current_season_percent_wins = (second_team_current_season_wins*100)/second_team_current_season_games
second_team_current_season_percent_draws = (second_team_current_season_draws*100)/second_team_current_season_games
second_team_current_season_percent_loses = (second_team_current_season_loses*100)/second_team_current_season_games

season_percent_home = (first_team_current_season_percent_wins + second_team_current_season_percent_loses)/2
season_percent_draw = (first_team_current_season_percent_draws + second_team_current_season_percent_draws)/2
season_percent_away = (first_team_current_season_percent_loses + second_team_current_season_percent_wins)/2

if(season_percent_home + season_percent_draw + season_percent_away)<99:
    print("Error")

if(season_percent_home + season_percent_draw + season_percent_away)>100:
    print("Error")

if debug == 1 :
    print("current season:")
    print(str(season_percent_home))
    print(str(season_percent_draw))
    print(str(season_percent_away))
          
# Last 5 games 
first_team_last5games_wins = int(input("Enter " + first_team_name + " last 5 games wins: "))
first_team_last5games_draws = int(input("Enter " + first_team_name + " last 5 games draws: "))
first_team_last5games_loses = 5 -(first_team_last5games_wins + first_team_last5games_draws)

if first_team_last5games_wins + first_team_last5games_draws > 5 :
    print("Error")
    
second_team_last5games_wins = int(input("Enter " + second_team_name + " last 5 games wins: "))
second_team_last5games_draws = int(input("Enter " + second_team_name + " last 5 games draws: "))
second_team_last5games_loses = 5 - (second_team_last5games_wins + second_team_last5games_draws)

if second_team_last5games_wins + second_team_last5games_draws> 5 :
    print("Error")

last5games_percent_home = (((first_team_last5games_wins + second_team_last5games_loses)/2)*100)/5
last5games_percent_draw = (((first_team_last5games_draws + second_team_last5games_draws)/2)*100)/5
last5games_percent_away = (((first_team_last5games_loses + second_team_last5games_wins)/2)*100)/5

if(last5games_percent_home +last5games_percent_draw +last5games_percent_away)<99:
    print("Error")

if(last5games_percent_home +last5games_percent_draw +last5games_percent_away)>100:
    print("Error")

if debug == 1 :          
    print("last 5 games:")
    print(str(last5games_percent_home))
    print(str(last5games_percent_draw))
    print(str(last5games_percent_away))
    
#Calculated percents
	
calculated_home = (season_percent_home + last5games_percent_home)/2
calculated_draw = (season_percent_draw + last5games_percent_draw)/2
calculated_away = (season_percent_away + last5games_percent_away)/2

calculated_home = round(calculated_home, 1)
calculated_draw = round(calculated_draw, 1)
calculated_away = round(calculated_away, 1)

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

bet_home = round(bet_home, 1)
bet_draw = round(bet_draw, 1)
bet_away = round(bet_away, 1)

print("bet percents home: ")
print(bet_home)
print("bet percents draw: ")
print(bet_draw)
print("bet percents away: ")
print(bet_away)

if bet_home + 10 < calculated_home :
    print("Bet 1")
    if calculated_home < 25 :
        print("WARNING! bet 1 is under 25%")
if bet_draw + 10 < calculated_draw :
    print("Bet X")
    if calculated_draw < 25 :
        print("WARNING! bet x is under 25%")
if bet_away + 10 < calculated_away :
    print("Bet 2")
    if calculated_away < 25 :
        print("WARNING! bet 2 is under 25%")

with open("stats.txt", "a") as myfile:
    myfile.write("------------------\n")
    myfile.write(datetime.date.today().strftime("%B %d, %Y")+"\n")
    myfile.write("calculated percents: \n")
    myfile.write(first_team_name +" "+ str(calculated_home)+"\n")
    myfile.write("X " + str(calculated_draw)+"\n")
    myfile.write(second_team_name +" "+ str(calculated_away)+"\n")
    if bet_home + 10 < calculated_home :
        myfile.write("Bet 1 for " + str(bet1) + "\n")
        if calculated_home < 25 :
            myfile.write("WARNING! bet 1 is under 25%\n")
    if bet_draw + 10 < calculated_draw :
       myfile.write ("Bet X for " + str(betx) + "\n")
       if calculated_draw < 25 :
           myfile.write ("WARNING! bet x is under 25%\n")
    if bet_away + 10 < calculated_away :
        myfile.write("Bet 2 for " + str(bet2) + "\n")
        if calculated_away < 25 :
            myfile.write("WARNING! bet 2 is under 25%\n")
    myfile.write("RESULT:\n")
    myfile.write("MONEY:\n")
    myfile.write("------------------\n") 
myfile.close()

theend = input("done")
