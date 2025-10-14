// Accepts children (which will be the Suspense block) and a className
function JokeCard({ children, className }) {
  return (
    <div className={`card shadow-lg joke-card mb-4 ${className || ''}`}>
      <div className="card-body d-flex align-items-center justify-content-center">
        {children}
      </div>
    </div>
  );
}

export default JokeCard;