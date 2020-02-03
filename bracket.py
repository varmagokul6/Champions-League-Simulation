import math
from random import random, sample
from Match import match, penalties, championship, points, diffSkill, knockoutMatch
from Teams import team
from listOfTeams import TeamsList

#def quarterFinalsBracket(matches):

def bracketGraphics(matches):
    n = 16
    k = 0
    while k < 5:
        if k == 0:
            for i in range(len(matches)//2):      #DOES NOT WORK FOR ALL NUMBER OF MATCHES
                match1 = matches[k]
                match2 = matches[k+1]
                Team1 = match1[0]
                Team2 = match1[1]
                Team3 = match2[0]
                Team4 = match2[1]
                print(('%-30s %40s')% (Team1.name, Team3.name))
                print(('%-30s %40s')% ('------------', '------------'))
                print(('%-30s %40s')% (Team2.name, Team4.name))
                print('\n')
                #print(('%30s %10s')% ('TBD', 'TBD'))
                #print(('%30s %19s')% ('------------', '------------'))
                #print(('%30s %10s')% ('TBD', 'TBD'))
                #print('\n')
        k = k + 1

def graphics(matches):
    n = 16
    x = math.log(n, 2)
    j = 0
    while j < math.log(n, 2):
        k = 0
        #if len(matches) <= n/:
    if len(matches) <= n/2:
        for i in range(len(matches)//2):      #DOES NOT WORK FOR ALL NUMBER OF MATCHES
            match1 = matches[k]
            match2 = matches[k+1]
            Team1 = match1[0]
            Team2 = match1[1]
            Team3 = match2[0]
            Team4 = match2[1]
            print(('%-30s %40s')% (Team1.name, Team3.name))
            print(('%-30s %40s')% ('------------', '------------'))
            print(('%-30s %40s')% (Team2.name, Team4.name))
            print('\n')
            print(('%30s %10s')% ('TBD', 'TBD'))
            print(('%30s %19s')% ('------------', '------------'))
            print(('%30s %10s')% ('TBD', 'TBD'))
            print('\n')
            k = k + 2
    j = j + 1



def bracketSetup(Teams):
    #print(Teams)
    topTeams = sample(Teams, len(Teams))      #randomly draws a list of the top teams for competition
    matches = []
    k = 0
    while k < len(topTeams)/2:
        Team1 = topTeams[k]
        Team2 = topTeams[len(topTeams)-k-1]
        match = [Team1, Team2]
        matches.append(match)                   #sets the first round schedule
        k = k + 1
    #print(matches)
    graphics(matches)
    return matches

def knockout(Teams):
    k = 0
    mid = len(Teams)/2
    set1 = Teams[:mid]
    set2 = Teams[mid:]
    matches = []
    while k < mid:
        Team1 = set1[k]
        Team2 = set1[k+2]
        Team3 = set2[k]
        Team4 = set2[k+2]
        match = Team1, Team2
        matches.append(match)
        match = Team3, Team4
        matches.append(match)
        k = k + 1
    return matches

def stage1(Teams):
    topTeams = []
    #print(Teams)
    for i in Teams:
        topTeams.append(i[0])
        topTeams.append(i[1])
    #print(topTeams)
    k = 0
    winners = []
    while k < len(topTeams):
        Team1 = topTeams[k]
        Team2 = topTeams[k + 1]
        Team1.points = 0
        Team2.points = 0
        print('\n')
        knockoutMatch(Team1, Team2)
        Team2away = Team2.points
        Team1home = Team1.points
        knockoutMatch(Team2, Team1)
        Team1away = Team1.points - Team1home
        if Team1.points > Team2.points:
            winners.append(Team1)
            print(Team1.name, "is advancing to the next stage.")
        elif Team2.points > Team1.points:
            winners.append(Team2)
            print(Team2.name, "is advancing to the next stage.")
        elif Team1.points == Team2.points:
            if Team1away > Team2away:
                winners.append(Team1)
                print(Team1.name, "is advancing to the next stage.")
            elif Team2away > Team1away:
                winners.append(Team2)
                print(Team2.name, "is advancing to the next stage.")
            else:
                print('\nTiebreaker match')
                while Team1.points == Team2.points:
                    knockoutMatch(Team1, Team2)
        k = k + 2
    return(winners)

total_matches = bracketSetup(TeamsList)
graphics(total_matches)

