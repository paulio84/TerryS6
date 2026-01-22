import { useEffect, useState } from "react"
import type { Tournament } from "./types"
import { getTournaments } from "../../api/tournaments"

function TournamentList() {
  const [tournaments, setTournaments] = useState<Tournament[]>([])

  useEffect(() => {
    getTournaments()
      .then((tournamentData) => setTournaments(tournamentData))
      .catch(console.error)
  }, [])

  const tournamentElements = tournaments.map((tournament) => {
    return (
      <div key={tournament.id}>
        {tournament.name}
        <p>{tournament.start_date}</p>
        <p>{tournament.end_date}</p>
      </div>
    )
  })

  return (
    <>
      <h2>List of Tournaments</h2>
      {tournamentElements}
    </>
  )
}

export default TournamentList