from abc import ABC, abstractmethod

from .tournament import Tournament


class ITournamentRepository(ABC):
    @abstractmethod
    async def add(self, tournament: Tournament) -> int:
        pass

    @abstractmethod
    async def delete_by_id(self, id: int) -> None:
        pass

    @abstractmethod
    async def get_by_id(self, id: int) -> tuple[int, Tournament] | None:
        pass

    @abstractmethod
    async def get_all(self) -> list[tuple[int, Tournament]]:
        pass
