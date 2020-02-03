import math
from listOfTeams import TeamsList
from random import random
from operator import itemgetter, attrgetter
from Match import points, match


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
            match(j[0], j[1])
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
            match(j[1], j[0])
        k = k + 1

def rankings(Teams):
    print('\n')
    MyList = sorted(Teams, key = attrgetter('points', 'goaldiff'), reverse = True)
    print(('%-25s %3s %3s %3s %3s %3s') % ('Team', 'Pts', 'W', 'D', 'L', 'GD'))
    for i in MyList:
        print (("%-25s %3i %3i %3i %3i %3i") % (i.name, i.points, i.wins, i.draws, i.losses, i.goaldiff))
    return MyList

