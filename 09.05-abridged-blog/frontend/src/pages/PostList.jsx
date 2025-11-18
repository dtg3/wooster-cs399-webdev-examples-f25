import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { PostService } from '../api';

function PostList() {
    const [posts, setPosts] = useState([]);
    const [loading, setLoading] = useState(true);

    const navigate = useNavigate();

    const fetchPosts = async () => {
        setLoading(true);
        try {
            const data = await PostService.getAllPosts();
            setPosts(data);
        }
        catch (error) {
            console.error("Error fecthing posts: ", error);
            alert("Failed to load posts");
        }
        finally {
            setLoading(false);
        }
    }

    useEffect(() => {
        fetchPosts();
    }, []);

    if (loading) return <h2>Loading Posts...</h2>;

    return (
        <div>
            <h1>All Posts</h1>

            <div className="list-button-row">
                <button className="btn btn-primary" onClick={() => navigate('/add')}>
                    + Add New Post
                </button>
            </div>
            {posts.length === 0 ? (
                <p>No posts found. <button className="btn btn-primary" onClick={() => navigate('/add')}>Add one now!</button></p>
            ) : (
                <ul className="post-list">
                    {posts.map(post => (
                        <li key={post.id} className="post-item">
                            {
                                // Render the post details
                                <div>
                                    <div className="post-header">
                                        <h3>{post.title}</h3>
                                        <span style={{ fontSize: '0.9em', color: '#888' }}>ID: {post.id}</span>
                                    </div>
                                    <p className="post-content-text">{post.content}</p>
                                </div>
                            }                   
                        </li>
                    ))}
                </ul>
            )}
        </div>
    );

}

export default PostList;