function JokeButton({ onClick, isLoading }) {
  return (
    <button 
      id="get-joke-btn" 
      className="btn btn-warning btn-lg shadow-sm"
      onClick={onClick}
      disabled={isLoading} 
    >
      {isLoading ? 'Fetching...' : 'Get a New Joke'} 
    </button>
  );
}

export default JokeButton;