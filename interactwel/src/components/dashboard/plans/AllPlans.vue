<template>
    <div>
        <component v-bind:is="component='Header'"></component>
        <b-container fluid class="main">
            <b-row>
                <b-col>
                    <h3 class="mb-3">Plans</h3>
                </b-col>
            </b-row>
            <b-row>
                <b-col lg="12">
                    <b-card v-if="projects" no-body>
                        <b-tabs vertical nav-wrapper-class="w-25">
                            <b-tab
                                    v-for="project in projects"
                                    :title="project.name"
                                    v-on:click="projectSelected(project.project_id)">
                                <!--<router-view></router-view>-->
                                <b-card-body class="no-padding">
                                    <div class="d-lg-flex d-sm-block">
                                        <h5 class="mr-auto">{{project.name}}</h5>
                                        <b-button size="sm" variant="success" @click="$router.push('/adaptation-plans/'+ project.project_id)">Generate New Plan</b-button>
                                        <b-button size="sm" variant="outline-success" @click="$router.push('/visualize/'+ project.project_id)">View Project Data</b-button>
                                    </div>
                                    <b-card v-if="false">
                                        <b-card-body title="You don't have access to any saved plans">
                                            <b-card-text>
                                                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque luctus purus sit amet massa hendrerit semper at eu dui.
                                            </b-card-text>
                                        </b-card-body>
                                    </b-card>
                                    <div class="mt-3">
                                        <b-tabs>
                                            <b-tab title="Plan 1">
                                                <div class="d-lg-flex d-sm-block py-3">
                                                    <b-button size="sm" variant="outline-success">Visualize this Plan
                                                    </b-button>
                                                </div>
                                                <div class="d-lg-flex d-sm-block">
                                                    <b-list-group>
                                                        <b-list-group-item class="flex-column align-items-start">
                                                            <div class="d-flex w-100 justify-content-between">
                                                                <h5 class="mb-1">Goals</h5>
                                                                <small>3 Goals selected</small>
                                                            </div>
                                                            <small>
                                                                <ul class="no-padding">
                                                                    <li>Improve surface water quality</li>
                                                                    <li>Increase recharge to shallow aquifer</li>
                                                                    <li>Increase agriculture productivity</li>
                                                                    <li>Improve ecological habitat</li>
                                                                </ul>
                                                            </small>
                                                        </b-list-group-item>

                                                        <b-list-group-item class="flex-column align-items-start">
                                                            <div class="d-flex w-100 justify-content-between">
                                                                <h5 class="mb-1">Actors</h5>
                                                                <small class="text-muted">2 Actors Selected</small>
                                                            </div>
                                                            <small>
                                                                <ul class="no-padding">
                                                                    <li>Farmer with Columbia river water rights</li>
                                                                    <li>Farmer with other surface water rights</li>
                                                                    <li>Farmer with groundwater rights</li>
                                                                </ul>
                                                            </small>
                                                        </b-list-group-item>

                                                        <b-list-group-item class="flex-column align-items-start">
                                                            <div class="d-flex w-100 justify-content-between">
                                                                <h5 class="mb-1">Actions</h5></div>

                                                            <small>
                                                                <ul class="no-padding">
                                                                    <li>Farmer with Columbia river water rights
                                                                        <ul>
                                                                            <li>
                                                                                action 1
                                                                            </li>
                                                                            <li>
                                                                                action 2
                                                                            </li>
                                                                            <li>
                                                                                action 1
                                                                            </li>
                                                                        </ul>
                                                                    </li>
                                                                    <li>Farmer with other surface water rights
                                                                        <ul>
                                                                            <li>
                                                                                action 1
                                                                            </li>
                                                                        </ul>
                                                                    </li>
                                                                    <li>Farmer with groundwater rights</li>
                                                                </ul>
                                                            </small>
                                                        </b-list-group-item>
                                                    </b-list-group>
                                                    <div class="d-block mx-3">
                                                        <b-card>graph</b-card>
                                                    </div>
                                                </div>
                                                <div class="d-block my-3">
                                                    <b-card>feedback</b-card>
                                                </div>
                                            </b-tab>
                                        </b-tabs>
                                    </div>
                                </b-card-body>
                            </b-tab>
                        </b-tabs>
                    </b-card>
                </b-col>
            </b-row>
        </b-container>
        <component v-bind:is="component='Footer'"></component>
    </div>
</template>

<script>

    import Header from './../../Header.vue';
    import Footer from './../../Footer.vue';

    export default {
        components: {},
        name: "AllPlans",
        components: {
            Header, Footer
        },

        data() {
            return {
                projects: [],
                projectsUsers: []
            };
        },

        async mounted() {
            this.projects = await this.getProjectsListOfLoggedInUser();
        },

        methods: {},
        computed: {}
    };
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
    .main {
        background-color: #efefef;
        padding: 1rem 2rem;
        min-height: 90vh;
        text-align: left;
    }

</style>
