<template>
  <div>
    <component :is="component='Header'" />
    <b-container class="main"
      fluid
    >
      <b-navbar
        toggleable="sm"
        type="light"
        variant="light"
      >
        <b-navbar-toggle target="nav-text-collapse" />
        <b-navbar-brand><strong>Project :</strong></b-navbar-brand>
        <b-collapse
          id="nav-text-collapse"
          is-nav
        >
          <b-navbar-nav>
            <b-nav-text>
              <strong>{{ selectedProject.name }}</strong>
            </b-nav-text>
          </b-navbar-nav>
        </b-collapse>
        <b-button
          class="mr-2 btn-sm"
          variant="outline-secondary"
          @click="$router.push('../projects/my-projects')"
        >
          <i class="fa fa-chevron-left" /> Back to Projects
        </b-button>
      </b-navbar>
      <b-row />
      <b-row class="no-gutters">
        <b-col
          class="bg-dark pt-3"
          style="width: 240px; flex: inherit"
        >
          <div id="legend">
            <div class="list-group panel">
              <h5 class="text-light pb-2 px-3">
                Legend
              </h5>
              <div class="text-light">
                <b-form-group
                  v-slot="{ ariaDescribedby }"
                  label=""
                  class="px-3"
                >
                  <b-form-radio
                    v-model="selectedMapType"
                    :aria-describedby="ariaDescribedby"
                    name="street_map"
                    value="street_map"
                  >
                    Street Map
                  </b-form-radio>
                  <b-form-radio
                    v-model="selectedMapType"
                    :aria-describedby="ariaDescribedby"
                    name="satellite"
                    value="satellite"
                  >
                    Satellite
                  </b-form-radio>
                  <b-form-radio
                    v-model="selectedMapType"
                    :aria-describedby="ariaDescribedby"
                    name="terrain_map"
                    value="terrain_map"
                  >
                    Terrain Map
                  </b-form-radio>
                </b-form-group>
              </div>
              <div>
                <a
                  href="#default"
                  class="list-group-item bg-dark text-light font-weight-bold"
                  data-toggle="collapse"
                  data-parent="#legend"
                >Default Layers <i class="fa fa-caret-down" /></a>
                <div
                  id="default"
                  class="collapse show"
                >
                  <div class="list-group-item bg-secondary text-light">
                    <b-form-checkbox
                      id="checkbox-1"
                      v-model="sub_basins_layer_show"
                      name="checkbox-1"
                      value="checked"
                      unchecked-value="unchecked"
                    >
                      <img
                        src="../../../assets/sub_basin_ico.jpg"
                        style="width: 20px"
                      > Sub-basins
                    </b-form-checkbox>
                  </div>
                  <div class="list-group-item bg-secondary text-light">
                    <b-form-checkbox
                      id="checkbox-2"
                      v-model="streams_layer_show"
                      name="checkbox-1"
                      value="checked"
                      unchecked-value="unchecked"
                    >
                      <img
                        src="../../../assets/stream_ico.png"
                        style="width: 20px"
                      > Streams
                    </b-form-checkbox>
                  </div>
                </div>
              </div>
              <div>
                <a
                  href="#stationData"
                  class="list-group-item bg-dark font-weight-bold text-light"
                  data-toggle="collapse"
                  data-parent="#legend"
                >Station Data <i class="fa fa-caret-down" /></a>
                <div
                  id="stationData"
                  class="collapse show"
                >
                  <div class="list-group-item bg-secondary text-light">
                    <b-form-checkbox
                      id="checkbox-3"
                      v-model="reservoirs_layer_show"
                      name="checkbox-1"
                      value="checked"
                      unchecked-value="unchecked"
                    >
                      <img
                        src="../../../assets/sub_basin_ico.jpg"
                        style="width: 20px"
                      > Reservoirs
                    </b-form-checkbox>
                  </div>
                  <div class="list-group-item bg-secondary text-light">
                    <b-form-checkbox
                      id="checkbox-4"
                      v-model="gauging_stations_layer_show"
                      name="checkbox-1"
                      value="checked"
                      unchecked-value="unchecked"
                    >
                      <img
                        src="../../../assets/stream_ico.png"
                        style="width: 20px"
                      > Gauging Stations
                    </b-form-checkbox>
                  </div>
                  <div class="list-group-item bg-secondary text-light">
                    <b-form-checkbox
                      id="checkbox-5"
                      v-model="weather_stations_layer_show"
                      name="checkbox-1"
                      value="checked"
                      unchecked-value="unchecked"
                    >
                      <img
                        src="../../../assets/stream_ico.png"
                        style="width: 20px"
                      > Weather Stations
                    </b-form-checkbox>
                  </div>
                </div>
              </div>
              <div>
                <a
                  href="#additional"
                  class="list-group-item bg-dark font-weight-bold text-light"
                  data-toggle="collapse"
                  data-parent="#legend"
                >Addional Layers <i class="fa fa-caret-down" /></a>
                <div
                  id="additional"
                  class="collapse"
                >
                  <div class="list-group-item bg-secondary text-light">
                    <b-form-checkbox
                      id="checkbox-6"
                      v-model="gw_restricted_areas_layer_show"
                      name="checkbox-1"
                      value="checked"
                      unchecked-value="unchecked"
                    >
                      <img
                        src="../../../assets/stream_ico.png"
                        style="width: 20px"
                      > GW Restricted Areas
                    </b-form-checkbox>
                  </div>
                  <div class="list-group-item bg-secondary text-light">
                    <b-form-checkbox
                      id="checkbox-7"
                      v-model="tribal_lands_layer_show"
                      name="checkbox-1"
                      value="checked"
                      unchecked-value="unchecked"
                    >
                      <img
                        src="../../../assets/stream_ico.png"
                        style="width: 20px"
                      > Tribal Lands
                    </b-form-checkbox>
                  </div>
                  <div class="list-group-item bg-secondary text-light">
                    <b-form-checkbox
                      id="checkbox-8"
                      v-model="nowa_pumping_limit_layer_show"
                      name="checkbox-1"
                      value="checked"
                      unchecked-value="unchecked"
                    >
                      <img
                        src="../../../assets/stream_ico.png"
                        style="width: 20px"
                      > NOWA Pumping Limit
                    </b-form-checkbox>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </b-col>
        <b-col>
          <div class="lg-map-container">
            <l-map
              ref="myMap"
              :zoom="zoom"
              :center="center"
              :options="{zoomControl: false}"
            >
              <l-control-zoom position="topright" />
              <l-tile-layer
                :url="url"
                :attribution="attribution"
              />

              <l-tile-layer
                v-for="tileProvider in tileProviders"
                :key="tileProvider.name"
                :name="tileProvider.name"
                :visible="tileProvider.visible && tileProvider.mapType == selectedMapType"
                :url="tileProvider.url"
                :attribution="tileProvider.attribution"
                layer-type="base"
              />

              <l-layer-group
                layer-type="overlay"
                name="<font size=2 color=#5e6b7e><i><u><strong>Default Layers</strong></u></i></font>"
                @change="myFunction($event)"
              />

              <l-layer-group
                v-if="sub_basins_layer_show == 'checked'"
                layer-type="overlay"
                :visible="defaultvisibility"
                name="<font size=2><strong>Sub-basins</strong></font>"
              >
                <l-geo-json
                  v-if="show"
                  :geojson="geoJson_subbasin"
                  :options="options"
                  :options-style="styleFunction_subbasin"
                />
              </l-layer-group>

              <l-layer-group
                v-if="streams_layer_show == 'checked'"
                layer-type="overlay"
                :visible="defaultvisibility"
                name="<font size=2><strong>Streams</strong></font>"
              >
                <l-geo-json
                  v-if="show"
                  :geojson="geoJson_reach"
                  :options="options_noclick"
                  :options-style="styleFunction_reach"
                />
              </l-layer-group>

              <l-layer-group
                layer-type="overlay"
                name="<font size=2 color=#5e6b7e><i><u><strong>Station Data</strong></u></i></font>"
              />

              <l-layer-group
                v-if="reservoirs_layer_show == 'checked'"
                layer-type="overlay"
                :visible="stationvisibility"
                name="<font size=2><strong>Reservoirs</strong></font>"
              >
                <l-marker
                  v-for="reservoirStation in reservoirStationList"
                  :key="reservoirStation.id"
                  :lat-lng.sync="reservoirStation.position"
                  :icon="reservoirIcon"
                  :visible="true"
                >
                  <l-popup>
                    <popup-content-rs
                      :data="reservoirStation"
                      :pcpdata="ReservoirData"
                    />
                  </l-popup>
                </l-marker>
              </l-layer-group>

              <l-layer-group
                v-if="gauging_stations_layer_show == 'checked'"
                layer-type="overlay"
                :visible="stationvisibility"
                name="<font size=2><strong>Gauging stations</strong></font>"
              >
                <l-marker
                  v-for="gaugingStation in gaugingStationList"
                  :key="gaugingStation.id"
                  :lat-lng.sync="gaugingStation.position"
                  :icon="gaugingIcon"
                  :visible="true"
                >
                  <l-popup>
                    <popup-content-gs
                      :data="gaugingStation"
                      :pcpdata="GaugeData"
                    />
                  </l-popup>
                </l-marker>
              </l-layer-group>

              <l-layer-group
                v-if="weather_stations_layer_show == 'checked'"
                layer-type="overlay"
                :visible="stationvisibility"
                name="<font size=2><strong>Weather stations</strong></font>"
              >
                <l-marker
                  v-for="weatherStation in weatherStationList"
                  :key="weatherStation.id"
                  :lat-lng.sync="weatherStation.position"
                  :icon="wstationIcon"
                  :visible="true"
                >
                  <l-popup>
                    <popup-content-ws
                      :data="weatherStation"
                      :pcpdata="PrecipData"
                    />
                  </l-popup>
                </l-marker>
              </l-layer-group>

              <l-layer-group
                layer-type="overlay"
                name="<font size=2 color=#5e6b7e><i><u><strong>Additional Layers</strong></u></i></font>"
              />

              <l-layer-group
                v-if="gw_restricted_areas_layer_show == 'checked'"
                layer-type="overlay"
                :visible="otherlayersvisibility"
                name="<font size=2><strong>GW Restricted Areas</strong></font>"
              >
                <l-geo-json
                  v-if="show"
                  :geojson="geoJson_gwrestricted"
                  :options="options_noclick"
                  :options-style="styleFunction_gwrestricted"
                />
              </l-layer-group>

              <l-layer-group
                v-if="tribal_lands_layer_show == 'checked'"
                layer-type="overlay"
                :visible="otherlayersvisibility"
                name="<font size=2><strong>Tribal Lands</strong></font>"
              >
                <l-geo-json
                  v-if="show"
                  :geojson="geoJson_triballand"
                  :options="options_noclick"
                  :options-style="styleFunction_triballand"
                />
              </l-layer-group>

              <l-layer-group
                v-if="nowa_pumping_limit_layer_show == 'checked'"
                layer-type="overlay"
                :visible="otherlayersvisibility"
                name="<font size=2><strong>NOWA Pumping Limit</strong></font>"
              >
                <l-geo-json
                  v-if="show"
                  :geojson="geoJson_pumping_limit"
                  :options="options_noclick"
                  :options-style="styleFunction_pumping_limit"
                />
              </l-layer-group>

              <l-control-scale
                position="bottomright"
                :max-width="200"
                imperial="imperial"
              />
              <!--<img @click="Layerselector" src="../../../assets/water_rights_legend.png" id="WRlegend" class="map-legend">-->
              <!--<img src="../../../assets/water_rights_legend.png" class="map-legend">-->

              <l-control-layers
                v-if="ResultsMap"
                ref="layersControl"
                position="topright"
                :sort-layers="false"
              />
              <l-layer-group
                v-if="ResultsMap"
                ref="RegionalMap"
                layer-type="overlay"
                name="<font size=2 color=#5e6b7e><i><u><strong>Regional Results</strong></u></i></font>"
              >
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
      </b-row>
    </b-container>
    <component :is="component='Footer'" />
    <component
      :is="component='regional-summary'"
      v-show="!regionalSummaryVisibility"
    />
    <welcome
      v-show="isModalVisible"
      @close="closeModal"
    />
    <tutor-step1
      v-show="istutor1Visible"
      :class="{active: isStep1Active}"
      @continue="continuetutor"
      @close="closeTutor"
    />
    <tutor-step2
      v-show="istutor2Visible"
      :class="{active: isStep2Active}"
      @close="closeTutor"
    />
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

import {
  LMap,
  LTileLayer,
  LMarker,
  LGeoJson,
  LControlLayers,
  LControlScale,
  LLayerGroup,
  LPopup,
  LControlZoom,
} from 'vue2-leaflet';
import L from 'leaflet';

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

import paraguayGeojson from './../../../../public/static/BASIN_Irrigation_basins_data.json';
import {pyDepartmentsData} from './../../../../public/static/py-departments-data';

export default {
  name: 'Visualize',
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
        shadowAnchor: [0, 0], // the same for the shadow
      }),
      wstationIcon: L.icon({
        iconUrl: require('../../../../public/static/img/OSU_icon_rain_01.png'),
        iconSize: [27, 27], // size of the icon
        shadowSize: [0, 0], // size of the shadow
        iconAnchor: [0, 0], // point of the icon which will correspond to marker's location
        shadowAnchor: [0, 0], // the same for the shadow
      }),

      gaugingIcon: L.icon({
        iconUrl: require('../../../../public/static/img/OSU_icon_water.png'),
        iconSize: [27, 27], // size of the icon
        shadowSize: [0, 0], // size of the shadow
        iconAnchor: [0, 0], // point of the icon which will correspond to marker's location
        shadowAnchor: [0, 0], // the same for the shadow
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
          mapType: 'street_map',
          name: "<font size=2><strong>Street Map</strong></font>",
          visible: true,
          attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
          url: "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
        },
        {
          mapType: 'satellite',
          name: "<font size=2><strong>Satellite</strong></font>",
          visible: true,
          attribution: 'Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community',
          url: "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}.png",
        },
        {
          mapType: 'terrain_map',
          name: "<font size=2><strong>Terrain Map",
          visible: true,
          attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
          url: "https://stamen-tiles-{s}.a.ssl.fastly.net/terrain/{z}/{x}/{y}{r}.png",
        },
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
          'className': 'custom',
        },
      ],

      colorScale: ["e7d090", "e9ae7b", "de7062"],
      value: {
        key: "amount_w",
        metric: "% of SW Reduction",
      },
      extraValues: [{
        key: "amount_m",
        metric: "% of GW Reduction",
      }],

      mapOptions: {attributionControl: false},
      currentStrokeColor: '3d3213',
      selectedProject: {},
      selectedMapType: 'terrain_map',
      sub_basins_layer_show: 'checked',
      streams_layer_show: 'checked',
      reservoirs_layer_show: 'checked',
      gauging_stations_layer_show: 'checked',
      weather_stations_layer_show: 'checked',
      gw_restricted_areas_layer_show: 'checked',
      tribal_lands_layer_show: 'checked',
      nowa_pumping_limit_layer_show: 'checked',
    };
  },

  computed: {
    //jsonData() {
    //    return JSONData;
    //},
    options() {
      return {
        onEachFeature: this.onEachFeatureFunction,
      };
    },

    options_noclick() {
      return {};
    },

    options_wrrights() {
      return {
        onEachFeature: this.GetWRcolor,
      };
    },

    options_heatmap() {
      return {
        onEachFeature: this.getHeatMapColor_Perct,
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
          fillOpacity: 1,
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
          fillOpacity: 1,
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
          fillOpacity: 0.5,
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
          fillOpacity: 1,
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
          fillOpacity: 0.6,
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
          fillOpacity: 0.6,
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
          fillOpacity: 0.6,
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
          fillColor: '#8c2d04',
        };
      };
    },

    getHeatMapColor() {
      return (feature, layer) => {
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

      };
    },

    getHeatMapColor_Perct() {
      return (feature, layer) => {
        var subid = feature.properties[this.HeatMapProp];
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

        layer.on('click', function(e) {
        });
      };
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

        layer.on('click', function(e) {
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
              fillOpacity: 0.5,
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
    },
  },

  mounted() {
    const { utils } = AiravataAPI;
    this.projectId = this.$route.params.projectId;
    let adaptationPlan = JSON.parse(localStorage.getItem("adaptationPlan"));
    if (adaptationPlan) {
      adaptationPlan.projectId = this.projectId;
    } else {
      localStorage.setItem('adaptationPlan', JSON.stringify({'projectId': this.projectId}));
    }

    // TODO: call the /interactwel/api/projects/{project_id} to get the specific project
    utils.FetchUtils.get("/interactwel/api/projects/")
      .then(projects=>{
        this.selectedProject = projects.find(project=>{
          return project.project_id == this.projectId;
        });
      })
      .catch(error => {
        alert("Could not get the project. API error! " + error);
      });

    let $this = this;
    EventBus.$on('SELECTED_BASIN', function(selectedBasinID) {

      $this.regionalSummaryVisibility = true;

      if ($this.prevLayerClicked !== null || $this.prevLayerClicked == selectedBasinID) {
        $this.regionalSummaryVisibility = true;
      }
      if ($this.prevLayerClicked !== selectedBasinID) {
        $this.createRegionSummary(selectedBasinID);
        $this.regionalSummaryVisibility = false;
        $this.prevLayerClicked = selectedBasinID;
      } else {
        $this.regionalSummaryVisibility = true;
        $this.prevLayerClicked = null;
      }
    }), EventBus.$on('CLOSE', function() {
      $this.regionalSummaryVisibility = true;
    });

    //const map = this.$refs.myMap.mapObject;
    EventBus.$on('START_RESULTSMAP', function() {
      var active = [];
      var default_selected_layers = [];
      var i;
      active = $('.leaflet-control-layers-selector');
      for (i = 3; i < active.length; i++) {
        //if ($this.unchecked_layers.includes(active[i].labels[0].innerText)==false && active[i].checked==true){
        if (active[i].checked == true && $this.default_selected_layers.includes(active[i].labels[0].innerText) == false) {
          default_selected_layers.push(active[i].labels[0].innerText);
          $('.leaflet-control-layers-selector')[i].click();
        }
      }
      $this.ResultsMap = true;
      $this.default_selected_layers = default_selected_layers;
    }),

    EventBus.$on('START_REGIONHEATMAP', function() {
      var active = [];
      var i;
      active = $('.leaflet-control-layers-selector');
      for (i = $this.default_num_layers; i < active.length; i++) {
        if ($this.title_layers.includes(active[i].labels[0].innerText) == true) {
          $('.leaflet-control-layers-selector')[i].hidden = true;
        }
      }
      $this.RegionHeatMap = true;
    }),

    EventBus.$on('HIDE_RESULTSMAP', function() {
      var active = [];
      var i;
      active = $('.leaflet-control-layers-selector');
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
    });
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
      });
    axios.get("/static/reaches.geojson")
      .then(response => {
        this.geoJson_reach = response.data;
        this.loading = true;
      });
    axios.get("/static/NOWA_Pumping_Limit.geojson")
      .then(response => {
        this.geoJson_pumping_limit = response.data;
        this.loading = true;
      });
    axios.get("/static/irrigated_land.geojson")
      .then(response => {
        this.geoJson_irrland = response.data;
        this.loading = true;
      });
    axios.get("/static/Tribal_Lands.geojson")
      .then(response => {
        this.geoJson_triballand = response.data;
        this.loading = true;
      });

    axios.get("/static/GW_Restricted_Areas_Umatilla.geojson")
      .then(response => {
        this.geoJson_gwrestricted = response.data;
        this.loading = true;
      });

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

    closeModal() {
      this.isModalVisible = false;
      this.isStep1Active = true;
      this.istutor1Visible = true;

    },

    closeTutor() {
      this.istutor1Visible = false;
      this.istutor2Visible = false;
      this.isStep1Active = false;
      this.isStep2Active = false;
    },

    continuetutor(){
      this.isStep2Active = true;
      this.istutor1Visible = false;
      this.isStep1Active = false;
      this.istutor2Visible = true;
    },
  },

};

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
    @import '../../../assets/vendor/Vue2Leaflet/leaflet.css';
    .lg-map-container {
        height: 85vh;
        overflow: auto;
    }
    .modal-backdrop {
        position: fixed;
        top: 0;
        bottom: 0;
        left: 0;
        right: 0;
        background-color: rgba(0, 0, 0, 0.3);
        display: flex;
        justify-content: center;
        align-items: center;
    }

    #welcome-modal .modal {
        background: #FFFFFF;
        box-shadow: 2px 2px 20px 1px;
        height: auto;
        overflow: scroll;
        position: fixed;
        top: 52%;
        left: 50%;
        /* bring your own prefixes */
        transform: translate(-50%, -50%);
        max-width: 800px;
        /*overflow-x: auto;*/
        display: flex;
        flex-direction: column;
    }

    #welcome-modal .modal-header,
    #welcome-modal .modal-footer {
        padding: 15px;
        display: flex;
    }

    #welcome-modal .modal-header {
        border-bottom: 1px solid #eeeeee;
        color: #4cae4c;
        justify-content: space-between;
        font-size: 25px;
        font-weight: bold;
    }

    #welcome-modal .modal-footer {
        justify-content: flex-end;
    }

    #welcome-modal .modal-body {
        position: relative;
        padding: 30px 40px;
        font-size: 16px;
        max-height: 400px;
        overflow: auto;

    }

    .btn-close {
        border: none;
        font-size: 20px;
        padding: 20px;
        cursor: pointer;
        font-weight: bold;
        color: #4cae4c;
        background: transparent;
    }

    .btn-green {
        border: none;
        font-size: 20px;
        cursor: pointer;
        font-weight: bold;
        color: #4cae4c;
        background: transparent;
    }

    .tutor {
        background: #FFFFFF;
        box-shadow: 2px 2px 20px 1px;
        max-height: 450px;
        overflow: visible;
        /* bring your own prefixes */
        /*transform: translate(-50%, -50%);*/
        max-width: 800px;
        /*overflow-x: auto;*/
        display: flex;
        flex-direction: column;
    }

    .tutor-footer {
        display: flex;
        justify-content: flex-end;
    }

</style>

