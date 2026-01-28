import { StrictMode } from 'react'
import ReactDOM from 'react-dom/client'
import { createBrowserRouter, RouterProvider } from 'react-router-dom'

import './index.css'

// layout
import Layout from './layouts/Layout'
// pages
import LeagueTable from './pages/LeagueTable'
import TournamentsPage, { createTournamentsAction, tournamentsLoader } from './pages/tournaments/TournamentsPage'

const router = createBrowserRouter([
  {
    path: "/",
    element: <Layout />,
    children: [
      {
        index: true,
        element: <LeagueTable />
      },
      {
        path: "tournaments",
        element: <TournamentsPage />,
        loader: tournamentsLoader,
        action: createTournamentsAction
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
