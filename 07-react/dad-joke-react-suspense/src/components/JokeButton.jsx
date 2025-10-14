function JokeButton({ onClick }) {
  return (
    <button 
      id="get-joke-btn" 
      className="btn btn-warning btn-lg shadow-sm"
      onClick={onClick}
    >
      Get a New Joke
    </button>
  );
}

export default JokeButton;