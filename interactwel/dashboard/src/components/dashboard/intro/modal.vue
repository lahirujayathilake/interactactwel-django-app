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
         <p align="justify">Many communities are caught off-guard when sudden or slow changes in the environment (e.g., changing climate, new policies, etc.) impair access to, supply of, and/or quality of water, energy, and natural resources that they depend on. </p>
         <p align="justify">In this activity, we are going to view multiple water, energy, and land management plans that have been created for you and your community to take actions and adapt to one or more unexpected changes before they happen. </p>
         <p align="justify">Further, we will also be able to view how these response actions impact the short term and long term goals and resilience of your community!</p>
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
