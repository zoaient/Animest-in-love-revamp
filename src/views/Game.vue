<script setup>
import Navigation from '../components/Navigation.vue';
import Message from '../components/Message.vue';
import { VApp, VAppBar, VMain, VContainer, VToolbarTitle } from 'vuetify/components';
</script>


<template>
  <v-app class="background">
    <Navigation />
    <v-app-bar elevation="1" color="transparent" style="appbar">
        <v-avatar size="48">
          <v-app-bar-nav-icon @click="drawer = !drawer" icon ="$vuetify"></v-app-bar-nav-icon>
        </v-avatar>
      <v-toolbar-title>Nom du salon</v-toolbar-title>
    </v-app-bar>
      <v-container fluid class="fill-height flex-column">
        <Message />
      </v-container>
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
