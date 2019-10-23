<template>
    <b-card-group>
        <b-card footer-tag="footer">
            <div class="step-header" slot="header">My Projects
            </div>
            <b-card-text>
                <div class="map-wrapper">
                <component v-bind:is="component='LeafletMap'"></component>
                </div>
                <!--<b-tabs pills vertical nav-wrapper-class="w-25">
                    <b-tab title="Umatilla" active>

                        <b-card footer-tag="footer" class="p-0">
                            <div class="step-header" slot="header">Umatilla
                                <em slot="header">

                                    <b-button size="sm">Share</b-button>
                                    <b-button class="mr-2" size="sm">Suggest to a friend</b-button>
                                    <b-button class="mr-2"  size="sm"><router-link v-bind:to="'/visualization/' + this.projectId">Visualize</router-link></b-button>
                                </em>
                            </div>
                                <div class="map-wrapper">
                                    <component v-bind:is="component='LeafletMap'"></component>
                            </div>
                        </b-card>
                    </b-tab>
                    <b-tab title="Texas">
                        <b-card-text>Texas</b-card-text>
                    </b-tab>
                    <b-tab title="Colarado">
                        <b-card-text>Colarado</b-card-text>
                    </b-tab>
                </b-tabs>-->
            </b-card-text>
        </b-card>
    </b-card-group>
</template>

<script>
    import Header from './../Header.vue';
    import Footer from './../Footer.vue';
    import LeafletMap from './LeafletMap.vue'

    export default {
        components: {
            Header, Footer, LeafletMap
        },
        name: 'MyProjects',

        data() {
            return {
                projectId: 'project1',
            }
        },

        mounted() {
        },


        methods: {}

    }

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
    .main {
        background-color: #efefef;
        padding: 1rem;
        min-height: 90vh;
    }

    .map-wrapper {
        height: 400px;
    }

    .widget {
        background-color: #f7f7f7;
        padding: 1rem;
        border: 1px solid #efefef;
        border-radius: 5px;
        margin-bottom: 10px;
    }

    .widget-title {
        font-size: 16px;
        font-weight: 700;
    }
</style>

