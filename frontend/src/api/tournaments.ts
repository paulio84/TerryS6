import type { Tournament, GetTournamentsResponse, CreateTournamentDTO } from "../pages/tournaments/types"

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL

export async function getTournaments(): Promise<Tournament[]> {
  const url = `${API_BASE_URL}/tournaments`
  const response = await fetch(url)
  if (!response.ok) {
    throw new Error("Failed to fetch tournaments.")
  }
  const json: GetTournamentsResponse = await response.json()
  return json.tournaments
}

export async function createTournament(payload: CreateTournamentDTO): Promise<void> {
  const url = `${API_BASE_URL}/tournaments`
  const response = await fetch(url, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload)
  })

  if (!response.ok) {
    throw new Error("There was an error creating the tournament.")
  }
}

export async function deleteTournament(id: Number): Promise<void> {
  const url = `${API_BASE_URL}/tournaments/${id}`
  const response = await fetch(url, { method: "DELETE" })

  if (!response.ok) {
    const data = await response.json()
    console.log("--", data)
    throw new Error("Failed to delete tournament.")
  }
}
