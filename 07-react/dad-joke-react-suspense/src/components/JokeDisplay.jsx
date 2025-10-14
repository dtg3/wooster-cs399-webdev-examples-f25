function JokeDisplay({ jokeText }) {
  return (
    <p id="joke-text" className="card-text fs-5 text-muted text-center">
      {jokeText}
    </p>
  );
}

export default JokeDisplay;