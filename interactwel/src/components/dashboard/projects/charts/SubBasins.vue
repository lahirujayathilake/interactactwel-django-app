<template>
  <div
    id="graph"
    class="card"
  >
    <div class="card-header">
      <div class="row">
        <div class="col-8">
          <strong>Sub-basins</strong>
        </div>
        <div class="col-4">
          <div class="form-group">
            <v-select
              :options="options"
              v-model="selectedSubBasin"
            >
            </v-select>
          </div>
        </div>
      </div>
    </div>
    <div class="card-body no-padding">
      <b-tabs card>
        <b-tab title="NO3 - Lateral Flow"
               active>
          <div class="card-body">
            <b-row>
              <b-col
                lg="6"
              >
                <h6 class="baseline-graph-title text-center">
                  Action Plan {{ $route.params.planId }}
                </h6>
            <latq-sub-graph :selected-basin-id="selectedSubBasin.code" v-bind:base-graph="false"></latq-sub-graph>
              </b-col>
              <b-col
                lg="6"
              >
                <h6 class="baseline-graph-title text-center">
                  Business as Usual
                </h6>
                <latq-sub-graph :selected-basin-id="selectedSubBasin.code" v-bind:base-graph="true"></latq-sub-graph>
              </b-col>
            </b-row>
          </div>
        </b-tab>
        <b-tab title="NO3 - Surface Runoff">
          <div class="card-body">
            <b-row>
              <b-col
                  lg="6"
              >
                <h6 class="baseline-graph-title text-center">
                  Action Plan {{ $route.params.planId }}
                </h6>

              </b-col>
              <b-col
                  lg="6"
              >
                <h6 class="baseline-graph-title text-center">
                  Business as Usual
                </h6>

              </b-col>
            </b-row>
          </div>
        </b-tab>
        <b-tab title="Sediment Yield">
          <div class="card-body">
            <b-row>
              <b-col
                  lg="6"
              >
                <h6 class="baseline-graph-title text-center">
                  Action Plan {{ $route.params.planId }}
                </h6>

              </b-col>
              <b-col
                  lg="6"
              >
                <h6 class="baseline-graph-title text-center">
                  Business as Usual
                </h6>

              </b-col>
            </b-row>
          </div>
        </b-tab>
        <b-tab title="Percolation to Aquifers">
          <div class="card-body">
            <b-row>
              <b-col
                  lg="6"
              >
                <h6 class="baseline-graph-title text-center">
                  Action Plan {{ $route.params.planId }}
                </h6>

              </b-col>
              <b-col
                  lg="6"
              >
                <h6 class="baseline-graph-title text-center">
                  Business as Usual
                </h6>

              </b-col>
            </b-row>
          </div>
        </b-tab>
        <b-tab title="Soil Water">
          <div class="card-body">
            <b-row>
              <b-col
                  lg="6"
              >
                <h6 class="baseline-graph-title text-center">
                  Action Plan {{ $route.params.planId }}
                </h6>

              </b-col>
              <b-col
                  lg="6"
              >
                <h6 class="baseline-graph-title text-center">
                  Business as Usual
                </h6>

              </b-col>
            </b-row>
          </div>
        </b-tab>
        <b-tab title="Evapotranspiration">
          <div class="card-body">
            <b-row>
              <b-col
                  lg="6"
              >
                <h6 class="baseline-graph-title text-center">
                  Action Plan {{ $route.params.planId }}
                </h6>

              </b-col>
              <b-col
                  lg="6"
              >
                <h6 class="baseline-graph-title text-center">
                  Business as Usual
                </h6>

              </b-col>
            </b-row>
          </div>
        </b-tab>
        <b-tab title="Groundwater to Stream">
          <div class="card-body">
            <b-row>
              <b-col
                  lg="6"
              >
                <h6 class="baseline-graph-title text-center">
                  Action Plan {{ $route.params.planId }}
                </h6>

              </b-col>
              <b-col
                  lg="6"
              >
                <h6 class="baseline-graph-title text-center">
                  Business as Usual
                </h6>

              </b-col>
            </b-row>
          </div>
        </b-tab>
        <b-tab title="Water Yield">
          <div class="card-body">
            <b-row>
              <b-col
                  lg="6"
              >
                <h6 class="baseline-graph-title text-center">
                  Action Plan {{ $route.params.planId }}
                </h6>

              </b-col>
              <b-col
                  lg="6"
              >
                <h6 class="baseline-graph-title text-center">
                  Business as Usual
                </h6>

              </b-col>
            </b-row>
          </div>
        </b-tab>
        <b-tab title="Precipitation ">
        <div class="card-body">
          <b-row>
            <b-col
                lg="6"
            >
              <h6 class="baseline-graph-title text-center">
                Action Plan {{ $route.params.planId }}
              </h6>

            </b-col>
            <b-col
                lg="6"
            >
              <h6 class="baseline-graph-title text-center">
                Business as Usual
              </h6>

            </b-col>
          </b-row>
        </div>
      </b-tab>

      </b-tabs>
    </div>
  </div>
</template>

<script>

import EventBus from './../../../../event-bus';
import axios from 'axios';
import VerticalBarChart from "./lib/VerticalBarChart";
import LatqSubGraph from "@/components/dashboard/projects/charts/data/latqSubGraph";

export default {
  name: 'SubBasins',

  components: {
    LatqSubGraph,
  },

  data() {
    return {
      selectedSubBasin: {label: 'Sub-basin: 1', code: '1'},
      planName: 'Adaptation Plan 1',
      JSONData: null,
      options: [
        {label: 'Sub-basin: 1', code: '1'},
        {label: 'Sub-basin: 2', code: '2'},
        {label: 'Sub-basin: 3', code: '3'},
        {label: 'Sub-basin: 4', code: '4'},
        {label: 'Sub-basin: 6', code: '6'},
        {label: 'Sub-basin: 7', code: '7'},
        {label: 'Sub-basin: 8', code: '8'},
        {label: 'Sub-basin: 9', code: '9'},
        {label: 'Sub-basin: 10', code: '10'},
        {label: 'Sub-basin: 11', code: '11'},
        {label: 'Sub-basin: 100', code: '100'},
        {label: 'Sub-basin: 101', code: '101'},
        {label: 'Sub-basin: 102', code: '102'},
        {label: 'Sub-basin: 103', code: '103'},
        {label: 'Sub-basin: 104', code: '104'},
        {label: 'Sub-basin: 105', code: '105'},
      ],
      datacollection: null,
      graphColors: [
        "#3d71ff",
        "#00b3eb",
        "#61cf94",
      ],
      optionsirr: {
        responsive: true,
        title: {
          display: true,
          text: 'Irrigation - Yearly totals per water source',
        },
        tooltips: {
          mode: 'point',
          intersect: false,
        },
        hover: {
          mode: 'nearest',
          intersect: true,
        },
        scales: {
          xAxes: [{
            display: true,
            stacked: false,
            scaleLabel: {
              display: true,
              labelString: 'Years',
            },
          }],
          yAxes: [{
            display: true,
            stacked: false,
            scaleLabel: {
              display: true,
              labelString: 'acre-ft',
            },
          }],
        },
      },
    };
  },
  computed: {},

  mounted() {
    let $this = this;
    EventBus.$on('CLICK_ITEM_SIDEBAR', function(planName) {
      $this.planName = planName;
      $this.buildDataCollection($this.JSONData, $this.planName, $this.selectedSubBasin.code);
    });

  },

  created() {
    axios.get("/static/BASIN_Irrigation_basins_data.json").then(response => {
      this.JSONData = response.data;
      this.buildDataCollection(this.JSONData, this.planName, this.selectedSubBasin.code);
    });
  },

  methods: {
    dismiss() {
      EventBus.$emit('CLOSE');
    },

    buildDataCollection(data, adaptationPlan, basinID) {
      this.datacollection = {};
      this.datacollection.labels = [];
      for (let legend in data.Legend) {
        this.datacollection.labels.push(data.Legend[legend]);
      }
      this.datacollection.datasets = [];
      let i = 0;
      for (let dataIndex in data.Adaptation_plans[adaptationPlan][basinID]["Data"]) {
        let dataPoint = data.Adaptation_plans[adaptationPlan][basinID]["Data"][dataIndex];
        let dataset = {};
        dataset.label = dataPoint.Name;
        dataset.backgroundColor = this.getColor(i++);
        dataset.data = [];
        for (let dataValue in dataPoint.Data) {
          dataset.data.push(dataPoint.Data[dataValue]);
        }
        this.datacollection.datasets.push(dataset);
      }
      i++;
    },

    getColor(i) {
      let color;
      color = this.graphColors[i];
      return color;
    },

  },
  //props: ["jsonData"]

};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
