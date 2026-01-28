from datetime import date

from pydantic import BaseModel

from .dto import CreateTournamentDTO, TournamentDTO, TournamentListDTO


class CreateTournamentRequest(BaseModel):
    name: str
    end_date: date

    def to_dto(self) -> CreateTournamentDTO:
        return CreateTournamentDTO(
            name=self.name,
            end_date=self.end_date,
        )

    class Config:
        frozen = True
        extra = "forbid"


class TournamentResponse(BaseModel):
    id: int
    name: str
    slug: str
    end_date: date

    @classmethod
    def from_dto(cls, dto: TournamentDTO) -> "TournamentResponse":
        return TournamentResponse(
            id=dto.id,
            name=dto.name,
            slug=dto.slug,
            end_date=dto.end_date,
        )

    class Config:
        frozen = True


class TournamentListResponse(BaseModel):
    tournaments: list[TournamentResponse]

    @classmethod
    def from_dto(cls, dto: TournamentListDTO) -> "TournamentListResponse":
        tournaments = [
            TournamentResponse.from_dto(tournament_dto)
            for tournament_dto in dto.tournaments
        ]
        return TournamentListResponse(tournaments=tournaments)
