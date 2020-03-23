class team:
    def __init__(team, name, points, wins, draws, losses, skill, goaldiff, championships, players, money, transferBudget, winPercentage):

        team.name = name
        team.points = points
        team.wins = wins
        team.draws = draws
        team.losses = losses
        team.skill = skill
        team.goaldiff = goaldiff
        team.championships = championships
        team.players = players
        team.money = money
        team.transferBudget = transferBudget
        team.winPercentage = winPercentage

    def __repr__(self):
        return repr((self.name, self.skill, self.money, self.transferBudget, self.winPercentage*100))
        #return repr((self.name, self.points, self.wins, self.draws, self.losses, self.skill, self.goaldiff, self.championships))


class player:
    def __init__(player, name, overall, team, position, years, salary, goals, priority, satisfaction):
        player.name = name
        player.overall = overall
        player.team = team
        player.position = position
        player.years = years
        player.salary = salary
        player.goals = goals
        player.priority = priority
        player.satisfaction = satisfaction

    def __repr__(self):
        return repr((self.name, self.overall, self.team, self.position, self.years, self.salary))

