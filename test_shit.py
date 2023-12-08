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

# Function to simulate a playoff round
def simulate_playoff_round(teams):
    winners = []

    # Sort teams and seeds before the playoff round
    teams.sort(key=lambda x: x[1])  # Sort by seeds

    while len(teams) > 1:
        team1, seed1 = teams.pop(0)
        team2, seed2 = teams.pop()  # Select teams from the end of the list to pair seeds correctly

        # Determine the home and away teams
        home_team, away_team = (team1, team2) if seed1 < seed2 else (team2, team1)

        # If seeds are the same, randomly assign home and away
        if seed1 == seed2:
            home_team, away_team = random.sample([team1, team2], k=2)

        # Get simultaneous user input for the scores with tie check
        while True:
            try:
                print(f"\nHome Team ({home_team} - Seed {seed1}) vs. Away Team ({away_team} - Seed {seed2}):")
                score_home_team = int(input(f"{home_team}: "))
                score_away_team = int(input(f"{away_team}: "))

                # Check for a tie
                if score_home_team == score_away_team:
                    raise ValueError("Scores cannot be tied. Please enter different scores.")

                break
            except ValueError as e:
                print(f"Error: {e}")

        # Determine the winner based on scores
        winner = home_team if score_home_team > score_away_team else away_team

        # Append the winner to the list, preserving the original seeds
        # winners.append((winner, seed1 if winner == home_team else seed2))

        # Append the winner to the list, preserving the original seeds
        winners.append((winner, seed1 if winner == team1 else seed2))

    return winners


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
# print("Playoff Teams")
# print("Teams:", playoff_data_instance.team)
# print("Conferences:", playoff_data_instance.conference)
# print("Seeds:", playoff_data_instance.seed)
# print("Playoff Record:", playoff_data_instance.playoff_record)

nfc_playoffs = []
afc_playoffs = []

for x in range(len(playoff_data_instance.team)):
    if playoff_data_instance.conference[x] == "NFC":
        nfc_playoffs.append((playoff_data_instance.team[x], playoff_data_instance.seed[x]))
    else:
        afc_playoffs.append((playoff_data_instance.team[x], playoff_data_instance.seed[x]))

print(f"AFC Playoffs are: {afc_playoffs} \n")
print(f"NFC Playoffs are: {nfc_playoffs} \n")

# Simulate playoff rounds for AFC and NFC
while len(afc_playoffs) > 1:
    afc_playoffs = simulate_playoff_round(afc_playoffs)

while len(nfc_playoffs) > 1:
    nfc_playoffs = simulate_playoff_round(nfc_playoffs)

# Print the champions
print(f"AFC Champion: {afc_playoffs[0][0]} Ranked: {afc_playoffs[0][1]}")
print(f"NFC Champion: {nfc_playoffs[0][0]} Ranked: {nfc_playoffs[0][1]}")

# Simulate the final round for League Championship
league_championship = [(afc_playoffs[0][0], afc_playoffs[0][1]), (nfc_playoffs[0][0], nfc_playoffs[0][1])]

while len(league_championship) > 1:
    league_championship = simulate_playoff_round(league_championship)

# Print the League Champion
league_champion = league_championship[0][0]
print(f"League Champion: {league_champion} Ranked: {league_championship[0][1]}")
