<template>
    <div>
        <div class="top-fixed-nav">
            <b-navbar toggleable="md" type="dark" variant="success">
                <b-navbar-toggle target="nav_collapse"></b-navbar-toggle>
                <b-navbar-brand href="#">InterActwell</b-navbar-brand>
                <b-collapse is-nav id="nav_collapse">
                    <b-navbar-nav>
                        <b-nav-item href="#">Project</b-nav-item>
                        <b-nav-item href="#" disabled>Umatilla Region Adapts to New Water Allocation</b-nav-item>
                    </b-navbar-nav>
                    <!-- Right aligned nav items -->
                    <b-navbar-nav class="ml-auto">
                        <b-button v-show="!startButtonVisibility" v-on:click="start" variant="warning"
                                  class="my-2 my-sm-0" type="submit">Start Here
                        </b-button>
                        <b-button v-show="startButtonVisibility" v-on:click="exit" variant="danger"
                                  class="my-2 my-sm-0" type="submit">Exit
                        </b-button>

                        <b-nav-item-dropdown text="Settings" right>
                            <b-dropdown-item href="#">EN</b-dropdown-item>
                            <b-dropdown-item href="#">ES</b-dropdown-item>
                            <b-dropdown-item href="#">RU</b-dropdown-item>
                            <b-dropdown-item href="#">FA</b-dropdown-item>
                        </b-nav-item-dropdown>

                        <b-nav-item-dropdown right>
                            <!-- Using button-content slot -->
                            <template slot="button-content">
                                <em>User</em>
                            </template>
                            <b-dropdown-item href="#">Profile</b-dropdown-item>
                            <b-dropdown-item href="#">Signout</b-dropdown-item>
                        </b-nav-item-dropdown>
                    </b-navbar-nav>
                </b-collapse>
            </b-navbar>
        </div>
        <!-- <component v-bind:is="progressbarComponent"></component>-->
        <div id="main">
            <nav v-show id="sidebar-left">
                <component v-bind:is="component"></component>
            </nav>
            <article id="map">
                <component v-bind:is="step1Component"></component>
                <leaflet-map></leaflet-map>
            </article>
            <aside v-show id="sidebar-right">
                <component v-bind:is="component"></component>
            </aside>
        </div>
    </div>
</template>

<script>

    import Sidebar from './sidebar/Sidebar.vue'
    import Feedback from './feedback/feedback.vue'
    import Regions from './regions/Regions.vue'
    import ProgressBar from './progressBar/ProgressBar.vue'
    import Step1Content from '../steps/Step1Content.vue'
    import LeafletMap from './map/LeafletMap.vue'

    export default {
        components: {
            'progress-bar': ProgressBar,
            'regions': Regions,
            'feedback': Feedback,
            'sidebar': Sidebar,
            'step1content': Step1Content,
            'leafletMap' : LeafletMap,
        },
        name: 'Dashboard',



        data() {
            return {
                step1Component: null,
                progressbarComponent: null,
                startButtonVisibility: false,
                component: null,
            }
        },


        methods: {

            start: function () {
                this.progressbarComponent = 'progress-bar',
                    this.step1Component = 'step1content',
                    this.startButtonVisibility = true

            },

            exit: function (event) {
                // `this` inside methods points to the Vue instance
                alert('You are going to quit the wizard!');
                // `event` is the native DOM event
                // if (event) {
                //    alert(event.target.tagName)
                //}
                return {
                    //component: 'progress-bar',
                }

            }
        }

    }

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>


    #main {
        display: flex;
        min-height: calc(100vh - 40vh);
    }

    #main > article {
        flex: 1;
        height: calc(92vh - 20px);
    }

    #main > nav {
        flex: 0 0 auto;
        min-width: 200px;
        height: calc(92vh - 20px);
        overflow: auto;
        background-color: #f2f3f5;
    }

    #main > nav {
        order: -1;
    }

    #main > aside {
        flex: 0 0 400px;
        height: calc(92vh - 20px);
        overflow: auto;
        padding: 1rem;
        background-color: #d6edfd;
    }

</style>
