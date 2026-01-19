from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class TournamentDTO:
    id: int
    name: str
    start_date: date
    end_date: date
    is_active: bool


@dataclass(frozen=True)
class CreateTournamentDTO:
    name: str
    start_date: date
    end_date: date


@dataclass(frozen=True)
class TournamentListDTO:
    tournaments: list[TournamentDTO]
