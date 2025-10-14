function JokeContent({ resource }) {
  /* 
    resource.read() is the core Suspense magic which can have one of three states
      1. If pending, it throws the promise (Suspense catches it, shows fallback).
      2. If success, it returns the data.
      3. If error, it throws the error.
  */
  const data = resource.read(); 

  // Render the joke text or the error message.
  return (
    <p 
      id="joke-text" 
      className="card-text fs-5 text-muted text-center" 
    >
      {data.joke || data.error}
    </p>
  );
}

export default JokeContent;