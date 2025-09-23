<script setup>
import { useRouter } from 'vue-router';
import Headere from '../components/Header.vue'
const router = useRouter();
const startGame = () => {
  router.push('/game'); 
};
</script>


<template>
  <Headere />
  <v-app class="background">
    <div>
      COUCOU CAA VA 
    </div>
  </v-app>
</template>

<style scoped>
.background :deep(.v-application__wrap){
  background-image:

  url('../assets/Backgrounds/fond_5.png'); 
  
  background-size: cover;
  background-position: center center;
  background-repeat: no-repeat;
  background-attachment: fixed;
  background-color: rgba(255, 255, 255, 255) !important;  
}

</style>


  