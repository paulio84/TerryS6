from abc import ABC, abstractmethod

from backend.app.api.v1.tournaments.domain.tournament import Tournament


class ITournamentRepository(ABC):
    @abstractmethod
    def add(self) -> Tournament:
        pass

    @abstractmethod
    def delete(self) -> None:
        pass

    @abstractmethod
    def get_by_id(self) -> Tournament | None:
        pass

    def get_all(self) -> list[Tournament]:
        pass
