<template>
    <div>
        <div class="top-fixed-nav">
            <b-navbar style="background-color: #263238!important;" toggleable="md" type="dark" variant="secondary">
                <b-navbar-toggle target="nav_collapse"></b-navbar-toggle>
                <a class="navbar-brand" href="#">
                    <img src="../../assets/InterACTWEL_logo.svg" width="140" height="35" class="d-inline-block align-top" alt="">
                </a>
                <b-collapse is-nav id="nav_collapse">
                    <b-navbar-nav>
                        <b-nav-item class="project-title" href="#"><strong>Project:</strong></b-nav-item>
                        <b-nav-item class="project-title" href="#" disabled><strong>Umatilla Region Adapts To Changes In Allocation Of Water For irrigation</strong></b-nav-item>
                    </b-navbar-nav>
                    <!-- Right aligned nav items -->
                    <b-navbar-nav class="ml-auto">
                        <b-button v-show="!startButtonVisibility" v-on:click="start" variant="success"
                                  class="my-2 my-sm-0" type="submit"><strong>Start Here</strong>
                        </b-button>
                        <b-button v-show="startButtonVisibility" v-on:click="exit" variant="danger"
                                  class="my-2 my-sm-0" type="submit"><strong> Exit </strong>
                        </b-button>

                       <!-- <b-nav-item-dropdown text="Settings" right>
                            <b-dropdown-item href="#">EN</b-dropdown-item>
                            <b-dropdown-item href="#">ES</b-dropdown-item>
                            <b-dropdown-item href="#">RU</b-dropdown-item>
                            <b-dropdown-item href="#">FA</b-dropdown-item>
                        </b-nav-item-dropdown>-->

                        <b-nav-item-dropdown right>
                            <!-- Using button-content slot -->
                            <template slot="button-content">
                                <em>Nick</em>
                            </template>
                            <b-dropdown-item href="#">Profile</b-dropdown-item>
                            <b-dropdown-item href="#">Signout</b-dropdown-item>
                        </b-nav-item-dropdown>
                    </b-navbar-nav>
                </b-collapse>
            </b-navbar>
        </div>
        <component v-show="!progressBarVisibility" v-on:next-click="addActiveClass" :fromparent="fromparent"
                   v-bind:is="component=progressbarComponent"></component>
        <component v-bind:is="component='container'"></component>
    </div>
</template>

<script>
    import ProgressBar from './progressBar/ProgressBar.vue'
    import Container from './container.vue'

    import EventBus from './../../event-bus';

    export default {
        components: {
            'progress-bar': ProgressBar,
            'container': Container,

        },
        name: 'Dashboard',


        data() {
            return {
                progressbarComponent: null,
                startButtonVisibility: false,
                progressBarVisibility: true,
                component: null,
            }
        },

        mounted() {
            //this.showSidebar()
        },


        methods: {

            start: function () {
                this.progressbarComponent = 'progress-bar',
                    this.startButtonVisibility = true
                this.progressBarVisibility = false
                this.startWizard()

            },

            startWizard() {
                EventBus.$emit('START_WIZARD');
            },

            exit() {
                // `this` inside methods points to the Vue instance
                alert('You are going to quit the wizard!');
                // `event` is the native DOM event
                // if (event) {
                //    alert(event.target.tagName)
                //}
                return {
                    //component: 'progress-bar',
                }

            },

            progressFinished() {
                alert('finished!');
            },

            afterWizardFinished() {
                this.sidebarLeftVisibility = false,
                    this.sidebarRightVisibility = false,
                    this.progressBarVisibility = false
                this.chartsVisibility = false
            },

            showChart() {
                alert('add active class!');
            },

            addActiveClass() {
                alert('add active class!');
                //this.startButtonVisibility = true
            }
        }

    }

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>

    .bg-secondary {
        background-color: #263238 !important;
    }

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
        background-color: #37474F;
    }

    #main > nav {
        order: -1;
    }

    #main > aside {
        flex: 0 0 400px;
        height: calc(92vh - 20px);
        overflow: auto;
        padding: 1rem;
        background-color: #FFF;
    }

    #sidebar-left a {
        color: #fff;
    }

    .project-title a{
        font-size: 18px;
        color: rgba(255, 255, 255, 0.78) !important;
    }

</style>

