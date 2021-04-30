<template>
  <div
    id="graph"
    class="card"
  >
    <div class="card-header">
      <span
        class="close"
        @click="dismiss"
      ><font-awesome-icon
        icon="times-circle"
      /> Close</span>
      <strong style="font-size:18px">Overview</strong>
    </div>
    <div class="card-body">
      <b-row>
        <b-col lg="6">
          <h6 class="chart-title">
            <strong>Selected Goals</strong>
          </h6>
          <b-list-group
            v-for="item in adaptationPlan.selectedGoals"
            :key="item.goal_id"
            class="no-padding"
          >
            <b-list-group-item class="no-border py-1">
              &#10003;&nbsp;{{ item.name }}
            </b-list-group-item>
          </b-list-group>
        </b-col>
        <b-col lg="6">
          <h6 class="chart-title">
            <strong>Selected Actors</strong>
          </h6>
          <b-list-group
            v-for="item in adaptationPlan.selectedActors"
            :key="item.actor_id"
            class="no-padding"
          >
            <b-list-group-item class="no-border py-1">
              &#10003;&nbsp;{{ item.description }}
            </b-list-group-item>
          </b-list-group>
        </b-col>
      </b-row>
      <b-row style="margin-top:20px;">
        <b-col lg="12">
          <h6 class="chart-title">
            <strong>Selected Actions for Actors</strong>
          </h6>

          <b-col lg="12">
            <b-list-group
              v-for="actor in adaptationPlan.selectedActors"
              :key="actor.id"
              class="no-padding"
            >
              <b-list-group-item class="no-border py-1">
                &#10003;&nbsp;{{ actor.description }}
                <b-list-group
                  v-for="item in adaptationPlan.selectedActions"
                  v-if="item.actor.actor_id == actor.actor_id "
                  :key="item.id"
                  class="no-padding py-0 mr-2"
                >
                  <b-list-group-item class="no-border py-1">
                    <small>&#10003;&nbsp;{{ item.action.name }}</small>
                  </b-list-group-item>
                </b-list-group>
              </b-list-group-item>
            </b-list-group>
          </b-col>
        </b-col>
      </b-row>
    </div>
  </div>
</template>
<script>
import EventBus from './../../../../event-bus';

export default {
  name: 'Overview',

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