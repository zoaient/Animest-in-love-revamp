<script setup>
const servers = ref([
  { id: 1, name: 'un', imageUrl: pfpUrl },
  { id: 2, name: 'deux', imageUrl: pfpUrl },
  { id: 3, name: 'trois', imageUrl: pfpUrl },
  { id: 4, name: 'quatre', imageUrl: pfpUrl },
]);

</script>

<template>
<v-navigation-drawer permanent location="left" :width="80" class="info-bar">
      <div class="d-flex flex-column align-center fill-height pa-2">
        <v-avatar size="48">
            <v-app-bar-nav-icon @click="drawer = !drawer" icon ="$vuetify"></v-app-bar-nav-icon>
        </v-avatar>
        <v-divider class="w-75"></v-divider>
        <v-btn v-for="server in servers" :key="server.id" icon class="my-3 contacts">
        <v-avatar size="48" class="contacts">
            <v-img :src="server.imageUrl" :alt="server.name"> 
            </v-img>
        </v-avatar>
        </v-btn>
      </div>
    </v-navigation-drawer>
</template>