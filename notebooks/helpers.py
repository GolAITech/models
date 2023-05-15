import pandas as pd

team_tiers = {
    'Leicester City': "3", 
    'Stoke City': "-1", 
    'West Bromwich Albion': "-1",
    'Amiens SC': "-1", 
    'Strasbourg': "3", 
    'Hamburger SV': "-1", 
    'SC Freiburg': "4",
    'Hannover 96': "-1", 
    'VfL Wolfsburg': "2",
    'Bayer 04 Leverkusen': "1",
       'Borussia Dortmund': "1", 
    'FC Bayern München': "1", 
    'RB Leipzig': "2", 
    'Sassuolo': "3",
       'Fiorentina': "3", 
    'Watford': "-1", 
    'Deportivo La Coruña': "-1", 
    'Celta de Vigo': "4",
       'Levante': "-1", 
    'VfB Stuttgart': "5", 
    'Real Betis': "3",
    'Girona': "5",
       'AFC Bournemouth': "6", 
    'Crystal Palace': "5", 
    'Liverpool': "1", 
    'Chelsea': "1",
       'Newcastle United': "4", 
    'Southampton': "4", 
    'Manchester City': "1",
       'Huddersfield Town': "-1", 
    'Brighton & Hove Albion': "6", 
    'Swansea City': "-1",
       'Rennes': "2", 
    'Saint-Étienne': "-1", 
    'Troyes': "6", 
    'FC Köln': "-1",
       'Borussia Mönchengladbach': "3", 
    'FSV Mainz 05': "4", 
    'Hertha BSC': "3",
       'Manchester United': "2", 
    'Dijon': "-1", 
    'Monaco': "1", 
    'Benevento': "-1", 
    'FC Augsburg': "4",
       'Caen': "-1", 
    'Sevilla': "2", 
    'Málaga': "-1", 
    'Angers SCO': "6", 
    'Deportivo Alavés': "-1",
       'Montpellier': "3",
    'Werder Bremen': "6", 
    'Cagliari': "-1", 
    'Athletic Club': "3",
       'Bologna': "-1", 
    'Genoa': "-1",
    'Hellas Verona': "6",
    'Nantes': "4", 
    'Nice': "3",
       'Olympique Lyonnais': "-1",
    'Metz': "-1", 
    'Paris Saint Germain': "1",
    'Leganés': "-1",
       'Las Palmas': "-1", 
    'Everton': "3",
    'Udinese': "4", 
    'Bordeaux': "-1", 
    'Sampdoria': "4",
       'Inter': "2",
    'Tottenham Hotspur': "2",
    'Arsenal': "2",
    'Lazio': "2",
       'West Ham United': "3",
    'Burnley': "-1", 
    'Roma':"1",
    'Torino': "3",
    'FC Barcelona': "1",
       'Olympique Marseille':"2",
    'Real Sociedad': "3",
    'Villarreal': "2",
       'Atlético Madrid':"3",
    'SD Eibar': "-1", 
    'Real Madrid': "1",
    'Getafe': "3",
    'Crotone': "-1",
       'Espanyol': "4", 
    'Valencia': "2",
    'Schalke 04': "2",
    'Guingamp': "-1", 
    'Lille': "-1",
       'Toulouse': "5",
    'Eintracht Frankfurt': "-1",
    'TSG Hoffenheim': "3",
    'Milan': "2",
       'Juventus':"1",
    'Napoli':"1",
    'SPAL': "-1", 
    'Atalanta': "3",
    'Chievo': "-1",
    'Cardiff City': "-1",
       'Wolverhampton Wanderers': "-1", 
    'Frosinone': "-1", 
    'Flamengo': "-1", 
    'Empoli': "5",
       'Reims': "3",
    'Rayo Vallecano': "5",
    'Nîmes': "-1", 
    'Fulham': "5", 
    'Fortuna Düsseldorf': "-1",
       'Nürnberg': "-1", 
    'Huesca': "-1",
    'Parma': "-1",
    'Corinthians': "-1", 
    'Real Valladolid': "6",
       'Brescia': "-1",
    'Lecce': "6", 
    'Paderborn': "-1", 
    'FC Union Berlin': "3",
    'Granada': "-1",
       'Norwich City': "-1",
    'Osasuna': "4",
    'Mallorca': "5",
    'Brest': "6",
    'Palmeiras': "-1",
       'Santos': "-1", 
    'Sheffield United': "-1",
    'Fluminense': "-1",
    'Aston Villa': "4",
       'Leeds United': "5",
    'Elche': "6",
    'Cádiz': "6",
    'Lorient': "5",
       'DSC Arminia Bielefeld': "-1", 
    'Spezia': "6",
    'Lens': "4",
    'Botafogo': "-1", 
    'Brentford': "6",
       'Internacional': "-1",
    'VfL Bochum 1848': "6",
    'Venezia': "-1", 
    'Clermont': "4",
       'Salernitana': "5",
    'Sport Recife': "-1",
    'SpVgg Greuther Fürth': "-1"
}
TEAM_TIERS = pd.Series(team_tiers, name="tier")