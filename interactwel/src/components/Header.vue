<template>
    <div>
        <div class="top-fixed-nav">
            <b-navbar style="background-color: #263238!important;" toggleable="md" type="dark" variant="secondary">
                <b-navbar-toggle target="nav_collapse"></b-navbar-toggle>
                <a class="navbar-brand" href="#">
                    <img src="../assets/InterACTWEL_logo.svg" width="140" height="35"
                         class="d-inline-block align-top" alt=""> Dashboard
                </a>
                <b-collapse id="nav-collapse" is-nav>
                    <b-navbar-nav>
                        <b-nav-item href="#"><router-link to="/dashboard">Home</router-link></b-nav-item>
                        <b-nav-item href="#"><router-link to="/community/events">Community</router-link></b-nav-item>
                        <b-nav-item href="#"><router-link to="/projects/my-projects">Project</router-link></b-nav-item>
                        <b-nav-item href="#" disabled>Plans</b-nav-item>
                        <b-nav-item href="#">Profile</b-nav-item>
                    </b-navbar-nav>
                </b-collapse>
                <b-collapse is-nav id="nav_collapse">
                    <!-- Right aligned nav items -->
                    <b-navbar-nav class="ml-auto">
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
    </div>
</template>

<script>

    export default {
        components: {

        },
        name: 'Header',

        data() {
            return {
            }
        },

        mounted() {
        },


        methods: {

        }

    }

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
    .top-fixed-nav{
        border-top: 4px solid #ff7853 !important;
    }
.top-fixed-nav a, button a{
    color: #fff;
}
</style>

