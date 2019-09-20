<template>
    <div>
        <component v-bind:is="component='Header'"></component>
        <b-container fluid class="main">
            <b-row>
                <b-col>
                    <b-nav>
                        <b-nav-item><h5>Umatilla Region Adapts to New Water Allocation</h5></b-nav-item>
                        <b-navbar-nav class="ml-auto">
                            <b-button v-show="!startButtonVisibility" v-on:click="start" variant="warning"
                                      class="my-2 my-sm-0" type="submit">Start Here
                            </b-button>
                            <b-button v-show="startButtonVisibility" variant="danger"
                                      class="my-2 my-sm-0" v-b-modal.exit-modal><strong> Exit </strong>
                            </b-button>
                        </b-navbar-nav>
                    </b-nav>
                </b-col>
            </b-row>
            <b-row>
                <div class="map-container">
                    <component v-show="!wizardVisibility" v-bind:is="component='Wizard'"></component>
                    <component v-bind:is="component='LeafletMap'"></component>
                    <component v-show="!regionalSummaryVisibility" v-bind:is="component='regional-summary'"></component>
                </div>
                <div class="feed-container" v-show="asideVisibility">
                    <feedback-x></feedback-x>
                </div>
            </b-row>
        </b-container>
        <component v-bind:is="component='Footer'"></component>
        <b-modal id="exit-modal">
            <template slot="modal-header">
                <h5>Exit Wizard</h5>
            </template>
            <template slot="default">
                <p>Do you want to save your changes?</p>
            </template>
            <template slot="modal-footer" slot-scope="{ ok, cancel }">
                <!-- Emulate built in modal footer ok and cancel button actions -->
                <b-button size="sm" @click="cancel()">
                    Cancel
                </b-button>
                <b-button size="sm" variant="success" @click="exitWizard()">
                    Save and Continue
                </b-button>
            </template>
        </b-modal>
    </div>
</template>

<script>
    import Header from './Header.vue';
    import Footer from './Footer.vue';
    import CreateProject from './project/CreateProject.vue';
    import Overview from './plans/Overview.vue';
    import Feedback from './plans/Feedback.vue';
    import Wizard from './../dashboard/wizard/Wizard.vue';
    import FeedbackX from './../dashboard/feedback/Feedback.vue';
    import RegionalSummary from './../dashboard/map/RegionalSummary.vue'
    import LeafletMap from '../dashboard/map/LeafletMap.vue';
    import EventBus from './../../event-bus';

    export default {
        components: {
            Header, Footer, LeafletMap, CreateProject, Overview, Feedback, Wizard, RegionalSummary, FeedbackX
        },
        name: 'Visualization',

        props: {
            adaptationPlan: {
                type: String,
                default: ""
            },
        },

        data() {
            return {
                startButtonVisibility: false,
                chartsVisibility: true,
                wizardVisibility: true,
                asideVisibility: false,
                regionalSummaryVisibility: true,
                breadcrumb: [
                    {
                        text: 'Home',
                        to: { name: 'Home' }
                    },
                    {
                        text: 'Plans',
                        to: { name: 'Plans' }
                    },
                    {
                        text: 'Overview',
                        to: { name: 'Overview' }
                    }
                ]
            }
        },

        mounted() {

            let $this = this;
            EventBus.$on('START_WIZARD', function () {
                $this.wizardVisibility = false;
            }),
                EventBus.$on('EXIT_WIZARD', function () {
                    $this.wizardVisibility = true;
                }),
                EventBus.$on('SHOW_ASIDE', function () {
                    $this.asideVisibility = true;
                }),
                EventBus.$on('HIDE_ASIDE', function () {
                    $this.asideVisibility = false;
                }),
                EventBus.$on('SELECTED_BASIN', function (selectedBasinID) {

                    $this.regionalSummaryVisibility = true;

                    if ($this.prevLayerClicked !== null || $this.prevLayerClicked == selectedBasinID) {
                        $this.regionalSummaryVisibility = true;
                    }
                    if ($this.prevLayerClicked !== selectedBasinID) {
                        $this.createRegionSummary(selectedBasinID)
                        $this.regionalSummaryVisibility = false;
                        $this.prevLayerClicked = selectedBasinID;
                    }else{
                        $this.regionalSummaryVisibility = true;
                        $this.prevLayerClicked = null;
                    }
                }),
                EventBus.$on('CLOSE', function () {
                    $this.regionalSummaryVisibility = true
                })
        },



        methods: {
            start: function () {
                this.startButtonVisibility = true
                this.startWizard()

            },

            startWizard() {
                EventBus.$emit('START_WIZARD');
            },

            exitWizard(){
                /*Save Visualization Data*/
                EventBus.$emit('EXIT_WIZARD');
                this.startButtonVisibility = false

            },

            afterWizardFinished() {
                this.sidebarLeftVisibility = false,
                    this.sidebarRightVisibility = false,
                    this.chartsVisibility = false
            },

            createRegionSummary(subbasinID){
                EventBus.$emit('CREATE_REGION_SUMMARY', subbasinID);
            }

        }

    }

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>

    .map-container {
        -webkit-box-flex: 1;
        -ms-flex: 1;
        flex: 1;
        height: calc(92vh - 20px);
    }
    .feed-container {
        flex: 0 0 400px;
        height: 92vh;
        overflow: auto;
        background-color: #ededed;
    }
</style>

