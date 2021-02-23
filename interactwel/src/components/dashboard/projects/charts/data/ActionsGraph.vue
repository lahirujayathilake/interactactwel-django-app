<template>
    <div>
      <i class="fas fa-2x fa-search-plus" @click="showActionsGraph()"></i>
      <actions-graph-modal v-show="isModalVisible" @close="closeModal"/>
      <line-chart :chart-data="datacollection" :options="options" :width="650" :height="400"></line-chart>
    </div>
</template>

<script>
    import axios from 'axios';
    import ActionsGraphModal from './../../intro/ActionsGraphModal.vue';
    import LineChart from "../lib/LineChart";
    import chartjsPluginAnnotation from "chartjs-plugin-annotation";

    export default {
        name: 'actions-graph-stepped-lines',

        components: {
            LineChart, ActionsGraphModal
        },

        data() {
            return {
                isModalVisible: false,
                planId: "1",
                JSONData: null,
                datacollection: null,
                cr_data: null,

              options: {
                hover: {
                  mode: 'dataset'
                },
                elements: {
                  line: {
                    tension: 0 // disables bezier curves
                  },
                  point: {
                    hitRadius: 10
                  }
                },
                responsive: true,
                legend: {
                  display: true
                },
                title: {
                  display: true,
                  text: 'Actions taken by each actor through time'
                },
                scales: {
                  //type: 'category',
                  xAxes: [{
                    gridLines: {
                      display: false,
                    },
                    scaleLabel: {
                      display: true,
                      labelString: 'Time'
                    },
                    position: 'bottom',
                    ticks: {
                      beginAtzero: false,
                      stepSize: 1
                    }
                  }],

                  yAxes: [{
                    gridLines: {
                      drawBorder: false,
                    },
                    //type: 'category',
                    scaleLabel: {
                      display: true,
                      labelString: 'Actions'
                    },
                    ticks: {
                      beginAtZero: false,
                      max: 10
                    },
                    //labels: ["Business as usual", "Increase amount of SW", "Decrease amount of SW", "Increase amount of GW", "Decrease amount of GW", "Increase amount of CR", "Decrease amount of CR"],
                  }]
                }
              }
            }
        },
        mounted() {

          this.planId = this.$route.params.planId;
          if (!this.planId){
            this.planId = localStorage.getItem('currentPlanId');
          }
          this.adaptationPlan = this.$store.state.currentAdaptationPlan;
          localStorage.setItem('currentPlanId','');
          this.buildDataCollection();

        },

        created(){

        },

        methods: {
          buildDataCollection () {
            const {utils} = AiravataAPI; // eslint-disable-line
            const colors = ['#286bde'];
            const hoverBorderColors = ['#286bde'];
            const borderColors = ['#286bde'];
            const pointHoverBackgroundColors = ['#286bde'];
            utils.FetchUtils.get("/interactwel/api/plans/?plan_id="+ this.planId).then(result => {
              this.datacollection = {};
              if (result.length < 1 || !result[0].plan_json) {
                return;
              }
              const json = JSON.parse(result[0].plan_json);
              this.datacollection.labels = json.Years;
              this.datacollection.datasets = json.Data.map((dataSeries, index)=>{
                const backgroundColor = colors.length > index ? colors[index] : "#" + ((1<<24)*Math.random() | 0).toString(16);
                const hoverBorderColor = hoverBorderColors.length > index ? hoverBorderColors[index] : "#" + ((1<<24)*Math.random() | 0).toString(16);
                const borderColor = borderColors.length > index ? borderColors[index] : "#" + ((1<<24)*Math.random() | 0).toString(16);
                const pointHoverBackgroundColor = pointHoverBackgroundColors.length > index ? pointHoverBackgroundColors[index] : "#" + ((1<<24)*Math.random() | 0).toString(16);
                return {
                  label: dataSeries.Actor,
                  backgroundColor,
                  borderColor,
                  hoverBorderColor,
                  pointHoverBackgroundColor,
                  borderDash: [5, 5],
                  borderWidth: 5,
                  data: dataSeries.Values,
                  steppedLine: true,
                  fill: false,
                }
              })
            }
            ).catch(error => {
              alert("Failed to fetch graph data. " + error);
            })
          },

          showActionsGraph(){
            this.isModalVisible = true;
          },

          closeModal() {
            this.isModalVisible = false;
          }
        }
    };
</script>