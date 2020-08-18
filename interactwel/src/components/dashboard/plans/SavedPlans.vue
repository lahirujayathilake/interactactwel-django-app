<template>
    <div>
        <b-card no-body>
                <b-tabs pills card vertical nav-wrapper-class="w-25">
                <b-tab
                        v-for="project in projects"
                        :title="project.name"
                        v-on:click="projectSelected(project.project_id)">
                    <!--<router-view></router-view>-->
                        <b-card-body class="no-padding">
                            <b-row class="mb-2">
                                <b-col lg="9"><h5>{{project.name}}</h5></b-col>
                           <b-col lg="3"><b-button class="float-right" size="sm" variant="success">Visualize Selected Plans</b-button></b-col>
                            </b-row>
                            <router-view></router-view>
                        </b-card-body>
                </b-tab>
            </b-tabs>
        </b-card>
    </div>
</template>


<script>

    export default {
        components: {
        },
        name: "SavedPlans",

        data() {
            return {
                projects: [],
                projectsUsers:[]
            };
        },

        async mounted() {

            this.projects = await this.getProjectsListOfLoggedInUser();

            if (this.projects.length > 0){
                this.$router.push('/plans/saved-plans/'+ projects[0].project_id);
            }


        },

        methods: {
            projectSelected: function (projectId) {
                this.$router.push('/plans/saved-plans/'+ projectId);

            }

        },
        computed: {}
    };
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>

</style>
