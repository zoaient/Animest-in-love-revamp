<template>
  <div class="logo-bg"></div>
  <div class="logo"></div>
</template>

<style scoped>
.logo-bg {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  z-index: -1;
  background-image: url('@/assets/Backgrounds/fond_matin.jpg');
  background-size: contain;
  background-repeat: no-repeat;
  background-position: center;
}
.logo {
    width: 50vw;
    height: 50vh;
    background-image: url('@/assets/Logo/animest_logo.png');
    background-size: contain;
    background-repeat: no-repeat;
    background-position: center;
}
</style>

  