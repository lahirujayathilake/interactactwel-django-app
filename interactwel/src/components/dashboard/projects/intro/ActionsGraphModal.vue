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
            datacollection: null,
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

        methods: {
          buildDataCollection () {
            this.datacollection = {
              labels:  ["2000","2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010"],
              datasets: [
                {
                  label: 'Actor 1',
                  backgroundColor: '#345fb5',
                  borderColor: "#286bde",
                  borderWidth: 5,
                  data: [1, 3, 4, 4, 4, 6, 2, 1, 1, 3, 5],
                  steppedLine: true,
                  fill: false,
                }, {
                  label: 'Actor 2',
                  backgroundColor: '#f87979',
                  borderColor: "#f87979",
                  borderWidth: 5,
                  data: [1, 5, 6, 3, 3, 3, 3, 4, 4, 6, 5],
                  steppedLine: true,
                  fill: false,
                }
              ]
            }
          },

            close() {
                this.$emit('close');
            },
        },
        async mounted() {
          this.buildDataCollection();
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
