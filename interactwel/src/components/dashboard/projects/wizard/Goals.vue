<template>
    <b-col lg="12">
        <ol class="progress-bar">
            <li class="col-md-2 active">
                <div id="active" class="step-progress-bar">
                    <div class="step-no">1</div>
                    <h4 class="list-group-item-heading">Goals</h4>
                    <h4r class="list-group-item-heading">&#10003;</h4r>
                    <p class="list-group-item-text">{{selectedGoals.length}} goals selected</p>
                </div>
            </li>
            <li class="col-md-2">
                <div class="step-progress-bar">
                    <div class="step-no">2</div>
                    <h4 class="list-group-item-heading">Actors</h4>
                    <h4r class="list-group-item-heading">&#10003;</h4r>
                    <p class="list-group-item-text">0 Actores selected</p>
                </div>
            </li>
            <li class="col-md-2">
                <div class="step-progress-bar">
                    <div class="step-no">3</div>
                    <h4 class="list-group-item-heading">Actions</h4>
                    <h4r class="list-group-item-heading">&#10003;</h4r>
                    <p class="list-group-item-text">0 Actions selected</p>
                </div>
            </li>
            <li class="col-md-2">
                <div class="step-progress-bar">
                    <div class="step-no">4</div>
                    <h4 class="list-group-item-heading">Visualization</h4>
                    <h4r class="list-group-item-heading">&#10003;</h4r>
                    <p class="list-group-item-text">Adaptation Plans</p>
                </div>
            </li>
            <li class="col-md-2">
                <div class="step-progress-bar">
                    <div class="step-no">5</div>
                    <h4 class="list-group-item-heading">Feedback</h4>
                    <h4r class="list-group-item-heading">&#10003;</h4r>
                    <p class="list-group-item-text">Rate each plan</p>
                </div>
            </li>
            <li class="col-md-2">
                <div class="step-progress-bar">
                    <div class="step-no">6</div>
                    <h4 class="list-group-item-heading">Share</h4>
                    <h4r class="list-group-item-heading">&#10003;</h4r>
                    <p class="list-group-item-text">Share with community</p>
                </div>
            </li>
        </ol>
        <div id="step1">
            <div class="help-block">
                <b-collapse visible id="collapse-what_are_goals">
                    <b-card class="mb-2"
                            tag="article"
                            style="max-width: 25rem;"
                    >
                        <h4 class="card-title"> "What are Goals?" {{$route.params.projectId}}
                            <b-button v-b-toggle.collapse-what_are_goals variant="outline-info" class="m-1b" size="sm">
                                <i>Hide panel</i>
                            </b-button>
                        </h4>

                        <!--<b-card title><strong>What are Goals?</strong></b-card title> -->
                        <!--<b-card-text v-if="isHelpStep1Active">-->
                        <b-card-text>
                            <!--<p align="justify">
                                A community can suffer severe consequences from not effectively managing its water, energy, and land resources, especially when slow and sudden changes in the environment (e.g., changing climate, new policies, etc.) impair the quality, quantity, and accessibility of these resources over time.</p>-->
                            <p align="justify">
                                Before choosing an appropriate plan of response (called <b>Adaptation Plan</b>), community members must choose what types of goals are important for them to achieve.
                            </p>
                            <ul>
                                <li>These goals, also called <b>Adaptation Goals</b>, allow different groups within the community to evaluate how an adaptation plan may impact the bottom-line of each group, as well as that of the community at large.
                                </li>
                                <li>
                                    Further, many of these goals may be short-term goals, while others may need to be accomplished over a longer period of time.
                                </li>
                            </ul>
                            <p align="justify"> In <b>Step 1</b>, think about what goals would be of interest to you and your stakeholders. Then choose from the options available in this list by clicking on the goals that reflect your priorities and interests.
                            </p>
                            <p aling="justify">
                                You will be able to visualize how each adaptation plan meets the goals in <strong>Step 4</strong>.
                            </p>
                        </b-card-text>

                    </b-card>
                </b-collapse>
            </div>
            <b-card no-body footer-tag="footer">
                <div class="step-header" slot="header">Choose Goals
                    <em slot="header">
                        <b-button v-b-toggle.collapse-what_are_goals class="m-1" size="sm"> Show instructions </b-button>
                    </em>
                </div>
                <b-card-body>
                    <p class="card-text"><i>
                        Choose adaptation goals that are important to you.
                    </i></p>
                </b-card-body>
                <b-list-group-item>
                    <b-form-checkbox-group>
                        <label class="form-checkbox">
                            <input type="checkbox" v-model="selectAllGoals" @click="selectGoals">
                            Select All
                        </label>
                          <!--<div class="text-uppercase text-bold">id selected: {{selectedGoals}}</div>-->
                    </b-form-checkbox-group>
                </b-list-group-item>
                <b-list-group flush>
                    <b-form>
                        <div class="list-group">
                            <li class="list-group-item" v-for="goal in goals" v-bind:key="goal.goal_id">
                                <label class="form-checkbox" :disabled="goal.readonly">
                                    <input type="checkbox" :value="goal" v-model="selectedGoals"/>
                                    {{goal.name}}
                                    <b-collapse :id="'collapse-'+goal.goal_id">
                                        <p class="item-info">
                                            <small>{{goal.description}}</small>
                                        </p>
                                    </b-collapse>
                                </label>
                                <b-button v-b-toggle="'collapse-' + goal.goal_id" variant="outline-secondary">
                                    <b-badge class="info-button" pill variant="secondary" >i</b-badge>
                                </b-button>
                                <!--<b-badge class="info-button" pill variant="secondary" v-b-tooltip.hover
                                         :title="goal.info">i
                                </b-badge>-->
                            </li>
                        </div>
                    </b-form>
                </b-list-group>
                <em slot="footer">
                    <b-button variant="next" size="sm" @click="submit($route.params.projectId)">Next</b-button>
                </em>
            </b-card>
        </div>
        <b-modal v-model="showInfoModal">
            <template slot="modal-title">
                <strong>No selections were made</strong>
            </template>
            You forgot to select any goals. We filled that for you.
            <template slot="modal-footer" slot-scope="{ ok, cancel, hide }">
                <b-button size="sm" variant="next" @click="onConfirm">Ok</b-button>
            </template>
        </b-modal>
    </b-col>
</template>

<script>
    //import GoalsOpts from './../../../../../public/static/goals.json';
    import * as axios from "axios";

    export default {
        name: 'Goals',
        props: {},
        data() {
            return {
                itemInfoVisibility: false,
                selectAllGoals: false,
                selectedGoals: [],
                goals: [],
                showInfoModal: false,
                goalsAssignedToThisProject:[],
                adaptationPlan: [],
            }
        },
        mounted() {

            this.adaptationPlan = this.$store.state.currentAdaptationPlan;
            if(this.adaptationPlan){
                this.selectedGoals=this.adaptationPlan.selectedGoals;
            }

            const { utils } = AiravataAPI;
            this.projectId = this.$route.params.projectId
            utils.FetchUtils.get('/interactwel/api/goals/')
                .then(data => {
                    this.goals = data;
                })
                .catch(error => {
                    alert("Could not get the projects list. API error! " + error)
                });
        },

        watch: {
            selectedGoals: {
                handler() {
                    this.goals;
                },
                deep: true,
            }
        },

        methods: {
            selectGoals() {
                this.selectedGoals = [];
                if(!this.selectAllGoals){
                    this.goals.forEach(element => {
                        this.selectedGoals.push(element);
                    });
                }else{
                    this.selectedGoals=[];
                }
            },

            showItemInfo() {
                if (this.itemInfoVisibility == true) {
                    this.itemInfoVisibility = false
                } else {
                    this.itemInfoVisibility = true
                }

            },

            toggleModal() {
                // We pass the ID of the button that we want to return focus to
                // when the modal has hidden
                this.$refs['my-modal'].toggle('#toggle-btn')
            },

            submit(projectId) {
                if(this.selectedGoals.length<1){
                    this.showInfoModal = true;
                    return;
                }

                const { utils } = AiravataAPI;

                this.selectedGoals.forEach(goal=>{
                    utils.FetchUtils.post(
                    '/interactwel/api/projectgoals/',
                    {
                        goal_id: goal.goal_id,
                        project_id: projectId,

                    })
                    .then(data => {
                        console.log("data");
                    })
                    .catch(error => {
                        alert("Create the Projects. API error! " + error)
                    });
                });
                
                this.$store.commit("setSelectedGoals", this.selectedGoals);
                this.$store.commit("step1", true);
                this.$router.push('/adaptation-plans/'+this.projectId+'/actors');
                return true
            },

            onConfirm() {
                this.selectGoals();
                const projectId=this.$route.params.projectId;
                const { utils } = AiravataAPI;
                this.selectedGoals.forEach(goal=>{
                    utils.FetchUtils.post(
                    '/interactwel/api/projectgoals/',
                    {
                        goal_id: goal.goal_id,
                        project_id: projectId,

                    })
                    .then(data => {
                        console.log("data");
                    })
                    .catch(error => {
                        alert("Create the Projects. API error! " + error)
                    });
                });
                console.log(this.selectAllGoals);
                this.$store.commit("setSelectedGoals", this.selectedGoals);
                this.$store.commit("step1", true);
                this.$router.push('/adaptation-plans/'+this.projectId+'/actors');
            }
        }

    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

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

    h3 {
        margin: 40px 0 0;
    }

    ul {
        list-style-type: none;
        padding: 0;
    }

    ol {
        margin-bottom: 0;
    }

    .progress-bar li {
        display: inline;
    }

    a {
        color: #42b983;
    }

    #active{
        background-color: #dcedc8;
    }
</style>
