import { isRouteErrorResponse, Link, useNavigate, useRouteError } from "react-router-dom"

const ErrorPage = () => {
  const error = useRouteError()
  const navigate = useNavigate()

  if (isRouteErrorResponse(error)) {
    return (
      <div>
        <h1>Uh oh! We've got a problem!</h1>
        {error.data?.detail && <p>{error.data.detail}</p>}
        <div>
          <button onClick={() => navigate(-1)}>Go back</button>
          <Link to="/">Go home</Link>
        </div>
      </div>
    )
  }

  if (error instanceof Error) {
    return (
      <div>
        <h1>Uh oh! We've got a problem!</h1>
        <p>{error.message}</p>
        <div>
          <button onClick={() => navigate(-1)}>Go back</button>
          <Link to="/">Go home</Link>
        </div>
      </div>
    )
  }

  return (
    <div>
      <h1>Uh oh! We've got a problem!</h1>
      <p>Something went wrong, we're not sure what.</p>
      <div>
        <button onClick={() => navigate(-1)}>Go back</button>
        <Link to="/">Go home</Link>
      </div>
    </div>
  )
}

export default ErrorPage
