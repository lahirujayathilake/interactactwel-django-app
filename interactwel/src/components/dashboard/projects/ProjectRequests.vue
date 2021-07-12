<template>
    <b-card no-body class="p-3">
    <table class="table table-responsive">
      <thead>
      <tr>
        <th>Project Id</th>
        <th>Project Name</th>
        <th>user id</th>
        <th>name</th>
        <th>Status</th>
        <th></th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="request in projectRequests">
        <td>{{ request.id }}</td>
        <td>{{ request.project_id }}</td>
        <td>{{ request.user_id }}</td>
        <td>{{ request.status }}</td>
        <td>
          <div class="btn btn-outline-success btn-sm">Approve</div>
          <div class="btn btn-danger btn-sm"><i class="fa fa-trash"></i></div>
        </td>
      </tr>
      </tbody>
    </table>
    </b-card>
</template>

<script>

export default {
  name: "ProjectRequests",
  components: {
  },

  data() {
    return {

      users: null,
      projects: null,
      projectRequests: null,

    };
  },

  async mounted() {

    const {utils, session} = AiravataAPI;

    utils.FetchUtils.get("/interactwel/api/projectjoinrquests/")
      .then(projectjoinrquests => {
        this.projectRequests = projectjoinrquests;
        if (this.projectRequests.length > 0) {
          this.projectRequests = this.projectRequests;
        }
      })
      .catch(error => {
        alert("Could not retrieve requests. API error! " + error);
      });

  },
  methods: {

  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
    @import "../../../assets/vendor/Vue2Leaflet/leaflet.css";

    table{
      font-size: 12px;
    }
</style>

