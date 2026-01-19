from fastapi import APIRouter, Depends, HTTPException, status
from kink import di

from backend.app.api.v1.tournaments.application.dto import (
    CreateTournamentRequest,
    TournamentResponse,
)
from backend.app.api.v1.tournaments.application.tournament_service import (
    TournamentService,
)
from backend.app.api.v1.tournaments.domain.exceptions import (
    InvalidTournamentDates,
    TournamentNameRequired,
)

router = APIRouter()


def get_tournament_service() -> TournamentService:
    return di[TournamentService]


@router.post(
    "/tournaments",
    status_code=status.HTTP_201_CREATED,
    response_model=TournamentResponse,
)
async def create_tournament(
    request: CreateTournamentRequest,
    service: TournamentService = Depends(get_tournament_service),
) -> TournamentResponse:
    try:
        return await service.create_tournament(request)
    except TournamentNameRequired as ex:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(ex))
    except InvalidTournamentDates as ex:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(ex))


@router.get(
    "/tournaments",
    status_code=status.HTTP_200_OK,
    response_model=list[TournamentResponse],
)
async def get_tournaments(
    service: TournamentService = Depends(get_tournament_service),
) -> list[TournamentService]:
    return await service.get_tournaments()
