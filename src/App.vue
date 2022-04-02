<template>
  <div id="app">
    <landingPage/>
  </div>
</template>

<script>
// @ is an alias to /src
import landingPage from '@/views/LandingPage.vue'

export default {
  name: 'LandingPage',
  components: {
    landingPage
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin: 0;
  padding: 0;
}
</style>
