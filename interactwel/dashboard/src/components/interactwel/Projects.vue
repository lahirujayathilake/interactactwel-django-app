<template>
    <div>
        <component v-bind:is="component='Header'"></component>
        <b-container fluid class="main">
                <b-breadcrumb :items="breadcrumb"></b-breadcrumb>
                <b-row>
                    <b-col lg="2">
                        <b-list-group>
                            <b-list-group-item><router-link to="/projects/my-projects">My Projects</router-link></b-list-group-item>
                            <b-list-group-item><router-link to="/projects/create-project">Create New project</router-link></b-list-group-item>
                            <b-list-group-item><router-link to="/projects/suggested-projects">Projects Suggested</router-link></b-list-group-item>
                            <b-list-group-item><router-link to="/projects/explore-projects">Explore Other Projects</router-link></b-list-group-item>
                        </b-list-group>
                    </b-col>
                    <b-col lg="10">
                            <router-view></router-view>
                    </b-col>
                </b-row>
        </b-container>
        <component v-bind:is="component='Footer'"></component>
    </div>
</template>

<script>
    import EventBus from './../../event-bus';
    import Header from './Header.vue';
    import Footer from './Footer.vue';
    import CreateProject from './project/CreateProject.vue';
    import LeafletMap from './../dashboard/map/LeafletMap.vue'

    export default {
        components: {
            Header, Footer, LeafletMap, CreateProject
        },
        name: 'Projects',

        data() {
            return {
                breadcrumb: [
                    {
                        text: 'Home',
                        to: { name: 'Home' }
                    },
                    {
                        text: 'Project',
                        to: { name: 'Project' }
                    },
                    {
                        text: 'Create New Project',
                        to: { name: 'CreateProject' }
                    }
                ]
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
        -webkit-box-flex: 1;
        -ms-flex: 1;
        flex: 1;
        min-height: calc(60vh);
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

