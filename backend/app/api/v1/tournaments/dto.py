from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class TournamentDTO:
    id: int
    name: str
    slug: str
    end_date: date


@dataclass
class CreateTournamentDTO:
    name: str
    end_date: date
    slug: str | None = None

    def create_slug_from_name(self) -> None:
        name_pieces = self.name.split()
        self.slug = "-".join(name_piece.lower() for name_piece in name_pieces)


@dataclass(frozen=True)
class TournamentListDTO:
    tournaments: list[TournamentDTO]
