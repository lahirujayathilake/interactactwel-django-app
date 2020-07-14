<template>
    <div>
        <component v-bind:is="component='Header'"></component>
        <b-container fluid class="main">
            <b-row>
                <b-col>
                    <h3>My Saved Plans</h3>
                </b-col>
            </b-row>
            <b-row class="mt-3">
                <b-col>
                    <b-card no-body>
                        <b-tabs pills card vertical>
                            <b-tab title="Plan 1" active><b-card-text>
                                <b-row>
                                <b-col lg="6">

                                </b-col>
                                <b-col lg="6">

                                </b-col>
                                </b-row>
                            </b-card-text></b-tab>
                            <b-tab title="Plan 2">
                                <b-row>
                                    <b-col lg="6">

                                    </b-col>
                                    <b-col lg="6">

                                    </b-col>
                                </b-row><b-card-text>

                            </b-card-text></b-tab>
                            <b-tab title="Plan 3"><b-card-text>
                                <b-row>
                                    <b-col lg="6">

                                    </b-col>
                                    <b-col lg="6">

                                    </b-col>
                                </b-row>
                            </b-card-text></b-tab>
                        </b-tabs>
                    </b-card>
                </b-col>
            </b-row>
        </b-container>
        <component v-bind:is="component='Footer'"></component>
    </div>
</template>


<script>
    import Header from './../Header.vue';
    import Footer from './../Footer.vue';

    export default {
        name: 'MyPlans',
        components: {
            Header, Footer
        },
        props: {
            msg: String
        }
    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    .main {
        background-color: #efefef;
        padding: 1rem 2rem;
        min-height: 90vh;
        text-align: left;
    }

    a {
        color: #42b983;
    }
</style>
