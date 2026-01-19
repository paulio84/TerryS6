from kink import di

from backend.app.api.v1.tournaments.application.tournament_service import (
    TournamentService,
)
from backend.app.api.v1.tournaments.domain.tournament_repository import (
    ITournamentRepository,
)
from backend.app.api.v1.tournaments.infrastructure.in_memory_tournament_repository import (
    InMemoryTournamentRepository,
)

repository = InMemoryTournamentRepository()
di[ITournamentRepository] = repository
di[TournamentService] = TournamentService(repository)
