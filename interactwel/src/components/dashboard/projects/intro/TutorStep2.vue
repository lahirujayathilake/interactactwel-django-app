<template>
  
    <div class="modal-backdrop">
      <div id="tutor-step2" class="tutor">
        <header class="modal-header">
          <slot name="header">
            Explore Adaptation Plans
          </slot>
        </header>
        <section class="modal-body">
          <slot name="body"> 
         <p align="justify"> Click on <strong>Start Here</strong> to begin viewing and exploring adaptation plans created for your community.</p>
          </slot>
        </section>
        <footer class="tutor-footer">
          <slot name="footer">
            <button type="button" class="btn-green" @click="nextstep">Continue</button>
            <button type="button" class="btn-close" @click="close">Exit tutorial</button>
          </slot>
        </footer>
      
        <img src="../../../../assets/tutor_arrow.png" id="tutor-step2-arrow" class="hover">
      </div>
    </div>

</template>

<script>
  
  export default {
    name: 'TutorStep2',

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
  #tutor-step2{
    top: 100px;
    right: 200px;
    width: 300px;
    position: absolute;
  }
  #tutor-step2-arrow{
    position: absolute;
    top: -30px;
    left: 260px;
    height: 100px;
  }
.hover {
  -webkit-transform: scaleX(-1);
  transform: scaleX(-1);
}


</style>
