    
<template>
  <div class="Home">
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
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router'; 
const router = useRouter();
const showingCredits = ref(false);
const startGame = () => {
  console.log('Démarrage d\'une nouvelle partie !');
  router.push('/game'); 
};
</script>


  