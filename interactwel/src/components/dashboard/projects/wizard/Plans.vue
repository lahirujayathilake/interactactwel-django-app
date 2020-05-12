<template>
    <b-col lg="12">
        <ol class="progress-bar">
            <li class="col-md-2">
                <div id="active" class="step-progress-bar">
                    <div class="step-no">1</div>
                    <h4 class="list-group-item-heading">Goals</h4>
                    <h4r class="list-group-item-heading">&#10003;</h4r>
                    <p class="list-group-item-text">{{adaptationPlan.selectedGoals.length}} goals selected</p>
                </div>
            </li>
            <li class="col-md-2">
                <div class="step-progress-bar">
                    <div class="step-no">2</div>
                    <h4 class="list-group-item-heading">Actors</h4>
                    <h4r class="list-group-item-heading">&#10003;</h4r>
                    <p class="list-group-item-text">{{adaptationPlan.selectedActions.length}} Actors selected</p>
                </div>
            </li>
            <li class="col-md-2">
                <div class="step-progress-bar">
                    <div class="step-no">2</div>
                    <h4 class="list-group-item-heading">Actions</h4>
                    <h4r class="list-group-item-heading">&#10003;</h4r>
                    <p class="list-group-item-text">{{adaptationPlan.selectedActions.length}} Actions selected</p>
                </div>
            </li>
            <li class="col-md-2 active">
                <div class="step-progress-bar">
                    <div class="step-no">2</div>
                    <h4 class="list-group-item-heading">Visualization</h4>
                    <h4r class="list-group-item-heading">&#10003;</h4r>
                    <p class="list-group-item-text">Adaptation Plans</p>
                </div>
            </li>
            <li class="col-md-2">
                <div class="step-progress-bar">
                    <div class="step-no">2</div>
                    <h4 class="list-group-item-heading">Feedback</h4>
                    <h4r class="list-group-item-heading">&#10003;</h4r>
                    <p class="list-group-item-text">Rate each plan</p>
                </div>
            </li>
            <li class="col-md-2">
                <div class="step-progress-bar">
                    <div class="step-no">2</div>
                    <h4 class="list-group-item-heading">Share</h4>
                    <h4r class="list-group-item-heading">&#10003;</h4r>
                    <p class="list-group-item-text">Share with community</p>
                </div>
            </li>
        </ol>
    <div id="step4" title="Step 4">
        <div class="help-block-viz">
            <b-collapse visible id="collapse-4">
                <b-card
                        tag="article"
                        style="max-width: 33rem;"
                        class="mb-2"
                >
                    <h4 class="card-title">"What are Adaptation Plans?"
                        <b-button v-b-toggle.collapse-4 variant="outline-info" class="m-1b" size="sm"><i>Hide panel</i>
                        </b-button>
                    </h4>
                    <!--<b-card-text><strong>Who are Actors?</strong></b-card-text><br/>-->
                    <b-card-text>
                        <p align="justify">
                            In this section you will be able to view multiple adaptation plans that incorporate the actors <strong>(Step 2)</strong>
                            and actions <strong>(Step 3)</strong>
                            that you selected.  You can compare how each adaptation plan meets the goals you selected in <strong>Step 1</strong>
                            for the entire basin, sub-basins, and individual streams.  You can also compare the actions and their timeframes included within each plan.
                        </p>
                        <p aling="justify">Remember that you can click the map to visualize the data. </p>
                    </b-card-text>

                </b-card>
            </b-collapse>
        </div>
        <b-card no-body footer-tag="footer">
            <div class="step-header" slot="header">Visualization
                <em slot="header">
                    <b-button v-b-toggle.collapse-4 class="m-1" size="sm"> Show instructions </b-button>
                </em>
            </div>
            <b-card-body class="no-padding">
                <b-container     class="">
                    <b-row>
                            <div id="sidebar" role="tablist">

                                <b-nav header-tag="header" class="p-1" role="tab">
                                    <b-nav-item block href="#" v-b-toggle.collapse-0 variant="info" >
                                        <router-link :to="{ name: 'Overview', params: { planId: 1 }}">Overview</router-link>
                                    </b-nav-item>
                                </b-nav>

                                <div  v-for="plan in plans" v-bind:key="plan.id">
                                    <b-nav header-tag="header" class="p-1" role="tab">
                                        <b-nav-item block href="#" v-b-toggle="plan.id" variant="info" v-bind:class="{ nav_item_disabled: plan.disabled }" >
                                            {{plan.name}}
                                        </b-nav-item>
                                    </b-nav>

                                    <b-collapse :id="plan.id" accordion="my-accordion" role="tabpanel">
                                        <b-nav-item @click="$router.push({ name: 'ChartActions', params: { planId: plan.id }})" class="collapse-item">
                                            Actions
                                        </b-nav-item>
                                        <b-nav-item class="collapse-item">
                                            <router-link :to="{ name: 'ChartStreams', params: { planId:  plan.id  }}">Streams
                                            </router-link>
                                        </b-nav-item>
                                        <b-nav-item class="collapse-item">
                                            <router-link :to="{ name: 'ChartRegion', params: { planId:  plan.id  }}">Region
                                            </router-link>
                                        </b-nav-item>
                                        <b-nav-item class="collapse-item">
                                            <router-link :to="{ name: 'ChartSubBasins', params: { planId:  plan.id  }}">Sub Basins
                                            </router-link>
                                        </b-nav-item>
                                        <b-nav-item class="collapse-item">
                                            <router-link :to="{ name: 'Feedback', params: { planId:  plan.id  }}">Feedback
                                            </router-link>
                                        </b-nav-item>
                                    </b-collapse>
                                </div>

                            </div>
                        <b-col>
                            <router-view></router-view>
                        </b-col>
                    </b-row>
                </b-container>
            </b-card-body>
            <em slot="footer">
                <!--<b-button-group>
                    <b-button id="step2-back-btn" @click="step4BackClicked" variant="outline-success" size="sm">
                        Back
                    </b-button>
                    <b-button id="step2-next-btn" @click="step4NextClicked" variant="success" size="sm">Next
                    </b-button>
                </b-button-group>-->
                <b-button id="step2-next-btn" @click="submit" variant="next" size="sm">Next</b-button>
                <b-button id="step2-back-btn" @click="back" variant="back" size="sm">Back</b-button>

            </em>
        </b-card>
    </div>
        <div v-show="!feedbackVisibility" class="feedback-container">
                <div class="header-container">
                    <h5>Evaluate Adaptation Plan {{$route.params.planId}}</h5>
                </div>
                <div v-show="feedbackBlock" id="feedback-block">
                    <b-form v-show="initialFeedback" @submit="onSubmit" @reset="onReset">
                        <b-form-group label="Do you think the actions and timeframes presented in this plan are feasible?">
                            <b-form-radio v-model="feasibility" value="1" name="some-radios">Yes</b-form-radio>
                            <b-form-radio v-model="feasibility" value="0" name="some-radios">No</b-form-radio>
                        </b-form-group>
                    </b-form>
                    <b-form v-if="feasibility === '0'">
                        <b-form-group label="Please state why this plan is infeasible">
                            <b-form-textarea
                                    id="textarea"
                                    v-model="ifNotFeasiblecomment"
                                    rows="3"
                                    max-rows="6"
                            ></b-form-textarea>
                        </b-form-group>
                    </b-form>
                    <b-form v-if="feasibility === '1'">

                        <b-form-group
                                label="How well does this plan (alternative plan 1, 2, etc.) meet the management goals you identified in Step 1?">
                            <b-form-radio-group
                                    id="radio-group-1"
                                    v-model="q1Selected"
                                    :options="options"
                                    name="q1"
                            ></b-form-radio-group>
                        </b-form-group>

                        <b-form-group
                                label="Do you think that the projected results/impacts from this plan will occur if the proposed actions are implemented?">
                            <b-form-radio-group
                                    id="radio-group-2"
                                    v-model="q2Selected"
                                    :options="options"
                                    name="q2"
                            ></b-form-radio-group>
                        </b-form-group>

                        <b-form-group label="What factors might prevent you from taking the recommended actions listed in this plan? (check all that apply)">
                            <b-form-checkbox-group
                                    id="checkbox-group-1"
                                    v-model="SelectedFactors"
                                    :options="factors"
                                    name="q3"
                            ></b-form-checkbox-group>
                        </b-form-group>

                        <b-form-group
                                label="What factors might prevent you from taking the recommended actions listed in this plan? (check all that apply)">
                            <b-form-radio-group
                                    id="radio-group-3"
                                    v-model="q3Selected"
                                    :options="options"
                                    name="q4"
                            ></b-form-radio-group>
                        </b-form-group>

                        <b-form-group
                                label="How likely are you to implement the actions recommended in this plan?">
                            <b-form-radio-group
                                    id="radio-group-4"
                                    v-model="q4Selected"
                                    :options="options"
                                    name="q5"
                            ></b-form-radio-group>
                        </b-form-group>

                        <b-form-group
                                label="How likely are you to work with other stakeholder groups to implement this plan?">
                            <b-form-radio-group
                                    id="radio-group-5"
                                    v-model="q5Selected"
                                    :options="options"
                                    name="q6"
                            ></b-form-radio-group>
                        </b-form-group>
                        <b-form-group label="Rate this plan">
                            <star-rating star-size="30  "></star-rating>
                        </b-form-group>

                        <b-form-group label="Please share any additional thoughts about the alternative plans or the plan builder tool">
                            <b-form-textarea
                                    id="textarea"
                                    v-model="ifNotFeasiblecomment"
                                    rows="3"
                                    max-rows="6"
                            ></b-form-textarea>
                        </b-form-group>

                    </b-form>
                    <b-button @click="submitFeedback">Submit</b-button>
                </div>
                <div id="thankyou-block" v-show="thankyouBlock">
                    Thank you
                </div>
            </div>
    </b-col>
</template>

<script>
    //import ActionsOpts from './../../../../../public/static/actions.json';
    //import Feedback from './../charts/Feedback.vue'

    export default {
        /*components: {Feedback},*/
        name: 'Actors',
        props: {},
        data() {
            return {
                feedbackVisibility: true,
                feedbackBlock: true,
                thankyouBlock: false,
                feasibility: false,
                initialFeedback: true,
                ifFeasible: [],
                ifNotFeasible: [],
                ifFeasiblecomment: null,
                ifNotFeasiblecomment: null,

                options: [
                    {text: 'Not at all', value: 1},
                    {text: 'Satisfactory', value: 2},
                    {text: 'Neutral', value: 3},
                    {text: 'Well', value: 4},
                    {text: 'Very Well', value: 5},
                ],

                factors: [
                    {text: 'Infrastructure costs', value: 'Infrastructure costs'},
                    {text: 'Permits or other regulatory approval processes and cost', value: 'Permits or other regulatory approval processes and cost'},
                    {text: 'Reliance on other stakeholders to take action', value: 'Reliance on other stakeholders to take action'},
                    {text: 'Long time period before seeing positive results', value: 'Long time period before seeing positive results'},
                    {text: 'Public disapproval of the actions listed in the plan', value: 'Public disapproval of the actions listed in the plan'},
                ],

                plans:[
                    {id: 1, name: "Plan 1", feedbackProvided: false, disabled: false},
                    {id: 2, name: "Plan 2", feedbackProvided: false, disabled: true},
                    {id: 3, name: "Plan 3", feedbackProvided: false, disabled: true},
                ],

                feedbackProvided: false,
                currentRouteName: '',

                q1Selected: [],
                q2Selected: [],
                q3Selected: [],
                q4Selected: [],
                q5Selected: [],
                SelectedFactors: [],

                adaptationPlan: [],
            }
        },
        mounted() {
            this.adaptationPlan = this.$store.state.currentAdaptationPlan;

            if(!localStorage.feedbackProvided){
                localStorage.setItem('feedbackProvided', false);
            }else{
            let $this = this
            $this.feedbackProvided = localStorage.feedbackProvided;
            }

        },
        computed: {

            },
        watch: {

        },
        methods: {
            submit(){
                localStorage.setItem('step4', true);
                //this.feedbackVisibility = false
                this.$router.push('/adaptation-plans/1/share')

            },
            back(){
                this.$router.push('/adaptation-plans/1/actions')
            },
            submitFeedback() {
                let adaptationPlan = JSON.parse(localStorage.getItem("adaptationPlan"));
                adaptationPlan.planId = this.$route.params.planId;
                localStorage.setItem('adaptationPlan', JSON.stringify(adaptationPlan));

                localStorage.feedbackProvided = true
                this.feedbackProvided = true
                this.thankyouBlock = true
                this.feedbackBlock = false
            },
            onSubmit(evt) {
                evt.preventDefault()
                alert(JSON.stringify(this))
            },
            onReset(evt) {
                evt.preventDefault()
                // Reset our form values
                this.comment = null
                this.feasibility = []
                this.selected = []
                // Trick to reset/clear native browser form validation state
                this.show = false
                this.$nextTick(() => {
                    this.show = true
                })
            }
        }
    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
    .no-padding {
        padding: 0;
    }

    #graph{
        width:700px;
        height: 500px;
        overflow: auto;
    }

    #feedback{
        position: absolute;
        z-index: 1000;
        right: 30px;
        top: 125px;
        min-width: 350px;
        background-color: #ffffff;
    }

    #sidebar .active {
        color: #FFF !important;
        background-color: #4cae4c;
        margin: 5px !important;
        border-radius: 5px;
    }

    #sidebar > div > ul > li > a {
        color: rgba(255, 255, 255, 0.8) !important;
    }

    #sidebar > div > ul > li > a:hover {
        color: #fff !important;
    }

    .filter-options input {
        margin-left: 10px !important;
    }

    #sidebar {
        background-color: #263238;
        width: 200px;
    }

    #sidebar .nav-item {
        list-style: none;
    }

    #sidebar .collapse .nav-item {
        border-bottom: 1px solid #37474f !important;
        list-style: none;
    }

    #sidebar .collapse .nav-item a {
        color: rgba(255, 255, 255, 0.7);
    }

    #sidebar .p-1 {
        border-bottom: 1px solid #37474f !important;
        font-size: 14px;
        font-weight: bold;
    }

    #sidebar .p-1:hover {
        background-color: #000;
        border-right: 5px solid #4cae4c;
    }

    #sidebar .list-header a {
        color: #fff;
    }

    #sidebar .collapse-item a {
        font-size: 12px;
        text-indent: 15px;
    }

    #sidebar .collapsing-section {
        background-color: #000;
    }

    #sidebar .nav-link:hover {
        background-color: #000;
    }

    .feedback-container {
        background-color: #ffffff;
        padding: 1rem;
        position: absolute;
        right: 0px;
        width: 400px;
        z-index: 10000;
    }

    #feedback-block {
        background-color: #f5f8fa;
        padding: 20px;
        border-radius: 10px;
        margin-top: 20px;
        font-size: 12px;
        width: 100%;
        height: 81vh;
        overflow: auto;
    }

    #thankyou-block {
        background-color: #f5f8fa;
        padding: 20px;
        border-radius: 10px;
        margin-top: 20px;
        font-size: 12px;
        width: 100%;
    }

    #feedback-block legend {
        font-weight: bold;
        font-size: 14px;
    }
    .nav_item_disabled{
        pointer-events:none;
        opacity:0.6;
    }
</style>
