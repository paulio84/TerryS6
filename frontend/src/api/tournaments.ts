import type { Tournament, GetTournamentsResponse } from "../features/tournaments/types"

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL

export async function getTournaments(): Promise<Tournament[]> {
  const url = `${API_BASE_URL}/tournaments`
  const response = await fetch(url)
  if (!response.ok) {
    throw new Error("Failed to fetch tournaments")
  }
  const json: GetTournamentsResponse = await response.json()
  return json.tournaments
}