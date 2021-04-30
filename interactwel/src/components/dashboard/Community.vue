<template>
  <div>
    <component :is="component='Header'" />
    <b-container
      fluid
      class="main"
    >
      <b-row>
        <b-col>
          <h3>Community</h3>
        </b-col>
        <!--<b-col align="right">
                    <b-button>Create New Project</b-button>
                </b-col>-->
      </b-row>
      <b-row>
        <b-col>
          <b-nav
            tabs
            justified
          >
            <b-nav-item>
              <router-link to="/community/events">
                Events
              </router-link>
            </b-nav-item>
            <b-nav-item>
              <router-link to="/community/groups">
                Groups
              </router-link>
            </b-nav-item>
            <b-nav-item>
              <router-link to="/community/members">
                Members
              </router-link>
            </b-nav-item>
          </b-nav>
        </b-col>
      </b-row>
      <b-row>
        <b-col class="mt-4">
          <router-view />
        </b-col>
      </b-row>
    </b-container>
    <component :is="component='Footer'" />
  </div>
</template>

<script>
import Header from './../Header.vue';
import Footer from './../Footer.vue';

export default {
  name: 'Dashboard',
  components: {
    Header, Footer,
  },
  props: {
    msg: String,
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    .main {
        /*background-color: #efefef;*/
        padding: 1rem;
        min-height: 90vh;
        max-width: 1400px;
        text-align: left;
    }

    a {
        color: #42b983;
    }
</style>
