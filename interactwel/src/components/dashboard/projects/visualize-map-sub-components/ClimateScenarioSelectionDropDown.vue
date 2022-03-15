<template>
  <div>
    <div
      v-for="climateScenarioOption in climateScenarioOptions"
      :key="climateScenarioOption.fileNamePrefix"
    >
      <a
        :href="'#' + climateScenarioOption.fileNamePrefix"
        class="list-group-item bg-dark font-weight-bold text-light"
        data-toggle="collapse"
        data-parent="#legend"
      >
        {{ climateScenarioOption.title }}
        <i class="fa fa-caret-down" />
      </a>
      <div
        :id=climateScenarioOption.fileNamePrefix
        class="collapse"
      >
        <div>
          <!-- SPI -->
          <div class="list-group-item bg-secondary text-light">
            <p>Standardized Precipitation Index (Meteorological Drought)</p>
            <b-form-group
              label=""
              class="px-3"
            >
              <b-form-radio
                v-model="selectedClimateScenario"
                name="SPI - Total drought events"
                :value="'SPI_' + climateScenarioOption.fileNamePrefix + '-NUM_DR_sub'"
              >
                Number of Drought Events
              </b-form-radio>
              <b-form-radio
                v-model="selectedClimateScenario"
                name="SPI - Average Duration"
                :value="'SPI_' + climateScenarioOption.fileNamePrefix + '-DURAVG_sub'"
              >
                Average Drought Duration
              </b-form-radio>
              <b-form-radio
                v-model="selectedClimateScenario"
                name="SPI - No. of Extreme & Exceptional Drought Months"
                :value="'SPI_' + climateScenarioOption.fileNamePrefix + '-NUMEX_sub'"
              >
                No. of Extreme & Exceptional Drought Months
              </b-form-radio>
            </b-form-group>
          </div>

          <!-- SSI -->
          <div class="list-group-item bg-secondary text-light">
            <p>Standardized Soil-moisture Index (Agricultural Drought)</p>
            <b-form-group
              label=""
              class="px-3"
            >
              <b-form-radio
                v-model="selectedClimateScenario"
                name="SSI - Total drought events"
                :value="'SSI_' + climateScenarioOption.fileNamePrefix + '-NUM_DR_sub'"
              >
                Number of Drought Events
              </b-form-radio>
              <b-form-radio
                v-model="selectedClimateScenario"
                name="SSI - Average Duration"
                :value="'SSI_' + climateScenarioOption.fileNamePrefix + '-DURAVG_sub'"
              >
                Average Drought Duration
              </b-form-radio>
              <b-form-radio
                v-model="selectedClimateScenario"
                name="SSI - No. of Extreme & Exceptional Drought Months"
                :value="'SSI_' + climateScenarioOption.fileNamePrefix + '-NUMEX_sub'"
              >
                No. of Extreme & Exceptional Drought Months
              </b-form-radio>
            </b-form-group>
          </div>

          <!-- SRI -->
          <div class="list-group-item bg-secondary text-light">
            <p>Standardized Runoff Index (Hydrological Drought)</p>
            <b-form-group
              label=""
              class="px-3"
            >
              <b-form-radio
                v-model="selectedClimateScenario"
                name="SRI - Total drought events"
                :value="'SRI_' + climateScenarioOption.fileNamePrefix + '-NUM_DR_sub'"
              >
                Number of Drought Events
              </b-form-radio>
              <b-form-radio
                v-model="selectedClimateScenario"
                name="SRI - Average Duration"
                :value="'SRI_' + climateScenarioOption.fileNamePrefix + '-DURAVG_sub'"
              >
                Average Drought Duration
              </b-form-radio>
              <b-form-radio
                v-model="selectedClimateScenario"
                name="SRI - No. of Extreme & Exceptional Drought Months"
                :value="'SRI_' + climateScenarioOption.fileNamePrefix + '-NUMEX_sub'"
              >
                No. of Extreme & Exceptional Drought Months
              </b-form-radio>
            </b-form-group>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import EventBus from "@/event-bus";

export default {
  name: "ClimateScenarioSelectionDropDown",
  data() {
    return {
      selectedClimateScenario: String,
      climateScenarioOptions: [
        {
          title: '1981-2006 Historical',
          fileNamePrefix: 'historical',
        },
        {
          title: '2030-2059 RCP 4.5 Ensemble Average',
          fileNamePrefix: 'rcp45_40s',
        },
        {
          title: '2030-2059 RCP 8.5 Ensemble Average',
          fileNamePrefix: 'rcp85_40s',
        },
        {
          title: '2070 - 2099 RCP 4.5 Ensemble Average',
          fileNamePrefix: 'rcp45_80s',
        },
        {
          title: '2070 - 2099 RCP 8.5 Ensemble Average',
          fileNamePrefix: 'rcp85_80s',
        },
      ],
    };
  },
  watch: {
    selectedClimateScenario: function(value) {
      EventBus.$emit('SELECTED_CLIMATE_SCENARIO_OPTION', value);
    },
  },
};
</script>

<style scoped>

</style>