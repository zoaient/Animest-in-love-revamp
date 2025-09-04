<template>
    <header class="header">
        <h1 class="header-title">Anim'est in love</h1>
    </header>
</template>

<script setup>
</script>

<style scoped>
.header {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    background-color: #ff69b4;
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