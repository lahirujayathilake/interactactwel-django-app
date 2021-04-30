<template>
  <div>
    <h6 class="mt-3">
      Adaptation Plan {{ $route.params.planId }}
    </h6>
    <router-view />
  </div>
</template>
<script>

export default {
  name: 'Visualization',
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
