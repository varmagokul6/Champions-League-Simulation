from ClassList import team, player
from Creation import overallCalc
from random import random, sample
from operator import itemgetter, attrgetter


def freeAgents(allTeams):
    #print(allTeams)
    freeAgents = []
    allTeams = sample(allTeams, len(allTeams))
    for i in allTeams:
        k = 0
        while k < len(i.players):
            player = i.players[k]
            if player.years == 0:
                team = i.players
                team.remove(player)
                freeAgents.append(player)
                player.team = ' '
            else:
                k = k + 1
            #print(player)
    #print(freeAgents)
    return freeAgents


def unsatisfiedPlayers(Teams):
    transferPlayers = []
    Teams = sorted(Teams, key = attrgetter('points' ,'skill', 'goaldiff'), reverse = True)
    #teams = sorted(teams, key = attrgetter('points', 'goaldiff'), reverse = True)
    rank = 1
    for team in Teams:
        for player in team.players:
            #print(player.name, player.satisfaction, player.priority)
            contribution = player.goals * 10
            if player.years != 0:
                if team.skill < 166 and team.winPercentage < .5 and rank/len(Teams) > .25 and player.priority == 'W':
                    player.satisfaction = player.satisfaction - 10*random()
                elif team == Teams[0] or team == Teams[1] or team == Teams[2] or team == Teams[3] or team.skill >=166 and player.priority == 'W':
                    player.satisfaction = player.satisfaction + 10*random()
                elif contribution == 0 and player.priority == 'C' and player.position != 'GK':
                    player.satisfaction = player.satisfaction - 10*random()
                elif contribution > 0 and player.priority == 'C':
                    player.satisfaction = player.satisfaction + contribution*1/2
                elif contribution >= 40 and player.priority == 'M':
                    player.satisfaction = player.satisfaction - 10*random()
                elif player.priority == 'L':
                    player.satisfaction = 50
                if player.satisfaction <= 30:
                    transferPlayers.append(player)
        rank = rank + 1
    return transferPlayers

def findingTradeValue(player, Team):
    playerValue = player.overall + player.salary + player.goals * 5
    tradeOptions = []
    tradeAssets = []
    tradeOptions = sorted(Team.players, key = attrgetter('overall', 'satisfaction'))
    return tradeOptions[0]




def transfer(transferPlayers, Teams):
    Teams = sample(Teams, len(Teams))
    transferPlayers = sorted(transferPlayers, key = attrgetter('overall'), reverse = True)
    #print(transferPlayers)
    #print('Transfer players:')
    #for i in transferPlayers:
    #    print(i.name)
    for player in transferPlayers:
        trade = False
        interest = False
        interestedTeams = []
        maxOffer = 0
        #print(player)
        #print(player, 'Transfer:')
        playerValue = player.overall + player.salary + player.goals * 5
        transferOffer = playerValue/7
        currentTeam = player.team
        if player.priority == 'W':
            #print('W')
            for team in Teams:
                if currentTeam == team.name:
                    currentTeam = team
                    for otherTeams in Teams:
                        ovrWithout = overallCalc(otherTeams.players, otherTeams)
                        ovrWith = overallCalc(otherTeams.players+[player], otherTeams)
                        if otherTeams.winPercentage > currentTeam.winPercentage and len(otherTeams.players) <= 11 and currentTeam != otherTeams:
                            interestedTeams.append(otherTeams)
                            #print(otherTeams.name, "'s skill is greater than", currentTeam.name)
                        elif ovrWith > ovrWithout and currentTeam!= otherTeams:
                            interestedTeams.append(otherTeams)
                            #print(otherTeams.name, 'W is interested in acquiring', player.name)
        elif player.priority == 'C':
            #print('C')
            for team in Teams:
                if player.team == team.name:
                    currentTeam = team
                    for otherTeams in Teams:
                        ovrWithout = overallCalc(otherTeams.players, otherTeams)
                        ovrWith = overallCalc(otherTeams.players+[player], otherTeams)
                        if otherTeams.skill < currentTeam.skill and len(otherTeams.players) < 11 and currentTeam != otherTeams:
                            interestedTeams.append(otherTeams)
                            #print(otherTeams.name, 'provides a better opportunity than', currentTeam.name)
                        elif ovrWith > ovrWithout and currentTeam != otherTeams:
                            interestedTeams.append(otherTeams)
                            #print(otherTeams, 'C is interested in acquiring', player.name)
        elif player.priority == 'M':
            #print('M')
            for team in Teams:
                if player.team == team.name:
                    currentTeam = team
                    for otherTeams in Teams:
                        ovrWithout = overallCalc(otherTeams.players, otherTeams)
                        ovrWith = overallCalc(otherTeams.players+[player], otherTeams)
                        if otherTeams.money >= currentTeam.money and len(otherTeams.players) < 11 and currentTeam != otherTeams:
                            interestedTeams.append(otherTeams)
                            #print('MONEY for this player')
                        elif ovrWith > ovrWithout and currentTeam!= otherTeams:
                            interestedTeams.append(otherTeams)
                            #print(otherTeams.name, 'provides more money than', currentTeam.name)
        tradeValue = 0
        playerTrade = []
        playerValue = player.overall + player.salary + player.goals * 5
        transferOffer = playerValue/7
        topTeam = []
        topTrade = False
        for team in interestedTeams:
            varia = False
            interest = False
            if playerValue/7 > team.transferBudget and len(team.players) != 11:
                transferOffer = team.transferBudget/(11-len(team.players))
                interest = True
                trade = False
                varia = False
                #print('Players is Not 11')
            elif len(team.players) == 11:
                tradePlayer = findingTradeValue(player, team)
                tradeValue = (tradePlayer.overall + tradePlayer.salary + tradePlayer.goals * 5)
                #print(tradePlayer.name, ':', tradeValue, player.name, ':', playerValue)
                #print('Players is 11')
                if tradeValue >= playerValue:
                    transferOffer = tradeValue/7
                #    print('Trade value is greater')
                #    print(team, 'offer:', tradePlayer.name)
                #    print(team, 'offer:', tradePlayer.name)
                else:
                    transferOffer = playerValue/7 + 20*random()
                    #    print('Trade value is lesser')
                    while transferOffer - tradeValue >= team.transferBudget:
                        transferOffer = transferOffer * 9/10
                    #print('Final Offer')
                #    print(team.name, 'offer:', tradePlayer.name, 'and', transferOffer-tradeValue/7)
                trade = True
                varia = True
                interest = True
                #print('Trade Offer:', transferOffer)
            elif playerValue/7 < team.transferBudget:
                #print('Enough money')
                interest = True
                trade = False
                varia = False
                if player.overall >=86:
                    transferOffer = playerValue/6 + team.transferBudget/(12-len(team.players))
                else:
                    transferOffer = playerValue/7
                while transferOffer > team.transferBudget:
                    transferOffer = transferOffer * 9/10
            if transferOffer > maxOffer:
                maxOffer = transferOffer
                topTeam = team
                if varia == True:
                    toptrade = True
                    playerTrade = tradePlayer
                elif varia == False:
                    toptrade = False
            #print(team.name, 'transfer offer for', player.name, ':', transferOffer, 'Trade:', trade, ', Varia:', varia)
        #print(topTeam, toptrade, varia)
        if maxOffer <= (playerValue/7)-5:
            topTeam = []
        if topTeam:
            newTeamroster = topTeam.players
            oldTeamroster = currentTeam.players
            #print(trade, interest)
            if toptrade == False and interest == True:
                #print('No Trade')
                topTeam.transferBudget = topTeam.transferBudget - round(maxOffer)
                currentTeam.transferBudget = currentTeam.transferBudget + round(maxOffer)
                newTeamroster.append(player)
                oldTeamroster.remove(player)
                #print(oldTeamroster)
                print(player.name, '(', player.overall, ') has been transferred from', currentTeam.name, 'to', topTeam.name,
                      'for a fee of $', round(maxOffer), 'M')
                player.team = topTeam.name
                player.satisfaction = 50
            elif toptrade == True and interest == True:
                #print(playerTrade)
                tradeValue = (playerTrade.overall + playerTrade.salary + playerTrade.goals * 5)/7
                transferOffer = round(maxOffer - tradeValue)
                topTeam.transferBudget = topTeam.transferBudget - transferOffer
                currentTeam.transferBudget = currentTeam.transferBudget + transferOffer
                #print(currentTeam)
                #print(newTeamroster)
                #print(oldTeamroster)
                newTeamroster.append(player)
                oldTeamroster.append(playerTrade)
                newTeamroster.remove(playerTrade)
                oldTeamroster.remove(player)
                playerTrade.team = currentTeam.name
                player.team = topTeam.name
                #print(newTeamroster)
                #print(oldTeamroster)
                player.satisfaction = 50
                if player.years < 2:
                    player.years == 3
                if playerTrade.years < 2:
                    player.years == 3
                #for person in tradePlayers:
                #    oldTeamroster.append(person)
                #    person.satisfaction = 50
                #    print(newTeamroster)
                #    newTeamroster.remove(person)
                #    if person.years < 2:
                #        person.years = 3
                #print(oldTeamroster)
                print(player.name, '(', player.overall, ') has been transferred from', currentTeam.name,
                      'to', topTeam.name, 'for a fee of $',
                      transferOffer, 'M and', playerTrade.name, '(', playerTrade.overall, ')')
            #print(currentTeam.name, "'s transfer budget is now: ", currentTeam.transferBudget)
            #print(topTeam.name, "'s transfer budget is now: ", topTeam.transferBudget)
            if maxOffer < 0:
                print('ALERT!!!!')
            if player.priority == 'M' and interest == True:
                player.salary = round(player.salary + topTeam.money/10, 1)
                print(player.name, 'now has a salary of $', player.salary, 'M')
            if player.years < 2:
                player.years = 3
            if interest == True:
                for allPlayers in oldTeamroster:
                    if allPlayers == player:
                        oldTeamroster.remove(player)
                        break
    return Teams

def signingPlayers(availablePlayers, twelve):
    k = 0
    availablePlayers = sorted(availablePlayers, key = attrgetter('overall'), reverse = True)
    #print(availablePlayers)
    #count = len(availablePlayers)
    while k < len(availablePlayers):
        player = availablePlayers[k]
        #print('k =', k)
        #print(player)
        teamsInterested = []
        #print(player)
        playerValue = player.overall/7
        twelve = sample(twelve, len(twelve))
        for team in twelve:
            goalie = False
            ovrWithout = overallCalc(team.players, team)
            ovrWith = overallCalc(team.players+[player], team)
            #print(team.name, 'OVR With:', ovrWith)
            #print(team.name, 'OVR Without:', ovrWithout)
            if player.position == 'GK':
                for players in team.players:
                    if players.position == 'GK':
                        goalie = True
            if playerValue < team.money and ovrWith > ovrWithout and len(team.players) < 11 and goalie == False:
                #    print(team.name, "is interested in", player.name)
                teamsInterested.append(team)
            elif playerValue < team.money and len(team.players) < 11 and goalie == False:
                #    print(team.name, "needs to fill out its roster with", player.name)
                teamsInterested.append(team)
            elif len(team.players) < 11 and goalie == False:
                teamsInterested.append(team)
            elif len(team.players) < 11:
                teamsInterested.append(team)
                #print(team.name, "is not interested in", player.name, '\n')
        playerInterest = 0
        topTeam = []
        maxOffer = 0
        teamsInterested = sample(teamsInterested, len(teamsInterested))
        for team in teamsInterested:
            #print(playerInterest)
            ovrWithout = overallCalc(team.players, team)
            ovrWith = overallCalc(team.players+[player], team)
            if ovrWith - ovrWithout > 3:
                offer = playerValue + ovrWith - ovrWithout + 20 * random()
            else:
                offer = playerValue + ovrWith - ovrWithout + 10 * random()
            #print(team.name, 'Player Offer:', offer)
            #while offer > team.money//(11-len(team.players)):          PROBLEM
            #offer = offer*6/8
            if offer < team.money and ovrWith > ovrWithout:
                if team.skill/5 + offer > playerInterest:
                    playerInterest = team.skill/5 + offer
                    topTeam = team
                    maxOffer = offer
            elif offer < team.money:
                offer = playerValue + ovrWith - ovrWithout
                if team.skill/5 + offer > playerInterest:
                    playerInterest = team.skill/5 + offer
                    #print('Player Interest in', team.name, 'is:', playerInterest)
                    topTeam = team
                    maxOffer = offer
            else:
                while offer > team.money:
                    offer = offer * 9/10
                if team.skill/5 + offer > playerInterest:
                    playerInterest = team.skill/5 + offer
                    #print('Player Interest in', team.name, 'is:', playerInterest)
                    topTeam = team
                    maxOffer = offer
            #print('Player Interest in', team.name, 'is:', team.skill/5 + offer)
        if topTeam:
            roster = topTeam.players
            roster.append(player)
            player.salary = maxOffer // 1
            while player.years == 0:
                player.years = round(4*random())
            #print(topTeam.name, "salary before:", topTeam.money)
            topTeam.money = topTeam.money - player.salary
            print(player.name, '(', player.overall, ')',"has signed with", topTeam.name, "for $", player.salary,
                  'M per year for', player.years, 'Years')
            #print(topTeam.name, "salary after:", topTeam.money, '\n')
            player.team = topTeam.name
            availablePlayers.remove(player)
        else:
            k = k + 1
    #print(availablePlayers)
    for team in twelve:
        print(team, len(team.players))
        #print(team.players)
    #print('\n', availablePlayers)
    return availablePlayers

def yearLoop(years, teams):
    k = 0
    while k < years:
        print('\nFree Agency: Year', k + 1,' \n')
        availablePlayers = freeAgents(teams)
        signingPlayers(availablePlayers, teams)
        for team in teams:
            #print(team)
            team.money = team.money + 60
            for player in team.players:
                player.years = player.years - 1
        k = k + 1


def goalkeeperTrade(Teams):
    multipleGoalieTeams = []
    noGoalieTeams = []
    availableGoalies = []
    for team in Teams:
        goalie = False
        count = 0
        for player in team.players:
            if player.position == 'GK':
                count = count + 1
                goalie = True
        if goalie == False:
            noGoalieTeams.append(team)
        elif count > 1:
            #print(team.name, 'has', count, 'goalies')
            multipleGoalieTeams.append(team)
    for team in multipleGoalieTeams:
        count = 0
        team.players = sorted(team.players, key = attrgetter('overall', 'satisfaction'))
        k = 0
        for player in team.players:
            if player.position == 'GK':
                count = count + 1
        for player in team.players:
            if player.position == 'GK':
                #print(player)
                if k < count-1:
                    availableGoalies.append(player)
                k = k + 1
    #print(availableGoalies)
    availableGoalies = sample(availableGoalies, len(availableGoalies))
    #print(len(availableGoalies), len(noGoalieTeams))
    noGoalieTeams = sample(noGoalieTeams, len(noGoalieTeams))
    #print(noGoalieTeams, 'need goalie')
    #print(multipleGoalieTeams, 'have too many goalies')
    if len(availableGoalies) != 0:
        for team in noGoalieTeams:
            tradeGoalie = availableGoalies[0]
            goalieValue = tradeGoalie.overall + tradeGoalie.salary + tradeGoalie.goals * 5
            team.players = sorted(team.players, key = attrgetter('overall', 'satisfaction'), reverse = True)
            #print(team.players)
            tradePlayer = team.players[0]
            for player in team.players:
                playerValue = player.overall + player.salary# + player.goals * 5
                if playerValue >= goalieValue:
                    tradePlayer = player
                else:
                    break
            for club in Teams:
                if tradeGoalie.team == club.name:
                    currentClub = club
            currentClub.players.append(tradePlayer)
            tradePlayer.team = currentClub.name
            team.players.append(tradeGoalie)
            tradeGoalie.team = team.name
            currentClub.players.remove(tradeGoalie)
            team.players.remove(tradePlayer)
            availableGoalies.remove(tradeGoalie)
            print(tradeGoalie.name, tradeGoalie.overall, 'has been transferred from', currentClub.name, 'to', team.name,
                  'in exchange for', tradePlayer.name, tradePlayer.overall)

