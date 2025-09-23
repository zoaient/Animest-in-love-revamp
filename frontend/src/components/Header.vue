<script setup>
const logoUrl = new URL('../Logo_slash_zoaient_sans.png', import.meta.url).href;
</script>


<template>
<header class="header">
    <v-app-bar elevation="1" color="transparent" style="appbar" >
      <v-img :src="logoUrl">  
      </v-img>
    </v-app-bar>        
</header>
</template>

<style scoped>
.header {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    background-color: #8E143C;
    color: white;
    padding: 0.5rem 0;
    text-align: center;
    z-index: 1000;
    height: 7%;
}


.header-title {
  font-size: clamp(18px, 2.5vw, 32px);
}
.header-nav a {
  font-size: clamp(14px, 1.8vw, 22px);
  margin-left: 20px;
}
</style>