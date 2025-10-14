import JokeDisplay from './JokeDisplay';
import LoadingSpinner from './LoadingSpinner';

function JokeCard({ jokeText, isLoading }) {
  return (
    <div className="card shadow-lg joke-card mb-4">
      <div className="card-body d-flex align-items-center justify-content-center">
        
        {/* Conditional Rendering: Show spinner OR joke text */}
        {isLoading ? (
          <LoadingSpinner /> 
        ) : (
          <JokeDisplay jokeText={jokeText} />
        )}
        
      </div>
    </div>
  );
}

export default JokeCard;