<template>
  <div class="planData">
    <b-card no-body>
      <b-tabs
        pills
        card
        vertical
      >
        <b-tab title="Overview">
          <div class="d-lg-flex d-sm-block">
            <plan-overview
              :plan="plan"
              :actors="actors"
              :actions="actions"
              :goals="goals"
            />
          </div>
        </b-tab>
        <b-tab
          title="Actions"
          active
        >
          <b-card-text>
            <actions-graph
              :selected-actors="getActorsList(plan.actors)"
              :adaptation-plan-id="parseInt(this.$route.params.planId)"
            />
          </b-card-text>
        </b-tab>
        <b-tab title="Streams">
          <b-card-text>
            Streams
            <component :is="component='ChartStreams'" />
          </b-card-text>
        </b-tab>
        <b-tab title="Region">
          <b-card-text>
            Region
            <component :is="component='ChartRegion'" />
          </b-card-text>
        </b-tab>
        <b-tab title="Sub Basins">
          <b-card-text>
            Sub Basins
            <component :is="component='ChartSubBasins'" />
          </b-card-text>
        </b-tab>
        <b-tab title="Feedback">
          <b-card-text>
            Feedback
            <component :is="component='Feedback'" />
          </b-card-text>
        </b-tab>
      </b-tabs>
    </b-card>
  </div>
</template>

<script>
import PlanOverview from '@/components/dashboard/plans/all-plans-sub-components/PlanOverview';
import ActionsGraph from '@/components/dashboard/projects/charts/data/ActionsGraph';

export default {
  name: "PlanDataTabView",
  components: {PlanOverview, ActionsGraph},
  data() {
    return {
      plan: {},
      goals: [],
      actors: [],
      actions: [],
    };
  },
  async mounted() {

    // eslint-disable-next-line no-undef
    const {utils} = AiravataAPI;

    const planId = this.$route.params.planId;

    utils.FetchUtils.get("/interactwel/api/selectedplans/?plan_id=" + planId)
      .then(plans => {
        this.plan = plans[0];
        const action_mapping = this.plan.action_mapping;
        this.plan.actors = [];
        action_mapping.forEach(mapping => {
          if (!this.plan.actors.includes(mapping.actor_id)) {
            this.plan.actors.push(mapping.actor_id);
          }
        });
      })
      .catch(error => {
        alert("Could not get the projects list. API error! " + error);
      });

    utils.FetchUtils.get("/interactwel/api/goals/")
      .then(goals => {
        this.goals = goals;
      })
      .catch(error => {
        alert("Could not get the projects list. API error! " + error);
      });

    utils.FetchUtils.get("/interactwel/api/actors/")
      .then(actors => {
        this.actors = actors;
      })
      .catch(error => {
        alert("Could not get the projects list. API error! " + error);
      });

    utils.FetchUtils.get("/interactwel/api/actions/")
      .then(actions => {
        this.actions = actions;
      })
      .catch(error => {
        alert("Could not get the projects list. API error! " + error);
      });

  },
  methods: {
    getActorsList(actorIds) {
      if (actorIds && this.actors) {
        return this.actors.filter(actor => actorIds.includes(actor.actor_id));
      }

      return [];

    },
  },
};
</script>

<style scoped>

</style>