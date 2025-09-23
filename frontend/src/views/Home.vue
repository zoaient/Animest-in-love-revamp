<script setup>
import { useRouter } from 'vue-router';
import Opening from '../components/Opening.vue';
import Headere from '../components/Header.vue'
const router = useRouter();
const startGame = () => {
  router.push('/game'); 
};
</script>


<template>
  <Headere />
  <div class="Home">
  <Opening />
    <h1>QUOICOU</h1>
    <div class="menu-buttons">
      <button @click="startGame">Nouvelle Partie</button>
      <button @click="loadGame">Charger Partie</button>
    </div>
  </div>
</template>




  