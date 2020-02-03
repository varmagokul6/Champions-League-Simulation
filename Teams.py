class team:
    def __init__(team, name, points, wins, draws, losses, skill, goaldiff, championships):

        team.name = name
        team.points = points
        team.wins = wins
        team.draws = draws
        team.losses = losses
        team.skill = skill
        team.goaldiff = goaldiff
        team.championships = championships

    def __repr__(self):
        return repr((self.name, self.points, self.wins, self.draws, self.losses, self.skill, self.goaldiff, self.championships))