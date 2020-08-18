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
    import L from "leaflet";
    import {LMap, LTileLayer, LMarker, LGeoJson, LControlLayers, LControlScale, LLayerGroup, LPopup, LControlZoom} from 'vue2-leaflet';
    import ReservoirList from './../../../../public/static/reservoirs_list.json';
    import ReservoirDataJson from "./../../../../public/static/reservoirs_data.json";
    import PopupContentReservoirs from "./../projects/popup/PopupContent_Reservoirs";


    export default {
        components: {
            'l-map': LMap,
            'l-tile-layer': LTileLayer,
            'l-marker': LMarker,
            'l-control-layers': LControlLayers,
            'l-layer-group': LLayerGroup,
            'l-control-scale': LControlScale,
            'l-popup': LPopup,
            'l-control-zoom': LControlZoom,
            'popup-content-rs': PopupContentReservoirs,
        },
        name: "SavedPlans",

        data() {
            return {
                projects: [],
                projectsUsers:[]
            };
        },

        async mounted() {
            const {utils} = AiravataAPI;
            let user = await this.getLoggedInUser();

            utils.FetchUtils.get("/interactwel/api/projectusers/")
                .then(projectsUsers => {
                    this.projectsUsers = projectsUsers.filter(projectUser => {
                        return projectUser.user_id === user.id && projectUser.status === "Active";
                    })
                    utils.FetchUtils.get("/interactwel/api/projects/")
                        .then(projects => {
                            this.projects = projects.filter(project => {
                                return this.projectsUsers.findIndex(projectUser => {
                                    return projectUser.project_id === project.project_id;
                                }) !== -1 ? true : false;
                            });
                            //set the route to first project
                            if (projects.length > 0){
                                this.$router.push('/plans/saved-plans/'+ projects[0].project_id);
                            }
                        })
                        .catch(error => {
                            alert("Could not get the projects list. API error! " + error);
                        });

                })
                .catch(error => {
                    alert("Could not get the projects list. API error! " + error);
                });


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
