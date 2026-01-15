class InvalidTournamentDates(Exception):
    def __init__(self, message):
        return super().__init__(message)


class TournamentNameRequired(Exception):
    def __init__(self, message):
        return super().__init__(message)
