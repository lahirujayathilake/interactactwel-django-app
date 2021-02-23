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
            this.datacollection = {
              labels:  ["2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010"],
              datasets: [
                {
                  label: 'Actor 1',
                  backgroundColor: '#286bde',
                  borderColor: "rgba(40, 107, 222, 0.5)",
                  hoverBorderColor: '#286bde',
                  pointHoverBackgroundColor: '#28de40',
                  borderDash: [5, 5],
                  borderWidth: 5,
                  data: [1, 3, 4, 4, 4, 6, 2, 1, 1, 3, 5],
                  steppedLine: true,
                  fill: false,
                }, {
                  label: 'Actor 2',
                  backgroundColor: '#f87979',
                  borderColor: "rgba(248, 121, 121, 0.5)",
                  hoverBorderColor: '#f87979',
                  borderWidth: 5,
                  data: [1, 5, 6, 3, 3, 3, 3, 4, 4, 6, 5],
                  steppedLine: true,
                  fill: false,
                }
              ]
            }
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