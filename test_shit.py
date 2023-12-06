from dataclasses import dataclass, field
from typing import Tuple, List

@dataclass (frozen=False)
class TeamData:
    team: str 
    conference: str
    in_playoffs: bool
    seed: int
    record: list = field(default_factory=lambda: [0,0])

@dataclass (frozen=True)
class LeagueData:
    teams: List[TeamData]

arizona = TeamData("Arizona", "NFC", in_playoffs= False, record=[4,0], seed=9)
NFL = LeagueData([arizona])

Teams_Conf = [('Arizona Cardinals', 'NFC'),('Atlanta Falcons', 'NFC'),('Baltimore Ravens', 'AFC'),('Buffalo Bills', 'AFC'),('Carolina Panthers', 'NFC'),
              ('Chicago Bears', 'NFC'),('Cincinnati Bengals', 'AFC'),('Cleveland Browns', 'AFC'),('Dallas Cowboys', 'NFC'),('Denver Broncos', 'AFC'),
              ('Detroit Lions', 'NFC'),('Green Bay Packers', 'NFC'),('Houston Texans', 'AFC'),('Indianapolis Colts', 'AFC'),('Jacksonville Jaguars', 'AFC'),
              ('Kansas City Chiefs', 'AFC'),('Los Angeles Rams', 'NFC'),('Los Angeles Chargers', 'AFC'),('Los Angeles Rams', 'NFC'),('Las Vegas Raiders', 'AFC'),
              ('Miami Dolphins', 'AFC'),('Minnesota Vikings', 'NFC'),('New England Patriots', 'AFC'),('New Orleans Saints', 'NFC'),('New York Giants', 'NFC'),
              ('New York Jets', 'AFC'),('Oakland Raiders', 'AFC'),('Philadelphia Eagles', 'NFC'),('Pittsburgh Steelers', 'AFC'),('San Diego Chargers', 'AFC'),
              ('Seattle Seahawks', 'NFC'),('San Francisco 49ers', 'NFC'),('St. Louis Rams', 'NFC'),('Tampa Bay Buccaneers', 'NFC'),('Tennessee Titans', 'AFC'),
              ('Washington Commanders', 'NFC')
              ]

print(f"The team Arizona is: {arizona}")
print(f"The league is: {NFL}")
