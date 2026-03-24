import UploadBox from "../components/UploadBox"
import './Home.css'

function Home() {

  return (
    <div className="card">

      <h1>Fluent speech. Zero friction.</h1>

      <p>
        Transform disfluent audio into natural speech instantly — while keeping your voice uniquely yours.
      </p>

      <UploadBox />

      <div className="or">OR</div>

      <button className="recordBtn">
        🎤 Record Audio
      </button>

    </div>
  )
}

export default Home