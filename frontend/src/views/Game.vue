<script setup>
import Navigation from '../components/Navigation.vue';
import Message from '../components/Message.vue';
import { VApp, VAppBar, VContainer, VToolbarTitle } from 'vuetify/components';
import { useCharacterStore } from '@/stores/characterStore';
const characterStore = useCharacterStore();
</script>


<template>
  <v-app class="background">
    <Navigation />
    <v-app-bar elevation="1" color="transparent" style="appbar" >
        <v-avatar size="32" class="ml-4">
            <v-img :src=characterStore.selectedCharacter?.picture>
            </v-img>
        </v-avatar>
      <v-toolbar-title>{{ characterStore.selectedCharacter?.name }}</v-toolbar-title>
    </v-app-bar>
      <Message />
  </v-app>
</template>





<style scoped>
.background :deep(.v-application__wrap) {
  background-image:
  linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), 
  url('../assets/Backgrounds/placeholder_bg.jpg'); 

  background-size: cover;
  background-position: center center;
  background-repeat: no-repeat;
  background-attachment: fixed;
  background-color: rgba(0, 0, 0, 0.5) !important;
}



</style>
