<template>
  
    <div class="modal-backdrop">
      <div class="tutor" style="top: 35%; left: 18%; max-width: 20%; max-height: 50%;">
        <header class="modal-header">
          <slot name="header">
            Explore Datasets
          </slot>
        </header>
        <section class="modal-body">
          <slot name="body"> 
         <p align="left"> You can explore map data used in your community adaptation plans. </p>
          </slot>
        </section>
        <footer class="tutor-footer">
          <slot name="footer">
            <button type="button" class="btn-green" @click="nextstep">Continue</button>
            <button type="button" class="btn-close" @click="close">Exit tutorial</button>
          </slot>
        </footer>
      </div>
           <img src="../../../assets/tutor_arrow.png" class="rotate"
        style = "position: relative; top: -22%; left: -45%; max-width: 15%; max-height: 15%;">
    </div>

</template>

<script>
  
  export default {
    name: 'tutorStep1',

    methods: {
      close() {
        this.$emit('close');
      },
      nextstep() {
        this.$emit('continue');
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
