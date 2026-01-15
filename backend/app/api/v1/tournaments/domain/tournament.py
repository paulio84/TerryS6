from dataclasses import dataclass, field
from datetime import date

from .exceptions import InvalidTournamentDates, TournamentNameRequired


@dataclass
class Tournament:
    name: str
    start_date: date
    end_date: date
    is_active: bool = field(default=False)

    def __post_init__(self):
        if self.name is None or self.name.strip() == "":
            raise TournamentNameRequired("Tournament name is required.")
        if self.start_date >= self.end_date:
            raise InvalidTournamentDates("Start date must be before the end date.")
