<template>
    <div>
        <b-card no-body>
            <b-tabs pills card vertical nav-wrapper-class="w-25">
                <b-tab title="My Projects">
                    <div class="card map-container">
                        <l-map :zoom="zoom" :center="center">
                            <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>
                            <l-marker :lat-lng="marker"></l-marker>
                        </l-map>
                    </div>
                </b-tab>
                <b-tab v-for="projectUser in projectsUsers" :title="'Project Id : ' + projectUser.project_id">
                    <b-card-body :title="'Project Id : ' + projectUser.project_id">
                        <b-card-text>
                            User Assigned to this project is: {{projectUser.user_id}}
                        </b-card-text>
                        <div class="card map-container">
                            <l-map ref="myMap" :zoom="zoom" :center="center" :options="{zoomControl: false}">
                                <l-control-zoom position="topright"></l-control-zoom>
                                <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>
                                <l-control-layers position="topright" ref="layersControl" :sort-layers="true">
                                </l-control-layers>

                                <l-tile-layer
                                        v-for="tileProvider in tileProviders"
                                        :key="tileProvider.name"
                                        :name="tileProvider.name"
                                        :visible="tileProvider.visible"
                                        :url="tileProvider.url"
                                        :attribution="tileProvider.attribution"
                                        layer-type="base"/>

                                <l-control-scale position="bottomright" :maxWidth="200" imperial="imperial"/>
                            </l-map>
                        </div>
                        <div class="mt-3">
                            <b-button class="mr-2 btn-sm" disabled>Status</b-button>
                            <b-button class="mr-2 btn-sm" disabled>Send Email</b-button>
                            <b-button class="mr-2 btn-sm" disabled>Unjoin</b-button>
                            <b-button class="mr-2 btn-sm" disabled>Invite</b-button>
                            <b-button class="mr-2 btn-sm"><router-link :to="'/visualize/'+ projectUser.project_id">Visualize</router-link></b-button>
                            <b-button class="mr-2 btn-sm"><router-link to="/adaptation-plans/1">Adaptation Plans</router-link></b-button>
                        </div>
                    </b-card-body>
                </b-tab>
            </b-tabs>
        </b-card>
        <b-card v-show="">
        <b-card-body title="You don't have access to any projects">
            <b-card-text>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque luctus purus sit amet massa hendrerit semper at eu dui.
            </b-card-text>
        </b-card-body>
        </b-card>
    </div>
</template>

<script>
    import L from 'leaflet';
    import {LMap, LTileLayer, LMarker} from 'vue2-leaflet';

    export default {
        components: {
            LMap, LTileLayer, LMarker

        },
        name: 'MyProjects',

        data() {
            return {
                zoom:13,
                center: L.latLng(47.413220, -1.219482),
                url:'http://{s}.tile.osm.org/{z}/{x}/{y}.png',
                attribution:'&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
                marker: L.latLng(47.413220, -1.219482),

                users : [],
                projects : [],
                projectsUsers : [],
            }

        },

        mounted() {
            const { utils } = AiravataAPI;
            utils.FetchUtils.get('/interactwel/api/projectuserss/')
                .then(data => {
                    this.projectsUsers = data;
                })
                .catch(error => {
                    alert("Could not get the projects list. API error! " + error)
                });

            utils.FetchUtils.get('/interactwel/api/users/')
                .then(data => {
                    this.users = data;
                })
                .catch(error => {
                    alert("Could not get the projects list. API error! " + error)
                });

            utils.FetchUtils.get('/interactwel/api/projects/')
                .then(data => {
                    this.projects = data;
                })
                .catch(error => {
                    alert("Could not get the projects list. API error! " + error)
                });

        },


        methods: {}

    }

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
    @import '../../../assets/vendor/Vue2Leaflet/leaflet.css';
    .map-container{
        height: 400px;
        overflow:auto;
    }
</style>

