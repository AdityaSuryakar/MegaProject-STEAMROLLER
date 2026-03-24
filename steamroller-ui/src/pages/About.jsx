import FeatureCard from "../components/FeatureCard"

function About() {

  return (
    <div className="card">

      <h1>Speech, without limits.</h1>

      <p>
        SteamRoller rebuilds speech in real time — preserving meaning, identity, and conversational flow.
      </p>

      <FeatureCard
        title="Live Speech Reconstruction"
        text="Continuously repairs disfluencies as you speak — no pauses, no interruptions."
      />

      <FeatureCard
        title="Meaning Preservation"
        text="Understands context to ensure your message stays intact, not distorted."
      />

      <FeatureCard
        title="Instant Response"
        text="Ultra-fast processing enables seamless, natural conversations."
      />

    </div>
  )
}

export default About