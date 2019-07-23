<template>
    <div id="graph" class="card">
        <div class="card-header"><span v-on:click="dismiss" class="close"><font-awesome-icon
                icon="times-circle"/> Close</span>
            <strong>Overview</strong>
        </div>
        <div class="card-body">
            <b-row>
                <b-col lg="6">
                    <h6>Selected Goals</h6>
                    <b-list-group class="no-padding" v-for="item in selectedGoals">
                        <b-list-group-item><small>{{item.goal}}</small></b-list-group-item>
                    </b-list-group>
                </b-col>
                <b-col lg="6">
                    <h6>Selected Actors</h6>
                    <b-list-group class="no-padding" v-for="item in selectedGoals">
                        <b-list-group-item><small>{{item.goal}}</small></b-list-group-item>
                    </b-list-group>
                </b-col>
            </b-row>
            <b-row style="margin-top:20px;">
                <b-col lg="12">
                    <h6>Selected Actions by each actor</h6>
                    <b-tabs>
                        <b-tab v-for="actor in selectedActors" v-bind:key="actor.id"  :title="actor.name" active>
                            <b-list-group v-for="item in getActions(actor)">
                                <b-list-group-item><small>{{item.action}}</small></b-list-group-item>
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
