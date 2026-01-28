import { StrictMode } from 'react'
import ReactDOM from 'react-dom/client'
import { createBrowserRouter, RouterProvider } from 'react-router-dom'

import './index.css'

// layout
import Layout from './layouts/Layout'
// pages
import LeagueTable from './pages/LeagueTable'
import TournamentsPage, {
  createTournamentsAction,
  deleteTournamentAction,
  tournamentsLoader,
} from './pages/tournaments/TournamentsPage'
import ErrorPage from './pages/ErrorPage'

const router = createBrowserRouter([
  {
    path: "/",
    element: <Layout />,
    children: [
      {
        index: true,
        element: <LeagueTable />,
        errorElement: <ErrorPage />,
      },
      {
        path: "tournaments",
        element: <TournamentsPage />,
        errorElement: <ErrorPage />,
        loader: tournamentsLoader,
        action: createTournamentsAction,
        children: [
          {
            path: ":id/delete",
            action: deleteTournamentAction,
          }
        ]
      }
    ]
  }
])

function App() {
  return (
    <div className="app">
      <RouterProvider router={router} />
    </div>
  )
}

ReactDOM
  .createRoot(document.getElementById('root')!)
  .render(
    <StrictMode>
      <App />
    </StrictMode>,
  )
