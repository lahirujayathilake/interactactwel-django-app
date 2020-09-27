<template>
    <div>
        <div class="wizard-container">
            <b-navbar toggleable="sm" type="dark" variant="dark">
                <b-navbar-toggle target="nav-text-collapse"></b-navbar-toggle>

                <b-navbar-brand>Project Id : {{ $route.params.projectId }}</b-navbar-brand>

                <b-collapse id="nav-text-collapse" is-nav>
                    <b-navbar-nav>
                        <b-nav-text>{{selectedProject.name}}</b-nav-text>
                    </b-navbar-nav>
                </b-collapse>
                <b-button v-show="!isWizardFlowStarted" variant="success" @click="startWizard($route.params.projectId)" class="mr-2 btn-sm">Start</b-button>
                <b-button v-show ="!isWizardFlowStarted" class="mr-2 btn-sm">
                    <router-link to="/plans/new-plan">Back to Plans</router-link>
                </b-button>
                <b-button v-show ="isWizardFlowStarted" variant="danger" @click="exitWizard" class="btn-sm">Exit</b-button>
            </b-navbar>
           <!-- <component v-show="!wizardVisibility" v-bind:is="component='Wizard'"></component>-->
                <router-view></router-view>
                <b-col>
                    <div class="lg-map-container">
                        <l-map ref="myMap" :maxZoom="maxZoom" :zoom="zoom" :center="center" :options="{zoomControl: false}">
                            <l-control-zoom position="topright"></l-control-zoom>
                            <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>
                            <!--<l-control-layers position="topright" ref="layersControl" :sort-layers="true" :autoZIndex="true">-->
                            <l-control-layers position="topright" ref="layersControl"
                                              :sort-layers="false"></l-control-layers>

                            <l-tile-layer
                                    v-for="tileProvider in tileProviders"
                                    :key="tileProvider.name"
                                    :name="tileProvider.name"
                                    :visible="tileProvider.visible"
                                    :url="tileProvider.url"
                                    :attribution="tileProvider.attribution"
                                    layer-type="base"/>

                            <l-layer-group layer-type="overlay"
                                           name="<font size=2 color=#5e6b7e><i><u><strong>Default Layers</strong></u></i></font>"
                                           v-on:change="myFunction($event)"></l-layer-group>

                            <l-layer-group layer-type="overlay" :visible="defaultvisibility"
                                           name="<font size=2><strong>Sub-basins</strong></font>">
                                <l-geo-json
                                        v-if="show"
                                        :geojson="geoJson_subbasin"
                                        :options="options"
                                        :options-style="styleFunction_subbasin"
                                />
                            </l-layer-group>

                            <l-layer-group layer-type="overlay" :visible="defaultvisibility"
                                           name="<font size=2><strong>Streams</strong></font>">
                                <l-geo-json
                                        v-if="show"
                                        :geojson="geoJson_reach"
                                        :options="options_noclick"
                                        :options-style="styleFunction_reach"
                                />
                            </l-layer-group>


                            <l-layer-group layer-type="overlay"
                                           name="<font size=2 color=#5e6b7e><i><u><strong>Station Data</strong></u></i></font>"></l-layer-group>


                            <l-layer-group layer-type="overlay" :visible="stationvisibility"
                                           name="<font size=2><strong>Reservoirs</strong></font>">
                                <l-marker
                                        v-for="reservoirStation in reservoirStationList"
                                        :key="reservoirStation.id"
                                        :lat-lng.sync="reservoirStation.position"
                                        :icon="reservoirIcon"
                                        :visible="true">
                                    <l-popup>
                                        <popup-content-rs :data="reservoirStation" :pcpdata="ReservoirData"/>
                                    </l-popup>
                                </l-marker>
                            </l-layer-group>

                            <l-layer-group layer-type="overlay" :visible="stationvisibility"
                                           name="<font size=2><strong>Gauging stations</strong></font>">
                                <l-marker
                                        v-for="gaugingStation in gaugingStationList"
                                        :key="gaugingStation.id"
                                        :lat-lng.sync="gaugingStation.position"
                                        :icon="gaugingIcon"
                                        :visible="true">
                                    <l-popup>
                                        <popup-content-gs :data="gaugingStation" :pcpdata="GaugeData"/>
                                    </l-popup>
                                </l-marker>
                            </l-layer-group>

                            <l-layer-group layer-type="overlay" :visible="stationvisibility"
                                           name="<font size=2><strong>Weather stations</strong></font>">
                                <l-marker
                                        v-for="weatherStation in weatherStationList"
                                        :key="weatherStation.id"
                                        :lat-lng.sync="weatherStation.position"
                                        :icon="wstationIcon"
                                        :visible="true">
                                    <l-popup>
                                        <popup-content-ws :data="weatherStation" :pcpdata="PrecipData"/>
                                    </l-popup>
                                </l-marker>
                            </l-layer-group>


                            <l-layer-group layer-type="overlay"
                                           name="<font size=2 color=#5e6b7e><i><u><strong>Additional Layers</strong></u></i></font>"></l-layer-group>

                            <l-layer-group id="wtrights" layer-type="overlay" :visible="otherlayersvisibility"
                                           name="<font size=2><strong>Water Rights</strong></font>">
                                <l-geo-json
                                        v-if="show"
                                        :geojson="geoJson_WaterRigths"
                                        :options="options_wrrights"
                                        :options-style="styleFunction_waterrigths"
                                />
                            </l-layer-group>

                            <l-layer-group layer-type="overlay" :visible="otherlayersvisibility"
                                           name="<font size=2><strong>Irrigated Land</strong></font>">
                                <l-geo-json
                                        v-if="show"
                                        :geojson="geoJson_irrland"
                                        :options="options_noclick"
                                        :options-style="styleFunction_irrland"

                                />
                            </l-layer-group>

                            <l-layer-group layer-type="overlay" :visible="otherlayersvisibility"
                                           name="<font size=2><strong>GW Restricted Areas</strong></font>">
                                <l-geo-json
                                        v-if="show"
                                        :geojson="geoJson_gwrestricted"
                                        :options="options_noclick"
                                        :options-style="styleFunction_gwrestricted"
                                />
                            </l-layer-group>

                            <l-layer-group layer-type="overlay" :visible="otherlayersvisibility"
                                           name="<font size=2><strong>Tribal Lands</strong></font>">
                                <l-geo-json
                                        v-if="show"
                                        :geojson="geoJson_triballand"
                                        :options="options_noclick"
                                        :options-style="styleFunction_triballand"
                                />
                            </l-layer-group>

                            <l-layer-group layer-type="overlay" :visible="otherlayersvisibility"
                                           name="<font size=2><strong>NOWA Pumping Limit</strong></font>">
                                <l-geo-json
                                        v-if="show"
                                        :geojson="geoJson_pumping_limit"
                                        :options="options_noclick"
                                        :options-style="styleFunction_pumping_limit"

                                />
                            </l-layer-group>


                            <l-control-scale position="bottomright" :maxWidth="200" imperial="imperial"/>
                            <!--<img @click="Layerselector" src="../../../assets/water_rights_legend.png" id="WRlegend" class="map-legend">-->
                            <!--<img src="../../../assets/water_rights_legend.png" class="map-legend">-->

                            <l-control-layers v-if="ResultsMap" position="topright" ref="layersControl"
                                              :sort-layers="false"></l-control-layers>
                            <l-layer-group ref="RegionalMap" v-if="ResultsMap" layer-type="overlay"
                                           name="<font size=2 color=#5e6b7e><i><u><strong>Regional Results</strong></u></i></font>">
                                <l-geo-json
                                        v-if="RegionHeatMap"
                                        :geojson="geoJson_subbasin"
                                        :options="options_heatmap"
                                        :options-style="getStyle_HeatMap"

                                />
                            </l-layer-group>

                            <!--<l-choropleth-layer
                              id="regional_layer"
                              v-if="RegionHeatMap"
                              :data="pyDepartmentsData"
                              titleKey="department_name"
                              idKey="department_id"
                              :value="value"
                              :extraValues="extraValues"
                              geojsonIdKey="Name"
                              :geojson="paraguayGeojson"
                              :colorScale="colorScale">
                                <template slot-scope="props">
                                <l-reference-chart
                                    title="% of Change in Water Rights"
                                    :colorScale="colorScale"
                                    :min="props.min"
                                    :max="props.max"
                                    position="bottomright"/>
                                  <l-info-control
                                    :item="props.currentItem"
                                    :unit="props.unit"
                                    position="bottomright"
                                    title="Sub-basins"
                                    placeholder="Hover over a Sub-basin"/>

                                </template>
                            </l-choropleth-layer>-->


                        </l-map>
                    </div>
                </b-col>
        </div>
        <component v-show="!regionalSummaryVisibility" v-bind:is="component='regional-summary'"></component>
    </div>
</template>
<script>
    import Welcome from './intro/Welcome.vue';
    import TutorStep1 from './intro/TutorStep1.vue';
    import TutorStep2 from './intro/TutorStep2.vue';
    import Header from './../../Header.vue';
    import Footer from './../../Footer.vue';
    import axios from 'axios';
    import EventBus from './../../../event-bus';

    import L from 'leaflet';
    import {
        LMap,
        LTileLayer,
        LMarker,
        LGeoJson,
        LControlLayers,
        LControlScale,
        LLayerGroup,
        LPopup,
        LControlZoom
    } from 'vue2-leaflet';

    import PrecipDataJson from "./../../../../public/static/weather_station_data.json";
    import ReservoirDataJson from "./../../../../public/static/reservoirs_data.json";
    import GaugeDataJson from "./../../../../public/static/streamflow_station_data.json";

    import GaugingStations from './../../../../public/static/gauging_stations.json';
    import ReservoirList from './../../../../public/static/reservoirs_list.json';
    import WeatherStations from './../../../../public/static/weather_stations.json';

    import PopupContentReservoirs from "./popup/PopupContent_Reservoirs";
    import PopupContent_WaterRights from "./popup/PopupContent_WaterRights";
    import PopupContentWStations from "./popup/PopupContent_WStations";
    import PopupContentGaugeStations from "./popup/PopupContent_GaugeStations.vue";
    import RegionalSummary from './popup/RegionalSummary.vue';

    import {InfoControl, ReferenceChart, ChoroplethLayer} from 'vue-choropleth';

    import paraguayGeojson from './../../../../public/static/BASIN_Irrigation_basins_data.json'
    import {pyDepartmentsData} from './../../../../public/static/py-departments-data'

    export default {
        name: 'AdaptationPlans',
        components: {
            Header, Footer, RegionalSummary, Welcome, TutorStep1, TutorStep2,
            'l-map': LMap,
            'l-tile-layer': LTileLayer,
            'l-marker': LMarker,
            'l-geo-json': LGeoJson,
            'l-control-layers': LControlLayers,
            'l-layer-group': LLayerGroup,
            'l-control-scale': LControlScale,
            'l-popup': LPopup,
            'l-control-zoom': LControlZoom,
            'popup-content-ws': PopupContentWStations,
            'popup-content-rs': PopupContentReservoirs,
            'popup-content-gs': PopupContentGaugeStations,
            'popup-content-wr': PopupContent_WaterRights,
            'l-choropleth-layer': ChoroplethLayer,
            'l-info-control': InfoControl,
            'l-reference-chart': ReferenceChart,

        },

        data() {
            return {
                startBtn: true,
                isModalVisible: true,
                isStep1Active: false,
                isStep2Active: false,
                istutor1Visible: false,
                istutor2Visible: false,

                geoJson_reach: null,
                geoJson_subbasin: null,
                geoJson_reservoir: null,
                geoJson_WaterRigths: null,
                geoJson_irrland: null,
                geoJson_triballand: null,
                geoJson_pumping_limit: null,
                geoJson_gwrestricted: null,
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
                update_flag: true,

                unchecked_layers: [" Irrigated Land", " NOWA Pumping Limit", " GW Restricted Areas", " Tribal Lands", " Water Rights"],
                title_layers: [" Default Layers", " Station Data", " Additional Layers", " Regional Results"],
                default_num_layers: 0,
                default_selected_layers: [],
                paraguayGeojson,
                pyDepartmentsData,
                RegionHeatMap: false,
                ResultsMap: false,
                HeatMapProp: 'Name',
                defaultvisibility: true,
                otherlayersvisibility: true,
                stationvisibility: true,
                regionalSummaryVisibility: true,

                fillColor: "rgba(76, 175, 80, 0.44)",
                reservoirIcon: L.icon({
                    iconUrl: require('../../../../public/static/img/reservoir_trans.png'),
                    iconSize: [27, 27], // size of the icon
                    shadowSize: [0, 0], // size of the shadow
                    iconAnchor: [0, 0], // point of the icon which will correspond to marker's location
                    shadowAnchor: [0, 0]  // the same for the shadow
                }),
                wstationIcon: L.icon({
                    iconUrl: require('../../../../public/static/img/OSU_icon_rain_01.png'),
                    iconSize: [27, 27], // size of the icon
                    shadowSize: [0, 0], // size of the shadow
                    iconAnchor: [0, 0], // point of the icon which will correspond to marker's location
                    shadowAnchor: [0, 0]  // the same for the shadow
                }),

                gaugingIcon: L.icon({
                    iconUrl: require('../../../../public/static/img/OSU_icon_water.png'),
                    iconSize: [27, 27], // size of the icon
                    shadowSize: [0, 0], // size of the shadow
                    iconAnchor: [0, 0], // point of the icon which will correspond to marker's location
                    shadowAnchor: [0, 0]  // the same for the shadow
                }),

                subbasinID: null,

                PrecipData: PrecipDataJson,
                ReservoirData: ReservoirDataJson,
                GaugeData: GaugeDataJson,

                weatherStationList: WeatherStations,
                reservoirStationList: ReservoirList,
                gaugingStationList: GaugingStations,

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

                customPopup: "<div class=\"region_summary_popup\">" +
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
                        'className': 'custom'
                    }
                ],

                colorScale: ["e7d090", "e9ae7b", "de7062"],
                value: {
                    key: "amount_w",
                    metric: "% of SW Reduction"
                },
                extraValues: [{
                    key: "amount_m",
                    metric: "% of GW Reduction"
                }],

                mapOptions: {attributionControl: false},
                currentStrokeColor: '3d3213',
                selectedProject:{},
                isWizardFlowStarted:false,
            }
        },

        computed: {
            //jsonData() {
            //    return JSONData;
            //},
            options() {
                return {
                    onEachFeature: this.onEachFeatureFunction
                };
            },

            options_noclick() {
                return {};
            },

            options_wrrights() {
                return {
                    onEachFeature: this.GetWRcolor
                };
            },

            options_heatmap() {
                return {
                    onEachFeature: this.getHeatMapColor_Perct
                };
            },

            styleFunction_reach() {
                const fillColor = this.fillColor; // important! need touch fillColor in computed for re-calculate when change fillColor
                return () => {
                    return {
                        weight: 2.5,
                        color: "#3386ff",
                        opacity: 1,
                        fillColor: fillColor,
                        fillOpacity: 1
                    };
                };
            },

            styleFunction_pumping_limit() {
                const fillColor = this.fillColor; // important! need touch fillColor in computed for re-calculate when change fillColor
                return () => {
                    return {
                        weight: 1.5,
                        color: "#e773e1",
                        opacity: 1,
                        fillColor: fillColor,
                        fillOpacity: 1
                    };
                };
            },

            styleFunction_subbasin() {
                return () => {
                    return {
                        weight: 1.5,
                        color: "#7c7c7c",
                        opacity: 1,
                        fillColor: "#e3dddd",
                        dashArray: '5, 5',
                        dashOffset: '10',
                        fillOpacity: 0.5
                    };
                };
            },

            styleFunction_waterrigths() {
                return () => {
                    return {
                        weight: 1,
                        color: "#7c7c7c",
                        opacity: 0,
                        fillColor: "#3386ff",
                        fillOpacity: 1
                    };
                };
            },

            styleFunction_irrland() {
                return () => {
                    return {
                        weight: 0.5,
                        color: "#7c7c7c",
                        opacity: 0.4,
                        fillColor: "#eb984e",
                        fillOpacity: 0.6
                    };
                };
            },

            styleFunction_triballand() {
                return () => {
                    return {
                        weight: 0.8,
                        color: "#ffffff",
                        opacity: 0.4,
                        fillColor: "#00cccc",
                        dashArray: '5, 5',
                        dashOffset: '10',
                        fillOpacity: 0.6
                    };
                };
            },

            styleFunction_gwrestricted() {
                return () => {
                    return {
                        weight: 0.8,
                        color: "#ffffff",
                        opacity: 0.4,
                        fillColor: "#aff479",
                        dashArray: '5, 5',
                        dashOffset: '10',
                        fillOpacity: 0.6
                    };
                };
            },

            getStyle_HeatMap() {
                return () => {
                    return {
                        weight: 1.5,
                        color: "#ffffff",
                        opacity: 1,
                        fillOpacity: 0.7,
                        fillColor: '#8c2d04'
                    };
                };
            },

            getHeatMapColor() {
                return (feature, layer) => {
                    //console.log(feature.properties.Name);
                    if (feature.properties.Name > 1000) {
                        layer.setStyle({fillColor: '#581845'});
                    } else if (feature.properties.Name > 500) {
                        layer.setStyle({fillColor: '#900C3F'});
                    } else if (feature.properties.Name > 200) {
                        layer.setStyle({fillColor: '#C70039'});
                    } else if (feature.properties.Name > 100) {
                        layer.setStyle({fillColor: '#FF5733'});
                    } else if (feature.properties.Name > 50) {
                        layer.setStyle({fillColor: '#FFC300'});
                    } else if (feature.properties.Name > 20) {
                        layer.setStyle({fillColor: 'fee391'});
                    } else if (feature.properties.Name > 10) {
                        layer.setStyle({fillColor: '#fff7bc'});
                    } else {
                        layer.setStyle({fillColor: '#ffffe5'});

                    }
                    ;
                };
            },

            getHeatMapColor_Perct() {
                return (feature, layer) => {
                    //console.log(feature.properties[this.HeatMapProp]);
                    var subid = feature.properties[this.HeatMapProp];
                    //console.log(this.paraguayGeojson["Adaptation_plans"]["Adaptation Plan 1"][subid]["Data"]["1"]["Data"]["1"])
                    //console.log(subid);
                    if (feature.properties[this.HeatMapProp] > 20) {
                        layer.setStyle({fillColor: '#800026'});
                    } else if (feature.properties[this.HeatMapProp] > 15) {
                        layer.setStyle({fillColor: '#E31A1C'});
                    } else if (feature.properties[this.HeatMapProp] > 10) {
                        layer.setStyle({fillColor: '#FF5733'});
                    } else if (feature.properties[this.HeatMapProp] > 5) {
                        layer.setStyle({fillColor: '#FD8D3C'});
                    } else if (feature.properties[this.HeatMapProp] > 2) {
                        layer.setStyle({fillColor: '#FED976'});
                    } else {
                        layer.setStyle({fillColor: '#ffffe5'});
                        layer.setStyle({fillOpacity: "0"});
                    }
                    ;
                };
            },

            GetWRcolor() {
                return (feature, layer) => {
                    if (feature.properties.WRSCI == '3') {
                        layer.setStyle({fillColor: 'red'});
                    } else if (feature.properties.WRSCI == '1') {
                        layer.setStyle({fillColor: 'blue'});
                    } else if (feature.properties.WRSCI == '5') {
                        layer.setStyle({fillColor: 'green'});
                    } else {
                        layer.setStyle({fillColor: 'black'});
                        layer.setStyle({fillOpacity: "0"});
                    }

                    layer.on('click', function (e) {
                    });
                }
            },

            onEachFeatureFunction() {
                var prevLayerClicked = null;
                if (!this.enableTooltip) {
                    return () => {
                    };
                }
                return (feature, layer) => {
                    layer.bindTooltip(
                        "<div><strong>Click and explore!</strong>",
                    );

                    layer.on('click', function (e) {
                        EventBus.$emit('SELECTED_BASIN', feature.properties.Name);

                        var layer = e.target;
                        if (prevLayerClicked !== null || prevLayerClicked == layer) {
                            prevLayerClicked.setStyle({
                                weight: 1.5,
                                color: "#7c7c7c",
                                opacity: 1,
                                fillColor: "#e3dddd",
                                dashArray: '5, 5',
                                dashOffset: '10',
                                fillOpacity: 0.5
                            });
                        }
                        if (prevLayerClicked !== layer) {
                            layer.setStyle({fillColor: 'blue'});
                            prevLayerClicked = layer;

                        } else {
                            prevLayerClicked = null;
                        }

                    });

                };
            }
        },

        mounted() {
            const { utils } = AiravataAPI;
            this.projectId = this.$route.params.projectId
            // let adaptationPlan = JSON.parse(localStorage.getItem("adaptationPlan"));
            // if (adaptationPlan) {
            //     adaptationPlan.projectId = this.projectId;
            // } else {
            //     localStorage.setItem('adaptationPlan', JSON.stringify({'projectId': this.projectId}));
            // }

            this.$store.commit("setWizardFlowStarted", false);

            this.$store.commit("setProjectId", this.projectId);


            // TODO: call the /interactwel/api/projects/{project_id} to get the specific project 
           utils.FetchUtils.get("/interactwel/api/projects/")
                .then(projects=>{
                    this.selectedProject=projects.find(project=>{
                        console.log(project.project_id+" "+this.projectId);
                        console.log(project.project_id==this.projectId);
                        return project.project_id==this.projectId;
                    });
                    console.log(this.selectedProject);
                })
                .catch(error => {
                    alert("Could not get the project. API error! " + error);
                });


            let $this = this;
            EventBus.$on('SELECTED_BASIN', function (selectedBasinID) {

                $this.regionalSummaryVisibility = true;

                if ($this.prevLayerClicked !== null || $this.prevLayerClicked == selectedBasinID) {
                    $this.regionalSummaryVisibility = true;
                }
                if ($this.prevLayerClicked !== selectedBasinID) {
                    $this.createRegionSummary(selectedBasinID)
                    $this.regionalSummaryVisibility = false;
                    $this.prevLayerClicked = selectedBasinID;
                } else {
                    $this.regionalSummaryVisibility = true;
                    $this.prevLayerClicked = null;
                }
            }),EventBus.$on('CLOSE', function () {
                $this.regionalSummaryVisibility = true
            })

            const map = this.$refs.myMap.mapObject;
            EventBus.$on('START_RESULTSMAP', function () {
                var active = [];
                var default_selected_layers = [];
                var i;
                active = $('.leaflet-control-layers-selector')
                for (i = 3; i < active.length; i++) {
                    //if ($this.unchecked_layers.includes(active[i].labels[0].innerText)==false && active[i].checked==true){
                    if (active[i].checked == true && $this.default_selected_layers.includes(active[i].labels[0].innerText) == false) {
                        //console.log(active[i].labels[0].innerText);
                        default_selected_layers.push(active[i].labels[0].innerText);
                        $('.leaflet-control-layers-selector')[i].click();
                    }
                }
                //console.log(default_selected_layers);
                $this.ResultsMap = true;
                $this.default_selected_layers = default_selected_layers;
            }),

                EventBus.$on('START_REGIONHEATMAP', function () {
                    var active = [];
                    var i;
                    active = $('.leaflet-control-layers-selector')
                    for (i = $this.default_num_layers; i < active.length; i++) {
                        if ($this.title_layers.includes(active[i].labels[0].innerText) == true) {
                            $('.leaflet-control-layers-selector')[i].hidden = true;
                        }
                    }
                    $this.RegionHeatMap = true;
                }),

                EventBus.$on('HIDE_RESULTSMAP', function () {
                    var active = [];
                    var i;
                    console.log(this.default_selected_layers);
                    active = $('.leaflet-control-layers-selector')
                    for (i = 0; i < active.length; i++) {

                        if ($this.default_selected_layers.includes(active[i].labels[0].innerText) == true) {
                            $('.leaflet-control-layers-selector')[i].click();
                        }

                        if (i >= $this.default_num_layers && active[i].checked == true) {
                            $('.leaflet-control-layers-selector')[i].click();
                        }

                        if ($this.title_layers.includes(active[i].labels[0].innerText) == true) {
                            $('.leaflet-control-layers-selector')[i].hidden = true;
                        }
                    }
                    $this.RegionHeatMap = false;
                    $this.ResultsMap = false;
                })
        },

        beforeDestroy() {
            this.$parent.mapObject = $('.parent.mapObject');
        },

        created() {
            this.loading = true;
            axios.get("/static/subbasins.geojson")
                .then(response => {
                    this.geoJson_subbasin = response.data;
                    this.loading = true;
                })
            axios.get("/static/reaches.geojson")
                .then(response => {
                    this.geoJson_reach = response.data;
                    this.loading = true;
                })
            axios.get("/static/NOWA_Pumping_Limit.geojson")
                .then(response => {
                    this.geoJson_pumping_limit = response.data;
                    this.loading = true;
                })
            axios.get("/static/irrigated_land.geojson")
                .then(response => {
                    this.geoJson_irrland = response.data;
                    this.loading = true;
                })
            axios.get("/static/Tribal_Lands.geojson")
                .then(response => {
                    this.geoJson_triballand = response.data;
                    this.loading = true;
                })

            axios.get("/static/GW_Restricted_Areas_Umatilla.geojson")
                .then(response => {
                    this.geoJson_gwrestricted = response.data;
                    this.loading = true;
                })

            axios.get("/static/water_rigths.geojson")
                .then(response => {
                    this.geoJson_WaterRigths = response.data;
                    this.loading = true;
                });

            // var active = [];
            // var i;
            // active = $('.leaflet-control-layers-selector')
            // this.default_num_layers = active.length;

            // for (i = 0; i < active.length; i++) {
            //     if (this.unchecked_layers.includes(active[i].labels[0].innerText)==true && active[i].checked==true){
            //     //if (active[i].checked==true){
            //         $('.leaflet-control-layers-selector')[i].click();
            //     }else{
            //         this.default_selected_layers.push(active[i].labels[0].innerText);
            //     }

            //     if (this.title_layers.includes(active[i].labels[0].innerText)==true){
            //         $('.leaflet-control-layers-selector')[i].hidden=true;
            //     }
            // }
        },

        /*updated: function(){
            // Create array for holding active layers
            var active = [];
            var i;
            if (this.update_flag){
                active = $('.leaflet-control-layers-selector')
                this.default_num_layers = active.length;

                for (i = 0; i < active.length; i++) {
                    if (this.unchecked_layers.includes(active[i].labels[0].innerText)==true && active[i].checked==true){
                        //if (active[i].checked==true){
                        $('.leaflet-control-layers-selector')[i].click();
                    }

                    //if (this.title_layers.includes(active[i].labels[0].innerText)==true && active[i].labels[0].innerText !== this.title_layers[0]){
                    if (this.title_layers.includes(active[i].labels[0].innerText)==true){
                        $('.leaflet-control-layers-selector')[i].hidden=true;
                        //console.log(active[i].labels[0].innerText);
                        //$('.leaflet-control-layers-selector')[i].click();
                    }
                }
                this.update_flag = false;
            }
        },*/

        methods: {
            createRegionSummary(subbasinID) {
                EventBus.$emit('CREATE_REGION_SUMMARY', subbasinID);
            },
            startWizard(projectId){
                this.isWizardFlowStarted=true;
                this.$store.commit("setWizardFlowStarted", true);
                this.$store.commit("resetWizardFlow", null);
                this.startBtn = false;
                this.exitBtn = true;
                this.$router.push('/adaptation-plans/'+projectId+'/goals')
            },

            exitWizard(){
                
                let confirmResponse=confirm("If you exit now all data will be cleared. Do you want to proceed");
                if(confirmResponse){
                    this.$store.commit("resetWizardFlow", null);
                    this.$router.push('/plans/saved-plans');
                    this.isWizardFlowStarted=false;
                }
                
            }
        }

    }

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
    @import '../../../assets/vendor/Vue2Leaflet/leaflet.css';
    .lg-map-container{
        height: 85vh;
        overflow: auto;
    }
    #step1 {
        position: absolute;
        z-index: 1000;
        left: 30px;
        top: 70px;
        min-width: 350px;
    }

    #step2 {
        position: absolute;
        z-index: 1000;
        left: 30px;
        top: 70px;
        min-width: 350px;
    }

    #step3 {
        position: absolute;
        z-index: 1000;
        left: 30px;
        top: 70px;
    }

    #step4 {
        display: flex;
        position: absolute;
        z-index: 1000;
        left: 30px;
        top: 70px;
        width: 1000px;
    }

    #step5 {
        position: absolute;
        z-index: 1000;
        left: 30px;
        top: 70px;
        width: 1000px;
    }

    #step6 {
        position: absolute;
        z-index: 1000;
        left: 30px;
        top: 70px;
        width:900px;
    }

    .step-progress-bar{
        padding: 0.5rem;
    }
    .step-progress-bar h4 {
        font-size: 1em;
        font-weight: 700;
        color: #5f6c73;
        margin-bottom: .05rem;
        text-align: left;
    }

    .step-progress-bar h4r {
        float: right;
        font-size: 1em;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: .05rem;
        text-align: right;
    }

    .step-progress-bar p {
        font-weight: 400;
        font-size: .72857143em;
        color: #5f6c73;
        margin-bottom: 0;
        text-align: left;
    }

    .step-progress-bar .step-no {
        float: left;
        font-size: 25px;
        font-weight: 700;
        color: #28a745;
        width: 30px;
    }
    .progress-bar{
        display: inline;
        padding-inline-start: 0;
        border-bottom: 1px solid #dee2e6;
    }
    .progress-bar li {
        display: inline-block !important;
        background-color: #ffffff;
        margin:0 !important;
        padding: 0;
    }

    .progress-bar .active {
        background: #dcedc8!important;
    }

    .wizard-container .nav-tabs .nav-item.show .nav-link, .nav-tabs .nav-link.active {
        /*background: #DCEDC8 !important;
        border: none;*/
    }

    .wizard-container .nav-tabs .nav-item.show .nav-link, .nav-tabs .nav-link:hover {
        background: #e4f5d0 !important;
        border: none;
    }

    .arrow_box {
        position: relative;
        background: #DCEDC8;
        border-right: 2px solid #28a745;
        border-left: none;
    }

    .arrow_box:after, .arrow_box:before {
        left: 100%;
        top: 50%;
        border: solid transparent;
        content: " ";
        height: 0;
        width: 0;
        position: absolute;
        pointer-events: none;
    }

    .arrow_box:after {
        border-color: rgba(136, 183, 213, 0);
        border-left-color: #28a745;
        border-width: 11px;
        margin-top: -11px;
    }

    .arrow_box:before {
        border-color: rgba(95, 108, 115, 0);
        border-left-color: #28a745;
        border-width: 10px;
        margin-top: -10px;
        z-index: 1 !important;
    }

    .info-button {
        float: right !important;
    }

    .help-block {
        position: absolute;
        border: none;
        right: -440px;
        z-index: 1000;
    }

    .help-block-actors {
        position: absolute;
        border: none;
        right: -440px;
        z-index: 1000;
    }

    .help-block-viz {
        width: 330px;
        position: absolute;
        border: none;
        right: -275px;
        z-index: 1000;
    }

    .help-block-actions {
        position: absolute;
        right: -450px;
        z-index: 1000;
    }

    .help-block .card-body, .help-block-actors .card-body, .help-block-actions .card-body {
        padding: 1.5rem;
    }

    .step-header {
        font-size: 18px;
        font-weight: bold;
    }

    .card-text {
        font-size: 13px;
        color: #5e6b7e;
    }

    .card-title {
        font-size: 25px;
        font-weight: bold;
        color: #5e6b7e;
        border-bottom: 2px solid #28a645;
        padding-bottom: 5px;
    }

    #step4 > article {
        flex: 1;
        height: calc(60vh - 20px);
    }

    #step4 nav,#step5 nav {
        flex: 0 0 auto;
        min-width: 200px;
        overflow: auto;
        background-color: #263238;
        height: inherit;
    }

    .item-info {
        margin-top: 5px;
        max-width: 250px;
    }

    .nav-pills .nav-link.active, .nav-pills .show > .nav-link {
        color: #fff;
        background-color: #4cae4c !important;
    }

    #step3 .nav-item a, #graph .nav-item a {
        color: #28a645;
        text-decoration: none;
        font-weight: 500;
        background-color: transparent;
        font-size: 14px;
    }

    #step3 .nav-item .nav-link.active,  #graph .nav-item .nav-link.active{
        color: #5e6b7e;
        font-weight: 500;
        background-color: #FFFFFF;
        font-size: 14px;
        border-top: 2px solid #28a645;
    }

    .btn{
        float: right;
        margin-right: 0px;
    }

    .btn.m-1{
        margin: -0.05rem !important;
    }

    .btn-next{
        color: #fff !important;
        background-color: #28a745 !important;
        border-color: #28a745 !important;
        padding: .25rem 3rem !important;
        float: right !important;
        margin-right: 0px !important;
    }

    .btn-back{
        color: #28a745 !important;
        background-color: transparent !important;
        border-color: #28a745 !important;
        padding: .25rem 3rem !important;
        float: left !important;
        margin-left: 0px !important;
    }

    .btn-outline-info{
        margin: .05rem !important;
        background-color: #FFFFFF;
        border-color: #FFF !important;
    }

    .list-group-item{
        padding: 0.5rem 1.25rem;
        font-size: 14px;
    }

    .wizard-container{
        height: 92vh;
        overflow: auto;
    }

</style>

