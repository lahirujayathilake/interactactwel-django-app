<template>
  
    <div class="modal-backdrop">
      <div class="tutor" style="top: 26%; left: 25%; height: 250px; width: 420px;">
        <header class="modal-header">
          <slot name="header">
            Explore the model data
          </slot>
        </header>
        <section class="modal-body">
          <slot name="body"> 
         <p align="justify"> You can explore the spatial data used to create the models. </p>
          </slot>
        </section>
        <footer class="tutor-footer">
          <slot name="footer">
            <button type="button" class="btn-green" @click="close">Continue</button>
            <button type="button" class="btn-close" @click="close">Exit tutorial</button>
          </slot>
        </footer>
        <img src="../../../assets/tutor_arrow.png" class="rotate"
        style = "position: relative; top: -250px; right: 250px; width: 300px; height: 300px;">
      </div>
    </div>

</template>

<script>
  
  export default {
    name: 'tutorStep1',

    methods: {
      close() {
        this.$emit('close');
      },
    },
  };
</script>
<style>
.rotate {
    -webkit-transform: rotate(-45deg);
    -moz-transform: rotate(-45deg);
    -o-transform: rotate(-45deg);
    -ms-transform: rotate(-45deg);
    transform: rotate(-45deg);
}
</style>
