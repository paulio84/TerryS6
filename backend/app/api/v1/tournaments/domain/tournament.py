from dataclasses import dataclass, field
from datetime import datetime

from backend.app.api.v1.tournaments.exceptions import (
    InvalidTournamentDates,
    TournamentNameRequired,
)


@dataclass
class Tournament:
    Id: int
    name: str
    start_date: datetime
    end_date: datetime
    is_active: bool = field(default=False)

    def __post_init__(self):
        if self.name.strip() == "" or self.name is None:
            raise TournamentNameRequired("Tournament name is required.")
        if self.start_date >= self.end_date:
            raise InvalidTournamentDates("Start date must be before the end date.")
