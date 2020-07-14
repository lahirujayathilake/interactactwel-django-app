<template>
    <div>
        <component v-bind:is="component='Header'"></component>
        <b-container fluid class="main">
            <b-row>
                <b-col>
                    <h3>Learn</h3>
                </b-col>
                <!--<b-col align="right">
                    <b-button>Create New Project</b-button>
                </b-col>-->
            </b-row>
            <b-row>
                <b-col>
                    <b-nav tabs justified>
                        <b-nav-item :active="$route.path === '/learn/videos/1'"><router-link to="/learn/videos/1">Instructional Videos</router-link></b-nav-item>
                        <b-nav-item :active="$route.path === '/learn/docs'"><router-link to="/learn/docs">Documentation</router-link></b-nav-item>
                        <b-nav-item :active="$route.path === '/learn/stories'"><router-link to="/learn/stories">Adaptation Stories</router-link></b-nav-item>
                        <b-nav-item :active="$route.path === '/learn/support'"><router-link to="/learn/support">Support</router-link></b-nav-item>
                    </b-nav>
                </b-col>
            </b-row>
            <b-row>
                <b-col class="mt-4">
                    <router-view></router-view>
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
        name: 'Learn',
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
        /*background-color: #efefef;*/
        padding: 1rem;
        min-height: 90vh;
        max-width: 1400px;
        text-align: left;
    }

    a {
        color: #42b983;
    }
</style>
