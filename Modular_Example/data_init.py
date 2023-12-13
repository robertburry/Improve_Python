# data_init.py
import csv
import random 
from data_classes import RegularSeasonData, LeagueData, PlayoffData
from typing import List, Tuple

def read_teams_from_csv(csv_file):
    teams_conf = []
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            teams_conf.append((row['Team'], row['Conference']))
    return teams_conf

def initialize_regular_season(teams_conf):
    teamlist: List[RegularSeasonData] = []

    for team_info in teams_conf:
        Win = random.randint(0,17)
        Loss = 17 - Win
        record_rand = [Win, Loss]

        team = RegularSeasonData(team_info[0], team_info[1], in_playoffs=False, seed=0, record=record_rand)
        teamlist.append(team)
    return teamlist

def sort_teams_for_playoffs(teamlist):
    for conf in set(team.conference for team in teamlist):
        teams_in_conf = [team for team in teamlist if team.conference == conf]
        teams_in_conf.sort(key=lambda x: x.record[0], reverse=True)
        # print(teams_in_conf)
    
        for i, teams in enumerate(teams_in_conf):
            teams.seed = i + 1
            teams.in_playoffs = i < 8
            # print(teams.in_playoffs)
    return [team for team in teamlist if team.in_playoffs]

def create_league_data(teamlist):
    return LeagueData(teamlist)

def create_playoff_data(league_data):
    playoff_data_instance = PlayoffData(team=[], conference=[], seed=[])

    for team_data in league_data.teams:
        if team_data.in_playoffs:
            playoff_data_instance.team.append(team_data.team)
            playoff_data_instance.conference.append(team_data.conference)
            playoff_data_instance.seed.append(team_data.seed)

    return playoff_data_instance

def generate_playoff_teams(playoff_data_instance):
    nfc_playoffs = [(team, seed) for team, seed, conf in zip(playoff_data_instance.team, playoff_data_instance.seed, playoff_data_instance.conference) if conf == "NFC"]
    afc_playoffs = [(team, seed) for team, seed, conf in zip(playoff_data_instance.team, playoff_data_instance.seed, playoff_data_instance.conference) if conf == "AFC"]

    return nfc_playoffs, afc_playoffs

def generate_initial_data(csv_file):
    teams_conf = read_teams_from_csv(csv_file)
    teamlist = initialize_regular_season(teams_conf)
    sort_teams_for_playoffs(teamlist)
    league_data = create_league_data(teamlist)
    playoff_data = create_playoff_data(league_data)
    nfc_playoffs, afc_playoffs = generate_playoff_teams(playoff_data)

    return teamlist, league_data, playoff_data, nfc_playoffs, afc_playoffs

# Use read_teams_from_csv to read Teams_Conf from CSV
Teams_Conf = read_teams_from_csv('Modular_Example/teams_conf.csv')
