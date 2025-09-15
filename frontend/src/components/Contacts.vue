<script setup lang="ts">
import { onMounted } from 'vue';
import { useCharacterStore } from '../stores/characterStore';
const characterStore = useCharacterStore();
onMounted(() => {
  if (characterStore.characters.length === 0) {
    characterStore.fetchCharacters();
  }
});
</script>


<template>
  <v-container>
    <div v-if="characterStore.isLoading" class="text-center my-8">
      <v-progress-circular indeterminate size="64" color="primary"></v-progress-circular>
      <p class="mt-4">Chargement...</p>
    </div>
    <v-alert v-else-if="characterStore.error" type="error" title="Erreur" :text="characterStore.error" variant="tonal"></v-alert>
    <v-row v-else v-for="char in characterStore.characters" :key="char.id" >
        <v-btn class="profile-bar character-button justify-start pa-2" variant="text" block height="auto" rounded="lg" @click="characterStore.selectCharacter(char.id)">
          <v-avatar size="40" class="mr-3">
            <v-img :src=char.picture>
            </v-img>
          </v-avatar>
          <div class="user-info flex-grow-1">
            <div class="font-weight-bold text-subtitle-1">{{char.name}}</div>
          </div>
        </v-btn>
    </v-row>
  </v-container>
</template>



    
<style scoped>
.character-button {
  text-transform: none;
  transition: background-color 0.2s ease-in-out;
}
.character-button:hover {
  background-color: rgba(255, 255, 255, 0.1) !important;
}
.character-button:active {
  background-color: rgba(255, 255, 255, 0.15) !important;
}
</style>

  