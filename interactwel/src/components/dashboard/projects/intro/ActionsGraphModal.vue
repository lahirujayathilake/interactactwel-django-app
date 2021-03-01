<template>
    <div id="actions-graph-modal" class="modal-backdrop">
        <div class="modal modal-lg">
            <section class="modal-body">
                <slot name="body">
                  <line-chart :chart-data="datacollection" :options="options" :width="650" :height="400"></line-chart>
                </slot>
            </section>
            <footer class="modal-footer">
                <slot name="footer">
                    <button type="button" class="btn btn-success btn-sm" @click="close">Close</button>
                </slot>
            </footer>
        </div>
    </div>
</template>

<script>
import LineChart from "../../projects/charts/lib/LineChart";

    export default {
        name: 'actions-graph-modal',

      components: {
        LineChart
      },

        data(){
          return {
            planId: "1",
            JSONData: null,
            datacollection: null,
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
                      borderDash: [2, 2],
                      borderWidth: 2,
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

          /*buildDataCollection () {
            this.datacollection = {
              labels:  ["2000","2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010"],
              datasets: [
                {
                  label: 'Actor 1',
                  backgroundColor: '#345fb5',
                  borderColor: "#286bde",
                  borderWidth: 2,
                  data: [1, 3, 4, 4, 4, 6, 2, 1, 1, 3, 5],
                  steppedLine: true,
                  fill: false,
                }, {
                  label: 'Actor 2',
                  backgroundColor: '#f87979',
                  borderColor: "#f87979",
                  borderWidth: 2,
                  data: [1, 5, 6, 3, 3, 3, 3, 4, 4, 6, 5],
                  steppedLine: true,
                  fill: false,
                }
              ]
            }
          },*/

            close() {
                this.$emit('close');
            },
        }
    };
</script>

<style>

#actions-graph-modal .modal {
  background: #FFFFFF;
  box-shadow: 2px 2px 20px 1px;
  height: auto;
  overflow: auto;
  position: fixed;
  top: 52%;
  left: 50%;
  transform: translate(-50%, -50%);
  max-width: 900px;
  display: flex;
  flex-direction: column;
}

#actions-graph-modal .modal-header {
  border-bottom: 1px solid #eeeeee;
  color: #4cae4c;
  justify-content: space-between;
  font-size: 25px;
  font-weight: bold;
}

#actions-graph-modal .modal-footer {
  justify-content: flex-end;
}

#actions-graph-modal .modal-body {
  position: relative;
  padding: 30px 40px;
  font-size: 16px;
}
#actions-graph-modal.modal-backdrop{
  background-color: rgba(0, 0, 0, 0.42);
}

</style>
