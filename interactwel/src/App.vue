<template>
  <div id="app">
    <router-view />
  </div>
</template>

<script>
export default {
  name: 'App',
  components: {

  },
};
</script>

<style>
  @import "https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css";
  @import "https://cdn.jsdelivr.net/npm/bootstrap-vue@2.0.0-rc.11/dist/bootstrap-vue.css";
#app {
  /*font-family: 'Avenir', Helvetica, Arial, sans-serif;*/
  font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,"Noto Sans",sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Noto Color Emoji";
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  width:100%;
  font-weight:500;
  font-size: 14px;
}

  .main{
    height: 90vh;
    overflow: auto;
  }

  .nav-pills .nav-link.active, .nav-pills .show>.nav-link {
    color: #fff;
    background-color: #28a645;
  }

  .card-title {
    font-size: 18px;
    font-weight: bold;
    color: #5e6b7e;
    border-bottom: 2px solid #28a645;
    padding-bottom: 5px;
  }

  .card-text {
    font-size: 13px;
    color: #5e6b7e;
  }

  .card-header{
    font-size: 14px !important;
  }

  td{
    font-size: 13px !important;
  }

  .c-nav{
    display:none;
  }

</style>
