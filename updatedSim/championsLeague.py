import math
from RoundRobin import roundRobin, rankings
from random import random, sample
from operator import attrgetter
from Match import advancedMatch


def group4stage(Clubs):
    Teams = sample(Clubs, len(Clubs))
    k = 0
    roundRobin(Teams)
    Teams = rankings(Teams)
    Teams = sorted(Teams, key = attrgetter('points', 'goaldiff', 'wins'), reverse = True)
    return Teams[0], Teams[1]


def numberOfGroups(Teams):
    for team in Teams:
        team.points = 0
        team.wins = 0
        team.losses = 0
        team.draws = 0
        team.goaldiff = 0
    clubs = len(Teams)
    Teams = sample(Teams, clubs)
    nextRound = []
    if clubs < 8:
        roundRobin(Teams)
        Teams = rankings(Teams)
        nextRound = [Teams[0]]
    else:
        k = 0
        y = 1
        if clubs % 4 == 0:
            while k < len(Teams):
                group = [Teams[k], Teams[k+1], Teams[k+2], Teams[k+3]]
                print('Group', y, ':\n')
                for team in group:
                    print(team.name)
                y = y + 1
                advanced = group4stage(group)
                nextRound.append(advanced)
                k = k + 4
        elif clubs % 5 == 0:
            while k < len(Teams):
                group = [Teams[k], Teams[k+1], Teams[k+2], Teams[k+3], Teams[k+4]]
                advanced = group4stage(group)
                nextRound.append(advanced)
                k = k + 5
        else:
            while k < len(Teams):
                group = [Teams[k], Teams[k+1], Teams[k+2]]
                advanced = group4stage(group)
                nextRound.append(advanced)
                k = k + 3
    return nextRound

def knockoutStage(Clubs):
    Clubs = sample(Clubs, len(Clubs))
    rounds = round(math.log(len(Clubs), 2))
    for i in range(rounds-1):
        print('\nRound', i+1)
        k = 0
        winners = []
        while k < len(Clubs):
            Team1 = Clubs[k]
            Team2 = Clubs[k+1]
            k = k + 2
            Team1.points = 0
            Team2.points = 0
            print('\nLeg 1:')
            print(Team1.name,'(H) vs', Team2.name)
            advancedMatch(Team1, Team2, 1)
            Team2away = Team2.points
            Team1home = Team1.points
            #print(Team1home, Team2away)
            print('\nLeg 2:')
            print(Team2.name,'(H) vs', Team1.name)
            advancedMatch(Team1, Team2, 1)
            Team1away = Team1.points - Team1home
            #print(Team1away, Team2away)
            if Team1.points > Team2.points:
                winners.append(Team1)
                print(Team1.name, "is advancing to the next stage.")
            elif Team2.points > Team1.points:
                winners.append(Team2)
                print(Team2.name, "is advancing to the next stage.")
            elif Team1.points == Team2.points:
                if Team1away > Team2away:
                    winners.append(Team1)
                    print(Team1.name, "is advancing on away goals(", Team1away, '-', Team2away, ")")
                elif Team2away > Team1away:
                    winners.append(Team2)
                    print(Team2.name, "is advancing on away goals(", Team2away, '-', Team1away, ")")
                else:
                    while Team1.points == Team2.points:
                        Team1.points = math.floor(random()*5)
                        Team2.points = math.floor(random()*5)
                    if Team1.points > Team2.points:
                        winners.append(Team1)
                        print(Team1.name, "won on penalties:")
                        print('(', Team1.points, '-', Team2.points, ')')
                    else:
                        winners.append(Team2)
                        print(Team2.name, "won on penalties:")
                        print('(', Team2.points, '-', Team1.points, ')')
        Clubs = winners
    advancedMatch(Clubs[0], Clubs[1], 2)


def championsPath(Clubs):
    qual = numberOfGroups(Clubs)
    if len(qual) == 1:
        Team = qual[0]
        print(Team.name, 'has won Champions League')
    else:
        knockoutStage(Clubs)







