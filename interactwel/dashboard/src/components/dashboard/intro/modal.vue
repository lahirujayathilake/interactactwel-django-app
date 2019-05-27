<template>
  
    <div class="modal-backdrop">
      <div class="modal">
        <header class="modal-header">
          <slot name="header">
            Welcome Nick!
          </slot>
        </header>
        <section class="modal-body">
          <slot name="body"> 
         <p align="justify">Many communities are caught off-guard when sudden or slow changes in the environment (e.g., changing climate, new policies, etc.) impair access to, supply of, and/or quality of water, energy, and land resources that they depend on. </p>
         <p align="justify">In this activity, we are going to view multiple water, energy, and land management plans that have been created for you and your community. These plans include management actions for adapting to one or more unexpected changes before they happen. </p>
         <p align="justify">In this preliminary version of this tool, we have set up an example SCENARIO of an unexpected change. Imagine a new water market that is introduced to the Umatilla and Morrow county region in the future. This market allows <strong>water rights to be redistributed among growers in the basins.  
                            In this scenario, no additional water rights are allocated to the region, but growers are able trade existing water rights freely without constraints.  Current policy withdrawal times (e.g. Division 33 rules) still apply.</strong> While this scenario ignores transaction and infrastructure expansion costs, 
                            the tool does allow users to explore management actions tailored for the region and visualize multiple costs and benefits of these adaptation plans.</p>
          </slot>
        </section>
        <footer class="modal-footer">
          <slot name="footer">
            <button type="button" class="btn-green" @click="close">Continue</button>
          </slot>
        </footer>
      </div>
    </div>

</template>

<script>
  import EventBus from './../../../event-bus';
  
  export default {
    name: 'modal',

    

    methods: {
      close() {
        this.$emit('close');
      },
    },
  };
</script>
