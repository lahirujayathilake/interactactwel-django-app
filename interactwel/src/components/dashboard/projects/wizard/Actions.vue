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
            <li class="col-md-2 active">
                <div class="step-progress-bar">
                    <div class="step-no">3</div>
                    <h4 class="list-group-item-heading">Actions</h4>
                    <h4r class="list-group-item-heading">&#10003;</h4r>
                    <p class="list-group-item-text">{{selectedActions.length}} Actions Selected</p>
                </div>
            </li>
            <li class="col-md-2">
                <div class="step-progress-bar">
                    <div class="step-no">4</div>
                    <h4 class="list-group-item-heading">Visualize and Evaluate</h4>
                    <h4r class="list-group-item-heading">&#10003;</h4r>
                    <p class="list-group-item-text">Adaptation Plans</p>
                </div>
            </li>
            <!--<li class="col-md-2">
                <div class="step-progress-bar">
                    <div class="step-no">5</div>
                    <h4 class="list-group-item-heading">Feedback</h4>
                    <h4r class="list-group-item-heading">&#10003;</h4r>
                    <p class="list-group-item-text">Rate each plan</p>
                </div>
            </li>-->
            <li class="col-md-2">
                <div class="step-progress-bar">
                    <div class="step-no">5</div>
                    <h4 class="list-group-item-heading">Wrap Up</h4>
                    <h4r class="list-group-item-heading">&#10003;</h4r>
                    <p class="list-group-item-text">Save and Print Plans</p>
                </div>
            </li>
        </ol>
    <div id="step3" title="Step 3"
         icon="ti-check">
        <div class="help-block-actions">
            <b-collapse visible id="collapse-3">
                <b-card
                        tag="article"
                        style="max-width: 25rem;"
                        class="mb-2">
                    <h4 class="card-title">"What are Actions?"
                        <b-button v-b-toggle.collapse-3 variant="outline-info" class="m-1b" size="sm"><i>Hide panel</i>
                        </b-button>
                    </h4>
                    <!-- <b-card-text><strong>Why select Actions?</strong></b-card-text><br/> -->
                    <b-card-text>
                        <p align="justify"><b>Adaptation Actions</b>
                            are management actions that adjust the allocation of resources, operations, and assets.  These management actions are formulated to adapt to changing basin conditions that effect quality, quantity, and accessibility of water, energy, and land resources. These actions include a variety of approaches – from infrastructure building, adopting new technologies to raising awareness.
                        </p>
                        <p align="justify">In <b>Step 3</b>, think about types of actions would be of interest to the actors you selected in Step 2 and select from the options available on the list. Please note that your adaptation plans (in Step 4) may include additional actions. But more on that when you reach Step 4!
                        </p>
                    </b-card-text>
                </b-card>
            </b-collapse>
        </div>
        <b-card style="width: 850px" no-body footer-tag="footer">
            <div class="step-header" slot="header">Choose Actions
                <em slot="header">
                    <b-button v-b-toggle.collapse-3 class="m-1" size="sm"> Show instructions </b-button>
                </em>
            </div>
            <b-list-group-item>
                <b-form-checkbox-group>
                    <label class="form-checkbox">
                        <input type="checkbox" v-model="selectAllActions" @click="selectActions">
                        Select All
                    </label>
                    <!-- <div class="text-uppercase text-bold">id selected: {{selectedActions}}</div>-->

                </b-form-checkbox-group>
            </b-list-group-item>
            <b-card-body>
                <p class="card-text"><i>
                    Please choose from the drop-down menu the actor for which you want to define the possible actions.</i>
                </p>
                <h6>Selected actors Available actions</h6>
                 <!-- <div class="text-uppercase text-bold">id selected: {{selectedActions}}</div> -->
                <!--<b-tabs card vertical content-class="" style="margin-top: 0px; height: 35vh; overflow: auto">
                    <b-tab :title="actor.actor" v-for="actor in selectedActors" v-bind:key="actor.id">
                        <div class="list-group">
                            <li class="list-group-item" v-for="action in actions" v-bind:key="action.id">
                                <label class="form-checkbox" :disabled="action.readonly">
                                    <input type="checkbox" :value="action"
                                           v-model="selectedActions"
                                           :disabled="action.readonly"/>
                                    {{action.action}}
                                </label>
                                <b-badge class="info-button" pill variant="secondary" v-b-tooltip.hover
                                         :title="action.info">
                                </b-badge>
                            </li>
                        </div>
                    </b-tab>
                </b-tabs>
-->

                <b-tabs card vertical content-class="" style="margin-top: 0px; height: 35vh; overflow: auto">
                    <b-tab :title="actor.actor" v-for="actor in selectedActors" v-bind:key="actor.id">
                        <div class="list-group">
                            <li class="list-group-item" v-for="item in actorActions" v-bind:key="item.id" v-if="item.actor.actor_id == actor.actor_id">
                                    <label class="form-checkbox" :disabled="item.action.readonly">
                                        <input type="checkbox" :value="item"
                                               v-model="selectedActions"
                                               :disabled="item.action.readonly"/>
                                        {{ item.action.name}}
                                    </label>
                                    <b-badge class="info-button" pill variant="secondary" v-b-tooltip.hover
                                             :title="item.action.description">
                                    </b-badge>

                            </li>
                        </div>
                    </b-tab>
                </b-tabs>

                <!--<b-form-select v-model="selected">
                    <option :value="null"disabled>-- Please select an actor --</option>
                    <option :value="actor.id" v-for="actor in selectedActors" v-bind:key="actor.id">{{actor.actor}}</option>
                </b-form-select>
                <div class="list-group">
                    <li class="list-group-item" v-for="action in actions" v-bind:key="action.id">
                        <label class="form-checkbox" :disabled="action.readonly">
                            <input type="checkbox" :value="selected + ',' + action.id"
                                    v-model="selectedActions"
                                    :disabled="action.readonly"/>
                            {{action.action}}
                        </label>
                        <b-badge class="info-button" pill variant="secondary" v-b-tooltip.hover
                                    :title="action.info">
                        </b-badge>
                    </li>
                </div>-->

            </b-card-body>
            <em slot="footer">
                <b-button id="step3-next-btn" @click="submit" variant="next" size="sm">Next</b-button>
                <b-button id="step3-back-btn" @click="back" variant="back" size="sm">Back</b-button>
            </em>
        </b-card>
    </div>
    <b-modal v-model="showInfoModal">
            <template slot="modal-title">
                <strong>No selections were made</strong>
            </template>
            You forgot to select any actions. We filled that for you.
            <template slot="modal-footer" slot-scope="{ ok, cancel, hide }">
                <b-button size="sm" variant="next" @click="onConfirm">Ok</b-button>
            </template>
        </b-modal>
    </b-col>
</template>

<script>
    // import ActionsOpts from './../../../../../public/static/actions.json';

    export default {
        name: 'Actors',
        props: {},
        data() {
            return {
                selectedActors: [],
                selectAllActions: false,
                selectedActions: [],
                actions: [], //ActionsOpts
                actorActions: [],
                showInfoModal: false,
                adaptationPlan: [],
                selectedActionsActorsIds: [],
                showInfoModal: false,
            }
        },
        mounted() {
            this.adaptationPlan = this.$store.state.currentAdaptationPlan;
            if(this.adaptationPlan){
                this.selectedActions=this.adaptationPlan.selectedActions;
            }

            this.projectId = this.$route.params.projectId;
            const { utils } = AiravataAPI;
            utils.FetchUtils.get('/interactwel/api/actions/')
                .then(data => {
                    this.actions = data;

                    this.selectedActors=this.$store.state.currentAdaptationPlan.selectedActors;
                    this.selectedActors.forEach( actor => {
                        this.actions.forEach( action => {
                        let actorAction = {};
                        actorAction.actor = actor;
                        actorAction.action = action;
                        this.actorActions.push(actorAction);
                    });
            });

                })
                .catch(error => {
                    alert("Could not get the actors list. API error! " + error)
                });

        },
        watch: {
            selectedActions: {
                handler() {
                    this.actions.id
                },
                deep: true,
            }
        },
        methods: {

            //todo: fix select all action
            selectActions() {
                this.selectedActions = [];
                if (!this.selectAllActions) {
                    for (let actor of this.selectedActors) {
                        for (let action of this.actions) {
                            console.log(actor,action);
                            let actorAction = {};
                            actorAction.actor = actor;
                            actorAction.action = action;
                            this.selectedActions.push(actorAction)
                            // this.selectedActionsActorsIds.push(this.selectedActors[actor].id + ',' + this.actions[action].id);
                        }
                    }
                }
            },

            submit() {
                if(this.selectedActions.length<1){
                    this.showInfoModal = true;
                    return;
                }
                
                this.$store.commit("setSelectedActions", this.selectedActions);
                this.$store.commit("step3", true);
                this.$router.push('/adaptation-plans/'+this.projectId+'/plans/overview');
            },

            back(){
                this.$router.push('/adaptation-plans/1/actors')
            },
            onConfirm() {
                this.selectActions();
                this.$store.commit("setSelectedActions", this.selectedActions);
                this.$store.commit("step3", true);
                this.$router.push('/adaptation-plans/'+this.projectId+'/plans/overview');
            },


            CheckActorsActions(){
                this.selectedActionsActors = [];
                this.missingActionsActors = [];
                if (!this.selectAllActions) {
                    for (var i = 0; i < this.selectedActions.length; i++) {
                        if(this.selectedActionsActors.includes(this.selectedActions[i][0]) == false){
                            this.selectedActionsActors.push(this.selectedActions[i][0]);
                            //console.log(this.selectedActions[i][0]);
                        }
                    }
                    for (let actor in this.selectedActors) {
                        if(this.selectedActionsActors.includes(actor) == false){
                            this.missingActionsActors.push(actor);
                            //console.log(actor);
                        }
                    }
                }
            },
        }
    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    h3 {
        margin: 40px 0 0;
    }

    ul {
        list-style-type: none;
        padding: 0;
    }

    li {
        display: inline-block;
        margin: 0 10px;
    }

    a {
        color: #42b983;
    }
</style>
