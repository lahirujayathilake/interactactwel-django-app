<template>
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
        :visible="tileProvider.visible && tileProvider.mapType === selectedMapType"
        :url="tileProvider.url"
        :attribution="tileProvider.attribution"
        layer-type="base"
      />

      <l-layer-group
        v-if="subBasinsLayerShow === 'checked'"
        layer-type="overlay"
        name="<font size=2><strong>Sub-basins</strong></font>"
      >
        <l-geo-json
          :geojson="geoJson_subbasin"
          :options="options"
          :options-style="styleFunction_subbasin"
        />
      </l-layer-group>

      <l-layer-group
        v-if="streamsLayerShow === 'checked'"
        layer-type="overlay"
        name="<font size=2><strong>Streams</strong></font>"
      >
        <l-geo-json
          :geojson="geoJson_reach"
          :options-style="styleFunction_reach"
        />
      </l-layer-group>

      <l-layer-group
        layer-type="overlay"
        name="<font size=2 color=#5e6b7e><i><u><strong>Station Data</strong></u></i></font>"
      />

      <l-layer-group
        v-if="reservoirsLayerShow === 'checked'"
        layer-type="overlay"
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
              :pcpdata="reservoirData"
            />
          </l-popup>
        </l-marker>
      </l-layer-group>

      <l-layer-group
        v-if="gaugingStationsLayerShow === 'checked'"
        layer-type="overlay"
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
              :pcpdata="gaugeData"
            />
          </l-popup>
        </l-marker>
      </l-layer-group>

      <l-layer-group
        v-if="weatherStationsLayerShow === 'checked'"
        layer-type="overlay"
        name="<font size=2><strong>Weather stations</strong></font>"
      >
        <l-marker
          v-for="weatherStation in weatherStationList"
          :key="weatherStation.id"
          :lat-lng.sync="weatherStation.position"
          :icon="wStationIcon"
        >
          <l-popup>
            <popup-content-ws
              :data="weatherStation"
              :pcpdata="precipData"
            />
          </l-popup>
        </l-marker>
      </l-layer-group>

      <l-layer-group
        layer-type="overlay"
        name="<font size=2 color=#5e6b7e><i><u><strong>Additional Layers</strong></u></i></font>"
      />

      <l-layer-group
        v-if="gwRestrictedAreasLayerShow === 'checked'"
        layer-type="overlay"
        name="<font size=2><strong>GW Restricted Areas</strong></font>"
      >
        <l-geo-json
          :geojson="geoJson_gwrestricted"
          :options-style="styleFunction_gwrestricted"
        />
      </l-layer-group>

      <l-layer-group
        v-if="tribalLandsLayerShow == 'checked'"
        layer-type="overlay"
        name="<font size=2><strong>Tribal Lands</strong></font>"
      >
        <l-geo-json
          :geojson="geoJson_triballand"
          :options-style="styleFunction_triballand"
        />
      </l-layer-group>

      <l-layer-group
        v-if="nowaPumpingLimitLayerShow === 'checked'"
        layer-type="overlay"
        name="<font size=2><strong>NOWA Pumping Limit</strong></font>"
      >
        <l-geo-json
          :geojson="geoJson_pumping_limit"
          :options-style="styleFunction_pumping_limit"
        />
      </l-layer-group>

      <climate-scenario-map-layer />

      <l-control-scale
        position="bottomright"
        :max-width="200"
        imperial="imperial"
      />

    </l-map>
  </div>
</template>

<script>
import L from 'leaflet';
import axios from "axios";

import {
  LControlScale,
  LControlZoom,
  LGeoJson,
  LLayerGroup,
  LMap,
  LMarker,
  LPopup,
  LTileLayer,
} from "vue2-leaflet";
import PopupContentWStations from "@/components/dashboard/projects/popup/PopupContent_WStations";
import PopupContentReservoirs from "@/components/dashboard/projects/popup/PopupContent_Reservoirs";
import PopupContentGaugeStations from "@/components/dashboard/projects/popup/PopupContent_GaugeStations";
import ReservoirList from "../../../../public/static/reservoirs_list.json";
import ReservoirDataJson from "../../../../public/static/reservoirs_data.json";
import GaugingStations from "../../../../public/static/gauging_stations.json";
import GaugeDataJson from "../../../../public/static/streamflow_station_data.json";
import WeatherStations from "../../../../public/static/weather_stations.json";
import PrecipDataJson from "../../../../public/static/weather_station_data.json";
import ClimateScenarioMapLayer
  from "@/components/dashboard/projects/visualize-map-sub-components/ClimateScenarioMapLayer";

export default {
  name: "StressesMap",
  components: {
    ClimateScenarioMapLayer,
    'l-map': LMap,
    'l-tile-layer': LTileLayer,
    'l-marker': LMarker,
    'l-geo-json': LGeoJson,
    'l-layer-group': LLayerGroup,
    'l-control-scale': LControlScale,
    'l-popup': LPopup,
    'l-control-zoom': LControlZoom,
    'popup-content-ws': PopupContentWStations,
    'popup-content-rs': PopupContentReservoirs,
    'popup-content-gs': PopupContentGaugeStations,
  },
  data() {
    return {

      //map settings
      zoom: 9,
      center: L.latLng(45.4435777, -119.4455003),
      url: 'https://stamen-tiles-{s}.a.ssl.fastly.net/terrain/{z}/{x}/{y}{r}.png',
      attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
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
      selectedMapType: 'terrain_map',

      //layer visibility controls
      subBasinsLayerShow: null,
      streamsLayerShow: 'checked',
      reservoirsLayerShow: 'checked',
      gaugingStationsLayerShow: 'checked',
      weatherStationsLayerShow: 'checked',
      gwRestrictedAreasLayerShow: 'checked',
      tribalLandsLayerShow: 'checked',
      nowaPumpingLimitLayerShow: 'checked',

      //geoJsons
      geoJson_reach: null,
      geoJson_subbasin: null,
      geoJson_WaterRigths: null,
      geoJson_irrland: null,
      geoJson_triballand: null,
      geoJson_pumping_limit: null,
      geoJson_gwrestricted: null,

      reservoirStationList: ReservoirList,
      reservoirData: ReservoirDataJson,
      gaugingStationList: GaugingStations,
      gaugeData: GaugeDataJson,
      weatherStationList: WeatherStations,
      precipData: PrecipDataJson,

      //icons
      reservoirIcon: L.icon({
        iconUrl: require('../../../../public/static/img/reservoir_trans.png'),
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
      wStationIcon: L.icon({
        iconUrl: require('../../../../public/static/img/OSU_icon_rain_01.png'),
        iconSize: [27, 27], // size of the icon
        shadowSize: [0, 0], // size of the shadow
        iconAnchor: [0, 0], // point of the icon which will correspond to marker's location
        shadowAnchor: [0, 0], // the same for the shadow
      }),

    };
  },
  created() {
    this.loading = true;

    axios.get("/static/subbasins1.geojson")
      .then(response => {
        this.geoJson_subbasin = response.data;
        this.loading = true;
      });
    axios.get("/static/reaches1.json")
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
  },

  computed: {
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
  },
  methods: {
    emitWindowResizeEvent: function() {
      window.dispatchEvent(new Event('resize')); //a hack to get rid of map partially showing issue
    },
  },

  mounted() {
    setInterval(() => this.emitWindowResizeEvent(), 500);
  },

};
</script>

<style scoped>

</style>