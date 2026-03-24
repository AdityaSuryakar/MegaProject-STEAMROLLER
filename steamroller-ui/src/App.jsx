import { useState } from "react"
import Navbar from "./components/Navbar"
import Home from "./pages/Home"
import About from "./pages/About"
import "./app.css"

function App() {

  const [page, setPage] = useState("home")

  return (
    <div className="app">

      <Navbar page={page} setPage={setPage} />

      {page === "home" ? <Home /> : <About />}

    </div>
  )
}

export default App