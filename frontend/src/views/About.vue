<script setup>
import Headere from '../components/Header.vue'
const pfpUrl = new URL('../assets/Pfp/zouaient.jpg', import.meta.url).href;
</script>




<template>
  <Headere />
  <v-app class="background">
  <v-container class="py-12">
    <v-row justify="center">
      <v-col cols="12" md="8" class="text-center">
        <h1 class="text-h2 font-weight-bold mb-4">À Propos</h1>
        <p class="text-h6 mt-10 mr-10 text-medium-emphasis">
          nterdum et malesuada fames ac ante ipsum primis in faucibus. Morbi in dolor nec eros porta mollis eu et nunc. Vivamus gravida lacus sit amet laoreet mattis. Maecenas ac eleifend diam, in pellentesque nibh. Quisque molestie hendrerit velit, in ornare lorem. Etiam ligula urna, semper vitae diam ac, rutrum pulvinar metus. Vivamus ultrices pharetra pharetra. Fusce ultrices massa at facilisis hendrerit. Nunc feugiat, odio nec imperdiet ultrices, ante est luctus risus, non lacinia quam libero at metus. Mauris et ex volutpat, finibus mauris vel, aliquet elit. 
        </p>
        <p class="text-h6 mt-10 mr-10 text-medium-emphasis">
          nterdum et malesuada fames ac ante ipsum primis in faucibus. Morbi in dolor nec eros porta mollis eu et nunc. Vivamus gravida lacus sit amet laoreet mattis. Maecenas ac eleifend diam, in pellentesque nibh. Quisque molestie hendrerit velit, in ornare lorem. Etiam ligula urna, semper vitae diam ac, rutrum pulvinar metus. Vivamus ultrices pharetra pharetra. Fusce ultrices massa at facilisis hendrerit. Nunc feugiat, odio nec imperdiet ultrices, ante est luctus risus, non lacinia quam libero at metus. Mauris et ex volutpat, finibus mauris vel, aliquet elit. 
        </p>
        <p class="text-h6 mt-10 mr-10 text-medium-emphasis">
          nterdum et malesuada fames ac ante ipsum primis in faucibus. Morbi in dolor nec eros porta mollis eu et nunc. Vivamus gravida lacus sit amet laoreet mattis. Maecenas ac eleifend diam, in pellentesque nibh. Quisque molestie hendrerit velit, in ornare lorem. Etiam ligula urna, semper vitae diam ac, rutrum pulvinar metus. Vivamus ultrices pharetra pharetra. Fusce ultrices massa at facilisis hendrerit. Nunc feugiat, odio nec imperdiet ultrices, ante est luctus risus, non lacinia quam libero at metus. Mauris et ex volutpat, finibus mauris vel, aliquet elit. 
        </p>
      </v-col>
            <v-img class="pfp" :src="pfpUrl"></v-img>
    </v-row>
  </v-container>
  </v-app>
</template>


<style scoped>
.background :deep(.v-application__wrap){
  background-image:

  url('../assets/Backgrounds/fond_5.png'); 
  
  background-size: cover;
  background-position: center center;
  background-repeat: repeat;
  background-attachment: fixed;
  background-color: rgba(255, 255, 255, 255) !important;  
}
.pfp{
  border-radius: 10px;
}

</style>