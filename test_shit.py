from dataclasses import dataclass, field
from typing import Tuple, List
import random
import time

@dataclass (frozen=False)
class PlayoffData:
    team: List[str]
    conference: List[str]
    seed: List[int]
    playoff_record: list = field(default_factory=lambda: [0,0])

@dataclass (frozen=False)
class RegularSeasonData:
    team: str 
    conference: str
    in_playoffs: bool
    seed: int
    record: list = field(default_factory=lambda: [0,0])

@dataclass (frozen=False)
class LeagueData:
    teams: List[RegularSeasonData]


Teams_Conf = [('Arizona Cardinals', 'NFC'),('Atlanta Falcons', 'NFC'),('Baltimore Ravens', 'AFC'),('Buffalo Bills', 'AFC'),('Carolina Panthers', 'NFC'),
              ('Chicago Bears', 'NFC'),('Cincinnati Bengals', 'AFC'),('Cleveland Browns', 'AFC'),('Dallas Cowboys', 'NFC'),('Denver Broncos', 'AFC'),
              ('Detroit Lions', 'NFC'),('Green Bay Packers', 'NFC'),('Houston Texans', 'AFC'),('Indianapolis Colts', 'AFC'),('Jacksonville Jaguars', 'AFC'),
              ('Kansas City Chiefs', 'AFC'),('Los Angeles Chargers', 'AFC'),('Los Angeles Rams', 'NFC'),('Las Vegas Raiders', 'AFC'),
              ('Miami Dolphins', 'AFC'),('Minnesota Vikings', 'NFC'),('New England Patriots', 'AFC'),('New Orleans Saints', 'NFC'),('New York Giants', 'NFC'),
              ('New York Jets', 'AFC'),('Philadelphia Eagles', 'NFC'),('Pittsburgh Steelers', 'AFC'),('Seattle Seahawks', 'NFC'),('San Francisco 49ers', 'NFC'),
              ('Tampa Bay Buccaneers', 'NFC'),('Tennessee Titans', 'AFC'),('Washington Commanders', 'NFC')
              ]


start_time = time.time()
teamlist: List[RegularSeasonData] = []

# Initializing the Regular Season
for team_info in Teams_Conf:

    Win = random.randint(0,17)
    Loss = 17 - Win
    record_rand = [Win, Loss]
    
    seed = 0  # Initialize seed
    
    teams = RegularSeasonData(team_info[0], team_info[1], in_playoffs=False, seed=seed, record=record_rand)
    teamlist.append(teams)

# Sort teams within each conference based on wins and assign playoff eligibility and seed
for conf in set(team.conference for team in teamlist):
    teams_in_conf = [team for team in teamlist if team.conference == conf]
    teams_in_conf.sort(key=lambda x: x.record[0], reverse=True)
    
    for i, team in enumerate(teams_in_conf):
        team.seed = i + 1
        team.in_playoffs = i < 8
        

end_time = time.time()

print(f"total time taken this loop: {end_time - start_time}s \n")

NFL = LeagueData(teamlist)

# Create an instance of PlayoffData
playoff_data_instance = PlayoffData(team=[], conference=[], seed=[])

for team_data in NFL.teams:
    # Check if the team is in playoffs
    if team_data.in_playoffs:
        # Append relevant information to PlayoffData
        playoff_data_instance.team.append(team_data.team)
        playoff_data_instance.conference.append(team_data.conference)
        playoff_data_instance.seed.append(team_data.seed)

# Print the PlayoffData
print("Playoff Teams")
print("Teams:", playoff_data_instance.team)
print("Conferences:", playoff_data_instance.conference)
print("Seeds:", playoff_data_instance.seed)
print("Playoff Record:", playoff_data_instance.playoff_record)