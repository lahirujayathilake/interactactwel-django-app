<template>
    <div id="graph" class="card">
        <div class="card-header"><span v-on:click="dismiss" class="close"><font-awesome-icon
                icon="times-circle"/> Close</span>
            <strong>Overview</strong>
        </div>
        <div class="card-body">
            <b-card header="Selected Goals">
                <b-list-group class="no-padding" v-for="item in selectedGoals">
                    <b-list-group-item>{{item.goal}}</b-list-group-item>
                </b-list-group>
            </b-card>

            <b-card header="Selected Actors">
                <b-list-group v-for="item in selectedActors">
                    <b-list-group-item>{{item.actor}}</b-list-group-item>
                </b-list-group>
            </b-card>

            <b-card header="Actions taken by each selected Actor">
            <b-tabs content-class="mt-3">
                <b-tab v-for="actor in selectedActors" v-bind:key="actor.id"  :title="actor.name" active>
                        <b-list-group v-for="item in getActions(actor)">
                            <b-list-group-item>{{item.action}}</b-list-group-item>
                        </b-list-group>
                </b-tab>

            </b-tabs>
            </b-card>
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
            goals:[],
            actors:[],
            actions:[],
            selectedGoals:[],
            selectedActors:[],
            selectedActions:[]

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
