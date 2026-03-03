import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/Home.vue';
import Game from '../views/Game.vue';
import About from '../views/About.vue'
import Login from '../views/Login.vue'
import Menu from '../views/Menu.vue'
import Cinematic from '../views/Cinematic.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component:  Home
  },
  {
    path: '/game',
    name: 'Game',
    component: Game
  },
  {
    path: '/about',
    name: 'About',
    component: About
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/Menu',
    name: 'Menu',
    component: Menu
  },
  {
    path: '/Cinematic',
    name: 'Cinematic',
    component: Cinematic
  },
];


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
});


export default router;