<template>
  <div>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <a class="navbar-brand" href="#" style="padding-left: 10%; margin-left: 20px; ">
        <img class="logo" src="/src/assets/jdpulse-logo.svg" alt="logo">
      </a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse justify-content-end" id="navbarNav" style="padding-right: 10%; margin-right: 20px">
        <ul class="navbar-nav ml-auto">
          <li class="nav-item" v-if="isAuthenticated">
            <a class="nav-link" href="#" @click.prevent="Logout">Logout</a>
          </li>
          <li class="nav-item" v-else>
            <a class="nav-link" href="#" @click.prevent="Login">Login</a>
          </li>
        </ul>
      </div>
    </nav>
    <div class="container my-5">
      <router-view />
    </div>
  </div>
</template>

<script>
export default {
  name: "Header"
}
</script>

<style scoped>
.navbar {
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
}
.logo {

  width: 200px; /* or any other value */
}

</style>