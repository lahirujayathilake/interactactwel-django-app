<template>
    <div>
        <b-card no-body>
            <b-tabs pills card vertical nav-wrapper-class="w-25">
                <b-tab title="Suggested Projects">
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
                </b-tab>
                <b-tab v-for="project in projects" :title="project.location">
                    <b-card-body :title="project.name">
                        <b-card-text>
                            {{project.description}}
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
                            <b-button class="mr-2 btn-sm" disabled>Request to join</b-button>
                        </div>
                    </b-card-body>
                </b-tab>
            </b-tabs>
        </b-card>
        <b-card v-show="projects.size == 0">
            <b-card-body title="You don't have any suggested projects" >
                <b-card-text>
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque luctus purus sit amet massa hendrerit semper at eu dui.
                </b-card-text>
            </b-card-body>
        </b-card>
    </div>
</template>

<script>

    import {LMap, LTileLayer, LMarker, LGeoJson, LControlLayers, LControlScale, LLayerGroup, LPopup, LControlZoom} from 'vue2-leaflet';
    import L from 'leaflet';
    import axios from 'axios';

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
        name: 'MyProjects',

        data() {
            return {
                geoJson_reach: null,
                geoJson_subbasin: null,
                geoJson_reservoir: null,
                geoJson_WaterRigths: null,
                geoJson_irrland: null,
                geoJson_triballand: null,
                zoom: 9,
                maxZoom: 17,
                minZoom: 3,
                center: L.latLng(45.4435777, -119.4455003),
                url: 'https://stamen-tiles-{s}.a.ssl.fastly.net/terrain/{z}/{x}/{y}{r}.png',
                attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
                marker: L.latLng(45.6735777, -118.8455003),
                detectRetina: true,
                enableTooltip: true,
                loading: true,
                show: true,
                fillColor: "rgba(76, 175, 80, 0.44)",
                subbasinID: null,

                projects : [],

                tileProviders: [
                    {
                        name: "<font size=4><strong>Street Map</strong></font>",
                        visible: false,
                        attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
                        url: "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                    },
                    {
                        name: "<font size=4><strong>Satellite</strong></font>",
                        visible: false,
                        attribution: 'Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community',
                        url: "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}.png"
                    },
                    {
                        name: "<font size=4><strong>Terrain Map",
                        visible: true,
                        attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
                        url: "https://stamen-tiles-{s}.a.ssl.fastly.net/terrain/{z}/{x}/{y}{r}.png"
                    }
                ],

                customPopup : "<div class=\"region_summary_popup\">" +
                "<div>\n" +
                "        <div>\n" +
                "            <h5>SubBasin</h5>\n" +
                "        </div>\n" +
                "        <div>Test Data</div>" +
                "</div>",
                customOptions: [
                    {
                        'font-size': '15px',
                        'maxWidth': '1000px',
                        'width': '500px',
                        'className' : 'custom'
                    }
                ]
            }

        },

        mounted() {
            const { utils } = AiravataAPI;
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
    }
</style>

