<script setup>
import { useRouter } from 'vue-router';
import Headere from '../components/Header.vue'
import { useAuthStore } from '@/stores/authStore'
const router = useRouter();
const errors =[];
const submit = () => {
    useAuthStore.login(username.value,password.value) // a corriger je fatiguée.
  
}
</script>


<template>
  <Headere />
  <v-app class="background">
    <form id="app" @submit="submit">
        <p>
            <label for="username">username</label>
            <input id="username" v-model="username" type="text" name="username">
        </p>

        <p>
            <label for="password">Mot de passe</label>
            <input id="password" v-model="password" type="text" name="password">
        </p>

        <p>
            <input type="submit"value="Submit">
        </p>
    </form>
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
