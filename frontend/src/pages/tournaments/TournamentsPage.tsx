import { Await, Form, redirect, useLoaderData, type ActionFunctionArgs } from "react-router-dom"
import { createTournament, deleteTournament, getTournaments } from "../../api/tournaments"
import type { CreateTournamentDTO, Tournament } from "./types"
import React from "react"

export async function tournamentsLoader(): Promise<Tournament[]> {
  return await getTournaments()
}

export async function createTournamentsAction({ request }: ActionFunctionArgs): Promise<Response> {
  const formData = await request.formData()
  const payload: CreateTournamentDTO = {
    name: formData.get("name") as string,
    end_date: formData.get("end_date") as string,
  }

  await createTournament(payload)

  return redirect("/tournaments")
}

export async function deleteTournamentAction({ params }: ActionFunctionArgs): Promise<Response> {
  const id = Number(params.id)
  if (Number.isNaN(id)) {
    throw new Error("Invalid tournament id")
  }

  await deleteTournament(Number(id))

  return redirect("/tournaments")
}

const TournamentsPage = () => {
  const tournaments = useLoaderData() as Promise<Tournament[]>

  function renderTournamentElements(tournaments: Tournament[]) {
    if (tournaments.length == 0) {
      return (
        <p>No tournaments at the moment. Create the next tournament above.</p>
      )
    }

    const tournamentElements = tournaments.map((tournament) => {
      return (
        <tr key={tournament.id}>
          <td>{tournament.name}</td>
          <td>{tournament.end_date}</td>
          <td>
            <Form
              method="post"
              action={`${tournament.id}/delete`}
              onSubmit={(e) => {
                if (!confirm("Are you sure you want to delete this tournament?")) {
                  e.preventDefault()
                }
              }}
            >
              <button type="submit">Delete</button>
            </Form>
          </td>
        </tr>
      )
    })

    return (
      <table className="table-auto">
        <thead>
          <tr>
            <th>Name</th>
            <th>End Date</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          {tournamentElements}
        </tbody>
      </table>
    )
  }

  return (
    <>
      <h2>Create a tournament</h2>
      <Form method="post">
        <div className="form-field">
          <label htmlFor="tournamentName">Tournament Name</label>
          <input type="text" name="name" required placeholder="Enter a tournament name" />
        </div>
        <div className="form-field">
          <label htmlFor="tournamentEndDate">End Date</label>
          <input type="date" name="end_date" required />
        </div>
        <button type="submit">Save</button>
      </Form>
      <h2>Tournaments</h2>
      <div className="tournament-table">
        <React.Suspense fallback={<h2>Loading tournaments...</h2>}>
          <Await resolve={tournaments}>
            {renderTournamentElements}
          </Await>
        </React.Suspense>
      </div>
    </>
  )
}

export default TournamentsPage