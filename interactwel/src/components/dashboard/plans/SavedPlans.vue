<template>
  <div>
    <b-card
      v-if="projects"
      no-body
    >
      <b-tabs
        pills
        card
        vertical
        nav-wrapper-class="w-25"
      >
        <b-tab
          v-for="project in projects"
          :title="project.name"
          @click="projectSelected(project.project_id)"
        >
          <!--<router-view></router-view>-->
          <b-card-body class="no-padding">
            <b-row class="mb-2">
              <b-col lg="9">
                <h5>{{ project.name }}</h5>
              </b-col>
              <b-col lg="3">
                <!--<b-button class="float-right" size="sm" variant="success">Visualize Selected Plans</b-button>-->
              </b-col>
            </b-row>
            <router-view />
          </b-card-body>
        </b-tab>
      </b-tabs>
    </b-card>
    <b-card v-if="!projects">
      <b-card-body title="You don't have any saved plans">
        <b-card-text>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque luctus purus sit amet massa hendrerit semper at eu dui.
        </b-card-text>
      </b-card-body>
    </b-card>
  </div>
</template>

<script>

export default {
  name: "SavedPlans",
  components: {
  },

  data() {
    return {
      projects: [],
      projectsUsers: [],
    };
  },
  computed: {},

  async mounted() {

    this.projects = await this.getProjectsListOfLoggedInUser();

    if (this.projects.length > 0){
      this.$router.push('/plans/saved-plans/' + this.projects[0].project_id);
    }

  },

  methods: {
    projectSelected: function(projectId) {
      this.$router.push('/plans/saved-plans/' + projectId);

    },

  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>

</style>
