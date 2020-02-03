import math
from random import random


def points(diffSkill):           #generates a random score for both teams
    raw_score = random()
    while raw_score < 0.17:
        raw_score = random()
    if raw_score > .85 and diffSkill <= 2:
        raw_score = 0
    else:
        raw_score = abs(math.floor(math.log(2/raw_score, 2)+diffSkill))
    return raw_score

def diffSkill(skill1, skill2):
    if skill1 > skill2:
        diff = math.floor((skill1*1.05 - skill2)/10)
    else:
        diff = 0
    return diff

def match(Team1, Team2):
    points1 = points(diffSkill(Team1.skill, Team2.skill))
    points2 = points(diffSkill(Team2.skill, Team1.skill))
    if points1 > points2:
        print(Team1.name, points1, ',', Team2.name, points2)
        Team1.points = Team1.points + 3     #adds three points to winner
        winner = Team1
        Team1.wins = Team1.wins + 1
        Team2.losses = Team2.losses + 1
    elif points2 > points1:
        print(Team2.name, points2, ',', Team1.name, points1)
        Team2.points = Team2.points + 3
        winner = Team2
        Team1.losses = Team1.losses + 1
        Team2.wins = Team2.wins + 1
    elif points1 == points2:
        print(Team1.name, points1, ',', Team2.name, points2)
        Team1.points = Team1.points + 1
        Team2.points = Team2.points + 1
        Team1.draws = Team1.draws + 1
        Team2.draws = Team2.draws + 1
        winner = 'Tie'
    Team1.goaldiff = Team1.goaldiff + points1 - points2     #calculates goal differential
    Team2.goaldiff = Team2.goaldiff + points2 - points1
    return winner

def penalties(Team1, Team2, points1, points2):
    team1pen = 0
    team2pen = 0
    while team1pen == team2pen:
        team1pen = math.floor(5*random())
        team2pen = math.floor(5*random())
    if team1pen > team2pen:
        print(Team1.name, points1, ',', Team2.name, points2)
        print(Team1.name, "has won on penalties(\n",team1pen, '-', team2pen, ').')
        winner = Team1
    elif team2pen > team1pen:
        print(Team2.name, points2, ',', Team1.name, points1)
        print(Team2.name, "has won on penalties\n", "(",team2pen, '-', team1pen, ').')
        winner = Team2
    return winner

def knockoutMatch(Team1, Team2):
    points1 = points(diffSkill(Team1.skill, Team2.skill))
    points2 = points(diffSkill(Team2.skill, Team1.skill))
    winner = []
    if points1 > points2:
        print(Team1.name, points1, ',', Team2.name, points2, " (", Team1.name, "is home )")
        winner = Team1
    elif points2 > points1:
        print(Team2.name, points2, ',', Team1.name, points1, " (", Team1.name, "is home )")
        winner = Team2
    elif points1 == points2:
        print(Team1.name, points1, ',', Team2.name, points2, " (", Team1.name, "is home )")
    Team1.points = points1 + Team1.points
    Team2.points = points2 + Team2.points
    return winner

def championship(Team1, Team2):
    points1 = points(diffSkill(Team1.skill, Team2.skill))
    points2 = points(diffSkill(Team2.skill, Team1.skill))
    if points1 > points2:
        winner = Team1
        print(Team1.name, points1,',', Team2.name, points2)
    elif points2 > points1:
        winner = Team2
        print(Team2.name, points2,',', Team1.name, points1)
    elif points1 == points2:
        winner = penalties(Team1, Team2, points1, points2)
    print('\n', winner.name, "is the champion!")
    return winner


