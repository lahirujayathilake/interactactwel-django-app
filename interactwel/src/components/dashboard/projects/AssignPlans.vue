<template>
    <b-card no-body class="p-3">
    <table class="table table-responsive">
      <thead>
      <tr>
        <th>Date Created</th>
        <th>Experiment ID</th>
        <th>Project ID</th>
        <th>Plan ID</th>
        <th>Actors</th>
        <th>Goals</th>
        <th>Actions</th>
        <th></th>
        <th></th>
      </tr>
      </thead>
<tbody>
<tr>
  <td>05/25/2021</td>
  <td>3124</td>
  <td>1</td>
  <td>15</td>
  <td>"Farmer: Columbia River (CR)”, "Farmer: Surface water (SW)“, "Farmer: Groundwater (GW)"</td>
  <td>"Improve surface water quality“, "Increase recharge to shallow aquifer“, "Increase agriculture productivity“ , "Improve ecological habitat"</td>
  <td>Increase the volume of non-Columbia surface water“, "Decrease the volume of non-Columbia surface water“</td>
  <td>
    <div class="btn btn-success btn-sm">Deploy</div>
  </td>
  <td><div class="btn btn-danger btn-sm"><i class="fa fa-trash"></i></div></td>
</tr>
</tbody>
    </table>
    </b-card>
</template>

<script>

export default {
  name: "AssignPlans",
  components: {
  },

  data() {
    return {

    };
  },

  mounted() {

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

