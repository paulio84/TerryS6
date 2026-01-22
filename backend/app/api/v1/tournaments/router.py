from fastapi import APIRouter, Depends, status
from kink import di

from .schemas import CreateTournamentRequest, TournamentListResponse, TournamentResponse
from .service import TournamentService

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
    tournament_to_create = request.to_dto()
    tournament_dto = await service.create_tournament(tournament_to_create)
    return TournamentResponse.from_dto(dto=tournament_dto)


@router.get(
    "/tournaments",
    status_code=status.HTTP_200_OK,
    response_model=TournamentListResponse,
)
async def get_tournaments(
    service: TournamentService = Depends(get_tournament_service),
) -> TournamentListResponse:
    tournament_list_dto = await service.get_tournaments()
    return TournamentListResponse.from_dto(dto=tournament_list_dto)


@router.get(
    "/tournaments/{tournament_id}",
    status_code=status.HTTP_200_OK,
    response_model=TournamentResponse,
)
async def get_tournament(
    tournament_id: int,
    service: TournamentService = Depends(get_tournament_service),
) -> TournamentResponse:
    return TournamentResponse.from_dto(
        dto=await service.get_tournament_by_id(tournament_id)
    )


@router.delete(
    "/tournaments/{tournament_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_tournament(
    tournament_id: int, service: TournamentService = Depends(get_tournament_service)
) -> None:
    return await service.delete_tournament_by_id(tournament_id)
