<template>
  <div
    id="welcome-modal"
    class="modal-backdrop"
  >
    <div class="responsive modal modal-sm">
      <section class="modal-body">
        <slot name="body">
          <p align="justify">
            The map here shows the regional and publicly available data used by InterACTWEL for your project region. Please use the map interactively to explore the different data on the water, energy, and land resources and their current management.
            Click on the START button on top right, when you are ready to generate new plans!
          </p>
        </slot>
      </section>
      <footer class="modal-footer">
        <slot name="footer">
          <button
            type="button"
            class="btn btn-success btn-sm"
            @click="close"
          >
            Close
          </button>
        </slot>
      </footer>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Infomodal',

  data(){
    return {
      //loggedInUser: null
    };
  },
  async mounted() {
    //this.loggedInUser = await this.getLoggedInUser();
  },

  methods: {
    close() {
      this.$emit('close');
    },
  },
};
</script>

<style>
    #welcome-modal .modal{
        overflow: hidden !important;
    }
    #welcome-modal .modal-body {
        color: #3f4558;
        max-height: 500px !important;
    }

    #welcome-modal .card-title {
        font-size: 25px;
        font-weight: bold;
        padding-bottom: 5px;
    }
</style>
