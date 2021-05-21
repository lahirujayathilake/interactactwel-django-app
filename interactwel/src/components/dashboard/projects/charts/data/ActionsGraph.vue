<template>
  <div>
    <b-button
      variant="secondary"
      size="sm"
      @click="showActionsGraph()"
    >
      <i class="fas fa-search-plus" />
    </b-button>
    <line-chart
      :chart-data="datacollection"
      :options="options"
      :width="650"
      :height="400"
    />
    <div
      v-show="isModalVisible"
      id="actions-graph-modal"
      class="modal-backdrop"
    >
      <div class="modal modal-lg">
        <section class="modal-body">
          <slot name="body">
            <line-chart
              :chart-data="datacollection"
              :options="options"
              :width="650"
              :height="400"
            />
          </slot>
        </section>
        <footer class="modal-footer">
          <slot name="footer">
            <button
              type="button"
              class="btn btn-success btn-sm"
              @click="closeModal"
            >
              Close
            </button>
          </slot>
        </footer>
      </div>
    </div>
  </div>
</template>

<script>
import LineChart from "../lib/LineChart";

export default {
  name: 'ActionsGraphSteppedLines',

  components: {
    LineChart,
  },

  props: {
    adaptationPlanId: {
      type: Number,
    },
    selectedActors: {
      type: Array,
    },
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
          mode: 'dataset',
        },
        elements: {
          line: {
            tension: 0, // disables bezier curves
          },
          point: {
            hitRadius: 10,
          },
        },
        responsive: true,
        legend: {
          display: true,
        },
        title: {
          display: true,
          text: 'Actions taken by each actor through time',
        },
        scales: {
          //type: 'category',
          xAxes: [{
            gridLines: {
              display: false,
            },
            scaleLabel: {
              display: true,
              labelString: 'Time',
            },
            position: 'bottom',
            ticks: {
              beginAtzero: false,
              stepSize: 1,
            },
          }],

          yAxes: [{
            gridLines: {
              drawBorder: false,
            },
            //type: 'category',
            scaleLabel: {
              display: true,
              labelString: 'Actions',
            },
            ticks: {
              beginAtZero: false,
              max: 10,
            },
          }],
        },
      },
    };
  },
  mounted() {

    this.planId = this.adaptationPlanId || this.$route.params.planId;
    if (!this.planId){
      this.planId = localStorage.getItem('currentPlanId');
    }
    this.selectedActors = this.selectedActors || this.$store.state.currentAdaptationPlan.selectedActors || {};
    localStorage.setItem('currentPlanId', '');
    this.buildDataCollection();

  },

  created(){

  },

  methods: {
    buildDataCollection() {
      const {utils} = AiravataAPI; // eslint-disable-line
      const colors = ['#43AA8B', '#F9C74F', '#F3722C', '#277DA1'];
      const selectedActorNames = this.selectedActors.map(actor => actor.name) || [];
      utils.FetchUtils.get("/interactwel/api/plans/?plan_id=" + this.planId).then(result => {
        this.datacollection = {};
        if (result.length < 1 || !result[0].plan_json) {
          return;
        }
        const json = JSON.parse(result[0].plan_json);
        this.datacollection.labels = json.Years;
        const filteredData = json.Data.filter(
          dataSeries => selectedActorNames.includes(dataSeries.Actor)
        );
        this.datacollection.datasets = filteredData.map((dataSeries, index)=>{
          const backgroundColor = colors.length > index ? colors[index] : "#" + ((1 << 24) * Math.random() | 0).toString(16);
          const borderColor = backgroundColor;
          const hoverBackgroundColor = '#000000';
          const hoverBorderColor = '#000000';
          const pointHoverBackgroundColor = '#000000';
          return {
            label: dataSeries.Actor,
            backgroundColor,
            borderColor,
            hoverBorderColor,
            pointHoverBackgroundColor,
            borderDash: [5, 5],
            hoverBorderDash: [2, 2],
            hoverBackgroundColor,
            borderWidth: 2,
            hoverBorderWidth: 4,
            data: dataSeries.Values,
            steppedLine: true,
            fill: false,
          };
        });
      }
      ).catch(error => {
        alert("Failed to fetch graph data. " + error);
      });
    },

    showActionsGraph(){
      this.isModalVisible = true;
    },

    closeModal() {
      this.isModalVisible = false;
    },
  },
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