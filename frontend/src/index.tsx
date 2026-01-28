import { StrictMode } from 'react'
import ReactDOM from 'react-dom/client'
import { createBrowserRouter, RouterProvider } from 'react-router-dom'

import './index.css'

// layout
import Layout from './layouts/Layout'
// pages
import LeagueTable from './pages/LeagueTable'
import Tournaments from './pages/Tournaments'

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
        element: <Tournaments />
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
