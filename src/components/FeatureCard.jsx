import "./FeatureCard.css"

function FeatureCard({ title, text }) {

  return (
    <div className="featureCard">
      <div className="featureIcon">⚡</div>
      <div>
        <h3>{title}</h3>
        <p>{text}</p>
      </div>
    </div>
  )
}

export default FeatureCard