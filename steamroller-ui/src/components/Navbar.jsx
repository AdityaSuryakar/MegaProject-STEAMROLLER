import "./Navbar.css"

function Navbar({ page, setPage }) {

  return (
    <div className="navbar">

      <h1 className="logo">SteamRoller</h1>

      <div className="tabs">
        <button
          className={page === "home" ? "active" : ""}
          onClick={() => setPage("home")}
        >
          Home
        </button>

        <button
          className={page === "about" ? "active" : ""}
          onClick={() => setPage("about")}
        >
          About
        </button>
      </div>

    </div>
  )
}

export default Navbar