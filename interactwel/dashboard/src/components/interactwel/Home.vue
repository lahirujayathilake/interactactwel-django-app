<template>
    <div>
        <component v-bind:is="component='Header'"></component>
        <b-container fluid class="main">
            <b-container>
                <b-row>
                    <b-col>
                        <b-card class="mb-2"
                                tag="article"
                                style="max-width: 25rem;"
                        >
                            <h4 class="card-title"> Learn</h4>
                            <b-card-text>
                                <p align="justify">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer volutpat mollis dolor id pellentesque. Aliquam lacinia sagittis fringilla.</p>
                                <b-button block>Instructional Videos</b-button>
                                <b-button block>Adaptation Stories</b-button>
                                <b-button block>Documentation</b-button>
                                <b-button block>Support</b-button>
                            </b-card-text>

                        </b-card>
                    </b-col>
                    <b-col>
                        <b-card class="mb-2"
                                tag="article"
                                style="max-width: 25rem;"
                        >
                            <h4 class="card-title"> Plan</h4>
                            <b-card-text>
                                <p align="justify">
                                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer volutpat mollis dolor id pellentesque. Aliquam lacinia sagittis fringilla. Curabitur lorem sapien, consectetur in faucibus vel, imperdiet at nulla.</p>
                                <b-button block>Explore Community Projects</b-button>
                                <b-button block>Visualize Potention Adaptation</b-button>
                                <b-button block>
                                    <router-link to="/Dashboard">Evaluate Adaptation Plans</router-link>
                                </b-button>
                            </b-card-text>

                        </b-card>
                    </b-col>
                    <b-col>
                        <b-card class="mb-2"
                                tag="article"
                                style="max-width: 25rem;"
                        >
                            <h4 class="card-title"> Act</h4>
                            <b-card-text>
                                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec tristique nisi ligula, sit amet sodales leo porta quis. Praesent nibh felis, finibus non venenatis vel, facilisis eget ante.</p>
                                <b-button block>Share Plans with community</b-button>
                                <b-button block>Create/ Edit plans</b-button>
                                <b-button block>Adopt Plans</b-button>
                            </b-card-text>

                        </b-card>
                    </b-col>
                </b-row>
            </b-container>
        </b-container>
        <component v-bind:is="component='Footer'"></component>
    </div>
</template>

<script>
    import EventBus from './../../event-bus';
    import Header from './Header.vue';
    import Footer from './Footer.vue';

    export default {
        components: {
            Header, Footer
        },
        name: 'Home',

        data() {
            return {}
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
</style>

