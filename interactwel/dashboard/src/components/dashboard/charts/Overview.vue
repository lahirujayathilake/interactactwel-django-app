<template>
    <div id="graph" class="card">
        <div class="card-header"><span v-on:click="dismiss" class="close"><font-awesome-icon
                icon="times-circle"/> Close</span>
            <strong>Overview</strong>
        </div>
        <div class="card-body">
            <b-table bordered hover small :items="selectedGoals"></b-table>
            <b-table bordered hover small :items="selectedActors"></b-table>

            <b-tabs content-class="mt-3">
                <b-tab v-for="actor in selectedActors" v-bind:key="actor.id"  :title="actor.name" active>
                    <b-table bordered hover small :items="getActions(actor)"></b-table>
                </b-tab>

            </b-tabs>
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
