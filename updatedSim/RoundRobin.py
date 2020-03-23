import math
from random import random
from operator import itemgetter, attrgetter
import os
from Match import points, match, advancedMatch


def roundRobin(Teams):
    n = len(Teams)
    map = list(range(n))    #map is array of numbers from 1 to n
    s = []
    mid = n // 2
    #print(map)
    for i in range(n-1):
        l1 = map[:mid]
        l2 = map[mid:]
        l2.reverse()
        #  print(l1)
        #   print(l2)
        round = []
        for j in range(mid):
            t1 = Teams[l1[j]]
            t2 = Teams[l2[j]]
            if j == 0 and i % 2 == 1:
                round.append((t2,t1))
            #            print(round)
            else:
                round.append((t1,t2))
        #            print(round)
        s.append(round)
        map = map[mid:-1] + map[:mid] + map[-1:]
    #print(s)
    k = 1
    for i in range(n-1):
        round = s[i]
        #print(s[i])
        print('\nWeek', k, ':\n')
        for j in round:
            Team1 = j[0]
            #print('\n', Team1.name, 'is home\n')
            advancedMatch(j[0], j[1], 0)
            #os.system('pause')
            #commentary(Teams)
        rankings(Teams)
        k = k + 1
    for i in range(n-1):
        l1 = map[:mid]
        l2 = map[mid:]
        #print(l1)
        #print(l2)
        #l2.reverse()
        #  print(l1)
        #   print(l2)
        round = []
        for j in range(mid):
            t1 = Teams[l2[j]]
            t2 = Teams[l1[j]]
            if j == 0 and i % 2 == 1:
                round.append((t2,t1))
            #            print(round)
            else:
                round.append((t1,t2))
        #            print(round)
        s.append(round)
        map = map[mid:-1] + map[:mid] + map[-1:]
    for i in range(n-1):
        round = s[i]
        #print(s[i])
        print('\nWeek', k, ':\n')
        for j in round:
            #Team2 = j[1]
            #print(Team2.name, 'is home\n')
            advancedMatch(j[1], j[0], 0)
            #os.system('pause')
            #commentary(Teams)
        rankings(Teams)
        k = k + 1

def commentary(Teams):
    Teams = sorted(Teams, key = attrgetter('points', 'goaldiff', 'wins'), reverse = True)
    totalMatches = 2 * (len(Teams)-1)
    topTeam = Teams[0]
    elim = 0
    for team in Teams:
        mp = team.wins + team.losses + team.draws
        left = totalMatches - mp
        if team.name == topTeam.name:
            print(team.name, "is currently the top team.")
        else:
            if team.points + left * 3 > topTeam.points:
                print(team.name, "is still in the race.")
            elif team.points + left * 3 == topTeam.points:
                print(team.name, "has a chance")
            else:
                print(team.name, "has been eliminated")
                elim = elim +1
        if elim == len(Teams)-1:
            print('\n', topTeam.name, 'has claimed the championship with', left, 'games remaining!')

    print('\n')


def rankings(Teams):
    print('\n')
    MyList = sorted(Teams, key = attrgetter('points', 'goaldiff', 'wins'), reverse = True)
    print(('%-25s %3s %3s %3s %3s %3s %3s %3s') % ('Team', 'MP', 'Pts', 'W', 'D', 'L', 'GD', 'WP'))
    for i in MyList:
        matches = i.wins + i.losses + i.draws
        if matches == 0:
            i.winPercentage = 0
        else:
            i.winPercentage = (i.points)/(3*matches)
        print (("%-25s %3i %3i %3i %3i %3i %3i %4.2f") % (i.name, matches, i.points, i.wins, i.draws, i.losses, i.goaldiff,
                                                          i.winPercentage))
    return MyList

