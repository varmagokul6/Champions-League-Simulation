import math
from random import random
from roundRobin import  roundRobin, rankings
from Teams import team

def history(Teams, n):
    for i in range(n):
        print('\nYear', i+1, ':')
        Teams = main(Teams)
        #myList = rankings(Teams)
        for k in Teams:
            k.points = 0
            k.wins = 0
            k.losses = 0
            k.draws = 0
            k.goaldiff = 0
            #print(k.points)
    return Teams

def championsSearch(Teams):
    print('\nChampions:')
    for i in Teams:
        trophies = i.championships
        if trophies > 1:
            print(i.name, '(', trophies, ')')
        elif trophies == 1:
            print(i.name)

def changeinSkill(TeamsList):
    k = 0
    for i in TeamsList:
        if k % 2 == 0:
            i.skill = i.skill - 1
        else:
            i.skill = i.skill + 2
        x = math.floor(random()*len(TeamsList))
        #print(x)
        if i == TeamsList[x]:
            i.skill = i.skill - 5

        k = k + 1

def main(TeamsList):
    roundRobin(TeamsList)
    #roundRobin(TeamsList)
    top = rankings(TeamsList)
    print('\n', top[0].name, 'is the champion!')
    champion = top[0]
    champion.championships = champion.championships + 1
    #os.system("pause")
    #changeinSkill(top)
    return top

def mainProgram(TeamsList):
    results = history(TeamsList, 1)
    championsSearch(results)
    print('\n')
    for i in TeamsList:
        print(i.name, i.skill)
    #return

def qualifiers(TeamsList):
    teams = main(TeamsList)
    qualified = []
    for i in range(4):
        qualified.append(teams[i])
    #    print(qualified)
    return qualified