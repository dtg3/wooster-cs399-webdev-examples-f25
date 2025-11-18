import axios from 'axios';

const API_URL = import.meta.env.VITE_API_URL || 'http://127.0.0.1:5000/api/v1';

const api = axios.create({
    baseURL: API_URL,
    headers: {
        'Content-Type': 'application/json'
    }
});

export const TimeService = {
    getCurrentTime: async () => {
        const response = await api.get('/dt');
        return response.data;
    }
}

export const PostService = {
    getAllPosts: async () => {
        const response = await api.get('/posts');
        return response.data;
    },

    addPost: async (postData) => {
        const response = await api.post('/posts', postData);
        return response.data;
    }
}