from backend.app.api.v1.tournaments.domain.tournament import Tournament
from backend.app.api.v1.tournaments.domain.tournament_repository import (
    ITournamentRepository,
)


class InMemoryTournamentRepository(ITournamentRepository):
    """
    In-memory implementation of ITournamentRepository.
    Assigns integer IDs starting from 1.
    Stores Tournament entities in a dict.
    """

    def __init__(self):
        self.next_id = 1
        self.data: dict[int, Tournament] = {}

    async def add(self, tournament: Tournament) -> int:
        id = self.next_id
        self.data[id] = tournament
        self.next_id += 1
        return id

    async def delete_by_id(self, id: int) -> None:
        self.data.pop(id, None)

    async def get_all(self) -> list[tuple[int, Tournament]]:
        return list(self.data.items())

    async def get_by_id(self, id: int) -> tuple[int, Tournament] | None:
        try:
            return (id, self.data[id])
        except KeyError:
            return None
