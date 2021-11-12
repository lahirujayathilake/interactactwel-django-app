<template>
  <vertical-bar-chart
    :chart-data="datacollection"
    :options="options"
    :width="320"
    :height="350"
  />
</template>

<script>
import axios from 'axios';
import VerticalBarChart from "../lib/VerticalBarChart";

export default {
  name: 'waterYieldGraph',
  components: {
    VerticalBarChart,
  },
  props: {
    selectedBasinID: {
      name: String,
    },
    baseGraph: Boolean,
  },

  data() {
    return {
      planId: "1",
      JSONData: null,
      datacollection: null,
      graphColors: [
        "#27ccff",
        "#00b3eb",
        "#61cf94",
      ],
      options: {
        responsive: true,
        title: {
          display: false,
          text: 'Water yield from watershed',
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
              labelString: 'mm',
            },
          }],
        },
      },
    };
  },

  mounted() {
    this.planId = this.$route.params.planId;
    this.buildDataCollection(this.JSONData, this.planId);
  },

  created() {
    axios.get("/static/water_yield.json").then(response => {
      this.JSONData = response.data;
      this.buildDataCollection(this.JSONData, this.planId);
    });
  },

  methods: {
    buildDataCollection(data, adaptationPlan) {
      this.datacollection = {};
      this.datacollection.labels = [];
      for (let legend in data.Legend) {
        this.datacollection.labels.push(data.Legend[legend]);
      }

      this.datacollection.datasets = [];

      let dataset = {};
      dataset.data = [];
      dataset.label = data.Description;
      dataset.backgroundColor = this.getColor(0);

      let plan = this.getPlanDataById(data, adaptationPlan, this.baseGraph);

      for (let dataIndex in plan["Data"]) {
        let dataPoint = plan["Data"][dataIndex];
        dataset.data.push(dataPoint);
      }

      this.datacollection.datasets.push(dataset);

    },

    getPlanDataById(data, planId, baseGraph) {
      for (let plan in data.Adaptation_Plans) {
        let planObj = data.Adaptation_Plans[plan];
        if (baseGraph) {
          if (planObj.planId === null) {
            return data.Adaptation_Plans[plan];
          }
          continue;
        }
        if (planObj.planId == planId) {
          return data.Adaptation_Plans[plan];
        }
      }
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