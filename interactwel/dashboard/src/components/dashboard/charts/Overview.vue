<template>
    <div id="graph" class="card">
        <div class="card-header"><span v-on:click="dismiss" class="close"><font-awesome-icon
                icon="times-circle"/> Close</span>
            <strong>Overview</strong>
        </div>
        <div class="card-body">
            <b-table bordered hover small :items="goals"></b-table>
            <b-table bordered hover small :items="actors"></b-table>
            <b-table bordered hover small :items="actions"></b-table>
        </div>
    </div>
</template>

<script>

    import EventBus from './../../../event-bus';

    export default {
        name: 'Overview',

        components: {
        },

        data() {
            return {
                goals: [
                    {
                        id: "0",
                        goal: 'Improve surface water quality'
                    },
                    {
                        id: "1",
                        goal: 'Increase recharge to shallow aquifer',
                    },
                    {
                        id: "2",
                        goal: 'Increase agriculture productivity',
                    },

                ],

                actions: [
                    {
                        id: 0,
                        action: 'No changes to current water right allocations'
                    },
                    {
                        id: 1,

                        action: 'Increase the volume of non-Columbia surface water'
                    },
                    {
                        id: 6,
                        action: 'Decrease the volume of Columbia surface water'
                    },
                ],

                actors: [
                    {
                        id: 0,
                        actor: 'Farmer with Columbia river water rights',
                    },
                    {
                        id: 1,
                        actor: 'Farmer with other surface water rights',
                    },
                    {
                        id: 2,
                        actor: 'Farmer with groundwater rights',
                    }
                ],
            }
        },

        props: {

        },


        computed: {
        },

        mounted() {
        },

        methods: {
            dismiss() {
                EventBus.$emit('CLOSE');
            },
        }
        
    }
</script>


<!-- Add "scoped" attribute to limit CSS to this component only -->
