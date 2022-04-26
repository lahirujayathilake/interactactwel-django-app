<template>
  <div v-if="!loading">
    <l-layer-group
      v-if="selectedClimateScenario === 'NUM_DR_sub'"
      layer-type="overlay"
      name="<font size=2><strong>Sub-basins</strong></font>"
    >
      <l-geo-json
        :geojson="geoJson"
        :options-style="styleFunctionChoroplethDroughtEvents"
      />
    </l-layer-group>
    <l-layer-group
      v-if="selectedClimateScenario === 'DURAVG_sub'"
      layer-type="overlay"
      name="<font size=2><strong>Sub-basins</strong></font>"
    >
      <l-geo-json
        :geojson="geoJson"
        :options-style="styleFunctionChoroplethMaxDuration"
      />
    </l-layer-group>
    <l-layer-group
      v-if="selectedClimateScenario === 'NUMEX_sub'"
      layer-type="overlay"
      name="<font size=2><strong>Sub-basins</strong></font>"
    >
      <l-geo-json
        :geojson="geoJson"
        :options-style="styleFunctionChoroplethAveDuration"
      />
    </l-layer-group>
    <l-control
      :position="'bottomright'"
      class="custom-control-watermark"
    >
      <div style="background-color: #FFFFFF; padding: 1rem;">
        <h6>{{ selectedClimateScenarioName }}</h6>
        <p>({{ displayUnit }})</p>
        <ul style="list-style-type: none; padding-left: 1rem">
          <li
            v-for="grade in grades"
            :key="grade.color"
          >
            <span
              style="height: 10px; width: 10px; margin-right: 10px; display: inline-block"
              :style="{'background-color':grade.color}"
            />
            <span v-html="grade.start !== null ? grade.start : ' < '" />
            <span>{{ grade.start !== null && grade.end !== null ? ' - ' : '' }}</span>
            <span v-html="grade.end !== null ? grade.end : ' < '" />
          </li>
        </ul>
      </div>
    </l-control>
  </div>
</template>

<script>
import axios from "axios";
import {LControl, LGeoJson, LLayerGroup} from "vue2-leaflet";
import EventBus from "@/event-bus";

export default {
  name: "ClimateScenarioMapLayer",
  components: {
    'l-geo-json': LGeoJson,
    'l-layer-group': LLayerGroup,
    'l-control': LControl,
  },

  data() {
    return {
      geoJson: null,
      loading: true,
      selectedOption: '',

      climateScenarios: [
        {id: 'NUM_DR_sub', name: 'Number of Drought Events'},
        {id: 'DURAVG_sub', name: 'Average Drought Duration'},
        {id: 'NUMEX_sub', name: ' No. of Extreme & Exceptional Drought Months '},
      ],
      colors: [
        "#2a2837",
        "#3f4f59",
        "#567068",
        "#9cb6ad",
        "#daddcf",
        "#fee08b",
        "#ffd711",
        "#ee925e",
        "#ff5f08",
        "#ff233c",
        "#7c0808",
      ],
    };
  },
  computed: {

    selectedClimateScenario: function() {
      return this.selectedOption.substr(this.selectedOption.indexOf('-') + 1) || 'NUM_DR_sub';
    },

    selectedClimateScenarioName() {
      return this.climateScenarios.find( scenario => scenario.id === this.selectedClimateScenario).name;
    },

    geoJsonName: function() {
      return (this.selectedOption.substr(0, this.selectedOption.indexOf('-')) || 'SPI_historical') + '.geojson';
    },

    grades: function() {
      if (!this.geoJson) {
        return [];
      }
      const properties = this.geoJson.features[0].properties;
      const min = properties['MIN_' + this.selectedClimateScenario];
      const max = properties['MAX_' + this.selectedClimateScenario];
      const step = (max - min) / 10;
      return this.colors.map(function(color, index) {
        return {
          "start": (min + step * index).toFixed(3),
          "end": (min + step * (index + 1)).toFixed(3),
          "color": color,
        };
      });
    },

    displayUnit: function() {
      if (!this.geoJson) {
        return '';
      }
      return this.geoJson.features[0].properties['UNITS_' + this.selectedClimateScenario];
    },

    styleFunctionChoroplethDroughtEvents() {
      let $this = this;
      return function(feature) {
        return $this.getStylesForClimateScenario(feature, 'NUM_DR_sub');
      };
    },

    styleFunctionChoroplethMaxDuration() {
      let $this = this;
      return function(feature) {
        return $this.getStylesForClimateScenario(feature, 'DURAVG_sub');
      };
    },

    styleFunctionChoroplethAveDuration() {
      let $this = this;
      return function(feature) {
        return $this.getStylesForClimateScenario(feature, 'NUMEX_sub');
      };
    },
  },

  watch: {
    geoJsonName: function(geoJsonFileName) {
      this.loading = true;
      axios.get("/static/drought/" + geoJsonFileName)
        .then(response => {
          this.geoJson = response.data;
          this.loading = false;
        });
    },
  },

  created() {
    axios.get("/static/drought/SPI_historical.geojson")
      .then(response => {
        this.geoJson = response.data;
        this.loading = false;
      });

    let $this = this;
    EventBus.$on('SELECTED_CLIMATE_SCENARIO_OPTION', function(value) {
      $this.selectedOption = value;
    });
  },

  methods: {
    getStylesForClimateScenario(feature, climateScenario) {
      return {
        weight: 1.5,
        color: "#9f1414",
        opacity: 1,
        fillColor: this.getColor(feature.properties[climateScenario]),
        dashArray: '5, 5',
        dashOffset: '10',
        fillOpacity: 1,
      };
    },

    getColor(value) {
      for (const cGrade of this.grades) {
        if (cGrade.start === null && cGrade.end >= value) {
          return cGrade.color;
        }
        if (cGrade.end === null && cGrade.start <= value) {
          return cGrade.color;
        }
        if (cGrade.start <= value && cGrade.end >= value) {
          return cGrade.color;
        }
      }
      return '#FFEDA0';
    },
  },

};
</script>

<style scoped>

</style>