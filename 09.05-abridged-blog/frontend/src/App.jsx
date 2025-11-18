import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Home from './pages/Home';
import PostList from './pages/PostList';
import AddPost from './pages/AddPost';
import './App.css'

function App() {

  return (
    <Router>
      <div className="App">
        <header>
          <nav className="main-nav">
            <Link to="/">Home</Link>
            <Link to="/posts">View All Posts</Link>
            <Link to="/add">Add New Post</Link>
          </nav>
        </header>
        <main className='page-container'>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/posts" element={<PostList />} />
            <Route path="/add" element={<AddPost />} />
            <Route path="*" element={<h1>404: Page Not Found</h1>} />
          </Routes>
        </main>
      </div>
    </Router>
  )
}

export default App
