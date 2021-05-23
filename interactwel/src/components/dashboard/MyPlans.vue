<template>
  <div>
    <component :is="component='Header'" />
    <b-container
      fluid
      class="main"
    >
      <b-row>
        <b-col>
          <h3 class="mb-3">
            Plans
          </h3>
        </b-col>
      </b-row>
      <b-row>
        <b-col>
          <b-tabs v-model="tabIndex">
            <b-tab
              title="Generate New Plan"
              @click="loadTabContent(&quot;/plans/new-plan&quot;)"
            />
            <b-tab
              title="Saved Plans"
              @click="loadTabContent(&quot;/plans/saved-plans&quot;)"
            />
          </b-tabs>
        </b-col>
      </b-row>
      <b-row>
        <b-col>
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
  name: 'MyPlans',
  components: {
    Header, Footer,
  },
  data(){
    return {
      tabIndex: 0,
    };
  },

  computed: {
    currentRoute(){
      return this.$route.path;
    },
  },

  mounted() {
    let currentRoutePath = this.$route.path;
    if (currentRoutePath.includes("new-plan")){
      this.tabIndex = 0;
    }
    if (currentRoutePath.includes("saved-plans")){
      this.tabIndex = 1;
    }
  },
  methods: {

    loadTabContent(path) {
      this.$router.push(path);
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    .main {
        background-color: #efefef;
        min-height: 90vh;
        text-align: left;
    }

    a {
        color: #42b983;
    }
</style>
