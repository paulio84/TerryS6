export interface Tournament {
  id: number
  name: string
  start_date: string
  end_date: string
}

export type GetTournamentsResponse = {
  tournaments: Tournament[]
}
