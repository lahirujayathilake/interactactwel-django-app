<template>
  <div class="lg-map-container">
    <l-map
      ref="myMap"
      :max-zoom="maxZoom"
      :zoom="zoom"
      :center="center"
      :options="{zoomControl: false}"
    >
      <l-control-zoom position="topright" />
      <l-tile-layer
        :url="url"
        :attribution="attribution"
      />
      <l-control-layers
        ref="layersControl"
        position="topright"
        :sort-layers="false"
      />

      <l-tile-layer
        v-for="tileProvider in tileProviders"
        :key="tileProvider.name"
        :name="tileProvider.name"
        :visible="tileProvider.visible"
        :url="tileProvider.url"
        :attribution="tileProvider.attribution"
        layer-type="base"
      />

      <l-layer-group
        layer-type="overlay"
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
        layer-type="overlay"
        name="<font size=2><strong>Drought</strong></font>"
      >
        <l-geo-json
          :geojson="geoJson_subbasin_drought"
          :options="options"
          :options-style="styleFunction_subbasin"
        />
      </l-layer-group>

      <l-layer-group
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
        layer-type="overlay"
        name="<font size=2><strong>Reservoirs</strong></font>"
      >
        <l-marker
          v-for="reservoirStation in reservoirStationList"
          :key="reservoirStation.id"
          :lat-lng.sync="reservoirStation.position"
          :icon="reservoirIcon"
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
        layer-type="overlay"
        name="<font size=2><strong>Gauging stations</strong></font>"
      >
        <l-marker
          v-for="gaugingStation in gaugingStationList"
          :key="gaugingStation.id"
          :lat-lng.sync="gaugingStation.position"
          :icon="gaugingIcon"
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
        layer-type="overlay"
        name="<font size=2><strong>Weather stations</strong></font>"
      >
        <l-marker
          v-for="weatherStation in weatherStationList"
          :key="weatherStation.id"
          :lat-lng.sync="weatherStation.position"
          :icon="wstationIcon"
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
        layer-type="overlay"
        name="<font size=2><strong>GW Restricted Areas</strong></font>"
      >
        <l-geo-json
          :geojson="geoJson_gwrestricted"
          :options-style="styleFunction_gwrestricted"
        />
      </l-layer-group>

      <l-layer-group
        layer-type="overlay"
        name="<font size=2><strong>Tribal Lands</strong></font>"
      >
        <l-geo-json
          v-if="show"
          :geojson="geoJson_triballand"
          :options-style="styleFunction_triballand"
        />
      </l-layer-group>

      <l-layer-group
        layer-type="overlay"
        name="<font size=2><strong>NOWA Pumping Limit</strong></font>"
      >
        <l-geo-json
          :geojson="geoJson_pumping_limit"
          :options-style="styleFunction_pumping_limit"
        />
      </l-layer-group>

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

import ReservoirList from "../../../../public/static/reservoirs_list.json";
import ReservoirDataJson from "../../../../public/static/reservoirs_data.json";
import GaugingStations from "../../../../public/static/gauging_stations.json";
import GaugeDataJson from "../../../../public/static/streamflow_station_data.json";
import WeatherStations from "../../../../public/static/weather_stations.json";
import PrecipDataJson from "../../../../public/static/weather_station_data.json";
import PopupContentWStations from "@/components/dashboard/projects/popup/PopupContent_WStations";
import PopupContentReservoirs from "@/components/dashboard/projects/popup/PopupContent_Reservoirs";
import PopupContentGaugeStations from "@/components/dashboard/projects/popup/PopupContent_GaugeStations";

export default {
  name: "ProjectMap",

  components: {
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
  },

  data() {
    return {

      //map settings
      zoom: 9,
      maxZoom: 17,
      center: L.latLng(45.4435777, -119.4455003),
      url: 'https://stamen-tiles-{s}.a.ssl.fastly.net/terrain/{z}/{x}/{y}{r}.png',
      attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
      tileProviders: [
        {
          name: "<font size=2><strong>Street Map</strong></font>",
          visible: false,
          attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
          url: "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
        },
        {
          name: "<font size=2><strong>Terrain Map",
          visible: false,
          attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
          url: "https://stamen-tiles-{s}.a.ssl.fastly.net/terrain/{z}/{x}/{y}{r}.png",
        },
        {
          name: "<font size=2><strong>Satellite</strong></font>",
          visible: true,
          attribution: 'Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community',
          url: "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}.png",
        },
      ],

      //geojsons
      geoJson_subbasin_drought: null,
      geoJson_reach: null,
      geoJson_gwrestricted: null,
      geoJson_triballand: null,
      geoJson_pumping_limit: null,

      //other data
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
      wstationIcon: L.icon({
        iconUrl: require('../../../../public/static/img/OSU_icon_rain_01.png'),
        iconSize: [27, 27], // size of the icon
        shadowSize: [0, 0], // size of the shadow
        iconAnchor: [0, 0], // point of the icon which will correspond to marker's location
        shadowAnchor: [0, 0], // the same for the shadow
      }),

    };
  },

  computed: {
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
  },

  created() {
    axios.get("/static/subbasins_drought.geojson")
      .then(response => {
        this.geoJson_subbasin_drought = response.data;
        this.loading = true;
      });
    axios.get("/static/reaches1.json")
      .then(response => {
        this.geoJson_reach = response.data;
        this.loading = true;
      });
    axios.get("/static/GW_Restricted_Areas_Umatilla.geojson")
      .then(response => {
        this.geoJson_gwrestricted = response.data;
        this.loading = true;
      });
    axios.get("/static/Tribal_Lands.geojson")
      .then(response => {
        this.geoJson_triballand = response.data;
        this.loading = true;
      });
    axios.get("/static/NOWA_Pumping_Limit.geojson")
      .then(response => {
        this.geoJson_pumping_limit = response.data;
        this.loading = true;
      });
  },
};
</script>

<style scoped>

</style>