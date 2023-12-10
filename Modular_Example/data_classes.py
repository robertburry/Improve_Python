# data_classes.py
from dataclasses import dataclass, field
from typing import List

@dataclass(frozen=False)
class PlayoffData:
    team: List[str]
    conference: List[str]
    seed: List[int]
    playoff_record: list = field(default_factory=lambda: [0, 0])

@dataclass(frozen=False)
class RegularSeasonData:
    team: str
    conference: str
    in_playoffs: bool
    seed: int
    record: list = field(default_factory=lambda: [0, 0])

@dataclass(frozen=False)
class LeagueData:
    teams: List[RegularSeasonData]
