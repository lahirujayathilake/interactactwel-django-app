<template>
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
        <b-card style="width: 700px" no-body footer-tag="footer">
            <div class="step-header" slot="header">Choose Actions
                <em slot="header">
                    <b-button v-b-toggle.collapse-3 class="m-1" size="sm"> Show instructions </b-button>
                </em>
            </div>
            <b-list-group-item>
                <b-form-checkbox-group>
                    <label class="form-checkbox">
                        <input type="checkbox" v-model="selectAllActions">
                        Select All
                    </label>
                    <!-- <div class="text-uppercase text-bold">id selected: {{selectedActions}}</div>-->

                </b-form-checkbox-group>
            </b-list-group-item>
            <b-card-body>
                <p class="card-text"><i>
                    Please choose from the drop-down menu the actor for which you want to define the possible actions.</i>
                </p>
                <h4>Selected actors Available actions</h4>
                <b-tabs card vertical content-class="mt-3" style="margin-top: 0px">
                    <b-tab :title="actor.actor" v-for="actor in selectedActors" v-bind:key="actor.id">
                        <div class="list-group">
                            <li class="list-group-item" v-for="action in actions" v-bind:key="action.id">
                                <label class="form-checkbox" :disabled="action.readonly">
                                    <input type="checkbox" :value="actor.actor + ',' + action.action"
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
                <!--<b-button-group>
                    <b-button id="step3-back-btn" @click="tabIndex--" variant="back" size="sm">
                        Back
                    </b-button>
                    <b-button id="step3-next-btn" @click="step3NextClicked" variant="next"
                              size="sm">Next
                    </b-button>
                </b-button-group>-->
                <b-button id="step3-next-btn" @click="submit" variant="next" size="sm">Next</b-button>
                <b-button id="step3-back-btn" @click="back" variant="back" size="sm">Back</b-button>
            </em>
        </b-card>
    </div>
</template>

<script>
    import ActionsOpts from './../../../../../public/static/actions.json';

    export default {
        name: 'Actors',
        props: {},
        data() {
            return {
                selectedActors: [],
                selectAllActions: false,
                selectedActions: [],
                actions: ActionsOpts,
            }
        },
        mounted() {
            this.selectedActors = JSON.parse(localStorage.getItem('selectedActors'));
            if (localStorage.getItem('selectedActions')) this.selectedActions = JSON.parse(localStorage.getItem('selectedActions'));

        },
        watch: {
            selectedActions: {
                handler() {
                    localStorage.setItem('selectedActions', JSON.stringify(this.selectedActions));
                },
                deep: true,
            }
        },
        methods: {

            selectActions() {
                this.selectedActions = [];
                if (!this.selectAllActions) {
                    for (let actor in this.selectedActors) {
                        for (let action in this.actions) {
                            if (this.selectedActors[actor].readonly == false && this.actions[action].readonly == false) {
                                this.selectedActions.push(this.selectedActors[actor].id + ',' + this.actions[action].id);
                            }
                        }
                    }
                }
            },

            submit() {
                localStorage.setItem('step3', true);
                let adaptationPlan = JSON.parse(localStorage.getItem("adaptationPlan"));
                adaptationPlan.selectedActions = this.selectedActions;
                localStorage.setItem('adaptationPlan', JSON.stringify(adaptationPlan));
                this.$router.push('/adaptation-plans/1/plans/1/overview')
            },

            back(){
                this.$router.push('/adaptation-plans/1/actors')
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
