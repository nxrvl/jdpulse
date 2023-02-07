<script setup>
import Home from "./components/Home.vue";
import Header from "./components/Header.vue";
</script>

<template>
  <header>
    <Header />
  </header>
  <div class="container-fluid h-100">
    <div class="row h-100">
      <div class="col-12 col-sm-10 mx-auto my-5" style="max-width: 80%">
        <Home />
      </div>
    </div>
  </div>
</template>

<style scoped>

</style>
