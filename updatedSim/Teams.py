from ClassList import player, team
import random
from Creation import playerCreator, overallCalc


def clubs():
    lions = team('Berlin Lions', 0, 0, 0, 0, 0, 0, 0, [], 60, 60, 0)
    kings = team('Kings City', 0, 0, 0, 0, 0, 0, 0, [], 60, 60, 0)
    bulls = team('Red Bulls Madrid', 0, 0, 0, 0, 0, 0, 0, [], 60, 60, 0)
    italia = team('Italia Infinity', 0, 0, 0, 0, 0, 0, 0, [], 60, 60, 0)
    paris = team('FC Paris', 0, 0, 0, 0, 0, 0, 0, [], 60, 60, 0)
    benelux = team('Benelux United', 0, 0, 0, 0, 0, 0, 0, [], 60, 60, 0)
    royal = team('Royal Fighters East', 0, 0, 0, 0, 0, 0, 0, [], 60, 60, 0)
    redDev = team('FC Red Devils', 0, 0, 0, 0, 0, 0, 0, [], 60, 60, 0)

    list = [lions, kings, bulls, italia, paris, benelux, royal, redDev]
    return list

def englishClubs():
    Tottenham = team('Tottenham', 0, 0, 0, 0, 0, 0, 0, [], 60, 60, 0)
    Arsenal = team('Arsenal', 0, 0, 0, 0, 0, 0, 0, [], 60, 60, 0)
    Chelsea = team('Chelsea', 0, 0, 0, 0, 0, 0, 0, [], 60, 60, 0)
    ManU = team('Man United', 0, 0, 0, 0, 0, 0, 0, [], 60, 60, 0)
    ManC = team('Man City', 0, 0, 0, 0, 0, 0, 0, [], 60, 60, 0)
    Liverpool = team('Liverpool', 0, 0, 0, 0, 0, 0, 0, [], 60, 60, 0)
    Wolves = team('Wolverhampton', 0, 0, 0, 0, 0, 0, 0, [], 60, 60, 0)
    Everton = team('Everton', 0, 0, 0, 0, 0, 0, 0, [], 60, 60, 0)
    Hudders = team('Huddersfield', 0, 0, 0, 0, 0, 0, 0, [], 60, 60, 0)
    Cardiff = team('Cardiff City', 0, 0, 0, 0, 0, 0, 0, [], 60, 60, 0)
    LC = team('Leicester City', 0, 0, 0, 0, 0, 0, 0, [], 60, 60, 0)
    WestHam = team('West Ham', 0, 0, 0, 0, 0, 0, 0, [], 60, 60, 0)
    Aston = team('Aston Villa', 0, 0, 0, 0, 0, 0, 0, [], 60, 60, 0)
    Watford = team('Watford', 0, 0, 0, 0, 0, 0, 0, [], 60, 60, 0)
    Bourne = team('Bournemouth', 0, 0, 0, 0, 0, 0, 0, [], 60, 60, 0)
    South = team('Southampton', 0, 0, 0, 0, 0, 0, 0, [], 60, 60, 0)


    list = [Tottenham, Arsenal, Chelsea, ManU, ManC, Liverpool, Wolves, Everton, Hudders, Cardiff,
            LC, WestHam, Aston, Watford, Bourne, South]
    return list

def frenchClubs():
    PSG = team('PSG',  0, 0, 0, 0, 0, 0, 0, [], 60, 60, 0)
    Monaco = team('AS Monaco',  0, 0, 0, 0, 0, 0, 0, [], 60, 60, 0)
    OL = team('Lyon',  0, 0, 0, 0, 0, 0, 0, [], 60, 60, 0)
    OM = team('Marseille',  0, 0, 0, 0, 0, 0, 0, [], 60, 60, 0)
    Nantes = team('Nantes',  0, 0, 0, 0, 0, 0, 0, [], 60, 60, 0)
    Lille = team('Lille',  0, 0, 0, 0, 0, 0, 0, [], 60, 60, 0)
    Montpellier = team('Montpellier HSC', 0, 0, 0, 0, 0, 0, 0, [], 60, 60, 0)
    Nice = team('OGC Nice', 0, 0, 0, 0, 0, 0, 0, [], 60, 60, 0)
    stade = team('Stade Rennais', 0, 0, 0, 0, 0, 0, 0, [], 60, 60, 0)
    Girondins = team('Girondins de Bx', 0, 0, 0, 0, 0, 0, 0, [], 60, 60, 0)
    ASSE = team('ASSE', 0, 0, 0, 0, 0, 0, 0, [], 60, 60, 0)
    Metz = team('Metz', 0, 0, 0, 0, 0, 0, 0, [], 60, 60, 0)
    Saint = team('Saint-Etienne', 0, 0, 0, 0, 0, 0, 0, [], 60, 60, 0)
    Stras = team('Strasbourg', 0, 0, 0, 0, 0, 0, 0, [], 60, 60, 0)
    Toulouse = team('Toulouse', 0, 0, 0, 0, 0, 0, 0, [], 60, 60, 0)
    Nimes = team('Nimes', 0, 0, 0, 0, 0, 0, 0, [], 60, 60, 0)

    list = [PSG, Monaco, OL, OM, Nantes, Lille, Montpellier, Nice, stade, Girondins, ASSE,
            Metz, Saint, Stras, Toulouse, Nimes]
    return list

def spanishClubs():
    Barca = team('Barcelona', 0, 0, 0, 0, 0, 0, 0, [], 60, 60, 0)
    Real = team('Real Madrid', 0, 0, 0, 0, 0, 0, 0, [], 60, 60, 0)
    Atletico = team('Atletico Madrid', 0, 0, 0, 0, 0, 0, 0, [], 60, 60, 0)
    Bilbao = team('Atletico Bilbao', 0, 0, 0, 0, 0, 0, 0, [], 60, 60, 0)
    Celta = team('Celta Vigo', 0, 0, 0, 0, 0, 0, 0, [], 60, 60, 0)
    Eibar = team('Eibar', 0, 0, 0, 0, 0, 0, 0, [], 60, 60, 0)
    Espanyol = team('Espanyol', 0, 0, 0, 0, 0, 0, 0, [], 60, 60, 0)
    Getafe = team('Getafe', 0, 0, 0, 0, 0, 0, 0, [], 60, 60, 0)
    Granada = team('Granada', 0, 0, 0, 0, 0, 0, 0, [], 60, 60, 0)
    Leganes = team('Leganes', 0, 0, 0, 0, 0, 0, 0, [], 60, 60, 0)
    Levante = team('Levante', 0, 0, 0, 0, 0, 0, 0, [], 60, 60, 0)
    Betis = team('Betis', 0, 0, 0, 0, 0, 0, 0, [], 60, 60, 0)
    Osasuna = team('Osasuna', 0, 0, 0, 0, 0, 0, 0, [], 60, 60, 0)
    Sevilla = team('Sevilla', 0, 0, 0, 0, 0, 0, 0, [], 60, 60, 0)
    Valencia = team('Valencia', 0, 0, 0, 0, 0, 0, 0, [], 60, 60, 0)
    Sociedad = team('Sociedad', 0, 0, 0, 0, 0, 0, 0, [], 60, 60, 0)

    list = [Barca, Real, Atletico, Bilbao, Celta, Eibar, Espanyol, Getafe, Granada, Leganes, Levante,
            Betis, Osasuna, Sevilla, Valencia, Sociedad]
    return list

def germanClubs():
    Bayern = team('Bayern Munich', 0, 0, 0, 0, 0, 0, 0, [], 60, 60, 0)
    Dortmund = team('Dortmund', 0, 0, 0, 0, 0, 0, 0, [], 60, 60, 0)
    Leverkusen = team('Leverkusen', 0, 0, 0, 0, 0, 0, 0, [], 60, 60, 0)
    Mgladbach = team('M''gladbach', 0, 0, 0, 0, 0, 0, 0, [], 60, 60, 0)
    Leipzig = team('RB Leipzig', 0, 0, 0, 0, 0, 0, 0, [], 60, 60, 0)
    Frankfurt = team('Frankfurt', 0, 0, 0, 0, 0, 0, 0, [], 60, 60, 0)
    Hoffenheim = team('TSG Hoffenheim', 0, 0, 0, 0, 0, 0, 0, [], 60, 60, 0)
    Wolfsburg = team('VfL Wolfsburg', 0, 0, 0, 0, 0, 0, 0, [], 60, 60, 0)
    Schalke = team('Schalke', 0, 0, 0, 0, 0, 0, 0, [], 60, 60, 0)
    Hertha = team('Hertha BSC', 0, 0, 0, 0, 0, 0, 0, [], 60, 60, 0)
    Werder = team('Werder', 0, 0, 0, 0, 0, 0, 0, [], 60, 60, 0)
    Stuttgart = team('VfB Stuttgart', 0, 0, 0, 0, 0, 0, 0, [], 60, 60, 0)
    Mainz = team('FSV Mainz 05',0, 0, 0, 0, 0, 0, 0, [], 60, 60, 0)
    Freiburg = team('SC Freiburg', 0, 0, 0, 0, 0, 0, 0, [], 60, 60, 0)
    Augs = team('FC Augsburg', 0, 0, 0, 0, 0, 0, 0, [], 60, 60, 0)
    Union = team('Union Berlin', 0, 0, 0, 0, 0, 0, 0, [], 60, 60, 0)


    bundesligaTeams = [Bayern, Dortmund, Leverkusen, Mgladbach, Leipzig, Frankfurt, Hoffenheim, Wolfsburg, Schalke,
                       Hertha, Werder, Stuttgart, Mainz, Freiburg, Augs, Union]
    return bundesligaTeams

def clubFormation(clubs):
    for club in clubs:
        club = playerCreator(club)
    for club in clubs:
        club.skill = overallCalc(club.players, club)
    return clubs

