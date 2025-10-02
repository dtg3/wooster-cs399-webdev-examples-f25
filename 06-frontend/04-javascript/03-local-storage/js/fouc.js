const savedTheme = localStorage.getItem('userThemePreference');
/* 
    Apply the saved theme class directly to the HTML tag as soon as possible.
    We can do this becaues the HTML tag was "seen" by the browser's HTML parser
    already. See it up there? ----^
    
    This gives us the background color for the entire viewport (browser window).
*/
document.documentElement.className = savedTheme ? `theme-${savedTheme}` : 'theme-default';