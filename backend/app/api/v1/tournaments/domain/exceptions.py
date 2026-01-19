class DomainException(Exception):
    pass


class InvalidTournamentDates(DomainException):
    pass


class TournamentNameRequired(DomainException):
    pass
