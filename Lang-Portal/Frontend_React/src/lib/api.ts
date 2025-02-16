import axios from 'axios';
import { handleApiError } from 'C:\\Users\\SUMA\\Desktop\\Github\\free-genai-bootcamp-2025-1\\Lang-Portal\\Frontend_React\\src\\lib\\errorHandler.ts';

const API_BASE_URL = 'http://localhost:5000/api';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

api.interceptors.response.use(
  (response) => response,
  (error) => handleApiError(error)
);

export default api;