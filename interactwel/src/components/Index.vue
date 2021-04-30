<template>
  <div class="">
    <div class="top-fixed-nav">
      <b-navbar
        style="background-color: #263238!important;"
        toggleable="md"
        type="dark"
        variant="secondary"
      >
        <b-navbar-toggle target="nav_collapse" />
        <a
          class="navbar-brand"
          href="#"
        >
          <img
            src="../assets/InterACTWEL_logo.svg"
            width="140"
            height="35"
            class="d-inline-block align-top"
            alt=""
          >
        </a>
        <b-collapse
          id="nav-collapse"
          is-nav
        >
          <b-navbar-nav>
            <!--<b-nav-item href="#"><router-link to="/dashboard">Home</router-link></b-nav-item>
            <b-nav-item href="#" disabled>Community</b-nav-item>
            <b-nav-item href="#"><router-link to="/projects/my-projects">Project</router-link></b-nav-item>
            <b-nav-item href="#" disabled>Plans</b-nav-item>
            <b-nav-item href="#">Profile</b-nav-item>-->
          </b-navbar-nav>
        </b-collapse>
        <b-collapse
          id="nav_collapse"
          is-nav
        >
          <!-- Right aligned nav items -->
          <b-navbar-nav class="ml-auto">
            <!--<b-nav-item href="#"><router-link to="/signup"><b-button variant="outline-success">SignUp</b-button></router-link></b-nav-item>
            <b-nav-item href="#"><router-link to="/login"><b-button variant="success">Login</b-button></router-link></b-nav-item>-->
          </b-navbar-nav>
        </b-collapse>
      </b-navbar>
    </div>
    <b-container
      fluid
      class="main"
    >
      <b-container>
        <b-row>
          <b-col>
            <h1>Welcome to InterACTWEL</h1>
            <b-button variant="dark">
              <router-link to="/dashboard">
                Go to Dashboard
              </router-link>
            </b-button>
          </b-col>
        </b-row>
      </b-container>
    </b-container>
  </div>
</template>

<script>
export default {
  name: 'Home',
  props: {

  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .main {
    /*background-color: #efefef;*/
    padding: 3rem 1rem;
    min-height: 90vh;
    text-align: center;
  }
  .top-fixed-nav{
    border-top: 4px solid #ff7853 !important;
  }
</style>
