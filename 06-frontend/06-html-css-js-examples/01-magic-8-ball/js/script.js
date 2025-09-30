const answers = [
    "Yes, for sure.",
    "No, absolutely not.",
    "The stars say yes.",
    "It is certain.",
    "Without a doubt.",
    "Don't count on it.",
    "As I see it, yes.",
    "Most likely.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful.",
    "Signs point to yes.",
    "Reply hazy, try again.",
    "Cannot predict now.",
    "Concentrate and ask again.",
];

const eightBall = document.getElementById('eight-ball');
const answerDisplay = document.getElementById('answer');
const askBtn = document.getElementById('ask-btn');

eightBall.addEventListener('click', function() {
    // This conditional check to prevent multiple clicks
    //  so you can't just jam (click) on the 8-ball constantly.
    if (eightBall.classList.contains('shaking')) {
        return;
    }

    // Add a CSS class to create a "shaking" effect
    eightBall.classList.add('shaking');
    answerDisplay.textContent = "..."
    answerDisplay.style.fontSize = "2.5em"; // Reset font size
    
    // Add a delay before the result is displayed
    setTimeout(() => {
        // Get a random 8-ball message from answers
        const randomIndex = Math.floor(Math.random() * answers.length);
        const randomAnswer = answers[randomIndex];

        // Update the DOM text content of the answer element
        answerDisplay.textContent = randomAnswer;
        
        // Change font size for longer answers
        if (randomAnswer.length > 20) {
            answerDisplay.style.fontSize = "1.5em";
        } else {
            answerDisplay.style.fontSize = "2.5em";
        }
        
        // Stop the "shaking"
        eightBall.classList.remove('shaking');
    }, 1500); // 1.5-second delay
});

// Add event listener to the "Ask Again" button
askBtn.addEventListener('click', function() {
    // Reset the display to the number 8
    answerDisplay.textContent = "8";
    answerDisplay.style.fontSize = "2.5em";
    eightBall.classList.remove('shaking');
});