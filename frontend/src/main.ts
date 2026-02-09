import "./assets/main.css";

import { createApp } from "vue";
import { createPinia } from "pinia";
import App from "./App.vue";
import router from './router';
import 'vuetify/styles';
import vuetify from './plugins/vuetify';
import './assets/main.css';
import '@mdi/font/css/materialdesignicons.css';
import axios from 'axios';

const app = createApp(App).use(router).use(vuetify); 

app.use(createPinia());

app.mount("#app");



axios.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

axios.interceptors.response.use(
  response => response,
  error => {
    if (error.response && error.response.status === 401) {
      localStorage.removeItem('token');
      window.location.href = '/login';
    }
    return Promise.reject(error);
  }
);