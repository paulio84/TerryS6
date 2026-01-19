from kink import inject

from backend.app.api.v1.tournaments.application.exceptions import TournamentNotFound
from backend.app.api.v1.tournaments.domain.tournament import Tournament
from backend.app.api.v1.tournaments.domain.tournament_repository import (
    ITournamentRepository,
)

from .dto import CreateTournamentRequest, TournamentResponse


@inject
class TournamentService:
    """
    A tournament service to create, list, get and delete tournaments.
    Depends on a ITournamentRepository to interact with data.
    """

    def __init__(self, repository: ITournamentRepository):
        self._repository = repository

    async def create_tournament(
        self, request: CreateTournamentRequest
    ) -> TournamentResponse:
        tournament: Tournament = Tournament(**request.model_dump())
        tournament_id = await self._repository.add(tournament)
        return TournamentResponse(
            id=tournament_id,
            name=tournament.name,
            start_date=tournament.start_date,
            end_date=tournament.end_date,
        )

    async def get_tournaments(self) -> list[TournamentResponse]:
        return [
            TournamentResponse(
                id=tournament_id,
                name=tournament.name,
                start_date=tournament.start_date,
                end_date=tournament.end_date,
            )
            for tournament_id, tournament in await self._repository.get_all()
        ]

    async def get_tournament_by_id(self, id: int) -> TournamentResponse:
        tournament_in_db: (
            tuple[int, Tournament] | None
        ) = await self._repository.get_by_id(id)

        if tournament_in_db is None:
            raise TournamentNotFound(f"Tournament with id of '{id}' was not found.")

        tournament_id, tournament = tournament_in_db
        return TournamentResponse(
            id=tournament_id,
            name=tournament.name,
            start_date=tournament.start_date,
            end_date=tournament.end_date,
        )

    async def delete_tournament_by_id(self, id: int) -> None:
        await self._repository.delete_by_id(id)
