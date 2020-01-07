<template>
    <div id="graph" class="card">
        <div class="card-header"><span v-on:click="dismiss" class="close"><font-awesome-icon
                icon="times-circle"/> Close</span>
            <strong style="font-size:18px">Overview</strong>
        </div>
        <div class="card-body">
            <b-row>
                <b-col lg="6">
                    <h6 class="chart-title"><strong>Selected Goals</strong></h6>
                    <b-list-group class="no-padding" v-for="item in adaptationPlan.selectedGoals" v-bind:key="item.id">
                        <b-list-group-item class="no-border"><small> &#10003;&nbsp;{{item.goal}}</small></b-list-group-item>
                    </b-list-group>
                </b-col>
                <b-col lg="6">
                    <h6 class="chart-title"><strong>Selected Actors</strong></h6>
                    <b-list-group class="no-padding" v-for="item in adaptationPlan.selectedActors" v-bind:key="item.id" >
                        <b-list-group-item class="no-border"><small>&#10003;&nbsp;{{item.actor}}</small></b-list-group-item>
                    </b-list-group>
                </b-col>
            </b-row>
            <b-row style="margin-top:20px;">
                <b-col lg="12">
                    <h6 class="chart-title"><strong>Selected Actions for Actors</strong></h6>

                    <b-col lg="6">
                        <b-list-group class="no-padding" v-for="actor in adaptationPlan.selectedActors" v-bind:key="actor.id" >
                            <b-list-group-item class="no-border">&#10003;&nbsp;{{actor.actor}}</b-list-group-item>
                            <b-list-group class="no-padding" v-for="item in adaptationPlan.selectedActions" v-bind:key="item.id"
                                          v-if="item.actor.id == actor.id ">
                                <b-list-group-item class="no-border"><small>&#10003;&nbsp;{{item.action.action}}</small></b-list-group-item>
                            </b-list-group>
                        </b-list-group>
                    </b-col>

                  <!--  <b-tabs card vertical>
                        <b-tab v-for="actor in selectedActors" v-bind:key="actor.id"  :title="actor.actor" active>
                            <b-list-group v-for="item in getActions(actor)">
                                <b-list-group-item class="no-border"><small>&#10003;&nbsp;{{item.action}}</small></b-list-group-item>
                            </b-list-group>
                        </b-tab>

                    </b-tabs>-->
                </b-col>
            </b-row>
        </div>
    </div>
</template>
<script>
    import EventBus from './../../../../event-bus';


    export default {
        name: 'Overview',

        components: {
            EventBus
        },

        props: {
        },
        data() {
            return {
                adaptationPlan : [],
                selectedGoals: [{
                    id: "1",
                    goal: "Increase recharge to shallow aquifer",
                    readonly: false,
                    tooltip: true,
                    info: "Shallow aquifer recharge is assessed for each sub-basin, based on millimeters of water infiltrated."
                },
                    {
                        id: "0",
                        goal: "Improve surface water quality",
                        readonly: false,
                        tooltip: true,
                        info: "Surface water quality is assessed for each stream, based on total nitrogen loading, temperature, and dissolved oxygen."
                    }
                ],
                selectedActors : [{id: 1,
                    name: "F_SW",
                    actor: "Farmer with other surface water rights",
                    readonly: false,
                    info: "actor's that currently produce agricultural products and have the right to use surface water (excluding Columbia River)."}],
                selectedActions: []

            }
        },

        computed: {

        },

        mounted() {
            EventBus.$emit('HIDE_RESULTSMAP');
            this.adaptationPlan = JSON.parse(localStorage.getItem('adaptationPlan'));
            /*this.selectedGoals = localStorage.getItem('selectedGoals');
            this.selectedActors = localStorage.getItem('selectedActors');
            this.selectedActions = localStorage.getItem('selectedActions');*/
        },

        methods: {

            getActions(actor){
                let actorActions = [];
                this.selectedActions.forEach(actorAction => {
                    let actorId = actorAction.split(",")[0];
                    let actionId = actorAction.split(",")[1];
                    if (actor.id == actorId) {
                        this.actions.forEach(action => {
                            if (action.id == actionId) {
                                actorActions.push(action);
                            }
                        });
                    }
                });
                return actorActions;
            },

            dismiss() {
                EventBus.$emit('CLOSE');
            },
        }

    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
    .chart-title {
        font-size: 18px;
        /*font-weight: bold;*/
        color: #5e6b7e;
        border-bottom: 2px solid #28a645 !important;
        padding-bottom: 5px;
    }

    .no-border{
        border: 0px solid rgba(0,0,0,.125) !important;
    }

</style>