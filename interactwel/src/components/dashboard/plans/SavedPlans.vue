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
                test_position: {"lat": 45.346896, "lng": -119.544586},
                zoom: 9,
                maxZoom: 17,
                minZoom: 3,
                //center: L.latLng(45.4435777, -119.4455003),
                url: 'https://stamen-tiles-{s}.a.ssl.fastly.net/terrain/{z}/{x}/{y}{r}.png',
                attribution:
                    '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
                marker: L.latLng(47.41322, -1.219482),


                urlx : 'https://stamen-tiles-{s}.a.ssl.fastly.net/terrain/{z}/{x}/{y}{r}.png',
                attributionx: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
                reservoirStationList: ReservoirList,
                ReservoirData: ReservoirDataJson,

                tileProviders: [
                    {
                        name: "<font size=2><strong>Street Map</strong></font>",
                        visible: false,
                        attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
                        url: "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                    },
                    {
                        name: "<font size=2><strong>Satellite</strong></font>",
                        visible: false,
                        attribution: 'Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community',
                        url: "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}.png"
                    },
                    {
                        name: "<font size=2><strong>Terrain Map",
                        visible: true,
                        attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
                        url: "https://stamen-tiles-{s}.a.ssl.fastly.net/terrain/{z}/{x}/{y}{r}.png"
                    }
                ],
                reservoirIcon: L.icon({
                    iconUrl: require('../../../../public/static/img/reservoir_trans.png'),
                    iconSize: [27, 27], // size of the icon
                    shadowSize: [0, 0], // size of the shadow
                    iconAnchor: [0, 0], // point of the icon which will correspond to marker's location
                    shadowAnchor: [0, 0]  // the same for the shadow
                }),

                users: [],
                projects: [],
                projectsUsers: [],
                loggedInUser: {
                    id: -1,
                    username: "",
                    first_name: "",
                    last_name: "",
                    email: "",
                    phone: "",
                    organization: ""
                }
            };
        },

        mounted() {
            const {utils, session} = AiravataAPI;
            const SessionData = AiravataPortalSessionData;
            this.loggedInUser.username = SessionData.username;
            utils.FetchUtils.get("/interactwel/api/users/")
                .then(users => {
                    this.loggedInUser = users.find(user => {
                        return user.username = this.loggedInUser.username;
                    });
                    utils.FetchUtils.get("/interactwel/api/projectusers/")
                        .then(projectsUsers => {
                            this.projectsUsers = projectsUsers.filter(projectUser => {
                                return projectUser.user_id === this.loggedInUser.id && projectUser.status === "Active";
                            })
                            utils.FetchUtils.get("/interactwel/api/projects/")
                                .then(projects => {
                                    this.projects = projects.filter(project => {
                                        return this.projectsUsers.findIndex(projectUser => {
                                            console.log(projectUser.project_id === project.project_id);
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
                })
                .catch(error => {
                    alert("Could not get the projects list. API error! " + error);
                });

        },

        methods: {
            getCenterOfMap: function (project) {
                return L.latLng(project.latitude, project.longtitude);
            },
            getMainMapCenterLocation: function () {
                return L.latLng(45.346896, -119.544586);

            },
            getMainMapZoomValue: function () {
                return 3;
            },
            mapSelected: function () {
                window.dispatchEvent(new Event('resize'))
            },
            projectSelected: function (projectId) {
                this.$router.push('/plans/saved-plans/'+ projectId);

            }

        },
        computed: {}
    };
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
    @import "../../../assets/vendor/Vue2Leaflet/leaflet.css";

    .map-container {
        height: 400px;
        overflow: auto;
    }
    .no-padding {
        padding: 0;
    }
</style>
