<template>
  <div
    id="graph"
    class="card"
  >
    <div class="card-body">
      <b-tabs card>
        <b-tab
            title="Historical (1991-2020)"
            active
        >
          <div class="card-body">
            <b-row>
              <b-col>
                <div class="h5">Select Drought Scenario</div>
                <div class="form-check">
                  <input class="form-check-input" type="radio" name="climate-scenario" id="historical">
                  <label class="form-check-label" for="historical">
                    No. of extreme and exceptional drought months per year based on SPI (meteorological drought characteristics)
                  </label>
                </div>
                <div class="form-check">
                  <input class="form-check-input" type="radio" name="climate-scenario" id="rcp45Mid">
                  <label class="form-check-label" for="rcp45Mid">
                    Average duration of extreme and exceptional SPI drought events  over the time period of climate scenario
                  </label>
                </div>
                <div class="form-check">
                  <input class="form-check-input" type="radio" name="climate-scenario" id="rcp85Mid">
                  <label class="form-check-label" for="rcp85Mid">
                    Maximum duration of extreme and exceptional SPI drought events during the time period of climate scenario
                  </label>
                </div>
                <div class="form-check">
                  <input class="form-check-input" type="radio" name="climate-scenario" id="rcp45Late">
                  <label class="form-check-label" for="rcp45Late">
                    No. of extreme and exceptional drought months per year based on SRI (hydrological drought characteristics)
                  </label>
                </div>
                <div class="form-check">
                  <input class="form-check-input" type="radio" name="climate-scenario" id="rcp85Late">
                  <label class="form-check-label" for="rcp85Late">
                    Average duration of extreme and exceptional SRI drought events  over the time period of climate scenario
                  </label>
                </div>
                <div class="form-check">
                  <input class="form-check-input" type="radio" name="climate-scenario" id="rcp85Late1">
                  <label class="form-check-label" for="rcp85Late">
                    Maximum duration of extreme and exceptional SRI drought events during the time period of climate scenario
                  </label>
                </div>
                <div class="form-check">
                  <input class="form-check-input" type="radio" name="climate-scenario" id="rcp85Late2">
                  <label class="form-check-label" for="rcp85Late">
                    No. of extreme and exceptional drought months per year based on SSI (agricultural drought characteristics)
                  </label>
                </div>
                <div class="form-check">
                  <input class="form-check-input" type="radio" name="climate-scenario" id="rcp85Late3">
                  <label class="form-check-label" for="rcp85Late">
                    Average duration of extreme and exceptional SSI drought events  over the time period of climate scenario
                  </label>
                </div>
                <div class="form-check">
                  <input class="form-check-input" type="radio" name="climate-scenario" id="rcp85Late3">
                  <label class="form-check-label" for="rcp85Late">
                    Maximum duration of extreme and exceptional SSI drought events during the time period of climate scenario
                  </label>
                </div>
              </b-col>
            </b-row>
          </div>
        </b-tab>
        <b-tab
            title="RCP 4.5 (Mid Century)"
        >
          <div class="card-body">
            <b-row>
              <b-col
                  lg="6"
                  class="p-3">
              </b-col>
            </b-row>
          </div>
        </b-tab>
        <b-tab
            title="RCP 8.5 (Mid Century)"
        >
          <div class="card-body">
            <b-row>
              <b-col
                  lg="6"
                  class="p-3">
              </b-col>
            </b-row>
          </div>
        </b-tab>
        <b-tab
          title="RCP 4.5 (Late Century)"
        >
          <div class="card-body">
            <b-row>
              <b-col
                lg="6"
                class="p-3">
              </b-col>
            </b-row>
          </div>
        </b-tab>
        <b-tab
          title="RCP 8.5 (Late Century)"
        >
          <div class="card-body">
            <b-row>
              <b-col
                lg="6"
                class="p-3">
              </b-col>
            </b-row>
          </div>
        </b-tab>
      </b-tabs>
    </div>
  </div>
</template>
<script>
import EventBus from '../../../../event-bus';

export default {
  name: 'Stresses',

  components: {
    EventBus,
  },

  props: {
  },
  data() {
    return {
      adaptationPlan: [],
      selectedGoals: [],
      selectedActors: [],
      selectedActions: [],

    };
  },

  computed: {

  },

  mounted() {

    EventBus.$emit('HIDE_RESULTSMAP');
    // this.adaptationPlan = JSON.parse(localStorage.getItem('adaptationPlan'));
    this.adaptationPlan = this.$store.state.currentAdaptationPlan;
    /*this.selectedGoals = localStorage.getItem('selectedGoals');
            this.selectedActors = localStorage.getItem('selectedActors');
            this.selectedActions = localStorage.getItem('selectedActions');*/
  },

  methods: {

    getActions(actor){
      let actorActions = [];
      this.selectedActions.forEach(actorAction => {
        let actorId = actorAction.split(",")[0];
        let actionId = actorAction.split(",")[1];
        if (actor.id == actorId) {
          this.actions.forEach(action => {
            if (action.id == actionId) {
              actorActions.push(action);
            }
          });
        }
      });
      return actorActions;
    },

    dismiss() {
      EventBus.$emit('CLOSE');
    },
  },

};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
    .chart-title {
        font-size: 18px;
        /*font-weight: bold;*/
        color: #5e6b7e;
        border-bottom: 2px solid #28a645 !important;
        padding-bottom: 5px;
    }

    .no-border{
        border: 0px solid rgba(0,0,0,.125) !important;
    }

</style>