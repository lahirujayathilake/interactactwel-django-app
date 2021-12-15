<template>
  <div
    id="graph"
    class="card"
  >
    <div class="card-body no-padding">
      <b-tabs card>
<!--        <b-tab
          title="Water Rights"
          active
        >
          <div class="card-body no-padding">
            <b-row>
              <b-col
                lg="6"
                class="action-graph-container"
              >
                <h6 class="baseline-graph-title">
                  Action Plan {{ $route.params.planId }}
                </h6>
                <overview-water-rights-graph />
              </b-col>
              <b-col
                lg="6"
                class="action-graph-container"
              >
                <h6 class="baseline-graph-title">
                  Business as Usual
                </h6>
                <overview-base-water-rights-graph />
              </b-col>
            </b-row>
          </div>
        </b-tab>-->
        <b-tab title="Crop yield">
          <div class="card-body no-padding">
            <b-row>
              <b-col
                lg="6"
                class="action-graph-container"
              >
                <h6 class="baseline-graph-title">
                  Action Plan {{ $route.params.planId }}
                </h6>
                <crop-yield-graph />
              </b-col>
              <b-col
                lg="6"
                class="action-graph-container"
              >
                <h6 class="baseline-graph-title">
                  Business as Usual
                </h6>
                <base-crop-yield-graph />
              </b-col>
            </b-row>
          </div>
        </b-tab>
        <b-tab title="N fertilizer">
          <div class="card-body no-padding">
            <b-row>
              <b-col lg="6">
                <h6 class="baseline-graph-title">
                  Action Plan {{ $route.params.planId }}
                </h6>
                <n-fertilizer-graph />
              </b-col>
              <b-col
                lg="6"
                class="baseline-graph-container"
              >
                <h6 class="baseline-graph-title">
                  Business as Usual
                </h6>
                <n-fertilizer-graph />
              </b-col>
            </b-row>
          </div>
        </b-tab>
        <b-tab title="P fertilizer">
          <div class="card-body no-padding">
            <b-row>
              <b-col lg="6">
                <h6 class="baseline-graph-title">
                  Action Plan {{ $route.params.planId }}
                </h6>
                <p-fertilizer-graph />
              </b-col>
              <b-col
                lg="6"
                class="baseline-graph-container"
              >
                <h6 class="baseline-graph-title">
                  Business as Usual
                </h6>
                <p-fertilizer-graph />
              </b-col>
            </b-row>
          </div>
        </b-tab>
        <b-tab title="Irrigation">
          <div class="card-body no-padding">
            <b-row>
              <b-col lg="6">
                <h6 class="baseline-graph-title">
                  Action Plan {{ $route.params.planId }}
                </h6>
                <irrigation-graph />
              </b-col>
              <b-col
                lg="6"
                class="baseline-graph-container"
              >
                <h6 class="baseline-graph-title">
                  Business as Usual
                </h6>
                <irrigation-base-line-graph />
              </b-col>
            </b-row>
          </div>
        </b-tab>
        <b-tab title="NO3 Percolation">
          <div class="card-body no-padding">
            <b-row>
              <b-col lg="6">
                <h6 class="baseline-graph-title">
                  Action Plan {{ $route.params.planId }}
                </h6>
                <no3-perc-graph v-bind:base-graph="false"/>
              </b-col>
              <b-col
                lg="6"
                class="baseline-graph-container"
              >
                <h6 class="baseline-graph-title">
                  Business as Usual
                </h6>
                <no3-perc-graph v-bind:base-graph="true"/>
              </b-col>
            </b-row>
          </div>
        </b-tab>
        <b-tab title="Nitrogen Plant Uptake">
          <div class="card-body no-padding">
            <b-row>
              <b-col lg="6">
                <h6 class="baseline-graph-title">
                  Action Plan {{ $route.params.planId }}
                </h6>
                <no3-crop-graph v-bind:base-graph="false"/>
              </b-col>
              <b-col
                lg="6"
                class="baseline-graph-container"
              >
                <h6 class="baseline-graph-title">
                  Business as Usual
                </h6>
                <no3-crop-graph v-bind:base-graph="true"/>
              </b-col>
            </b-row>
          </div>
        </b-tab>
        <b-tab title="Groundwater to Stream">
          <div class="card-body">
            <b-row>
              <b-col
                  lg="6"
                  class="p-3"
              >
                <h6 class="baseline-graph-title text-center">
                  Action Plan {{ $route.params.planId }}
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
                    Action Plan {{ $route.params.planId }}
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
                    Action Plan {{ $route.params.planId }}
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
                    Action Plan {{ $route.params.planId }}
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
                    Action Plan {{ $route.params.planId }}
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
        <b-tab title="NO3 - Percolated to Aquifer">
          <div class="card-body">
            <div class="card-body">
              <b-row>
                <b-col
                    lg="6"
                    class="p-3"
                >
                  <h6 class="baseline-graph-title text-center">
                    Action Plan {{ $route.params.planId }}
                  </h6>

                </b-col>
                <b-col
                    lg="6"
                    class="p-3"
                >
                  <h6 class="baseline-graph-title text-center">
                    Business as Usual
                  </h6>

                </b-col>
              </b-row>
            </div>
          </div>
        </b-tab>
        <b-tab title="NO3 - Surface Runoff">
          <div class="card-body">
            <div class="card-body">
              <b-row>
                <b-col
                    lg="6"
                    class="p-3"
                >
                  <h6 class="baseline-graph-title text-center">
                    Action Plan {{ $route.params.planId }}
                  </h6>

                </b-col>
                <b-col
                    lg="6"
                    class="p-3"
                >
                  <h6 class="baseline-graph-title text-center">
                    Business as Usual
                  </h6>

                </b-col>
              </b-row>
            </div>
          </div>
        </b-tab>
        <b-tab title="NO3 - Lateral Flow">
          <div class="card-body">
            <div class="card-body">
              <b-row>
                <b-col
                    lg="6"
                    class="p-3"
                >
                  <h6 class="baseline-graph-title text-center">
                    Action Plan {{ $route.params.planId }}
                  </h6>

                </b-col>
                <b-col
                    lg="6"
                    class="p-3"
                >
                  <h6 class="baseline-graph-title text-center">
                    Business as Usual
                  </h6>

                </b-col>
              </b-row>
            </div>
          </div>
        </b-tab>
        <b-tab title="Percolation to Aquifers">
          <div class="card-body">
            <div class="card-body">
              <b-row>
                <b-col
                    lg="6"
                    class="p-3"
                >
                  <h6 class="baseline-graph-title text-center">
                    Action Plan {{ $route.params.planId }}
                  </h6>

                </b-col>
                <b-col
                    lg="6"
                    class="p-3"
                >
                  <h6 class="baseline-graph-title text-center">
                    Business as Usual
                  </h6>

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
import JSONData from "../../../../../public/static/result_action_plans.json";
import IrrigationGraph from './data/IrrigationGraph.vue';
import CropYieldGraph from './data/CropYieldGraph.vue';
import BaseCropYieldGraph from './data/BaseCropYieldGraph.vue';
import NFertilizerGraph from './data/NFertilizerGraph.vue';
import PFertilizerGraph from './data/PFertilizerGraph.vue';
import OverviewWaterRightsGraph from './data/OverviewWaterRightsGraph.vue';
import OverviewBaseWaterRightsGraph from './data/OverviewBaseWaterRightsGraph.vue';
import EventBus from './../../../../event-bus';
import IrrigationBaseLineGraph from "./data/IrrigationBaselineGraph";
import GwqGraph from "@/components/dashboard/projects/charts/data/gwqGraph";
import No3PercGraph from "@/components/dashboard/projects/charts/data/no3PercGraph";
import No3CropGraph from "@/components/dashboard/projects/charts/data/no3CropGraph";
import SwGraph from "@/components/dashboard/projects/charts/data/swGraph";
import EtGraph from "@/components/dashboard/projects/charts/data/etGraph";
import SedimentYieldGraph from "@/components/dashboard/projects/charts/data/sedimentYieldGraph";
import WaterYieldGraph from "@/components/dashboard/projects/charts/data/waterYieldGraph";

export default {
  name: 'Region',

  components: {
    No3CropGraph,
    No3PercGraph,
    GwqGraph,SwGraph, EtGraph, SedimentYieldGraph, WaterYieldGraph,
    IrrigationBaseLineGraph,
    'irrigationGraph': IrrigationGraph,
    'cropYieldGraph': CropYieldGraph,
    'BaseCropYieldGraph': BaseCropYieldGraph,
    'nFertilizerGraph': NFertilizerGraph,
    'pFertilizerGraph': PFertilizerGraph,
    'overviewWaterRightsGraph': OverviewWaterRightsGraph,
    'OverviewBaseWaterRightsGraph': OverviewBaseWaterRightsGraph,
  },

  data() {
    return {};
  },
  computed: {
    jsonData() {
      return JSONData;
    },

    graphData() {
      var adaptationPlan = this.planName;

      return Object.keys(this.jsonData["Adaptation_plans"][adaptationPlan])
        .map(key => {
          return {
            key: key,
            value: this.jsonData["Adaptation_plans"][adaptationPlan][key],
          };
        })
        .filter(d => {
          if (this.selectedKeyList.findIndex(k => k === d.key) > -1) {
            return true;
          } else {
            return false;
          }
        });

    },
  },

  mounted() {
  },

  methods: {
    dismiss() {
      EventBus.$emit('CLOSE');
    },
  },
  //props: ["jsonData"]

};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
.baseline-graph-title{
    background-color: #6c757d;
    padding: 5px;
    text-align: center;
    color: #FFF;
    font-size: 12px;
}

.action-graph-title{
    background-color: #6c757d;
    padding: 5px;
    text-align: center;
    color: #FFF;
    font-size: 12px;
}
</style>
