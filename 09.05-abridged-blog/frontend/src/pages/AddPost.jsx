import React from 'react';
import { useNavigate } from 'react-router-dom';
import PostForm from '../components/PostForm';
import { PostService } from '../api';

function AddPost() {
    const navigate = useNavigate();

    const handleAddPost = async (postData) => {
        try {
            await PostService.addPost(postData);
            alert('Post created successfully!');
            navigate('/posts');
        } catch (error) {
            console.error('Error adding post:', error);
            const errorMessage = error.response?.data?.error || 'Failed to add post.';
            alert(errorMessage);
        }
    };

    return (
        <div>
            <h2>Add New Post</h2>
            <PostForm 
                onSubmit={handleAddPost} 
                buttonText="Create Post" 
                initialPost={{ title: '', content: '' }}
            />
        </div>
    );
}

export default AddPost;