<script setup>
import { useRouter } from 'vue-router';
import Headere from '../components/Header.vue'
import { ref } from 'vue'; 
import { useAuthStore } from '@/stores/authStore'
const router = useRouter();
const errors =[];
const authStore = useAuthStore(); 
const username = ref('')
const password = ref('');
const submit_login = async () => {
    try {
        await authStore.login(username.value, password.value);
        console.log("Login");
        router.push('/game'); 
    } catch (error) {
        console.error("Erreur lors du login", error);
    }
}
const logout = () => {
    try {
        authStore.logout();
        console.log("Logout");
    } catch(error){
        console.error("Erreur lors logout", error);
    }
}
</script>


<template>
  <Headere />
  <v-app class="background">
    <form id="app" @submit.prevent="submit_login">
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
    <v-btn @click="logout">
        logout
    </v-btn>
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
