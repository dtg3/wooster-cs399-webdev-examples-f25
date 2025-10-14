import React, { useState, useCallback } from 'react';
import JokeCard from './components/JokeCard';
import JokeButton from './components/JokeButton';

function App() {
  const [joke, setJoke] = useState('Click the button below to get a funny dad joke!'); 
  const [isLoading, setIsLoading] = useState(false);

  const getNewJoke = useCallback(async () => {
    
    setIsLoading(true);

    try {
      const response = await fetch('https://icanhazdadjoke.com/', {
        headers: {
          'Accept': 'application/json' //
        }
      });

      if (!response.ok) {
        throw new Error('Network response was not ok'); 
      }

      const data = await response.json();
      // The API doesn't take long, so this will simulate a longer delay
      //  to demonstrate the effect.
      await new Promise(resolve => setTimeout(resolve, 5000));
      
      setJoke(data.joke);

    } catch (error) {
      setJoke("Failed to fetch a joke. Please try again."); //
      console.error('Error fetching joke:', error); //
      
    } finally {
      setIsLoading(false); 
    }
  }, []); 

  return (
    <div className="container">
      <div className="row justify-content-center">
        <div className="col-lg-8 col-md-10">
          <div className="text-center p-4">
            <h1 className="mb-5 text-dark">Dad Joke Generator 😂</h1> {/* */}
            
            <JokeCard 
              jokeText={joke}
              isLoading={isLoading} 
            />

            <JokeButton 
              onClick={getNewJoke}
              isLoading={isLoading}
            />
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;