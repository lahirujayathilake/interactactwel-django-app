<template>
    <div>
        <component v-bind:is="component='Header'"></component>
        <b-container fluid class="main">
            <b-container>
                <b-row>
                    <b-col style="padding-top: 2rem;">
                        <b-card class="mb-2"
                                tag="article"
                                style="max-width: 25rem; height: 17rem;"
                        >
                            <h4 class="card-title"> Learn</h4>
                            <b-card-text>
                                <!--<p align="justify">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer volutpat mollis dolor id pellentesque. Aliquam lacinia sagittis fringilla.</p> -->
                                <b-button block><router-link to="/learn/videos/1">Instructional Videos</router-link></b-button>
                                <b-button block><router-link to="/learn/stories">Adaptation Stories</router-link></b-button>
                                <b-button block><router-link to="/learn/docs">Documentation</router-link></b-button>
                                <b-button block><router-link to="/learn/support">Support</router-link></b-button>
                            </b-card-text>

                        </b-card>
                    </b-col>
                    <b-col style="padding-top: 2rem;">
                        <b-card class="mb-2"
                                tag="article"
                                style="max-width: 25rem; height: 17rem;"
                        >
                            <h4 class="card-title"> Plan</h4>
                            <b-card-text style="padding-top: 1rem;">
                                <!-- <p align="justify">
                                     Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer volutpat mollis dolor id pellentesque. Aliquam lacinia sagittis fringilla. Curabitur lorem sapien, consectetur in faucibus vel, imperdiet at nulla.</p> -->
                                <b-button block><router-link to="/projects/explore-projects">Explore Community Projects</router-link></b-button>
                                <b-button block>Visualize Potential Adaptation Plans</b-button>
                                <b-button block>
                                    <router-link to="/Dashboard">Evaluate Adaptation Plans</router-link>
                                </b-button>
                            </b-card-text>

                        </b-card>
                    </b-col>
                    <b-col style="padding-top: 2rem;">
                        <b-card class="mb-2"
                                tag="article"
                                style="max-width: 25rem; height: 17rem;"
                        >
                            <h4 class="card-title"> Act</h4>
                            <b-card-text style="padding-top: 1rem;">
                                <!--<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec tristique nisi ligula, sit amet sodales leo porta quis. Praesent nibh felis, finibus non venenatis vel, facilisis eget ante.</p>-->
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
    import Header from './Header.vue';
    import Footer from './Footer.vue';

    export default {
        name: 'Dashboard',
        components: {
            Header,Footer
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
        padding: 3rem 1rem;
        min-height: 90vh;
        text-align: center;
    }

     .card-title {
         font-size: 25px;
         font-weight: bold;
         color: #5e6b7e;
         border-bottom: 2px solid #28a645;
         padding-bottom: 5px;
     }

    .card-text {
        font-size: 13px;
        color: #5e6b7e;
    }
</style>
