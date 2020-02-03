import math
from random import random, sample
from Teams import team
from operator import itemgetter, attrgetter
from listOfTeams import TeamsList
from roundRobin import roundRobin
from Match import match, penalties, championship, points, diffSkill, knockoutMatch
from teamLists import premier, laLiga, ligueOne, serieA, bundesliga, restOfWorld, eredivisie, randomDiv
import os

def appendingTeams(array, group):
    print(group)
    #k = 0
    for k in group:
        k.points = 0
        k.wins = 0
        k.losses = 0
        k.draws = 0
        k.goaldiff = 0
        #print(group[i])
        array.append(k)
    return array

def qualifiedTeams():
    teams = []
    premierQual = premier()
    teams = appendingTeams(teams, premierQual)       #repeat for other leagues
#    os.system("pause")

    ligaQual = laLiga()
    print(ligaQual)
    teams = appendingTeams(teams, ligaQual)
 #   os.system("pause")

    ligueQual = ligueOne()
    print(ligueQual)
    teams = appendingTeams(teams, ligueQual)
  #  os.system("pause")

    serieAQual = serieA()
    teams = appendingTeams(teams, serieAQual)
   # os.system("pause")

    bundesQual = bundesliga()
    teams = appendingTeams(teams, bundesQual)
    #os.system("pause")

    restQual = restOfWorld()
    teams = appendingTeams(teams, restQual)
    #os.system("pause")

    ereQual = eredivisie()
    teams = appendingTeams(teams, ereQual)
    #os.system("pause")

    randQual = randomDiv()
    teams = appendingTeams(teams, randQual)

    return teams

def knockoutRounds(Teams):
    topTeams = Teams
    #print(Teams)
    topTeams = sample(topTeams, len(topTeams))
    #print(topTeams)
    k = 0
    winners = []
    while k < len(topTeams)/2:
        Team1 = topTeams[k]
        Team2 = topTeams[len(topTeams)-k-1]
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
                print(Team1.name, "is advancing on away goals(", Team1away, '-', Team2away, ")")
            elif Team2away > Team1away:
                winners.append(Team2)
                print(Team2.name, "is advancing on away goals(", Team2away, '-', Team1away, ")")
            else:
                points1 = random()
                points2 = random()
                while points1 == points2:
                    points1 = random()
                    points2 = random()
                if points1 > points2:
                    winners.append(Team1)
                    print(Team1.name, "is advancing to the next stage.")
                else:
                    winners.append(Team2)
                    print(Team2.name, "is advancing to the next stage.")

        k = k + 1
    return winners

def quarterFinals(Teams):
    topTeams = []
    #print(Teams)
    for i in Teams:
        topTeams.append(i[0])
        topTeams.append(i[1])
    topTeams = sample(topTeams, len(topTeams))
    #print(topTeams)
    k = 0
    winners = []
    while k < len(topTeams)/2:
        Team1 = topTeams[k]
        Team2 = topTeams[len(topTeams)-k-1]
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
        k = k + 1
        #os.system("pause")
    return(winners)

def GroupStage(Team1, Team2, Team3, Team4):
    Teams = [Team1, Team2, Team3, Team4]
    #print(Teams)
    roundRobin(Teams)
    #os.system('pause')
    print('\n')
    #roundRobin(Teams)
    #os.system('pause')
    finalTeams = rankings(Team1, Team2, Team3, Team4)
    #os.system('pause')
    return finalTeams

def rankings(Team1, Team2, Team3, Team4):
    print('\n')
    Teams = [Team1, Team2, Team3, Team4]
    myList = sorted(Teams, key = attrgetter('points', 'goaldiff'), reverse = True) #orders groups by top teams
    Team1 = myList[0] #sets teams in order of performance
    Team2 = myList[1]
    Team3 = myList[2]
    Team4 = myList[3]
    print (("%-15s %3i %3i") % (Team1.name, Team1.points, Team1.goaldiff))
    print (("%-15s %3i %3i") % (Team2.name, Team2.points, Team2.goaldiff))
    print (("%-15s %3i %3i") % (Team3.name, Team3.points, Team3.goaldiff))
    print (("%-15s %3i %3i") % (Team4.name, Team4.points, Team4.goaldiff))
    return Team1, Team2

def drawGroups(listofTeams):
    x = len(listofTeams)
    newlist = sample(listofTeams, len(listofTeams))     #rearranges the list of teams into random order to represent drawing
    #print('\n', newlist)
    k = 0
    knockout = []
    while k < x/4:
        print('\nGroup', k+1, 'consists of:')           #takes every four teams in new list and makes a group
        print(newlist[4*k])
        print(newlist[4*k + 1])
        print(newlist[4*k + 2])
        print(newlist[4*k + 3])
        print('\nGroup', k + 1, "Results:")
        finalTeams = GroupStage(newlist[4*k], newlist[4*k+1],newlist[4*k+2],newlist[4*k+3])
        k = k + 1
        knockout.append(finalTeams)
    return knockout

def printWinners(Teams):
    print("\nThe following teams have qualified for the next round:")
    for i in Teams:
        Team1 = i[0]
        Team2 = i[1]
        print(Team1.name)
        print(Team2.name)

def printWinners2(Teams):
    print("\nThe following teams have qualified for the next round:")
    for i in Teams:
        print(i.name)

def knockoutBracket(Teams):
    n = len(Teams)
    matches = math.log(n,2)
    #print(matches)
    if matches > 0:
        Teams = quarterFinals(Teams)
        #printWinners2(Teams)
        #os.system("pause")
        k = 0
        while k < 6:
            #os.system("pause")
            k = k + 1
            if k == n - 4:
                print('\nQuarterfinals:')
                Teams = knockoutRounds(Teams)
            elif k == n - 3:
                print('\nSemifinals:')
                Teams = knockoutRounds(Teams)
            elif k == n -2:
                print('\nFinals:')
                champion = championship(Teams[0], Teams[1])
                champion.championships = champion.championships + 1
                print('The champion is:', champion.name)




def main(TeamsList):
    knockoutClubs = drawGroups(TeamsList)
    printWinners(knockoutClubs)
    print('\nLet the Knockout Stage Begin!')
    os.system('pause')

    winners1 = quarterFinals(knockoutClubs)
    printWinners2(winners1)
    os.system("pause")
    print('\nQuarterfinals:')
    winners2 = knockoutRounds(winners1)
    #printWinners2(winners2)
    os.system("pause")
    print('\nSemifinals:')
    winners3 = knockoutRounds(winners2)
    #printWinners2(winners3)
    os.system("pause")
    print('\nFinals:')
    champion = championship(winners3[0], winners3[1])
    champion.championships = champion.championships + 1
    #os.system("pause")
    return TeamsList


def testRun():
    clubs = qualifiedTeams()
    groupClubs = drawGroups(clubs)
    printWinners(groupClubs)
    x = knockoutBracket(groupClubs)
    return clubs

testRun()