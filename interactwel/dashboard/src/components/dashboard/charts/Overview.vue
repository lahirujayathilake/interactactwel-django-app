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
                    <b-list-group class="no-padding" v-for="item in selectedGoals">
                        <b-list-group-item><small> &#10003;&nbsp;{{item.goal}}</small></b-list-group-item>
                    </b-list-group>
                </b-col>
                <b-col lg="6">
                    <h6 class="chart-title"><strong>Selected Actors</strong></h6>
                    <b-list-group class="no-padding" v-for="item in selectedActors">
                        <b-list-group-item><small>&#10003;&nbsp;{{item.actor}}</small></b-list-group-item>
                    </b-list-group>
                </b-col>
            </b-row>
            <b-row style="margin-top:20px;">
                <b-col lg="12">
                    <h6 class="chart-title"><strong>Selected Actions for Actors</strong></h6>
                    <b-tabs card vertical>
                        <b-tab v-for="actor in selectedActors" v-bind:key="actor.id"  :title="actor.actor" active>
                            <b-list-group v-for="item in getActions(actor)">
                                <b-list-group-item><small>&#10003;&nbsp;{{item.action}}</small></b-list-group-item>
                            </b-list-group>
                        </b-tab>

                    </b-tabs>
                </b-col>
            </b-row>
        </div>
    </div>
</template>

<script>

    import EventBus from './../../../event-bus';

    export default {
        name: 'Overview',

        components: {
        },

        props: {
            goals:{
                type: Array,
                default: []
            },
            actors:{
                type: Array,
                default: []
            },
            actions:{
                type: Array,
                default: []
            },
            selectedGoals:{
                type: Array,
                default: []
            },
            selectedActors:{
                type: Array,
                default: []
            },
            selectedActions:{
                type: Array,
                default: []

            }
        },
        data() {
            return {

            }
        },

        computed: {

        },

        mounted() {
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

    .list-group-item{
        border: 0px solid rgba(0,0,0,.125) !important;
    }

</style>