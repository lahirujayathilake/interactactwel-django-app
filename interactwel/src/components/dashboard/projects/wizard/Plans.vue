<template>
    <b-col lg="12">
        <ol class="progress-bar">
            <li class="col-md-2">
                <div id="active" class="step-progress-bar">
                    <div class="step-no">1</div>
                    <h4 class="list-group-item-heading">Goals</h4>
                    <h4r class="list-group-item-heading">&#10003;</h4r>
                    <p class="list-group-item-text">{{adaptationPlan.selectedGoals.length}} Goals Selected</p>
                </div>
            </li>
            <li class="col-md-2">
                <div class="step-progress-bar">
                    <div class="step-no">2</div>
                    <h4 class="list-group-item-heading">Actors</h4>
                    <h4r class="list-group-item-heading">&#10003;</h4r>
                    <p class="list-group-item-text">{{adaptationPlan.selectedActors.length}} Actors Selected</p>
                </div>
            </li>
            <li class="col-md-2">
                <div class="step-progress-bar">
                    <div class="step-no">3</div>
                    <h4 class="list-group-item-heading">Actions</h4>
                    <h4r class="list-group-item-heading">&#10003;</h4r>
                    <p class="list-group-item-text">{{adaptationPlan.selectedActions.length}} Actions Selected</p>
                </div>
            </li>
            <li class="col-md-2 active">
                <div class="step-progress-bar">
                    <div class="step-no">4</div>
                    <h4 class="list-group-item-heading">Visualize and Evaluate</h4>
                    <h4r class="list-group-item-heading">&#10003;</h4r>
                    <p class="list-group-item-text">Adaptation Plans</p>
                </div>
            </li>
            <li class="col-md-2">
                <div class="step-progress-bar">
                    <div class="step-no">5</div>
                    <h4 class="list-group-item-heading">Wrap Up</h4>
                    <h4r class="list-group-item-heading">&#10003;</h4r>
                    <p class="list-group-item-text">Save and Print Plans</p>
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
                    <b-button v-b-toggle.collapse-4 class="m-1 show-info-btn" size="sm"> Show instructions </b-button>
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
                            <router-view :key="$route.fullPath"></router-view>
                        </b-col>
                    </b-row>
                </b-container>
            </b-card-body>
            <em slot="footer">
                <b-button id="step2-next-btn" @click="next" variant="next" size="sm">Next</b-button>
                <b-button id="step2-back-btn" @click="back" variant="back" size="sm">Back</b-button>
            </em>
        </b-card>
    </div>
    </b-col>
</template>

<script>

    export default {
        name: 'Actors',
        props: {},
        data() {
            return {
                factors: [
                    {text: 'Infrastructure costs', value: 'Infrastructure costs'},
                    {text: 'Permits or other regulatory approval processes and cost', value: 'Permits or other regulatory approval processes and cost'},
                    {text: 'Reliance on other stakeholders to take action', value: 'Reliance on other stakeholders to take action'},
                    {text: 'Long time period before seeing positive results', value: 'Long time period before seeing positive results'},
                    {text: 'Public disapproval of the actions listed in the plan', value: 'Public disapproval of the actions listed in the plan'},
                ],

                plans:[],

                currentRouteName: '',

                adaptationPlan: [],
            }
        },
        mounted() {
            this.adaptationPlan = this.$store.state.currentAdaptationPlan;
            this.projectId = this.$route.params.projectId
            this.getProjectPlans(this.projectId).then(result => {
                this.$store.commit("setPlanList", result);
                if (result == null) {
                    return;
                }
                result.forEach(plan => {
                    this.plans.push({
                        id : plan.plan_id,
                        name : "Plan " + plan.plan_id
                    })
                })
            })
        },
        computed: {

            },
        watch: {

        },
        methods: {
            next(){
                localStorage.setItem('step4', true);
                this.$router.push('/adaptation-plans/' + this.projectId+'/share')

            },
            back(){
                this.$router.push('/adaptation-plans/' + this.projectId +'/actions')
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

