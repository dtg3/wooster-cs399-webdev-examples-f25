import { useState, useCallback, Suspense } from 'react';
import JokeCard from './components/JokeCard';
import JokeButton from './components/JokeButton';
import JokeContent from './components/JokeContent';
import LoadingSpinner from './components/LoadingSpinner';


/* 
  Standard function to make a Promise suspense-ready).
  This is "boiler plate" code that can be used for most
  suspense usecases.
*/

function wrapPromise(promise) {
  let status = 'pending';
  let result;
  let suspender = promise.then(
    (r) => {
      status = 'success';
      result = r;
    },
    (e) => {
      status = 'error';
      result = e;
    }
  );
  return {
    read() {
      if (status === 'pending') {
        throw suspender; // Triggers Suspense
      } else if (status === 'error') {
        throw result; // Triggers on Error (if one existed)
      } else if (status === 'success') {
        return result;
      }
    },
  };
}

// Helper to create the initial state where we show the instructions
function createInitialResource() {
  const initialJoke = 'Click the button below to get a funny dad joke!';
  return {
    read: () => ({ joke: initialJoke })
  };
}

// Function that returns the actual API fetch promise
function fetchJokePromise() {
  return new Promise(async (resolve, reject) => {
      
    // Simulate a network delay
    await new Promise(res => setTimeout(res, 5000)); 
      
    try {
      const response = await fetch('https://icanhazdadjoke.com/', {
        headers: { 'Accept': 'application/json' }
      });

      if (!response.ok) {
        reject({ error: 'Failed to fetch joke: Network response was not ok.' });
        return;
      }
      const data = await response.json();
      resolve(data); 
    } catch (error) {
        reject({ error: "Failed to fetch a joke. Please try again." });
    }
  });
}

function App() {
  // State holds the resource object to track the promise status
  const [jokeResource, setJokeResource] = useState(createInitialResource);

  const getNewJoke = useCallback(() => {
    // Create and set a new suspense-ready resource whenever the button is clicked
    const newResource = wrapPromise(fetchJokePromise());
    setJokeResource(newResource);
  }, []);

  return (
    <div className="container">
      <div className="row justify-content-center">
        <div className="col-lg-8 col-md-10">
          <div className="text-center p-4">
            <h1 className="mb-5 text-dark">Dad Joke Generator 😂</h1>
            
            <JokeCard 
              className="w-75 mx-auto" // Card width and centering
            >
              {/* The Suspense Boundary */}
              <Suspense 
                // Fallback is shown ONLY when JokeContent is waiting for the promise to resolve
                fallback={<LoadingSpinner />}
              >
                {/* JokeContent attempts to read the data, triggering Suspense if pending */}
                <JokeContent resource={jokeResource} />
              </Suspense>
              
            </JokeCard>

            <JokeButton 
              onClick={getNewJoke}
            />
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;