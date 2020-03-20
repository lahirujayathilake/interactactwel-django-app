<template>
  <div>
    <b-card no-body>
      <div class="col-4 p-3">
        <b-form @submit.stop.prevent="submitAction">
          <b-form-select v-model="selectedUser" :options="users" size="sm" class="mt-3" required></b-form-select>
          <b-form-select
            v-model="selectedProject"
            :options="projects"
            size="sm"
            class="mt-3"
            required
          ></b-form-select>
          <b-form-select
            v-model="selectedStatus"
            :options="statusList"
            size="sm"
            class="mt-3"
            required
          ></b-form-select>
          <b-form-select v-model="selectedRole" :options="roles" size="sm" class="mt-3" required></b-form-select>
          <b-form-select
            v-model="selectedSector"
            :options="sectors"
            size="sm"
            class="mt-3"
            required
          ></b-form-select>
          <b-form-select v-model="selectedActor" :options="actors" size="sm" class="mt-3" required></b-form-select>

          <b-button
            type="submit"
            variant="success"
            size="sm"
            class="mt-3"
            style="float:right"
          >Assign</b-button>
        </b-form>
      </div>
    </b-card>
    <b-card v-show>
      <b-card-body title="You don't have access to any projects">
        <b-card-text>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque luctus purus sit amet massa hendrerit semper at eu dui.</b-card-text>
      </b-card-body>
    </b-card>
  </div>
</template>

<script>
import L from "leaflet";
import { LMap, LTileLayer, LMarker } from "vue2-leaflet";
import axios from "axios";

export default {
  components: {
    LMap,
    LTileLayer,
    LMarker
  },
  name: "AssignProjects",

  data() {
    return {
      selectedProject: null,
      selectedUser: null,
      selectedStatus: null,
      selectedRole: null,
      selectedSector: null,
      selectedActor: null,
      projects: [{ value: null, text: "Please select a Project" }],
      users: [{ value: null, text: "Please select an User" }],

      //todo: verify these values
      statusList: [
        { value: null, text: "Please select a Status" },
        { value: "Active", text: "Active" },
        { value: "Inactive", text: "Inactive" }
      ],

      roles: [
        { value: null, text: "Please select a Role" },
        { value: "Admin", text: "Admin" },
        { value: "Non-Admin", text: "Non-Admin" }
      ],
      sectors: [
        { value: null, text: "Please select a Sector" },
        { value: "Sector-1", text: "Sector-1" },
        { value: "Sector-2", text: "Sector-2" }
      ],
      actors: [
        { value: null, text: "Please select an Actor" },
        { value: "Actor-1", text: "Actor-1" },
        { value: "Actor-2", text: "Actor-2" }
      ]
    };
  },

  mounted() {
    const { utils } = AiravataAPI;
    utils.FetchUtils.get("/interactwel/api/projects/")
      .then(response => {
        response.forEach(projectItem => {
          this.projects.push({
            value: projectItem.project_id,
            text: projectItem.name
          });
        });
      })
      .catch(error => {
        alert("Could not get the projects list. API error! " + error);
      });

    utils.FetchUtils.get("/interactwel/api/users/")
      .then(response => {
        response.forEach(userItem => {
          this.users.push({ value: userItem.id, text: userItem.username });
          console.log(this.users);
        });
      })
      .catch(error => {
        alert("Could not get the projects list. API error! " + error);
      });
  },

  methods: {
    submitAction() {
      const { utils } = AiravataAPI;
      utils.FetchUtils.post("/interactwel/api/projectuserss/", {
        user_id: this.selectedUser,
        project_id: this.selectedProject,
        status: this.selectedStatus,
        role: this.selectedRole,
        sector: this.selectedSector,
        actor: this.selectedActor
      })
        .then(data => {
          console.log("data");
          if (data.error) {
            alert("failed to assign the user to the project");
          } else {
            alert("User project assignment was successful");
          }
        })
        .catch(error => {
          alert("Create the Projects. API error! " + error);
        });
      return true;
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
@import "../../../assets/vendor/Vue2Leaflet/leaflet.css";
.map-container {
  height: 400px;
  overflow: auto;
}
</style>

