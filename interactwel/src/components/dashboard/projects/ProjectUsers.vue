<template>
    <b-card no-body class="p-3">
      <b-row class="mb-3">
        <b-col><div class="btn btn-success btn-sm" v-b-modal.modal-1>Add New User</div></b-col>
      </b-row>
    <table class="table table-responsive">
      <thead>
      <tr>
        <th>#</th>
        <th>Username</th>
        <th>Name</th>
        <th>email</th>
        <th>Phone</th>
        <th>Organization</th>
        <th>Status</th>
        <th></th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="user in users">
        <td>{{ user.id }}</td>
        <td>{{ user.username}}</td>
        <td>{{ user.first_name }} {{ user.last_name }}</td>
        <td>{{ user.email }}</td>
        <td>{{ user.phone }}</td>
        <td>{{ user.organization }}</td>
        <td>Active</td>
        <td>
          <div class="btn btn-outline-success btn-sm">View Assigned Projects</div>
          <div class="btn btn-outline-danger btn-sm">Disable</div>
          <div class="btn btn-danger btn-sm"><i class="fa fa-trash"></i></div>
        </td>
      </tr>
      </tbody>
    </table>

      <b-modal id="modal-1" title="Add New User" hide-footer v-if="addUserModal">
        <div>
          <b-form>
            <b-form-group id="username" label="Username:" label-for="input-2">
              <b-form-input
                id="username"
                v-model="form.username"
                required
              ></b-form-input>
            </b-form-group>

            <b-form-group inline>
            <b-form-group id="firstname" label="First Name:" label-for="input-2">
              <b-form-input
                id="firstname"
                v-model="form.first_name"
                required
              ></b-form-input>
            </b-form-group>

            <b-form-group id="lastname" label="Last Name:" label-for="input-2">
              <b-form-input
                id="lastname"
                v-model="form.last_name"
                required
              ></b-form-input>
            </b-form-group>
            </b-form-group>
            <b-form-group
              id="email"
              label="Email"
              label-for="email"
              description="We'll never share your email with anyone else."
            >
              <b-form-input
                id="input-1"
                v-model="form.email"
                type="email"
                required
              ></b-form-input>
            </b-form-group>

            <b-form-group id="phone" label="Phone" label-for="phone">
              <b-form-input
                id="organization"
                v-model="form.phone"
                required
              ></b-form-input>
            </b-form-group>

            <b-form-group id="organization" label="Organization" label-for="organization">
              <b-form-input
                id="organization"
                v-model="form.organization"
                required
              ></b-form-input>
            </b-form-group>
            <b-button @click="createUserAction()" type="submit" variant="primary">Submit</b-button>
            <b-button type="reset" variant="danger">Reset</b-button>
          </b-form>
        </div>
      </b-modal>

    </b-card>
</template>

<script>

export default {
  name: "ProjectUsers",
  components: {
  },

  data() {
    return {

      form: {
        username: null,
        first_name: null,
        last_name: null,
        email: null,
        phone: null,
        organization: null,
      },

      users: [],
      user: null,

      addUserModal: true,

    };
  },

  async mounted() {

    const {utils, session} = AiravataAPI;

    utils.FetchUtils.get("/interactwel/api/users/")
      .then(users => {
        this.users = users;
        if (this.users.length > 0) {
          this.users = this.users;
        }

      })
      .catch(error => {
        alert("Could not create the user. API error! " + error);
      });

    this.user = await this.getLoggedInUser();

  },

  methods: {

    close() {
      this.$emit('close');
    },

    createUserAction() {
      const { utils } = AiravataAPI;
      utils.FetchUtils.post(
        '/interactwel/api/users/',
        {
          username: this.form.username,
          first_name: this.form.first_name,
          last_name: this.form.last_name,
          email: this.form.email,
          phone: this.form.phone,
          organization: this.form.organization,
        })
        .then(data => {
          this.users = data;
          this.addUserModal = false;
          this.$router.go();
        })
        .catch(error => {
          alert("Create New user. API error! " + error);
        });
      return true;
    },

  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
    @import "../../../assets/vendor/Vue2Leaflet/leaflet.css";

    table{
      font-size: 12px;
    }

    .modal-backdrop {
      position: fixed;
      top: 0;
      bottom: 0;
      left: 0;
      right: 0;
      background-color: rgba(0, 0, 0, 0.3);
      display: flex;
      justify-content: center;
      align-items: center;
    }
</style>

