import math
from random import random
from operator import attrgetter

#def goalieSaving(players, scorer):
#    for player in players:
#        if player.position == 'GK':


def playerScoring(players):
    potentialScorers = []
    for player in players:
        if player.position != 'GK' and player.position != 'RB' and player.position != 'CB' and player.position != 'LB' and player.position != 'CDM':
            potentialScorers.append(player)
    potentialScorers = sorted(potentialScorers, key = attrgetter('overall'), reverse = True)
    numb = round((len(potentialScorers)-1)*random())
    numb = abs(round((len(potentialScorers)-1) * math.log(random(), 10)))
    while numb >= len(potentialScorers):
        numb = abs(round((len(potentialScorers)-1) * math.log(random(), 10)))
    scorer = potentialScorers[numb]
    scorer.goals = scorer.goals + 1
    return scorer

def printScores(score1, score2, Team1, Team2, stage):
    if stage == 0:
        if score2 > score1:
            print('Final Score:', Team2.name, score2, ',', Team1.name, score1, '\n')
            Team2.points = Team2.points + 3
            Team2.wins = Team2.wins + 1
            Team1.losses = Team1.losses + 1
            Team2.money = Team2.money + .5
        elif score1 > score2:
            print('Final Score:', Team1.name, score1, ',', Team2.name, score2, '\n')
            Team1.points = Team1.points + 3
            Team1.wins = Team1.wins + 1
            Team2.losses = Team2.losses + 1
            Team1.money = Team1.money + .5
        else:
            print('Final Score:', Team1.name, score1, ',', Team2.name, score2, '\n')
            Team1.points = Team1.points + 1
            Team2.points = Team2.points + 1
            Team2.draws = Team2.draws + 1
            Team1.draws = Team1.draws + 1
            Team1.money = Team1.money + .25
            Team2.money = Team2.money + .25
        Team1.goaldiff = Team1.goaldiff + score1 - score2
        Team2.goaldiff = Team2.goaldiff + score2 - score1
    elif stage == 1:
        Team2.points = score2
        Team1.points = score1
        if score2 > score1:
            print('Final Score:', Team2.name, score2, ',', Team1.name, score1, '\n')
            Team2.money = Team2.money + 1
        elif score1 > score2:
            print('Final Score:', Team1.name, score1, ',', Team2.name, score2, '\n')
            Team1.money = Team1.money + 1
        else:
            print('Final Score:', Team1.name, score1, ',', Team2.name, score2, '\n')
            Team1.money = Team1.money + .5
            Team2.money = Team2.money + .5
        Team1.goaldiff = Team1.goaldiff + score1 - score2
        Team2.goaldiff = Team2.goaldiff + score2 - score1
    elif stage == 2:
        Team2.points = score2
        Team1.points = score1
        if score2 > score1:
            print('Final Score:', Team2.name, score2, ',', Team1.name, score1, '\n')
            Team2.money = Team2.money + 5
            print(Team2.name, 'has won the Champions League!')
        elif score1 > score2:
            print('Final Score:', Team1.name, score1, ',', Team2.name, score2, '\n')
            Team1.money = Team1.money + 5
            print(Team1.name, 'has won the Champions League!')
        else:
            print('Final Score:', Team1.name, score1, ',', Team2.name, score2, '\n')
            while Team1.points == Team2.points:
                Team1.points = math.floor(random()*5)
                Team2.points = math.floor(random()*5)
            if Team1.points > Team2.points:
                print(Team1.name, "won on penalties:")
                print('(', Team1.goaldiff, '-', Team2.goaldiff, ')')
                print(Team1.name, 'has won the Champions League!')
            else:
                print(Team2.name, "won on penalties:")
                print('(', Team2.goaldiff, '-', Team1.goaldiff, ')')
                print(Team2.name, 'has won the Champions League!')


def advancedMatch(Team1, Team2, stage):
    k = 0
    points1 = points(diffSkill(Team1.skill, Team2.skill))
    points2 = points(diffSkill(Team2.skill, Team1.skill))
    score1 = points1
    score2 = points2
    while k < 90:
        k = k + 1
        team1Rand = random()
        team2Rand = random()
        if team1Rand < .05 and points1 != 0:
            scorer = playerScoring(Team1.players)
            print(Team1.name, 'scores!', scorer.name, k, "'")
            points1 = points1 - 1
        elif team2Rand < .05 and points2 != 0:
            scorer = playerScoring(Team2.players)
            print(Team2.name, 'scores!', scorer.name, k, "'")
            points2 = points2 - 1
    printScores(score1-points1, score2-points2, Team1, Team2, stage)




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


