<template>
    <div>
        <component v-bind:is="component='Header'"></component>
        <b-container fluid class="main">
            <b-row>
                <b-col lg="10">
                    <h3 class="mb-3">Projects</h3>
                    <p>Projects in the tabs below include the community adaptation projects that you are a member of (<strong class="text-success">My Projects</strong>), projects that you have been invited
                        to participate in (<strong class="text-success">Invited Projects</strong>), and the other ongoing community adaptation projects globally that are using InterACTWEL (<strong class="text-success">Explore Projects</strong>).
                        If you are an administrator, you will also be able to Create New Project for your community, and invite InterACTWEL members to join your community project via Assign Projects.</p>
                </b-col>
                <!--<b-col align="right">
                    <b-button>Create New Project</b-button>
                </b-col>-->
            </b-row>

            <b-row>
                <b-col>
                    <b-tabs nav-wrapper-class="project-tabs">
                        <b-tab
                            :active="$route.path === '/projects/my-projects'"
                            title="My Projects" v-on:click='loadTabContent("/projects/my-projects")'>
                        </b-tab>
                        <b-tab
                            :active="$route.path === '/projects/suggested-projects'"
                            title="Invited Projects" v-on:click='loadTabContent("/projects/suggested-projects")'>
                        </b-tab>
                        <b-tab
                            :active="$route.path === '/projects/explore-projects'"
                            title="Explore Projects" v-on:click='loadTabContent("/projects/explore-projects")'>
                        </b-tab>
                        <b-tab
                            v-if="this.userRoleNames.includes('Global Admin') || this.userRoleNames.includes('Local Admin')"
                            :active="$route.path === '/projects/create-project'"
                            title="Create New Project" v-on:click='loadTabContent("/projects/create-project")'>
                        </b-tab>
                        <b-tab
                            v-if="this.userRoleNames.includes('Global Admin') || this.userRoleNames.includes('Local Admin')"
                            :active="$route.path === '/projects/assign-projects'"
                            title="Assign Projects"
                            v-on:click='loadTabContent("/projects/assign-projects")'>
                        </b-tab>
                    </b-tabs>
                </b-col>
            </b-row>
            <b-row>
                <b-col>
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
        name: 'Dashboard',
        components: {
            Header, Footer
        },
        props: {
            msg: String
        },

        data(){
            return{
                auth: null,
                isActive : true,
                currentPage : null,
                activeClass : 'active',
                userRoleNames: [],
            }
        },

        async mounted(){
            const SessionData = AiravataPortalSessionData;
            this.auth = SessionData.username;
            this.currentPage = this.$route.name
            const userRoles = await this.getUserRoles();
            this.userRoleNames = userRoles.map(role=> role.role_name);
        },

        computed: {
            currentRoute(){
                return this.$route.path;
            }
        },

        methods: {
            loadTabContent(path) {
                this.$router.push(path);
            }
        }
    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    .main {
        background-color: #efefef;
        padding: 1rem 2rem;
        min-height: 90vh;
        text-align: left;
    }
    .project-tabs ul li a{
        color: #2c3e50;
    }
    .project-tabs ul li a:hover{
        color: #28a745;
    }
    .project-tabs ul li a.active {
        font-weight: bold;
        border-top:2px solid #28a745 !important;
    }
</style>
