<template>
  <div
    id="graph"
    class="card"
  >
    <div class="card-header">
      <strong>Streams</strong>
    </div>
    <div class="card-body no-padding">
      <b-tabs card>
        <b-tab
          title="Stream Flows"
          active
        >
          <div class="card-body">
            <img
              class="img-fluid"
              src="../../../../assets/graph-placeholder.png"
            >
          </div>
        </b-tab>
        <b-tab title="Stream Temparature">
          <div class="card-body">
            <img
              class="img-fluid"
              src="../../../../assets/graph-placeholder.png"
            >
          </div>
        </b-tab>
      </b-tabs>
    </div>
  </div>
</template>
<script>

export default {
  name: 'Actions',
  props: {},
  data() {
    return {};
  },
  watch: {},
  mounted() {

  },
  methods: {},
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
