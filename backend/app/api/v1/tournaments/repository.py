from abc import ABC, abstractmethod

from .dto import CreateTournamentDTO, TournamentDTO, TournamentListDTO


class ITournamentRepository(ABC):
    @abstractmethod
    async def add(self, tournament: CreateTournamentDTO) -> TournamentDTO: ...

    @abstractmethod
    async def get_by_id_or_none(self, id: int) -> TournamentDTO | None: ...

    @abstractmethod
    async def get_by_name_or_none(self, name: str) -> TournamentDTO | None: ...

    @abstractmethod
    async def get_all(self) -> TournamentListDTO: ...

    @abstractmethod
    async def delete_by_id(self, id: int) -> None: ...


class InMemoryTournamentRepository(ITournamentRepository):
    """
    In-memory implementation of ITournamentRepository.
    Assigns integer IDs starting from 1.
    Stores Tournament entities in a dict.
    """

    def __init__(self):
        self.next_id = 1
        self.data: dict[int, TournamentDTO] = {}

    async def add(self, tournament: CreateTournamentDTO) -> TournamentDTO:
        id = self.next_id
        tournament_to_store = TournamentDTO(
            id=id,
            name=tournament.name,
            slug=tournament.slug,
            end_date=tournament.end_date,
        )
        self.data[id] = tournament_to_store
        self.next_id += 1
        return tournament_to_store

    async def delete_by_id(self, id: int) -> None:
        self.data.pop(id, None)

    async def get_all(self) -> TournamentListDTO:
        list_of_tournaments = [tournament for tournament in self.data.values()]
        return TournamentListDTO(tournaments=list_of_tournaments)

    async def get_by_id_or_none(self, id: int) -> TournamentDTO | None:
        try:
            return self.data[id]
        except KeyError:
            return None

    async def get_by_name_or_none(self, name: str) -> TournamentDTO | None:
        for tournament in self.data.values():
            if tournament.name == name:
                return tournament
        return None
