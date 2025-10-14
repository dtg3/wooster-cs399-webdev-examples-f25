import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App.jsx';

// Import local custom CSS (this loads after Bootstrap, allowing overrides)
import './index.css'; 

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
);