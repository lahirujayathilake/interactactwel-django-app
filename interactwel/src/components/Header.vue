<template>
    <div>
        <div class="top-fixed-nav">
            <b-navbar style="padding: 0 1rem; background-color: #263238!important;" toggleable="md" type="dark" variant="secondary">
                <b-navbar-toggle target="nav_collapse"></b-navbar-toggle>
                <!--<a class="navbar-brand" href="#">
                    <img src="../assets/InterACTWEL_logo.svg" width="140" height="35"
                         class="d-inline-block align-top" alt="">
                </a>-->
                <b-collapse id="nav-collapse" is-nav>
                    <b-navbar-nav>
                        <b-nav-item href="#"><router-link to="/dashboard">Home</router-link></b-nav-item>
                        <b-nav-item href="#"><router-link to="/community/events">Community</router-link></b-nav-item>
                        <b-nav-item href="#"><router-link to="/projects/my-projects">Projects</router-link></b-nav-item>
                        <b-nav-item href="#"><router-link to="/plans/new-plan">Plans</router-link></b-nav-item>
                        <b-nav-item href="#">Profile</b-nav-item>
                    </b-navbar-nav>
                </b-collapse>
                <b-collapse is-nav id="nav_collapse">
                    <b-navbar-nav class="ml-auto" type="dark" variant="secondary">
                        <b-nav-item v-if="!loggedInUser.username" href="/auth/login">Login</b-nav-item>
                        <b-nav-item-dropdown right v-if="loggedInUser.username">
                            <!-- Using button-content slot -->
                            <template slot="button-content">
                                <i class="fa fa-user"></i> <em> {{loggedInUser.username}}</em>
                            </template>
                            <b-dropdown-item href="/auth/logout">Signout</b-dropdown-item>
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

                site_url: "http://localhost:8000",

                loggedInUser: {
                    id: -1,
                    username: "",
                    first_name: "",
                    last_name: "",
                    email: "",
                    phone: "",
                    organization: ""
                }
            }
        },

        mounted() {
            const SessionData = AiravataPortalSessionData;
            this.loggedInUser.username = SessionData.username;
        },


        methods: {

        }

    }

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
    .top-fixed-nav{
        /*border-top: 4px solid #ff7853 !important;*/
    }
.top-fixed-nav a, button a{
    color: #fff;
}
</style>

