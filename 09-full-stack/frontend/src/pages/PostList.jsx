import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { PostService } from '../api';
import PostForm from '../components/PostForm';

function PostList() {
    const [posts, setPosts] = useState([]);
    const [loading, setLoading] = useState(true);
    const [editingPost, setEditingPost] = useState(null); // Hold the full post object being edited
    const navigate = useNavigate();

    const fetchPosts = async () => {
        setLoading(true);
        try {
            const data = await PostService.getAllPosts();
            setPosts(data);
        } catch (error) {
            console.error('Error fetching posts:', error);
            alert('Failed to load posts. Is the Flask API running?');
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => {
        fetchPosts();
    }, []);

    const handleDelete = async (id) => {
        if (!window.confirm(`Are you sure you want to delete post ID ${id}?`)) {
            return;
        }
        try {
            await PostService.deletePost(id);
            alert(`Post ID ${id} deleted successfully.`);
            fetchPosts(); // Re-fetch the list to update the UI
        } catch (error) {
            console.error('Error deleting post:', error);
            const errorMessage = error.response?.data?.message || 'Failed to delete post.';
            alert(errorMessage);
        }
    };

    const handleEdit = (post) => {
        setEditingPost(post);
    };
    
    const handleCancelEdit = () => {
        setEditingPost(null);
    };

    const handleUpdatePost = async (postData) => {
        if (!editingPost) return;

        try {
            await PostService.editPost(editingPost.id, postData);
            alert('Post updated successfully!');
            setEditingPost(null); // Exit edit mode
            fetchPosts(); // Re-fetch the list
        } catch (error) {
            console.error('Error updating post:', error);
            const errorMessage = error.response?.data?.error || error.response?.data?.message || 'Failed to update post.';
            alert(errorMessage);
        }
    };

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
                            {editingPost && editingPost.id === post.id ? (
                                // Render the form for editing
                                <div className="edit-form-container">
                                    <h3>Editing Post ID: {post.id}</h3>
                                    <PostForm
                                        onSubmit={handleUpdatePost}
                                        initialPost={post}
                                        buttonText="Save Changes"
                                        onCancel={handleCancelEdit}
                                    />
                                </div>
                            ) : (
                                // Render the post details
                                <div>
                                    <div className="post-header">
                                        <h3>{post.title}</h3>
                                        {/* You can display the ID here or in the title for reference */}
                                        <span style={{ fontSize: '0.9em', color: '#888' }}>ID: {post.id}</span>
                                    </div>
                                    <p className="post-content-text">{post.content}</p>
                                    <div className="post-actions">
                                        <button className="btn btn-secondary" onClick={() => handleEdit(post)}>Edit</button>
                                        <button className="btn btn-danger" onClick={() => handleDelete(post.id)}>Delete</button>
                                    </div>
                                </div>
                            )}
                        </li>
                    ))}
                </ul>
            )}
        </div>
    );
}

export default PostList;