from kink import inject

from .dto import CreateTournamentDTO, TournamentDTO, TournamentListDTO
from .exceptions import TournamentAlreadyExists, TournamentNotFound
from .repository import ITournamentRepository


@inject
class TournamentService:
    """
    A tournament service to create, list, get and delete tournaments.
    Depends on a ITournamentRepository to interact with data.
    """

    def __init__(self, repository: ITournamentRepository):
        self._repository = repository

    async def create_tournament(
        self, tournament_to_create: CreateTournamentDTO
    ) -> TournamentDTO:
        existing_tournament = await self._repository.get_by_name_or_none(
            tournament_to_create.name
        )
        if existing_tournament is not None:
            raise TournamentAlreadyExists(
                f"A tournament with the name: '{tournament_to_create.name}', already exists."
            )

        tournament_to_create.create_slug_from_name()

        return await self._repository.add(tournament_to_create)

    async def get_tournaments(self) -> TournamentListDTO:
        return await self._repository.get_all()

    async def get_tournament_by_id(self, id: int) -> TournamentDTO:
        tournament_in_db = await self._repository.get_by_id_or_none(id)
        if tournament_in_db is None:
            raise TournamentNotFound(f"Tournament with id of '{id}' was not found.")

        return tournament_in_db

    async def delete_tournament_by_id(self, id: int) -> None:
        await self._repository.delete_by_id(id)
