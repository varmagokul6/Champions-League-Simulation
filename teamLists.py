from Teams import team
from random import sample
from leagueGeneral import qualifiers

def premier():
    Tottenham = team('Tottenham', 0, 0, 0, 0, 166, 0, 0)
    Arsenal = team('Arsenal', 0, 0, 0, 0, 164, 0, 0)
    Watford = team('Watford', 0, 0, 0, 0, 150, 0, 0)
    Chelsea = team('Chelsea', 0, 0, 0, 0, 166, 0, 0)
    ManU = team('Man United', 0, 0, 0, 0, 164, 0, 0)
    ManC = team('Man City', 0, 0, 0, 0, 170, 0, 0)
    Liverpool = team('Liverpool', 0, 0, 0, 0, 166, 0, 0)
    WestHam = team('West Ham', 0, 0, 0, 0, 160, 0, 0)
    South = team('Southhampton', 0, 0, 0, 0,150, 0, 0)
    Brighton = team('Brighton', 0, 0, 0, 0, 152, 0, 0)
    Wolves = team('Wolverhampton', 0, 0, 0,0, 160, 0, 0)
    Everton = team('Everton', 0, 0, 0, 0, 158, 0, 0)
    Hudders = team('Huddersfield', 0, 0, 0, 0, 140, 0, 0)
    Cardiff = team('Cardiff City', 0, 0, 0,0, 140, 0, 0)
    LC = team('Leicester City', 0, 0, 0, 0, 156, 0, 0)
    AFC = team('AFC Bournemouth', 0, 0, 0, 0, 152, 0, 0)
    ACM = team('AC Milan', 0, 0, 0, 0, 162, 0, 0)
    Crystal = team('Crystal Palace', 0, 0, 0, 0, 156, 0, 0)
    Newcastle = team('Newcastle', 0, 0, 0, 0, 154, 0, 0)
    Fulham = team('Fulham', 0, 0, 0, 0, 150, 0, 0)
    Burnley = team('Burnley', 0, 0, 0, 0, 154, 0, 0)

    premierTeamsList = [Tottenham, Arsenal, Watford, Chelsea, ManC, ManU, Liverpool, WestHam, South, Brighton, Wolves,
                 Everton, Hudders, Cardiff, LC, AFC, Crystal, Newcastle, Fulham, Burnley]
    topTeams = qualifiers(premierTeamsList)
    return topTeams


def laLiga():
    Barca = team('Barcelona', 0, 0, 0, 0, 172, 0, 0)
    Real = team('Real Madrid', 0, 0, 0, 0, 172, 0, 0)
    Atletico = team('Atletico Madrid', 0, 0, 0, 0, 168, 0, 0)
    Bilbao = team('Atletico Bilbao', 0, 0, 0, 0, 158, 0, 0)
    Celta = team('Celta Vigo', 0, 0, 0, 0, 154, 0, 0)
    Eibar = team('Eibar', 0, 0, 0, 0, 154, 0, 0)
    Espanyol = team('Espanyol', 0, 0, 0, 0, 154, 0, 0)
    Getafe = team('Getafe', 0, 0, 0, 0, 154, 0, 0)
    Granada = team('Granada', 0, 0, 0, 0,150, 0, 0)
    Leganes = team('Leganes', 0, 0, 0, 0, 150, 0, 0)
    Levante = team('Levante', 0, 0, 0,0, 152, 0, 0)
    Osasuna = team('Osasuna', 0, 0, 0, 0, 140, 0, 0)
    Betis = team('Real Betis', 0, 0, 0,0, 160, 0, 0)
    Sociedad = team('Real Sociedad', 0, 0, 0, 0, 156, 0, 0)
    Sevilla = team('Sevilla', 0, 0, 0, 0, 160, 0, 0)
    Valencia = team('Valencia', 0, 0, 0, 0, 160, 0, 0)
    Valladolid = team('Valladolid', 0, 0, 0, 0, 148, 0, 0)
    Villarreal = team('Villarreal', 0, 0, 0, 0, 158, 0, 0)

    laLigaTeamsList = [Barca, Real, Atletico, Bilbao, Celta, Eibar, Espanyol, Getafe, Granada, Leganes, Levante, Osasuna, Betis, Sociedad
        , Sevilla, Valencia, Valladolid, Villarreal]
    topTeams = qualifiers(laLigaTeamsList)
    return topTeams

def serieA():
    Juventus = team('Juventus', 0, 0, 0, 0, 170, 0, 0)
    Napoli = team('Napoli', 0, 0, 0, 0, 164, 0, 0)
    Inter = team('Internazionale', 0, 0, 0, 0, 164, 0, 0)
    Roma = team('Roma', 0, 0, 0, 0, 160, 0, 0)
    Lazio = team('Lazio', 0, 0, 0, 0, 160, 0, 0)
    Milan = team('AC Milan', 0, 0, 0, 0, 160, 0, 0)
    Atalanta = team('Atalanta', 0, 0, 0, 0, 154, 0, 0)
    Torino = team('Torino', 0, 0, 0, 0, 154, 0, 0)
    Sampdoria = team('Sampdoria', 0, 0, 0, 0, 152, 0, 0)
    Fiorentina = team('Fiorentina', 0, 0, 0, 0, 152, 0, 0)
    Bologna = team('Bologna', 0, 0, 0, 0, 150, 0, 0)
    Udinese = team('Udinese', 0, 0, 0, 0, 150, 0, 0)
    Cagliari = team('Cagliari', 0, 0, 0, 0, 150, 0, 0)
    Sassuolo = team('Sassuolo', 0, 0, 0, 0, 150, 0, 0)
    Genoa = team('Genoa', 0, 0, 0, 0, 148, 0, 0)
    SPAL = team('SPAL', 0, 0, 0, 0, 148, 0, 0)

    seriATeamsList = [Juventus, Napoli, Inter, Roma, Lazio, Milan, Atalanta, Torino, Sampdoria, Fiorentina, Bologna, Udinese, Cagliari,
                      Sassuolo, Genoa, SPAL]
    topTeams = qualifiers(seriATeamsList)
    return topTeams

def bundesliga():
    Bayern = team('Bayern Munich', 0, 0, 0, 0, 170, 0, 0)
    Dortmund = team('Dortmund', 0, 0, 0, 0, 162, 0, 0)
    Leverkusen = team('Leverkusen', 0, 0, 0, 0, 160, 0, 0)
    Mgladbach = team('M''gladbach', 0, 0, 0, 0, 158, 0, 0)
    Leipzig = team('RB Leipzig', 0, 0, 0, 0, 158, 0, 0)
    Frankfurt = team('Frankfurt', 0, 0, 0, 0, 156, 0, 0)
    Hoffenheim = team('TSG Hoffenheim', 0, 0, 0, 0, 156, 0, 0)
    Wolfsburg = team('VfL Wolfsburg', 0, 0, 0, 0, 156, 0, 0)
    Schalke = team('Schalke', 0, 0, 0, 0, 156, 0, 0)
    Hertha = team('Hertha BSC', 0, 0, 0, 0, 154, 0, 0)
    Werder = team('Werder', 0, 0, 0, 0, 154, 0, 0)
    Stuttgart = team('VfB Stuttgart', 0, 0, 0, 0, 152, 0, 0)
    Mainz = team('FSV Mainz 05', 0, 0, 0, 0, 150, 0, 0)
    Freiburg = team('SC Freiburg', 0, 0, 0, 0, 148, 0, 0)


    bundesligaTeams = [Bayern, Dortmund, Leverkusen, Mgladbach, Leipzig, Frankfurt, Hoffenheim, Wolfsburg, Schalke, Hertha, Werder, Stuttgart,
                       Mainz, Freiburg]
    topTeams = qualifiers(bundesligaTeams)
    return topTeams

def restOfWorld():
    Lokomotiv = team('Lokomotiv Moscow', 0, 0, 0, 0, 154, 0, 0)
    Spartak = team('Spartak Moscow', 0, 0, 0, 0, 150, 0, 0)
    Brugge = team('Club Brugge', 0, 0, 0, 0, 150, 0, 0)
    Monterrey = team('Monterrey', 0, 0, 0, 0, 150, 0, 0)
    Shakhtar = team('Shakhtar', 0, 0, 0, 0, 150, 0, 0)
    Olymp = team('Olympiacos CFP', 0, 0, 0, 0, 150, 0, 0)
    PAOK = team('PAOK', 0, 0, 0, 0, 150, 0, 0)
    Kyiv = team('Dynamo Kyiv', 0, 0, 0, 0, 150, 0, 0)
    Hilal = team('Al Hilal', 0, 0, 0, 0, 148, 0, 0)
    Young = team('Young Boys', 0, 0, 0, 0, 148, 0, 0)

    worldTeams = [Lokomotiv, Spartak, Brugge, Monterrey, Shakhtar, Olymp, PAOK, Kyiv, Hilal, Young]
    topTeams = qualifiers(worldTeams)
    return topTeams

def ligueOne():
    PSG = team('PSG', 0, 0, 0, 0, 168, 0, 0)
    Monaco = team('AS Monaco', 0, 0, 0, 0, 158, 0, 0)
    OL = team('Lyon', 0, 0, 0, 0, 158, 0, 0)
    OM = team('OM', 0, 0, 0, 0, 156, 0, 0)
    ASSE = team('ASSE', 0, 0, 0, 0, 152, 0, 0)
    Lille = team('LOSC Lille', 0, 0, 0, 0, 152, 0, 0)
    stade = team('Stade Rennais', 0, 0, 0, 0, 150, 0, 0)
    Montpellier = team('Montpellier HSC', 0, 0, 0, 0, 150, 0, 0)
    Nice = team('OGC Nice', 0, 0, 0, 0, 150, 0, 0)
    Nantes = team('FC Nantes', 0, 0, 0, 0, 150, 0, 0)
    Girondins = team('Girondins de Bx', 0, 0, 0, 0, 148, 0, 0)
    Porto = team('FC Porto', 0, 0, 0, 0, 160, 0, 0)

    ligueOneTeams = [PSG, Monaco, OL, OM, ASSE, Lille, stade, Montpellier, Nice, Nantes, Girondins, Porto]
    topTeams = qualifiers(ligueOneTeams)
    return topTeams

def ligaNos():
    Porto = team('FC Porto', 0, 0, 0, 0, 160, 0, 0)
    Benfica = team('SL Benfica', 0, 0, 0, 0, 158, 0, 0)
    Sporting = team('Sproting CP', 0, 0, 0, 0, 156, 0, 0)
    Braga = team('SC Braga', 0, 0, 0, 0, 152, 0, 0)

def eredivisie():
    Ajax = team('Ajax', 0, 0, 0, 0, 160, 0, 0)
    PSV = team('PSV', 0, 0, 0, 0, 154, 0, 0)
    Feyenoord = team('Feyenoord', 0, 0, 0, 0, 148, 0, 0)
    Besiktas = team('Besiktas', 0, 0, 0, 0, 154, 0, 0)
    Galatasary = team('Galatasary', 0, 0, 0, 0, 152, 0, 0)
    Fenerbahce = team('Fenerbahce', 0, 0, 0, 0, 152, 0, 0)
    Benfica = team('SL Benfica', 0, 0, 0, 0, 158, 0, 0)
    Sporting = team('Sporting CP', 0, 0, 0, 0, 156, 0, 0)
    Braga = team('SC Braga', 0, 0, 0, 0, 152, 0, 0)
    Atlanta = team('Atlanta United', 0, 0, 0, 0, 144, 0, 0)

    otherTeams = [Ajax, PSV, Feyenoord, Besiktas, Galatasary, Fenerbahce, Benfica, Sporting, Braga]
    topTeams = qualifiers(otherTeams)
    return topTeams

def randomDiv():
    LAFC = team('LA FC', 0, 0, 0, 0, 140, 0, 0)
    Galaxy = team('LA Galaxy', 0, 0, 0, 0, 138, 0, 0)
    Kerala = team('Kerala Blasters', 0, 0, 0, 0, 120, 0, 0)
    Tokyo = team('Tokyo', 0, 0, 0, 0, 130, 0, 0)
    Pak = team('Pak', 0, 0, 0, 0, 131, 0, 0)
    NewYork = team('New York FC', 0, 0, 0, 0, 115, 0, 0)
    Chenn = team('Super Kings', 0, 0, 0, 0, 119, 0, 0)
    Dallas = team('FC Dallas', 0, 0, 0, 0, 116, 0, 0)

    otherTeams = [LAFC, Galaxy, Kerala, Tokyo, Pak, NewYork, Chenn, Dallas]
    topTeams = qualifiers(otherTeams)
    return topTeams