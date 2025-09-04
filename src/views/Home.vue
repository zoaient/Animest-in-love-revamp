<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import Header from '../components/Header.vue'; 
import Footer from '../components/Footer.vue';
import Opening from '../components/Opening.vue';
const router = useRouter();
const showingCredits = ref(false);
const startGame = () => {
  router.push('/game'); 
};
</script>


<template>
  <div class="Home">
  <Opening />
  <Header />
    <h1>QUOICOU</h1>
    <div class="menu-buttons">
      <button @click="startGame">Nouvelle Partie</button>
      <button @click="loadGame">Charger Partie</button>
      <button @click="goToSettings">Options</button>
      <button @click="showCredits">Crédits</button>
    </div>

    <div v-if="showingCredits" class="credits-panel">
      <button @click="showingCredits = false">Fermer</button>
    </div>
  <Footer />
  </div>
</template>




  