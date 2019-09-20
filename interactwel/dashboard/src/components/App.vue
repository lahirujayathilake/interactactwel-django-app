<template>
<div id="app">
    <!--<welcome v-show="isModalVisible" @close="closeModal"/>
    <tutor-step1 v-bind:class="{active: isStep1Active}" v-show="istutor1Visible" @continue="continuetutor" @close="closeTutor"/>
    <tutor-step2 v-bind:class="{active: isStep2Active}" v-show="istutor2Visible" @close="closeTutor"/>-->
    <router-view></router-view>
</div>
</template>

<script>
    import Welcome from './dashboard/intro/Welcome.vue';
    import TutorStep1 from './dashboard/intro/TutorStep1.vue';
    import TutorStep2 from './dashboard/intro/TutorStep2.vue';
    import Dashboard from './dashboard/Dashboard.vue'

    export default {

        name: 'app',
        components: {
            'welcome': Welcome,
            'dashboard': Dashboard,
            'tutorStep1': TutorStep1,
            'tutorStep2': TutorStep2,
        },
    
        data () {
            return {
            isModalVisible: true,
            isStep1Active: false,
            isStep2Active: false,
            istutor1Visible: false,
            istutor2Visible: false,
            };
        },
        methods: {
            closeModal() {
                this.isModalVisible = false;
                this.isStep1Active = true;
                this.istutor1Visible = true;
                
            },

            closeTutor() {
                this.istutor1Visible = false;
                this.istutor2Visible = false;
                this.isStep1Active = false;
                this.isStep2Active = false;
            },

            continuetutor(){
                this.isStep2Active = true;
                this.istutor1Visible = false;
                this.isStep1Active = false;
                this.istutor2Visible = true;
            }
        },
    }
</script>

<style>
    @import '../static/css/main.css';
    @import "https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css";
    @import "https://cdn.jsdelivr.net/npm/bootstrap-vue@2.0.0-rc.11/dist/bootstrap-vue.css";

    body{
        font-size: 14px;
    }

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

    #welcome-modal .modal {
    background: #FFFFFF;
    box-shadow: 2px 2px 20px 1px;
    height: auto;
    overflow: scroll;
    position: fixed;
    top: 52%;
    left: 50%;
    /* bring your own prefixes */
    transform: translate(-50%, -50%);
    max-width: 800px;
    /*overflow-x: auto;*/
    display: flex;
    flex-direction: column;
  }

    #welcome-modal .modal-header,
    #welcome-modal .modal-footer {
    padding: 15px;
    display: flex;
  }

    #welcome-modal .modal-header {
    border-bottom: 1px solid #eeeeee;
    color: #4cae4c;
    justify-content: space-between;
    font-size: 25px;
    font-weight: bold;
  }

    #welcome-modal .modal-footer {
    justify-content: flex-end;
  }

    #welcome-modal .modal-body {
    position: relative;
    padding: 30px 40px;
    font-size: 16px;
        max-height: 400px;
        overflow: auto;

  }

  .btn-close {
    border: none;
    font-size: 20px;
    padding: 20px;
    cursor: pointer;
    font-weight: bold;
    color: #4cae4c;
    background: transparent;
  }

  .btn-green {
    border: none;
    font-size: 20px;
    cursor: pointer;
    font-weight: bold;
    color: #4cae4c;
    background: transparent;
  }
 
   .tutor {
    background: #FFFFFF;
    box-shadow: 2px 2px 20px 1px;
    max-height: 450px;
    overflow: visible;
    /* bring your own prefixes */
    /*transform: translate(-50%, -50%);*/
    max-width: 800px;
    /*overflow-x: auto;*/
    display: flex;
    flex-direction: column;
  }

  .tutor-footer {
      display: flex;
    justify-content: flex-end;
  }

</style>
