<template>
  <div>
    <div class="wizard-container">
      <b-navbar
        toggleable="sm"
        type="dark"
        variant="dark"
      >
        <b-navbar-toggle target="nav-text-collapse" />
        <b-button
          v-show="!isWizardFlowStarted"
          class="btn-sm mr-3"
          variant="outline-light"
          @click="$router.push('/all-plans')"
        >
          <i class="fa fa-chevron-left" /> Plans
        </b-button>
        <b-navbar-brand class="h5 py-0">
          Project :
        </b-navbar-brand>

        <b-collapse
          id="nav-text-collapse"
          is-nav
        >
          <b-navbar-nav>
            <b-nav-text class="h5 py-0">
              {{ selectedProject.name }}
            </b-nav-text>
          </b-navbar-nav>
        </b-collapse>
        <b-button
          v-show="!isWizardFlowStarted"
          variant="success"
          class="mr-2 glowing-button"
          @click="startWizard()"
        >
          Start
        </b-button>
        <b-button
          v-show="isWizardFlowStarted"
          variant="danger"
          class=""
          @click="exitWizard"
        >
          Exit
        </b-button>
      </b-navbar>
      <router-view />
      <b-col>
        <div v-show="isInStresses">
          <stresses-map />
        </div>
        <div v-show="!isInStresses">
          <project-map />
        </div>
      </b-col>
    </div>
    <info-modal
      v-show="isModalVisible"
      @close="closeModal"
    />
  </div>
</template>
<script>
import InfoModal from './intro/InfoModal.vue';

import ProjectMap from "@/components/dashboard/projects/ProjectMap";
import StressesMap from "@/components/dashboard/projects/StressesMap";

export default {
  name: 'AdaptationPlans',
  components: {
    StressesMap,
    ProjectMap,
    InfoModal,
  },

  data() {
    return {
      startBtn: true,
      isModalVisible: true,
      subbasinID: null,
      selectedProject: {},
      isWizardFlowStarted: false,
    };
  },
  computed: {
    isInStresses() {
      return this.$route.name === 'Stresses';
    },
  },

  mounted() {
    const { utils } = AiravataAPI;
    this.isWizardFlowStarted = 'true' === this.$route.query.wizard;
    this.projectId = this.$route.params.projectId;

    this.$store.commit("setProjectId", this.projectId);

    // TODO: call the /interactwel/api/projects/{project_id} to get the specific project
    utils.FetchUtils.get("/interactwel/api/projects/")
      .then(projects=>{
        this.selectedProject = projects.find(project=>{
          return project.project_id == this.projectId;
        });
      })
      .catch(error => {
        alert("Could not get the project. API error! " + error);
      });
  },

  beforeDestroy() {
    this.$parent.mapObject = $('.parent.mapObject');
  },

  methods: {
    startWizard(){
      this.isWizardFlowStarted = true;
      this.$store.commit("setWizardFlowStarted", true);
      this.$store.commit("resetWizardFlow", null);
      this.startBtn = false;
      this.$router.push('/adaptation-plans/' + this.projectId + '/goals/?wizard=true');
    },

    exitWizard(){
      localStorage.setItem('adaptation_wizardStarted', false);
      let confirmResponse = confirm("If you exit now all data will be cleared. Do you want to proceed");
      if (confirmResponse){
        this.$store.commit("resetWizardFlow", null);
        this.$router.push('/all-plans');
        this.isWizardFlowStarted = false;
      }
    },

    closeModal() {
      this.isModalVisible = false;
    },
  },

};

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
@import '../../../assets/vendor/Vue2Leaflet/leaflet.css';
.lg-map-container{
  height: 85vh;
  overflow: auto;
}
#step1 {
  position: absolute;
  z-index: 1000;
  left: 30px;
  top: 70px;
  min-width: 350px;
}

#step2 {
  position: absolute;
  z-index: 1000;
  left: 30px;
  top: 70px;
  min-width: 350px;
}

#step3 {
  position: absolute;
  z-index: 1000;
  left: 30px;
  top: 70px;
}

#step4 {
  display: flex;
  position: absolute;
  z-index: 1000;
  left: 30px;
  top: 70px;
  width: 1000px;
}

#step5 {
  position: absolute;
  z-index: 1000;
  left: 30px;
  top: 70px;
  width: 1000px;
}

#step6 {
  position: absolute;
  z-index: 1000;
  left: 30px;
  top: 70px;
  width:900px;
}

.step-progress-bar{
  padding: 0.5rem;
}
.step-progress-bar h4 {
  font-size: 1em;
  font-weight: 700;
  color: #5f6c73;
  margin-bottom: .05rem;
  text-align: left;
}

.step-progress-bar h4r {
  float: right;
  font-size: 1em;
  font-weight: 700;
  color: #ffffff;
  margin-bottom: .05rem;
  text-align: right;
}

.step-progress-bar p {
  font-weight: 400;
  font-size: .72857143em;
  color: #5f6c73;
  margin-bottom: 0;
  text-align: left;
}

.step-progress-bar .step-no {
  float: left;
  font-size: 25px;
  font-weight: 700;
  color: #28a745;
  width: 30px;
}
.progress-bar{
  display: inline;
  padding-inline-start: 0;
  border-bottom: 1px solid #dee2e6;
}
.progress-bar li {
  display: inline-block !important;
  background-color: #ffffff;
  margin:0 !important;
  padding: 0;
}

.progress-bar .active {
  background: #dcedc8!important;
}

.wizard-container .nav-tabs .nav-item.show .nav-link, .nav-tabs .nav-link.active {
  /*background: #DCEDC8 !important;
  border: none;*/
}

.wizard-container .nav-tabs .nav-item.show .nav-link, .nav-tabs .nav-link:hover {
  background: #e4f5d0 !important;
  border: none;
}

.arrow_box {
  position: relative;
  background: #DCEDC8;
  border-right: 2px solid #28a745;
  border-left: none;
}

.arrow_box:after, .arrow_box:before {
  left: 100%;
  top: 50%;
  border: solid transparent;
  content: " ";
  height: 0;
  width: 0;
  position: absolute;
  pointer-events: none;
}

.arrow_box:after {
  border-color: rgba(136, 183, 213, 0);
  border-left-color: #28a745;
  border-width: 11px;
  margin-top: -11px;
}

.arrow_box:before {
  border-color: rgba(95, 108, 115, 0);
  border-left-color: #28a745;
  border-width: 10px;
  margin-top: -10px;
  z-index: 1 !important;
}

.info-button {
  float: right !important;
  cursor: pointer;
  border: 3px solid #6d757d
}

.info-button:hover {
  background-color: #000;
  border: 3px solid #000
}

.help-block {
  position: absolute;
  border: none;
  right: -440px;
  z-index: 1000;
}

.help-block-actors {
  position: absolute;
  border: none;
  right: -440px;
  z-index: 1000;
}

.help-block-viz {
  width: 330px;
  position: absolute;
  border: none;
  right: -275px;
  z-index: 1000;
}

.help-block-actions {
  position: absolute;
  right: -450px;
  z-index: 1000;
}

.help-block .card-body, .help-block-actors .card-body, .help-block-actions .card-body {
  padding: 1.5rem;
}

.step-header {
  font-size: 18px;
  font-weight: bold;
}

.card-text {
  font-size: 13px;
  color: #5e6b7e;
}

.card-title {
  font-size: 25px;
  font-weight: bold;
  color: #5e6b7e;
  border-bottom: 2px solid #28a645;
  padding-bottom: 5px;
}

#step4 > article {
  flex: 1;
  height: calc(60vh - 20px);
}

#step4 nav,#step5 nav {
  flex: 0 0 auto;
  min-width: 200px;
  overflow: auto;
  background-color: #263238;
  height: inherit;
}

.item-info {
  margin-top: 5px;
  max-width: 250px;
}

.nav-pills .nav-link.active, .nav-pills .show > .nav-link {
  color: #fff;
  background-color: #4cae4c !important;
}

#step3 .nav-item a, #graph .nav-item a {
  color: #28a645;
  text-decoration: none;
  font-weight: 500;
  background-color: transparent;
  font-size: 14px;
}

#step3 .nav-item .nav-link.active,  #graph .nav-item .nav-link.active{
  color: #5e6b7e;
  font-weight: 500;
  background-color: #FFFFFF;
  font-size: 14px;
  border-top: 2px solid #28a645;
}

.show-info-btn{
  float: right;
  margin-right: 0px;
}

.btn.m-1{
  margin: -0.05rem !important;
}

.btn-next{
  color: #fff !important;
  background-color: #28a745 !important;
  border-color: #28a745 !important;
  padding: .25rem 3rem !important;
  float: right !important;
  margin-right: 0px !important;
}

.btn-back{
  color: #28a745 !important;
  background-color: transparent !important;
  border-color: #28a745 !important;
  padding: .25rem 3rem !important;
  float: left !important;
  margin-left: 0px !important;
}

.btn-outline-info{
  margin: .05rem !important;
  background-color: #FFFFFF;
  border-color: #FFF !important;
}

.list-group-item{
  padding: 0.5rem 1.25rem;
  font-size: 14px;
}

.wizard-container{
  height: 92vh;
  overflow: auto;
}
.glowing-button{
  padding: 0.5rem 2rem;
  font-weight: bold;
  text-transform: uppercase;
  box-shadow: 1px 1px 1px #3f3f3f, 0 0 1em #72ffb3, 0 0 0.1em darkblue;
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
  max-width: 450px;
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
#welcome-modal.modal-backdrop{
  background-color: rgba(0, 0, 0, 0.42);
}

.h5{
  text-transform: capitalize;
  line-height: 1.5;
}

</style>

