<template>
  <div id="app">
    <dashboard></dashboard>
      <router-view></router-view>
  </div>
</template>

<script>

    import Dashboard from './components/dashboard/Dashboard.vue'

    export default {

        name: 'app',
        components: {
            Dashboard
        },
    }
</script>

<style>
  @import './static/css/main.css';
  @import "https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css";
  @import "https://cdn.jsdelivr.net/npm/bootstrap-vue@2.0.0-rc.11/dist/bootstrap-vue.css";


</style>
