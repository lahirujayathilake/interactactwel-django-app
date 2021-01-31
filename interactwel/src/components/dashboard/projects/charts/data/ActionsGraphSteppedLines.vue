<template>
    <div>
        <line-chart :chart-data="datacollection" :options="options" :width="650" :height="400"></line-chart>
    </div>
</template>

<script>
    import axios from 'axios';
    import LineChart from "../lib/LineChart";
    import chartjsPluginAnnotation from "chartjs-plugin-annotation";

    export default {
        name: 'actions-graph-stepped-lines',

        components: {
            LineChart
        },

        data() {
            return {
                planId: "1",
                JSONData: null,
                datacollection: null,
                cr_data: null,

                options: {
                    responsive: true,
                    legend: {
                        display: true
                    },
                    title: {
                        display: false,
                        text: 'Actions taken by each actor through time'
                    },
                    scales: {
                        xAxes: [{
                            type: 'category',
                            position: 'bottom',
                            scaleLabel: {
                                display: true,
                                labelString: 'Time'
                            },
                            ticks: {
                                beginAtzero: false,
                                stepSize: 1
                            }
                        }],
                        yAxes: [{
                            type: 'category',
                            scaleLabel: {
                                display: true,
                                labelString: 'Actions'
                            },
                            ticks: {
                                beginAtZero: false,
                                max: 9
                            },
                            labels: ["Business as usual", "Increase amount of SW", "Decrease amount of SW", "Increase amount of GW", "Decrease amount of GW", "Increase amount of CR", "Decrease amount of CR"],
                        }]
                    }
                },
            }
        },
        mounted() {
          this.planId = this.$route.params.planId;
          if (!this.planId){
            this.planId = localStorage.getItem('currentPlanId');
          }
          this.adaptationPlan = this.$store.state.currentAdaptationPlan;
          this.buildDataCollection(this.JSONData, this.planId);
          localStorage.setItem('currentPlanId','');

        },

        created(){
            axios.get("/static/BASIN_Action_Plans.json").then(response => {
                this.JSONData = response.data;
                this.buildDataCollection(this.JSONData, this.planId);
            });
        },

        methods: {
            buildDataCollection(data, adaptationPlan){
                this.datacollection = {
                    labels: ["2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010"],
                    datasets: this.getChartPlaceholderData()
                };

                for (let dataIndex in data.Adaptation_plans[adaptationPlan]["Data"]) {
                    
                    let dataPoint = data.Adaptation_plans[adaptationPlan]["Data"][dataIndex];
                    let dataset = [];

                  /**
                   * Tracked by the CR, GW or SW
                   * TODO: Track by actor ID
                   */
                  for (let selectedActorIndex in this.adaptationPlan['selectedActors']){
                    if ((dataPoint.Name.split(' ')[(dataPoint.Name.split(' ').length-1)]).replace('(','').replace(')','') == this.adaptationPlan['selectedActors'][selectedActorIndex].name.split('_')[(this.adaptationPlan['selectedActors'][selectedActorIndex].name.split('_').length-1)]) {
                      for (let dataValue in dataPoint.Data) {
                        dataset.push(dataPoint.Data[dataValue]);

                        if (dataIndex == 1){
                          this.datacollection.datasets[selectedActorIndex].data.push(dataPoint.Data[dataValue]);
                        }else if (dataIndex == 3){
                          this.datacollection.datasets[selectedActorIndex].data.push(dataPoint.Data[dataValue]);
                        }else if (dataIndex == 5){
                          this.datacollection.datasets[selectedActorIndex].data.push(dataPoint.Data[dataValue]);
                        }

                      }
                    }
                  }
                    
                }
            },
            showChart: function (selectedPlan) {
                this.planId = selectedPlan;
            },

            // TODO: remove when integration with backend, randomize colors, replace labels from input data
            getChartPlaceholderData: function () {
              let data = [{
                  label: "Farmers: Columbia River (CR)",
                  backgroundColor: "#186a3b",
                  borderColor: "#186a3b",
                  borderJoinStyle: 'round',
                  borderWidth: 6,
                  data: [],
                  steppedLine: true,
                  fill: false,
                },
                {
                  label: "Farmers: Groundwater (GW)",
                  backgroundColor: "#286bde",
                  borderColor: "#286bde",
                  borderJoinStyle: 'round',
                  borderWidth: 6,
                  data: [],
                  steppedLine: true,
                  fill: false,
                },
                {
                  label: "Farmers: Surface water (SW)",
                  fill: false,
                  backgroundColor: "#dd434e",
                  borderColor: "#dd434e",
                  borderJoinStyle: 'round',
                  borderWidth: 6,
                  data: [],
                  steppedLine: true,
                }];
              var selectedData = [];

              /**
               * Tracked by the CR, GW or SW
               * TODO: Track by actor ID
               */
              for (let dataIndex in data){
                let dataPoint = data[dataIndex];
                for (let selectedActorIndex in this.adaptationPlan['selectedActors']){
                  if ((dataPoint.label.split(' ')[(dataPoint.label.split(' ').length-1)]).replace('(','').replace(')','') == this.adaptationPlan['selectedActors'][selectedActorIndex].name.split('_')[(this.adaptationPlan['selectedActors'][selectedActorIndex].name.split('_').length-1)]) {
                    selectedData.push(data[dataIndex]);
                  }
                }
              }
              return selectedData;
            }
        }
    };
</script>