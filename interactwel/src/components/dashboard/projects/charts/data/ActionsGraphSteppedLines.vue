<template>
  <div>
    <line-chart
      :chart-data="datacollection"
      :options="options"
      :width="650"
      :height="400"
    />
  </div>
</template>

<script>
import axios from 'axios';
import LineChart from "../lib/LineChart";
import chartjsPluginAnnotation from "chartjs-plugin-annotation";

export default {
  name: 'ActionsGraphSteppedLines',

  components: {
    LineChart,
  },

  data() {
    return {
      planId: "1",
      plan: null,
      JSONData: null,
      datacollection: null,
      cr_data: null,

      options: {
        responsive: true,
        legend: {
          display: true,
        },
        title: {
          display: false,
          text: 'Actions taken by each actor through time',
        },
        scales: {
          xAxes: [{
            type: 'category',
            position: 'bottom',
            scaleLabel: {
              display: true,
              labelString: 'Time',
            },
            ticks: {
              beginAtzero: false,
              stepSize: 1,
            },
          }],
          yAxes: [{
            type: 'category',
            scaleLabel: {
              display: true,
              labelString: 'Actions',
            },
            ticks: {
              beginAtZero: false,
              max: 9,
            },
            labels: ["Business as usual", "Increase amount of SW", "Decrease amount of SW", "Increase amount of GW", "Decrease amount of GW", "Increase amount of CR", "Decrease amount of CR"],
          }],
        },
      },
    };
  },
  mounted() {
    this.planId = this.$route.params.planId;
    if (!this.planId){
      this.planId = localStorage.getItem('currentPlanId');
    }
    this.adaptationPlan = this.$store.state.currentAdaptationPlan;
    localStorage.setItem('currentPlanId', '');

  },

  created(){
    axios.get("/static/BASIN_Action_Plans.json").then(response => {
      this.getPlanById(this.$route.params.planId).then(planResponse => {
        this.plan = planResponse[0];
        this.plan.plan_json = JSON.parse(this.plan.plan_json);
        console.log(this.plan.plan_json.Years);
        this.JSONData = response.data;
        this.buildDataCollection(this.plan.plan_json, this.plan.plan_json.Years, this.adaptationPlan['selectedActors'], this.planId);
      });
    });
  },

  methods: {
    buildDataCollection(data, labelsArr, selectedActors, adaptationPlan){
      console.log(data);
      let actions = data.Actions;
      this.datacollection = {
        labels: [],
        datasets: this.getChartDataFromPlanJson(data, selectedActors),
      };
      this.datacollection.labels = this.datacollection.labels.concat(labelsArr);
    },
    showChart: function(selectedPlan) {
      this.planId = selectedPlan;
    },

    getChartDataFromPlanJson: function(plan_json, selectedActors) {
      let data = [];
      for (let i = 0; i < selectedActors.length; i++) {
        let color = '#' + Math.floor(Math.random() * 16777215).toString(16);
        let data_obj = {
          label: selectedActors[i].name,
          backgroundColor: color,
          borderColor: color,
          borderJoinStyle: 'round',
          borderWidth: 6,
          data: [],
          steppedLine: true,
          fill: false,
        };
        let actorsIndexes = Object.keys(plan_json.Actors);
        let plan_json_data = plan_json[Object.keys(plan_json)[3]].Data;
        let dataRow = [];
        for (let actorIndex of actorsIndexes) {
          if ((plan_json.Actors[actorIndex].split(' ')[plan_json.Actors[actorIndex].split(' ').length - 1]) == (selectedActors[i].name.split(' ')[selectedActors[i].name.split(' ').length - 1])) {
            for (let j = 0; j < plan_json_data[actorIndex].Data.length; j++) {
              dataRow.push(plan_json['Actions'][plan_json_data[actorIndex].Data[j]]);
            }
          }
        }
        data_obj.data = dataRow;
        data.push(data_obj);
      }
      return data;
    },
  },
};
</script>