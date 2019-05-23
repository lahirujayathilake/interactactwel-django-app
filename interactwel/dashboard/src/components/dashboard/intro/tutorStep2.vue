<template>
  
    <div class="modal-backdrop">
      <div class="tutor" style="top: 20%; left: 82%; height: 250px; width: 420px;">
        <header class="modal-header">
          <slot name="header">
            Explore Adaptation Plans
          </slot>
        </header>
        <section class="modal-body">
          <slot name="body"> 
         <p align="justify"> Click on Start to begin exploring adaptation plans. </p>
          </slot>
        </section>
        <footer class="tutor-footer">
          <slot name="footer">
            <button type="button" class="btn-green" @click="nextstep">Continue</button>
            <button type="button" class="btn-close" @click="close">Exit tutorial</button>
          </slot>
        </footer>
        <img src="../../../assets/tutor_arrow.png" class="hover"
        style = "position: relative; top: -315px; right: -350px; width: 300px; height: 300px;">
      </div>
    </div>

</template>

<script>
  
  export default {
    name: 'tutorStep2',

    methods: {
      close() {
        this.$emit('close');
      },
      nextstep() {
        this.$emit('close');
      },
    },
  };
</script>
<style>
.hover {
  -webkit-transform: scaleX(-1);
  transform: scaleX(-1);
}


</style>
