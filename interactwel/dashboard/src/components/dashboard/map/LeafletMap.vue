<template>
    <l-map ref="myMap" :zoom="zoom" :center="center">
        <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>
        <l-control-layers position="topleft" ref="layersControl" :sort-layers="true">
        </l-control-layers>

        <l-layer-group layer-type="overlay" name="<font size=4><strong>Sub-basins</strong></font>">
        <l-geo-json
                v-if="show"
                :geojson="geoJson_subbasin"
                :options="options"
                :options-style="styleFunction_subbasin"
        />
        </l-layer-group>

        <l-layer-group layer-type="overlay" name="<font size=4><strong>Streams</strong></font>">
        <l-geo-json
                v-if="show"
                :geojson="geoJson_reach"
                :options="options_noclick"
                :options-style="styleFunction_reach"
        />
        </l-layer-group>

        <l-layer-group id="wtrights" layer-type="overlay" name="<font size=4><strong>Water Rights</strong></font>">
        <l-geo-json
                v-if="show"
                :geojson="geoJson_WaterRigths"
                :options="options_wrrights"
                :options-style="styleFunction_waterrigths"
        />
        </l-layer-group>

        <l-layer-group layer-type="overlay" name="<font size=4><strong>Irrigated Land</strong></font>">
        <l-geo-json
                v-if="show"
                :geojson="geoJson_irrland"
                :options="options_noclick"
                :options-style="styleFunction_irrland"
        />
        </l-layer-group>

        <l-layer-group layer-type="overlay" name="<font size=4><strong>Reservoirs</strong></font>">
            <l-marker
                v-for="reservoirStation in reservoirStationList"
                :key="reservoirStation.id"
                :lat-lng.sync="reservoirStation.position"
                :icon="reservoirIcon"
                :visible="true" >
                <l-popup>
                    <popup-content-rs :data="reservoirStation" :pcpdata="ReservoirData"/>
                </l-popup>
            </l-marker>
        </l-layer-group>

        <l-layer-group layer-type="overlay" name="<font size=4><strong>Gauging stations</strong></font>">
            <l-marker
                v-for="gaugingStation in gaugingStationList"
                :key="gaugingStation.id"
                :lat-lng.sync="gaugingStation.position"
                :icon="gaugingIcon"
                :visible="true" >
                <l-popup>
                    <popup-content-gs :data="gaugingStation" :pcpdata="GaugeData"/>
                </l-popup>
            </l-marker>
        </l-layer-group>

        <l-layer-group layer-type="overlay" name="<font size=4><strong>Weather stations</strong></font>">
            <l-marker
                v-for="weatherStation in weatherStationList"
                :key="weatherStation.id"
                :lat-lng.sync="weatherStation.position"
                :icon="wstationIcon"
                :visible="true" >
                <l-popup>
                    <popup-content-ws :data="weatherStation" :pcpdata="PrecipData"/>
                </l-popup>
            </l-marker>
        </l-layer-group>

        <l-tile-layer
        v-for="tileProvider in tileProviders"
        :key="tileProvider.name"
        :name="tileProvider.name"
        :visible="tileProvider.visible"
        :url="tileProvider.url"
        :attribution="tileProvider.attribution"
        layer-type="base"/>

     <l-control-scale position="bottomleft" :maxWidth="200" imperial="imperial"/>
     <!--<img @click="Layerselector" src="../../../assets/water_rights_legend.png" id="WRlegend" class="map-legend">-->
     <img src="../../../assets/water_rights_legend.png" class="map-legend">
    </l-map>
    
</template>



<script>

    import {LMap, LTileLayer, LMarker, LGeoJson, LControlLayers, LControlScale, LLayerGroup, LPopup} from 'vue2-leaflet';
    import axios from 'axios';
    import L from 'leaflet';
    import EventBus from './../../../event-bus';
    import PopupContentWStations from "./popup/PopupContent_WStations";
    import PopupContentReservoirs from "./popup/PopupContent_Reservoirs";
    import PopupContentGaugeStations from "./popup/PopupContent_GaugeStations.vue"

    import PrecipDataJson from "../../../assets/weather_station_data.json";
    import ReservoirDataJson from "../../../assets/reservoirs_data.json";
    import GaugeDataJson from "../../../assets/streamflow_station_data.json";

    delete L.Icon.Default.prototype._getIconUrl;

    L.Icon.Default.mergeOptions({
        iconRetinaUrl: require('leaflet/dist/images/marker-icon-2x.png'),
        iconUrl: require('leaflet/dist/images/marker-icon.png'),
        shadowUrl: require('leaflet/dist/images/marker-shadow.png')
        });

    export default {
        name: 'Map',
        components: {
            'l-map': LMap,
            'l-tile-layer': LTileLayer,
            'l-marker': LMarker,
            'l-geo-json': LGeoJson,
            'l-control-layers': LControlLayers,
            'l-layer-group': LLayerGroup,
            'l-control-scale': LControlScale,
            'l-popup': LPopup,
            'popup-content-ws': PopupContentWStations,
            'popup-content-rs': PopupContentReservoirs,
            'popup-content-gs': PopupContentGaugeStations
        },

        data() {
            return {
                geoJson_reach: null,
                geoJson_subbasin: null,
                geoJson_reservoir: null,
                geoJson_WaterRigths: null,
                geoJson_irrland: null,
                zoom: 10,
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
                reservoirIcon: L.icon({
                        iconUrl: require('../../../assets/reservoir_trans.png'),
                        iconSize:     [37, 37], // size of the icon
                        shadowSize:   [0, 0], // size of the shadow
                        iconAnchor:   [0, 0], // point of the icon which will correspond to marker's location
                        shadowAnchor: [0, 0]  // the same for the shadow
                    }),
                wstationIcon: L.icon({
                        iconUrl: require('../../../assets/OSU_icon_rain_01.png'),
                        iconSize:     [37, 37], // size of the icon
                        shadowSize:   [0, 0], // size of the shadow
                        iconAnchor:   [0, 0], // point of the icon which will correspond to marker's location
                        shadowAnchor: [0, 0]  // the same for the shadow
                    }),

                gaugingIcon: L.icon({
                        iconUrl: require('../../../assets/OSU_icon_water.png'),
                        iconSize:     [37, 37], // size of the icon
                        shadowSize:   [0, 0], // size of the shadow
                        iconAnchor:   [0, 0], // point of the icon which will correspond to marker's location
                        shadowAnchor: [0, 0]  // the same for the shadow
                    }),

                subbasinID: null,

                PrecipData: PrecipDataJson,
                ReservoirData: ReservoirDataJson,
                GaugeData: GaugeDataJson,

                weatherStationList: [
                    {id: "1", name:'USC00353827 (Hempner, OR)', position: {lat: 45.365, lng: -119.584}, data_Range: '1/1/1940 – 12/31/2010', obs_type: 'Daily', num_Pobs: '25,840', num_Tobs: '25,832'},
                    {id: "2", name: 'USC00354161 (Ione 18 S, OR US)', position: {lat: 45.317, lng: -119.881}, data_Range: '1/1/1940 – 5/31/2010', obs_type: 'Daily', num_Pobs: '23,208', num_Tobs: '0'}
                ],

                reservoirStationList: [
                    {id: "1", name:'Willow Creek Reservoir', position: {lat: 45.346896, lng: -119.544586}, spillway_vol: '4142 ac-ft', spillway_sfarea: '125 ac', espillway_vol: '6048 ac-ft', espillway_sfarea: '158 ac',
                    release_schd0:'Jan. – Jun.: 0, 0, 0, 50, 375, 450', release_schd1:'Jul. – Dec.: 625, 550, 400, 50, 0, 0'},
                ],
                gaugingStationList: [
                    {id: "14036000", name:'WILLOW CREEK NR ARLINGTON, OREG.', position: {lat: 45.752977, lng: -120.011102}, data_Range: '1960-10 – 1979-09', obs_type: 'Daily', num_flowobs: '6938'}
                ],

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

        computed: {
            options() {
                return {
                    onEachFeature: this.onEachFeatureFunction
                };
            },
            options_noclick() {
                return {
                };
            },
            options_wrrights() {
                return {
                    onEachFeature: this.GetWRcolor
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

            GetWRcolor(){
                return (feature, layer) => {
                    if (feature.properties.WRSCI == '3'){
                        layer.setStyle({fillColor :'red'});
                    }else if (feature.properties.WRSCI == '1'){
                        layer.setStyle({fillColor :'blue'});
                    }else if (feature.properties.WRSCI == '5'){
                        layer.setStyle({fillColor :'green'});
                    }else{
                        layer.setStyle({fillColor :'black'});
                        layer.setStyle({fillOpacity: "0"});
                    }
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

                    layer.on('click', function(e){
                        EventBus.$emit('SELECTED_BASIN', feature.properties.Name);

                        var layer = e.target;
                        if (prevLayerClicked !== null || prevLayerClicked == layer) {
                            prevLayerClicked.setStyle({weight: 1.5,
                            color: "#7c7c7c",
                            opacity: 1,
                            fillColor: "#e3dddd",
                            dashArray: '5, 5',
                            dashOffset: '10',
                            fillOpacity: 0.5});
                        }
                        if (prevLayerClicked !== layer) {
                            layer.setStyle({fillColor :'blue'});
                            prevLayerClicked = layer;

                        }else{
                           prevLayerClicked = null;
                        }

                    });

                };
            }
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
            axios.get("/static/irrigated_land.geojson")
                .then(response => {
                    this.geoJson_irrland = response.data;
                    this.loading = true;
                    })
            axios.get("/static/water_rigths.geojson")
                .then(response => {
                    this.geoJson_WaterRigths = response.data;
                    this.loading = true;
                    });

        },
        methods: {
            layerClicked() {
                //alert("clicked me");
                return (feature, layer) => {

                    layer.bindPopup(this.customPopup,this.customOptions);
                    };
                
            }
            
            //Layerselector(){
                //alert('something');
                // var x = document.getElementById("WRlegend").__vue__;
                // console.log(x);
                // if (x.src == "../../../assets/water_rights_legend.png") {
                //     x.src = "none";
                // } else {
                //     x.src = "../../../assets/water_rights_legend.png";
                // }
                
            //}
        }
    };
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
    @import '../../../static/vendor/Vue2Leaflet/leaflet.css';

    .leaflet-touch .leaflet-control-layers-toggle {
        width: 60px;
        height: 60px;
    }

    .leaflet-control-scale-line {
        font-size: 14px;
        font-weight: bold;
    }

    .region_summary_popup {
        width: 300px;
        height: 300px;
    }

    #img, a {
        border: 0px transparent;
        outline: none;
    }

    .count-icon {
        background: #ff8888;
        border: 5px solid rgba(255, 255, 255, 0.5);
        color: #fff;
        font-weight: bold;
        text-align: center;
        border-radius: 50%;
        line-height: 30px;
    }

    .count-icon:hover {
        background: #bbb;
    }

    .map-legend {
        position: absolute;
        bottom: 85px;
        left: 25px;
        z-index: 500;
        width: 200px;
        height: 100px;
    }


</style>
