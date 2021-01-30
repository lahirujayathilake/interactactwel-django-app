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
                  display: true,
                  text: 'Actions taken by each actor through time'
                },
                scales: {
                  //type: 'category',
                  xAxes: [{
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
              labels:  ["2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010"],
              datasets: [
                {
                  label: 'Actor 1',
                  backgroundColor: '#345fb5',
                  borderColor: "#286bde",
                  borderWidth: 5,
                  data: [3, 4, 4, 4, 6, 2, 1, 1, 3, 5],
                  steppedLine: true,
                  fill: false,
                }, {
                  label: 'Actor 2',
                  backgroundColor: '#f87979',
                  borderColor: "#f87979",
                  borderWidth: 5,
                  data: [5, 6, 3, 3, 3, 3, 4, 4, 6, 5],
                  steppedLine: true,
                  fill: false,
                }
              ]
            }
          }

        }
    };
</script>