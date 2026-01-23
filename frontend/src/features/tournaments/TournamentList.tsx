import { useEffect, useState } from "react"
import type { Tournament } from "./types"
import { getTournaments } from "../../api/tournaments"

function TournamentList() {
  const [tournaments, setTournaments] = useState<Tournament[]>([])
  const [loading, setLoading] = useState<boolean>(true)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    getTournaments()
      .then((tournamentData) => setTournaments(tournamentData))
      .catch((error) => setError(error.message || "An error occurred"))
      .finally(() => setLoading(false))
  }, [])

  const tournamentElements = tournaments.map((tournament) => {
    return (
      <div key={tournament.id}>
        {tournament.name}
        <p>{new Date(tournament.start_date).toLocaleDateString()}</p>
        <p>{new Date(tournament.end_date).toLocaleDateString()}</p>
      </div>
    )
  })

  return (
    <>
      {loading && <p>Loading...</p>}
      {!loading && tournamentElements}
      {error && <p>Error fetching tournaments: {error}</p>}
    </>
  )
}

export default TournamentList
