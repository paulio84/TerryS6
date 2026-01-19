from datetime import date

from pydantic import BaseModel, model_validator

from .dto import CreateTournamentDTO, TournamentDTO, TournamentListDTO
from .exceptions import InvalidTournamentDates


class CreateTournamentRequest(BaseModel):
    name: str
    start_date: date
    end_date: date

    @model_validator(mode="after")
    def start_date_before_end_date(self) -> "CreateTournamentRequest":
        if self.start_date >= self.end_date:
            raise InvalidTournamentDates("Start date must be before the end date.")
        return self

    def to_dto(self) -> CreateTournamentDTO:
        return CreateTournamentDTO(
            name=self.name,
            start_date=self.start_date,
            end_date=self.end_date,
        )

    class Config:
        frozen = True
        extra = "forbid"


class TournamentResponse(BaseModel):
    id: int
    name: str
    start_date: date
    end_date: date
    is_active: bool

    @classmethod
    def from_dto(cls, dto: TournamentDTO) -> "TournamentResponse":
        return TournamentResponse(
            id=dto.id,
            name=dto.name,
            start_date=dto.start_date,
            end_date=dto.end_date,
            is_active=dto.is_active,
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
