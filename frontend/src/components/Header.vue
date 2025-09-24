<script setup>
import { ref } from 'vue';
const logoUrl = new URL('../assets/Logo/Logo_slash_zoaient_avec.png', import.meta.url).href;
const navItems = ref([
  { title: 'À Propos', path: '/about' },
  { title: 'Blog', path: '/blog' },
  { title: 'Contact', path: '/contact' },
]);
</script>

<template>
  <header class="header d-flex align-center justify-space-between pa-4">
    <v-img :src="logoUrl" max-width="360" class="logo-img"></v-img>
    <div class="nav-buttons">
      <v-btn v-for="item in navItems" :key="item.title" :to="item.path" variant="text" class="mx-2">
        {{ item.title }}
      </v-btn>
    </div>
  </header>
</template>


<style scoped>
.header {
  height: 80px; 
  background-color: rgba(255, 255, 255, 0.05); 
  backdrop-filter: blur(10px);
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  background-image: 
  url('../assets/Backgrounds/0.gif'); 
  background-position: center center;
  background-repeat: repeat;
  background-attachment: fixed;
}

.logo-img {
  cursor: pointer;
}

.nav-buttons .v-btn {
  text-transform: none;
  font-weight: 500;
  letter-spacing: normal;
}
</style>

  