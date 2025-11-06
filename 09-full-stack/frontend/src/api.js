import axios from 'axios';

// Get API URL from Vite environment variable
const API_URL = import.meta.env.VITE_API_URL || 'http://127.0.0.1:5000/api/v1';

// Create an Axios instance with the base URL
const api = axios.create({
    baseURL: API_URL,
    headers: {
        'Content-Type': 'application/json',
    },
});

export const TimeService = {
    getCurrentTime: async () => {
        const response = await api.get('/dt');
        return response.data;
    }
}

export const PostService = {
    // GET all posts
    getAllPosts: async () => {
        // Axios returns response.data directly
        const response = await api.get('/posts');
        return response.data; 
    },

    // POST new post
    addPost: async (postData) => {
        // POST to /posts. Axios automatically serializes postData to JSON.
        const response = await api.post('/posts', postData);
        return response.data; // Returns the newly created post object
    },

    // PATCH/EDIT post
    editPost: async (id, postData) => {
        // PATCH to /posts/<int:post_id>
        const response = await api.patch(`/posts/${id}`, postData);
        return response.data; // Returns the updated post object
    },

    // DELETE post
    deletePost: async (id) => {
        // DELETE to /posts/<int:post_id>
        // If the Flask service returns 200 or 204 with a body (e.g., {'success': true}), 
        // Axios handles it. We don't need the return value here, just success.
        await api.delete(`/posts/${id}`);
    },
};