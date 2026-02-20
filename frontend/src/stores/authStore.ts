import { defineStore } from 'pinia';
import axios from 'axios';

export const useAuthStore = defineStore('auth', {
  state: () => ({
    token: localStorage.getItem('token') || null,
    username: localStorage.getItem('username') || null,
  }),
  getters: {
    isAuthenticated: (state) => !!state.token,
  },
  actions: {
    async login(username : string, password : string) {
      console.log("coucou");
      const formData = new FormData();
      formData.append('username', username);
      formData.append('password', password);

      try {
        const response = await axios.post('/api/token', formData);
        this.token = response.data.access_token;
        this.username = username;        
        localStorage.setItem('token', this.token!);
        localStorage.setItem('username', username);
        return true;
      } catch (error) {
        console.error("Login failed", error);
        throw error;
      }
    },
    logout() {
      this.token = null;
      this.username = null;
      localStorage.removeItem('token');
      localStorage.removeItem('username');
    }
  }
});