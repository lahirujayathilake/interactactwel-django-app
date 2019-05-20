<template>
<div id="app">
    <modal v-show="isModalVisible" @close="closeModal"/>
    <dashboard></dashboard>   
</div>
</template>

<script>
    import modal from './dashboard/intro/modal.vue';
    import Dashboard from './dashboard/Dashboard.vue'
    import ProgressBar from './dashboard/progressBar/ProgressBar.vue'

    export default {

        name: 'app',
        components: {
            'Dashboard': Dashboard, 
            'modal': modal,
        },
    
        data () {
            return {
            isModalVisible: true,
            };
        },
        methods: {
            showModal() {
                this.isModalVisible = true;
            },
            closeModal() {
                this.isModalVisible = false;
            },
        },
    }
</script>

<style>
    @import '../static/css/main.css';
    @import "https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css";
    @import "https://cdn.jsdelivr.net/npm/bootstrap-vue@2.0.0-rc.11/dist/bootstrap-vue.css";

  .modal-backdrop {
    position: fixed;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    background-color: rgba(0, 0, 0, 0.3);
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .modal {
    background: #FFFFFF;
    box-shadow: 2px 2px 20px 1px;
    max-height: 450px;
    overflow: visible;
    position: fixed;
    top: 50%;
    left: 50%;
    /* bring your own prefixes */
    transform: translate(-50%, -50%);
    max-width: 800px;
    /*overflow-x: auto;*/
    display: flex;
    flex-direction: column;
  }

  .modal-header,
  .modal-footer {
    padding: 15px;
    display: flex;
  }

  .modal-header {
    border-bottom: 1px solid #eeeeee;
    color: #4AAE9B;
    justify-content: space-between;
    font-size: 25px;
    font-weight: bold;
  }

  .modal-footer {
    
    justify-content: flex-end;
  }

  .modal-body {
    position: relative;
    padding: 30px 40px;
    font-size: 18px;

  }

  .btn-close {
    border: none;
    font-size: 20px;
    padding: 20px;
    cursor: pointer;
    font-weight: bold;
    color: #4AAE9B;
    background: transparent;
  }

  .btn-green {
    border: none;
    font-size: 20px;
    cursor: pointer;
    font-weight: bold;
    color: #4AAE9B;
    background: transparent;
  }
 

</style>
