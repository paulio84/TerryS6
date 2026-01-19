class DomainException(Exception):
    _status_code: int = 0

    def get_status_code(self) -> int:
        return self._status_code


class InvalidTournamentDates(DomainException):
    _status_code = 400


class TournamentNameRequired(DomainException):
    _status_code = 400


class TournamentNotFound(DomainException):
    _status_code = 404


class TournamentAlreadyExists(DomainException):
    _status_code = 400
