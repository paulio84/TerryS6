import { Link, NavLink } from "react-router-dom";

export default function Header() {
  return (
    <header>
      <Link to="/">TerryS6</Link>
      <nav>
        <NavLink to="/tournaments">Tournaments</NavLink>
        <NavLink to="/">Sign Out</NavLink>{/* TODO: UPDATE THIS LINKS */}
      </nav>
    </header>
  )
}