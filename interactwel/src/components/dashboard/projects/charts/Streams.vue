<template>
  <div
    id="graph"
    class="card"
  >
    <div class="card-body no-padding">
      <b-tabs card>
        <b-tab
          title="Groundwater"
          active
        >
          <div class="card-body">
            <b-row>
              <b-col
                lg="6"
                class="p-3"
              >
                <h6 class="baseline-graph-title text-center">
                  GWQ_reg_year
                </h6>
                <gwq-graph v-bind:base-graph="false"/>
              </b-col>
              <b-col
                lg="6"
                class="p-3"
              >
                <h6 class="baseline-graph-title text-center">
                  Business as Usual
                </h6>
                <gwq-graph v-bind:base-graph="true"/>
              </b-col>
            </b-row>
          </div>
        </b-tab>
        <b-tab title="Water Yield">
          <div class="card-body">
            <div class="card-body">
              <b-row>
                <b-col
                  lg="6"
                  class="p-3"
                >
                  <h6 class="baseline-graph-title text-center">
                    WATER YIELD_reg_year
                  </h6>
                  <water-yield-graph v-bind:base-graph="false"/>
                </b-col>
                <b-col
                  lg="6"
                  class="p-3"
                >
                  <h6 class="baseline-graph-title text-center">
                    Business as Usual
                  </h6>
                  <water-yield-graph v-bind:base-graph="true"/>
                </b-col>
              </b-row>
            </div>
          </div>
        </b-tab>
        <b-tab title="Sediment Yield">
          <div class="card-body">
            <div class="card-body">
              <b-row>
                <b-col
                  lg="6"
                  class="p-3"
                >
                  <h6 class="baseline-graph-title text-center">
                    SED_YIELD_reg_year
                  </h6>
                  <sediment-yield-graph v-bind:base-graph="false"/>
                </b-col>
                <b-col
                  lg="6"
                  class="p-3"
                >
                  <h6 class="baseline-graph-title text-center">
                    Business as Usual
                  </h6>
                  <sediment-yield-graph v-bind:base-graph="true"/>
                </b-col>
              </b-row>
            </div>
          </div>
        </b-tab>
        <b-tab title="Evapotranspiration">
          <div class="card-body">
            <div class="card-body">
              <b-row>
                <b-col
                  lg="6"
                  class="p-3"
                >
                  <h6 class="baseline-graph-title text-center">
                    ET_reg_year
                  </h6>
                  <et-graph v-bind:base-graph="false"/>
                </b-col>
                <b-col
                  lg="6"
                  class="p-3"
                >
                  <h6 class="baseline-graph-title text-center">
                    Business as Usual
                  </h6>
                  <et-graph v-bind:base-graph="true"/>
                </b-col>
              </b-row>
            </div>
          </div>
        </b-tab>
        <b-tab title="Soil Water">
          <div class="card-body">
            <div class="card-body">
              <b-row>
                <b-col
                  lg="6"
                  class="p-3"
                >
                  <h6 class="baseline-graph-title text-center">
                    SW_reg_year
                  </h6>
                  <sw-graph v-bind:base-graph="false"/>
                </b-col>
                <b-col
                  lg="6"
                  class="p-3"
                >
                  <h6 class="baseline-graph-title text-center">
                    Business as Usual
                  </h6>
                  <sw-graph v-bind:base-graph="true"/>
                </b-col>
              </b-row>
            </div>
          </div>
        </b-tab>
      </b-tabs>
    </div>
  </div>
</template>
<script>

import GwqGraph from "@/components/dashboard/projects/charts/data/gwqGraph";
import WaterYieldGraph from "@/components/dashboard/projects/charts/data/waterYieldGraph";
import SedimentYieldGraph from "@/components/dashboard/projects/charts/data/sedimentYieldGraph";
import EtGraph from "@/components/dashboard/projects/charts/data/etGraph";
import SwGraph from "@/components/dashboard/projects/charts/data/swGraph";
export default {
  name: 'Actions',
  components: {SwGraph, EtGraph, SedimentYieldGraph, WaterYieldGraph, GwqGraph},
  props: {},
  data() {
    return {};
  },
  watch: {},
  mounted() {

  },
  methods: {},
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
