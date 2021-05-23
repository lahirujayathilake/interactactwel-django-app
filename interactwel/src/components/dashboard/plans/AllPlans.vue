<template>
  <div>
    <component :is="component='Header'" />
    <b-container
      fluid
      class="main"
    >
      <b-row class="pt-3 px-2">
        <b-col lg="1">
          <h3 class="mb-3">
            Plans
          </h3>
        </b-col>
        <b-col lg="11">
          <p>
            Plans are different scenarios of recommended adaptation decisions and strategies for the different
            community projects that you are a member of. <br>
            Under each Project tab, you can Generate New Plan with assistance from InterACTWEL as well as view details
            on plans previously saved by you.
          </p>
        </b-col>
      </b-row>
      <b-row>
        <b-col lg="12">
          <b-card
            v-if="projects"
            no-body
          >
            <b-tabs nav-wrapper-class="project-tabs">
              <b-tab
                v-for="project in projects"
                :key="project.id"
                :title="project.name"
              >
                <SavedPlansProjectComponent
                  :project="project"
                  :user="user"
                />
              </b-tab>
            </b-tabs>
          </b-card>
        </b-col>
      </b-row>
    </b-container>
    <component :is="component='Footer'" />
  </div>
</template>

<script>

import Header from './../../Header.vue';
import Footer from './../../Footer.vue';
import SavedPlansProjectComponent from '@/components/dashboard/plans/all-plans-sub-components/SavedPlansProjectComponent';

export default {
  name: "AllPlans",
  components: {
    SavedPlansProjectComponent,
    Header, Footer,
  },

  data() {
    return {
      projects: [],
      user: null,
    };
  },

  async mounted() {
    this.projects = await this.getProjectsListWithPlansOfLoggedInUser();
    this.user = await this.getLoggedInUser();
  },

  methods: {

  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
.main {
  background-color: #efefef;
  min-height: 90vh;
  text-align: left;
}

.project-tabs ul li a, .plan-tabs ul li a {
  color: #2c3e50;
}

.project-tabs ul li a:hover, .plan-tabs ul li a:hover {
  color: #28a745;
}

.plan-tabs ul li a.active {
  border-top: none;
  border-right: none;
  border-left: 3px solid #28a745 !important;
}

.project-tabs ul li a.active {
  font-weight: bold;
  border-top: 2px solid #28a745 !important;
}

</style>
