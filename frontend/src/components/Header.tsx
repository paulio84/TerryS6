import { Link, NavLink } from "react-router-dom";

export default function Header() {
  return (
    <header>
      <Link className="site-logo" to="/">TerryS6</Link>
      <nav>
        <NavLink to="/">My Predictions</NavLink>  {/* TODO: UPDATE THESE LINKS */}
        <NavLink to="/">Sign Out</NavLink>
      </nav>
    </header>
  )
}