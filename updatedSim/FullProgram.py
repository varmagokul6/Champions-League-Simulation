from Teams import clubFormation, clubs, englishClubs, frenchClubs, spanishClubs, germanClubs
from operator import attrgetter
from random import random, sample
from RoundRobin import roundRobin, rankings
from transferWindow import freeAgents, transfer, goalkeeperTrade, unsatisfiedPlayers, signingPlayers
from championsLeague import championsPath
import os
import math

def league(Teams):
    Teams = sample(Teams, len(Teams))
    #for team in Teams:
    #    print(team.name, team.skill)
    roundRobin(Teams)
    Teams = rankings(Teams)
    champion = Teams[0]
    tie = False
    tieTeams = [champion]
    for clubs in Teams:
        if clubs.name == champion.name:
            break
        elif clubs.points == champion.points and clubs.wins == champion.wins and champion.goaldiff == clubs.goaldiff:
            print('There is a tie for first place!')
            tie = True
            tieTeams.append(clubs)
    if tie == False:
        print('\n', champion.name, "is the champion!")
        champion.money = champion.money + 10
        champion.championships = champion.championships + 1
    else:
        print('The following teams have claimed the trophy over a tie!')
        for club in tieTeams:
            print(club.name)
            club.money = club.money + 10/len(tieTeams)
            champion.championships = 1/(len(tieTeams))
    Teams = sorted(Teams, key = attrgetter('points', 'goaldiff', 'wins'), reverse = True)
    return Teams

def championsQualifiers(Clubs):
    length = len(Clubs)
    qualTeamNum = math.ceil(length/5)
    qualTeams = []
    k = 0
    while k < qualTeamNum:
        qualTeams.append(Clubs[k])
        k = k + 1
    return qualTeams




def main(years):
    leagues = [englishClubs(), frenchClubs(), spanishClubs(), germanClubs()]
    allClubs = []
    for clubsList in leagues:
        clubsList = clubFormation(clubsList)
        for club in clubsList:
            allClubs.append(club)
    for club in allClubs:
        print(club.name, club.skill)
    for i in range(years):
        print('\nYEAR', i + 1)
        championsTeams = []
        for division in leagues:
            Teams = league(division)
            championsTeams = championsTeams + championsQualifiers(Teams)
            #print(Teams)
        print('\nThese teams qualified for Champions League:')
        for team in championsTeams:
            print(team.name)
        championsPath(championsTeams)
        topPlayers = []
        for team in allClubs:
            for person in team.players:
                topPlayers.append(person)
                person.years = person.years - 1
        topPlayers = sorted(topPlayers, key = attrgetter('goals'), reverse = True)
        #print(('\n%-20s %15s %18s')%('Player', 'Team', 'Goals'))
        for player in topPlayers:
            if player.position != 'GK':
                #print(('%-30s %-20s %-2s')%(player.name, player.team, player.goals))
                player.overall = player.overall + round(player.goals/10)
        print('\n')
        availablePlayers = freeAgents(allClubs)
        #os.system('pause')
        transferPlayers = unsatisfiedPlayers(allClubs)
        Teams = transfer(transferPlayers, allClubs)
        #os.system('pause')
        availablePlayers = signingPlayers(availablePlayers, allClubs)
        while availablePlayers:
            availablePlayers = signingPlayers(availablePlayers, allClubs)
        #os.system('pause')
        goalkeeperTrade(allClubs)
        for team in allClubs:
            #print(team)
            if team.money >=0:
                team.money = team.money + 50
            else:
                team.money = team.money + 20
            if team.transferBudget >= 0:
                team.transferBudget = team.transferBudget + 30
            else:
                team.transferBudget = team.transferBudget + 10
            team.points = 0
            team.wins = 0
            team.losses = 0
            team.draws = 0
            team.goaldiff = 0
            for player in team.players:
                player.goals = 0
        #for club in allClubs:
        #    print(club.name, club.skill)
    #print(Teams)
    #for team in allClubs:
        #print(team, len(team.players))
    #    team.players = sorted(team.players, key = attrgetter('overall', 'name'), reverse = True)
    #    for player in team.players:
    #        print(player.name, player.team, player.overall, player.position)
    #    print('\n')



main(5)
