<template>
    <div>
        <b-card v-if="projects" no-body>
            <b-tabs card vertical nav-wrapper-class="w-25">
                <!--<b-tab title="My Projects" v-on:click="mapSelected()">
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
                </b-tab>-->
                <b-tab
                        v-for="project in projects"
                        :title="project.name"
                        v-on:click="mapSelected()">
                    <!--<router-view></router-view>-->
                    <b-card-body>
                        <b-card-title>{{project.name}}</b-card-title>
                        <!--
                                    <b-card-text>User Assigned to this project is: {{loggedInUser.username}}</b-card-text>
                        -->
                        <b-container class="bv-example-row">
                            <b-row>
                        <b-col lg="5">
                            <div class="d-flex flex-column">
                                <div class="mt-3">
                                    <b-button class="mr-2" @click="$router.push('/visualize/'+ project.project_id)"
                                              variant="success">View Project Data
                                    </b-button>
                                    <b-button @click="$router.push('/all-plans/'+ project.project_id)"
                                              variant="outline-success">View Plans
                                    </b-button>
                                </div>
                                <div class="mt-4">
                                    <h6>Project Details</h6>
                                    <b-list-group>
                                        <b-list-group-item>{{project.description}}</b-list-group-item>
                                        <b-list-group-item>Location: {{project.location}}</b-list-group-item>
                                        <b-list-group-item>Latitude: {{project.latitude}}</b-list-group-item>
                                        <b-list-group-item>Longtitude: {{project.longtitude}} </b-list-group-item>
                                    </b-list-group>
                                </div>
                                <div class="mt-3">
                                    <div>
                                        <b-button class="mr-2 btn-sm" disabled><i class="fa fa-envelope"></i></b-button>
                                        <b-button class="mr-2 btn-sm" disabled>Unjoin</b-button>
                                        <b-button class="mr-2 btn-sm" disabled>Invite</b-button>
                                    </div>
                                </div>
                            </div>
                        </b-col>
                        <b-col lg="7">
                        <div class="card map-container">
                            <l-map ref="myMap" :zoom="zoom" :center="getCenterOfMap(project)">
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
                        </b-col>
                            </b-row>
                        </b-container>
                    </b-card-body>

                </b-tab>
            </b-tabs>
        </b-card>
        <b-card v-if="!projects">
            <b-card-body title="You don't have access to any projects">
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
            'l-control-layers': LControlLayers,
            'l-layer-group': LLayerGroup,
            'l-control-scale': LControlScale,
            'l-popup': LPopup,
            'popup-content-rs': PopupContentReservoirs,
        },
        name: "MyProjects",

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

        async mounted() {
            this.projects = await this.getProjectsListOfLoggedInUser();
            setInterval(() => this.emitWindowResizeEvent(), 500);

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
                this.$router.push('/projects/my-projects/'+ projectId);

            },
            emitWindowResizeEvent: function () {
                window.dispatchEvent(new Event('resize')) //a hack to get rid of map partially showing issue
            },

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
</style>
