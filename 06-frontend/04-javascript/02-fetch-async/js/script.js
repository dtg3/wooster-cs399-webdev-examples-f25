/*
    Get the important elements from the DOM so we can
    update them or attach listeners to them.
*/
const getJokeBtn = document.getElementById('get-joke-btn');
const jokeText = document.getElementById('joke-text');

/*
    Attach the function to the click event on the button
*/
getJokeBtn.addEventListener('click', getNewJoke);

/*
    Okay... this is an asynchronous function call.

    We are using async beacuse I don't want my entire
    application blocked (unusable) while waiting for 
    some long running operation to finish.

    In this case, we are going to use this to load our 
    jokes from the online API. Since I can't know how
    long it will take my program to get the complete
    data (e.g. the operation to finish) the async lets
    my ability to interact with the program while the 
    await portion of this code causes the async funciton
    to pause until an action is complete. In JavaScript,
    they refer to this as a promise. I'm basically using
    this function to wait for the data I am promised.
*/
async function getNewJoke() {
    jokeText.textContent = "Loading joke...";

    // Disable button to prevent multiple clicks
    getJokeBtn.disabled = true; 
    
    // The API doesn't take long, so I will simulate a longer delay
    //  to demonstrate the effect. You normally won't do this..
    await new Promise(resolve => setTimeout(resolve, 5000));

    /* 
        The try catch block is used to capture exceptions if
        somethign goes wrong during the API call (e.g. if the
        API we requested is unavailable or we make an incorrect
        request).
    */
    try {
        /* 
            I can't use the data from the API, until I receive the complete
            response from my request. So I patiently wait for the data, and
            then my function can resume execution.
        */
        const response = await fetch('https://icanhazdadjoke.com/', {
            headers: {
                'Accept': 'application/json' // Requesting JSON format
            }
        });
        
        /*
            Since we are in a try block, if the respose was bad,
            I can throw an error and handle it in the catch.
        */
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        // Parse the JSON data with the joke
        const data = await response.json();
        
        // Update the UI with the joke text
        jokeText.textContent = data.joke;

    // When things go wrong...
    } catch (error) {
        // Report the error
        jokeText.textContent = "Failed to fetch a joke. Please try again.";
        console.error('Error fetching joke:', error);
    // Finally always happens whether an exception and catch occurred or not.
    } finally {
        // Re-enable the button regardless of success or failure
        getJokeBtn.disabled = false;
    }
}