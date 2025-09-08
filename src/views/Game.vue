<script setup>
import { ref } from 'vue';
import { VApp, VAppBar, VAppBarNavIcon, VNavigationDrawer, VMain, VContainer, VList, VListItem, VToolbarTitle } from 'vuetify/components';
const drawer = ref(null);
const logoUrl = new URL('../assets/Logo/animest_logo.png', import.meta.url).href;
const pfpUrl = new URL('../assets/Pfp/zouaient.jpg', import.meta.url).href;
</script>


<template>
  <v-app class="background">
    <v-navigation-drawer permanent location="left" :width="80" class="info-bar">
      <div class="d-flex flex-column align-center fill-height pa-2">
        <v-avatar size="48" class="my-2">
            <v-app-bar-nav-icon @click="drawer = !drawer" icon ="$vuetify"></v-app-bar-nav-icon>
        </v-avatar>
        <v-divider class="w-75 my-2"></v-divider>
        <v-btn icon>
            <v-avatar size="48">
                <v-img :src="pfpUrl">
                </v-img>
            </v-avatar>
        </v-btn>
        
        <v-spacer></v-spacer>
        <v-btn icon="mdi-cog" variant="text" class="my-2"></v-btn>
      </div>
    </v-navigation-drawer>

    <v-navigation-drawer v-model="drawer" class="drawer" >
      <v-img :src="logoUrl">  
      </v-img>
      <v-list class="flex-grow-1">
        <v-list-item title="Salon #général"></v-list-item>
        <v-list-item title="Salon #annonces"></v-list-item>
        <v-list-item title="Salon #blabla"></v-list-item>
      </v-list>
      <template v-slot:append>
        <v-divider></v-divider>
        <div class="profile-bar d-flex align-center pa-2">
          <v-avatar size="40" class="mr-3">
            <v-img :src="pfpUrl">
            </v-img>
          </v-avatar>
          <div class="user-info flex-grow-1">
            <div class="font-weight-bold text-subtitle-1">Zouaient</div>
            <div class="text-caption text-grey">En ligne</div>
          </div>
          <v-btn icon="$vuetify" variant="text" size="small"></v-btn>
        </div>
      </template>
    </v-navigation-drawer>
    <v-app-bar elevation="1" color="transparent" style="appbar">
      <v-toolbar-title>Nom du salon</v-toolbar-title>
    </v-app-bar>
    <v-main>
        <v-container fluid class="fill-height d-flex flex-column">
            <h1>Contenu principal</h1>
            <p>Lezueheziuhre chat irait ici. ehize chat irait ici. ehizuhizuhe chat irait ici. ehizuhizuhe chat irait ici. ehizuhizuhuhizuhrr</p>
        </v-container>
    </v-main>
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
.drawer {
  background-color: rgba(255, 255, 255, 0.05) !important; 
  backdrop-filter: blur(10px);
}
.drawer :deep(.v-list) {
  background: transparent;
}
.appbar {
  background-color: rgba(255, 255, 255, 0.1) !important; 
  backdrop-filter: blur(10px);
  border-bottom: 1px solid rgba(255, 255, 255, 0.2) !important;
}

.info-bar {
  background-color: rgba(255, 255, 255, 0.1) !important; 
  backdrop-filter: blur(10px);
  border-right: 1px solid rgba(255, 255, 255, 0.2) !important;
}


</style>
