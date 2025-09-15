<script setup>
import { VNavigationDrawer,VList, VListItem} from 'vuetify/components';
import { ref } from 'vue';
const drawer = ref(null);
const logoUrl = new URL('../assets/Logo/animest_logo.png', import.meta.url).href;
const pfpUrl = new URL('../assets/Pfp/zouaient.jpg', import.meta.url).href;
import Contacts from './Contacts.vue';
</script>

<template> 

    <v-navigation-drawer v-model="drawer" class="drawer" >
      <v-img :src="logoUrl">  
      </v-img>
      <Contacts/>
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
</template>

<style scoped>
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
.contacts {
  border-radius: 25%;
}
</style>