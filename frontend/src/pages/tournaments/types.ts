export interface CreateTournamentDTO {
  name: string
  end_date: string
}

export interface Tournament {
  id: number
  name: string
  slug: string
  end_date: string
}

export type GetTournamentsResponse = {
  tournaments: Tournament[]
}
