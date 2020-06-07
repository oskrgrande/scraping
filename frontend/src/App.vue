<template>
  <div>
    <div id="app">
      <!-- <router-link to="international">International</router-link>
    <router-link to="sports">Sports</router-link>
    <router-link to="health">Health</router-link>-->
      <router-view />
    </div>
  </div>
</template>

<script>
export default {
  name: "app",
  components: {},
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  height: 100vh !important;
  width: 100vw !important;
  background: #00d2ff; /* fallback for old browsers */
  background: -webkit-linear-gradient(
    to right,
    #928dab,
    #00d2ff
  ); /* Chrome 10-25, Safari 5.1-6 */
  background: linear-gradient(
    to right,
    #928dab,
    #00d2ff
  ); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
}
</style>
