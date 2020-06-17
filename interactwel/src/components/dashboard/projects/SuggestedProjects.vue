<template>
    <div>
        <b-card no-body>
            <b-tabs pills card vertical nav-wrapper-class="w-25">
                <b-tab title="Invited Projects" v-on:click="mapSelected()">
                    <div class="card map-container">
                        <l-map :zoom="5" :center="getMainMapCenterLocation()">
                            <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>
                            <l-marker :lat-lng="marker"></l-marker>

                            <l-marker
                                    v-for="project in projects"
                                    :key="project.project_id"
                                    :lat-lng="{ lat: project.latitude, lng: project.longtitude }"
                                    :icon="reservoirIcon"
                                    :visible="true"/>
                        </l-map>
                    </div>
                </b-tab>
                <b-tab
                        v-for="project in projects"
                        :title="project.name"
                        v-on:click="mapSelected()">
                    <b-card-body :title="project.name">
                        <!--
                                    <b-card-text>User Assigned to this project is: {{loggedInUser.username}}</b-card-text>
                        -->
                        <b-card-text>{{project.description}}</b-card-text>
                        <div class="card map-container">
                            <l-map ref="myMap" :zoom="zoom" :center="getCenterOfMap(project)">
                                <l-control-zoom position="topright"></l-control-zoom>
                                <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>
                                <l-control-layers position="topright" ref="layersControl"
                                                  :sort-layers="true"></l-control-layers>

                                <l-tile-layer
                                        v-for="tileProvider in tileProviders"
                                        :key="tileProvider.name"
                                        :name="tileProvider.name"
                                        :visible="tileProvider.visible"
                                        :url="tileProvider.url"
                                        :attribution="tileProvider.attribution"
                                        layer-type="base"
                                />

                                <l-layer-group layer-type="overlay"
                                               name="<font size=2><strong>Reservoirs</strong></font>">
                                    <l-marker :key="project.project_id"
                                              :lat-lng="{ lat: project.latitude, lng: project.longtitude }"
                                              :icon="reservoirIcon"
                                              :visible="true">
                                        <l-popup>
                                            <div id="PopupContentReservoirs" class="card">
                                                <div class="card-header"><strong>{{ project.name }}</strong></div>
                                                <div class="card-body">
                                                    <table class="table table-borderless table-sm">
                                                        <tbody>
                                                        <tr>
                                                            <th>Description</th>
                                                            <th>{{project.description}}</th>
                                                        </tr>
                                                        <tr>
                                                            <td>latitude</td>
                                                            <td><span
                                                                    class="badge badge-secondary">{{project.latitude}}</span>
                                                            </td>
                                                        </tr>
                                                        <tr>
                                                            <td>longtitude</td>
                                                            <td><span
                                                                    class="badge badge-secondary">{{project.longtitude}}</span>
                                                            </td>
                                                        </tr>
                                                        </tbody>
                                                    </table>
                                                </div>
                                            </div>
                                        </l-popup>
                                    </l-marker>
                                </l-layer-group>

                                <l-control-scale position="bottomright" :maxWidth="200" imperial="imperial"/>
                            </l-map>
                        </div>
                        <div class="mt-3">
                            <b-button class="mr-2 btn-sm">Accept Invitation</b-button>
                        </div>
                    </b-card-body>
                </b-tab>
            </b-tabs>
        </b-card>
        <b-card v-show="">
            <b-card-body title="You don't have any projects to explore">
                <b-card-text>
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque luctus purus sit amet massa hendrerit semper at eu dui.
                </b-card-text>
            </b-card-body>
        </b-card>
    </div>
</template>

<script>

    import L from "leaflet";
    import {LMap, LTileLayer, LMarker, LGeoJson, LControlLayers, LControlScale, LLayerGroup, LPopup, LControlZoom} from 'vue2-leaflet';
    import ReservoirList from './../../../../public/static/reservoirs_list.json';
    import ReservoirDataJson from "./../../../../public/static/reservoirs_data.json";
    import PopupContentReservoirs from "./popup/PopupContent_Reservoirs";

    export default {
        components: {
            'l-map': LMap,
            'l-tile-layer': LTileLayer,
            'l-marker': LMarker,
            'l-geo-json': LGeoJson,
            'l-control-layers': LControlLayers,
            'l-layer-group': LLayerGroup,
            'l-control-scale': LControlScale,
            'l-popup': LPopup,
            'l-control-zoom': LControlZoom

        },
        name: 'ExploreProjects',

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
            }

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
                    console.log(this.loggedInUser);
                    utils.FetchUtils.get("/interactwel/api/projectusers/")
                        .then(projectsUsers => {
                            this.projectsUsers = projectsUsers.filter(projectUser => {
                                return projectUser.user_id === this.loggedInUser.id && projectUser.status === "Inactive";
                            })
                            console.log(this.projectsUsers);
                            utils.FetchUtils.get("/interactwel/api/projects/")
                                .then(projects => {
                                    console.log(projects);
                                    this.projects = projects.filter(project => {
                                        console.log(project);
                                        return this.projectsUsers.findIndex(projectUser => {
                                            console.log(projectUser.project_id === project.project_id);
                                            return projectUser.project_id === project.project_id;
                                        }) !== -1 ? true : false;
                                    });
                                    console.log(this.projects);
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

            // utils.FetchUtils.get("/interactwel/api/projects/")
            //   .then(data => {
            //     this.projects = data;
            //   })
            //   .catch(error => {
            //     alert("Could not get the projects list. API error! " + error);
            //   });
            // utils.FetchUtils.get("/interactwel/api/projects/")
            //     .then(projects => {
            //         this.projects=this.projects=projects.filter(project=>{
            //             return project.username===this.loggedInUserName;
            //         });
            //     })
            //     .catch(error => {
            //         alert("Could not get the projects list. API error! " + error);
            //     });
            // console.log(this.projects);

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
            }
        }

    }

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
    @import '../../../assets/vendor/Vue2Leaflet/leaflet.css';
    .map-container{
        height: 400px;
    }
</style>
