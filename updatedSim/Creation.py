from ClassList import player, team
import random

def salaryCalc(overall):
    if overall <= 83:
        salary = (10/83)* overall
    else:
        salary = (20/99) * overall
    salary = round(salary, 1)
    return salary

def overallCalc(players, team):
    ovr = 0
    #print(len(players))
    for i in players:
        ovr = ovr + i.overall
    if len(players) == 0:
        ovr = 0
    else:
        ovr = round(ovr/(len(players)))
    team.skill = ovr * 2
    #print(team.name, 'OVR:', ovr)
    return team.skill

def priorityDict(index):
    priority = ['C', 'W', 'M', 'L']
    priority = random.sample(priority, len(priority))
    return priority[index]

def playerNameGenerate():
    first_names = ('John', 'Harry', 'Raheem', 'Paulo', 'Lionel', 'Giovanni', 'Pablo', 'Fred', 'Pierre', 'Manuel',
                   'Hugo', 'Alfred', 'James', 'Rick','Norman', 'Giuseppe',
                   'Coos', 'Veljko', 'Calvin', 'Werner', 'Filiberto', 'Dell',
                   'Quinn', 'Julius', 'Julian', 'Gary', 'Wayne', 'Luka', 'Niko', 'Mohammad', 'Chris', 'David')
    last_names = ('Chandler', 'Boothman', 'Sterling', 'Johnson', 'Anderson',
                  'Behringer', 'Ramsey', 'Kirby', 'Howe', 'Westley', 'Chadwick',
                  'Rudawski', 'Riggi', 'Lynton', 'Schuhart', 'Nichols', 'Albert', 'London',
                  'Seaver', 'Raskob', 'Kroger', 'Haymens', 'Kunz', 'De Veen', 'Lawrenz',
                  'Aalfs', 'Hersch', 'Kay', 'Oliver', 'Beulens', 'Pottinger', 'Alfero', 'Brewster',
                  'Prince', 'Johnson')
    playerName = random.choice(first_names) + " " + random.choice(last_names)
    return playerName


def playerOverallGenerator():
    ovr = round(random.random() * 95)
    while ovr < 70:
        ovr = round(random.random() * 95)
    player.salary = salaryCalc(ovr)
    player.years = round(4 * random.random())
    return ovr


def playerPosition(loopVal):
    posDict = ['GK', 'RB', 'CB', 'LB', 'CDM', 'CDM', 'CAM', 'CAM', 'RW', 'LW', 'ST']
    return posDict[loopVal]

def playerCreator(Team):
    roster = Team.players
    for i in range(11):
        satisfaction = round(3*random.random())
        member = player(playerNameGenerate(), playerOverallGenerator(), Team.name, playerPosition(i), 0, 0, 0,
                        priorityDict(satisfaction), 100*random.random())
        member.salary = salaryCalc(member.overall)
        member.years = round(4*random.random())
        while member.years == 0:
            member.years = round(4*random.random())
        roster.append(member)
    return Team
