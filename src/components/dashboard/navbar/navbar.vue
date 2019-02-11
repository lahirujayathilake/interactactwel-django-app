<template>
    <div>
        <div class="top-fixed-nav" v-model="navbar">
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
                        <b-button v-show="!startButtonVisibility" v-on:click="start" variant="primary" class="my-2 my-sm-0" type="submit">Start Viz Builder</b-button>
                        <b-button v-show="startButtonVisibility" v-on:click="exit" variant="primary" class="my-2 my-sm-0" type="submit">Exit</b-button>

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
        <component v-bind:is="progressbarComponent"></component>
    </div>

</template>

<script>
    import ProgressBar from '../progressBar/ProgressBar.vue'

    export default{

        name: 'Navbar',
        components: {
            'progress-bar': ProgressBar
        },

        /*data() {
            return {
                startButtonVisibility: true,
                component: null
            }
        },

        methods: {

            start: function () {
                this.progressbarComponent = 'progress-bar'
                this.startButtonVisibility = false

            },

            exit: function (event) {
                // `this` inside methods points to the Vue instance
                alert('Hello ' + this.name + '!');
                // `event` is the native DOM event
                // if (event) {
                //    alert(event.target.tagName)
                //}
                return {
                    component: 'progress-bar',
                }

            }
        }*/
    }


</script>

<style>

</style>