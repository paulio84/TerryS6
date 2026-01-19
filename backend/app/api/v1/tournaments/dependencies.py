from kink import di

from .repository import InMemoryTournamentRepository, ITournamentRepository
from .service import TournamentService


def bootstrap_dependencies():
    repository = InMemoryTournamentRepository()
    di[ITournamentRepository] = repository
    di[TournamentService] = TournamentService(repository)
