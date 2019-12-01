<template>
  
    <div class="modal-backdrop">
      <div id="tutor-step1" class="tutor">
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
           <img src="../../../../assets/tutor_arrow.png" id="tutor-step1-arrow" class="rotate">
    </div>

</template>

<script>
  
  export default {
    name: 'TutorStep1',

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
    #tutor-step1{
        top: 200px;
        left: 200px;
        width: 300px;
        position: absolute;
    }
    #tutor-step1-arrow{
        position: absolute;
        top: 200px;
        left:30px;
        height: 100px;
    }
.rotate {
    -webkit-transform: rotate(-45deg);
    -moz-transform: rotate(-45deg);
    -o-transform: rotate(-45deg);
    -ms-transform: rotate(-45deg);
    transform: rotate(-45deg);
}
</style>
