<template>
  <vertical-bar-chart
    :chart-data="datacollection"
    :options="options"
    :width="320"
    :height="400"
  />
</template>
<script>
import VerticalBarChart from "../lib/VerticalBarChart";
import axios from "axios";

export default {
  name: 'OverviewWaterRightsGraph',
  components: {
    VerticalBarChart,
  },
  data() {
    return {
      planId: "1",
      JSONData: "{}",
      datacollection: null,
      graphColors: [
        "#3d71ff",
        "#00b3eb",
        "#61cf94",
      ],
      options: {
        responsive: false,
        title: {
          display: true,
          text: 'Total water rights volume (ac-ft)',
        },
        legend: {
          position: 'top',
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
              labelString: '(ac-ft)',
            },
          }],
        },
      },
    };
  },
  mounted() {

    // const {utils} = AiravataAPI;

    /*utils.FetchUtils.get("/interactwel/api/subbasins/")
      .then(JSONData => {
        this.JSONData = JSONData;
        if (this.JSONData.length > 0) {
          this.buildDataCollection(JSON.parse(this.JSONData[0].detail_json), this.planId);
        }
      })
      .catch(error => {
        alert("Could not retrieve requests. API error! " + error);
      });*/
    this.planId = this.$route.params.planId;
    this.buildDataCollection($this.JSONData, this.planId);
  },

  created(){
    axios.get("/static/BASIN_Water_Rights_plans.json").then(response => {
      this.JSONData = response.data;
      this.buildDataCollection(this.JSONData, this.planName);
    });
  },

  methods: {
    buildDataCollection(data, adaptationPlan){
      this.datacollection = {};
      this.datacollection.labels = [];
      for (let legend in data.Legend) {
        this.datacollection.labels.push(data.Legend[legend]);
      }
      this.datacollection.datasets = [];
      let i = 0;
      for (let dataIndex in data.Adaptation_plans[adaptationPlan]["Data"]) {
        let dataPoint = data.Adaptation_plans[adaptationPlan]["Data"][dataIndex];
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

    showChart: function(selectedPlan) {
      this.planName = selectedPlan;
    },

    getColor(i) {
      let color;
      color = this.graphColors[i];
      return color;
    },
  },
};
</script>
