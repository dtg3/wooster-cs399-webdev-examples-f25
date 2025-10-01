
// Target the <html> tag
const htmlElement = document.documentElement; 

const container = document.querySelector('.container');
const themeButtons = document.querySelectorAll('.theme-btn');
const resetBtn = document.getElementById('reset-storage-btn');

// This is the local storage key
const STORAGE_KEY = 'userThemePreference'; 

function applyTheme(themeName) {

    // Clear any of the theme classes on the HTML element
    htmlElement.classList.remove('theme-default', 'theme-green', 'theme-purple');
    
    // Add the selected theme
    htmlElement.classList.add(`theme-${themeName}`);
    
    /* 
        Save our choice to local storage.
        This is basically just a key/value store.
    */
    
    localStorage.setItem(STORAGE_KEY, themeName);
    
    console.log(`Theme set to: ${themeName} and saved to Local Storage.`);
}

/*
    For each of our theme buttons we attach the same
    listener function to occur on click which passes
    the value of the data-theme attribute to the
    applyTheme function.
*/
themeButtons.forEach(button => {
    button.addEventListener('click', () => {
        const theme = button.getAttribute('data-theme');
        applyTheme(theme);
    });
});


resetBtn.addEventListener('click', () => {
    // Remove our theme setting
    localStorage.removeItem(STORAGE_KEY)
    /* 
        We could also clear all of our local storage data
        for out site (the entire doamin). Might not be a
        good idea if we had more settings/data. :)
    */
    //localStorage.clear(); 
    alert("Local Storage has been completely cleared! The page will now reload.");
    window.location.reload();
});

/* 
    FOUC Mitigation
    Now that everything should be loaded (since this is loaded at the end) we
    can use the is-ready class to reveal our hidden content.
*/
container.classList.add('is-ready');