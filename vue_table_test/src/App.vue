<template>
  <div id="app" class="ui container">
    <h1>&lt;Vuetable-2&gt;</h1>
    <my-vuetable></my-vuetable>
  </div>
</template>

<script>
  import MyVuetable from './components/MyVuetable'

  export default {
    name: "App",
    components: {
      MyVuetable
    },
  };
</script>

<style>
  #app {
    font-family: "Avenir", Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    color: #2c3e50;
    margin-top: 20px;
  }
</style>