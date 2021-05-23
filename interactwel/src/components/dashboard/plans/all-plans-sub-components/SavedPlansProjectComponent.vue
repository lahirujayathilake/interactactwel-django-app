<template>
  <b-card-body>
    <div class="d-lg-flex d-sm-block">
      <h5 class="mr-auto">
        {{ project.name }}
      </h5>
      <b-button
        size="sm"
        variant="success"
        @click="$router.push('/adaptation-plans/'+ project.project_id)"
      >
        Generate New Plan
      </b-button>
      <b-button
        size="sm"
        variant="outline-success"
        @click="$router.push('/visualize/'+ project.project_id)"
      >
        View Project Data
      </b-button>
    </div>
    <b-card v-if="!plans.length">
      <b-card-body title="You don't have access to any saved plans">
        <b-card-text>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque luctus purus sit amet massa hendrerit semper at eu dui.
        </b-card-text>
      </b-card-body>
    </b-card>
    <div class="mt-3 pl-2">
      <b-tabs
        vertical
        nav-wrapper-class="plan-tabs bg-light px-0"
      >
        <section
          v-for="plan in plans"
          :key="plan.selected_plan_id"
        >
          <b-tab
            class="p-3 bg-light border"
            :title="'Plan ' + plan.plan_id"
          >
            <div class="d-lg-flex d-sm-block pb-3">
              <b-button
                size="sm"
                variant="dark"
                @click="visualizePlan(plan.plan_id)"
              >
                Visualize this Plan
              </b-button>
            </div>
            <div class="d-lg-flex d-sm-block">
              <plan-overview
                :plan="plan"
                :actions="actions"
                :actors="actors"
                :goals="goals"
              />
              <div class="d-block flex-column col-md-12 col-lg-6 col-sm-12">
                <b-card>
                  <actions-graph
                    :selected-actors="getActorsList(plan.actors)"
                    :adaptation-plan-id="plan.plan_id"
                  />
                </b-card>
              </div>
              <div class="d-block col-lg-3 col-md-12 col-sm-12">
                <PlanFeedbackComponent :selected-plan="plan" />
              </div>
            </div>
          </b-tab>
        </section>
      </b-tabs>
    </div>
  </b-card-body>
</template>

<script>
import PlanFeedbackComponent from '@/components/dashboard/plans/all-plans-sub-components/PlanFeedbackComponent';
import ActionsGraph from "@/components/dashboard/projects/charts/data/ActionsGraph";
import PlanOverview from '@/components/dashboard/plans/all-plans-sub-components/PlanOverview';

export default {
  name: "SavedPlansProjectComponent",
  components: {
    PlanOverview,
    PlanFeedbackComponent,
    ActionsGraph,
  },
  props: {
    project: {
      type: Object,
    },
    user: {
      type: Object,
    },
  },
  data() {
    return {
      plans: [],
      goals: [],
      actors: [],
      actions: [],
    };
  },
  async mounted() {
    const {utils} = AiravataAPI;

    utils.FetchUtils.get("/interactwel/api/selectedplans/").then(
      result => {
        const userPlans = result.filter(plan => plan.user_id === this.user.id);//todo: do this filtering in backend
        userPlans.forEach(plan => {
          const action_mapping = plan.action_mapping;
          plan.actors = [];
          action_mapping.forEach(mapping => {
            if (!plan.actors.includes(mapping.actor_id)) {
              plan.actors.push(mapping.actor_id);
            }
          });
          this.plans.push(plan);
        });
      }
    );

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
    visualizePlan(planId) {
      this.$router.push('/plans/' + this.project.project_id + '/' + planId);
    },

    getGoalName(goalId) {
      if (this.goals) {
        return this.goals.find(goal => goal.goal_id === goalId);
      }
      return {};
    },

    getActorName(actorId) {
      if (this.actors) {
        return this.actors.find(actor => actor.actor_id === actorId);
      }
      return {};
    },

    getActionName(actionId) {
      if (this.actions) {
        return this.actions.find(action => action.action_id === actionId);
      }
      return {};
    },

    getActionMappings(actorId, mappings) {
      if (mappings) {
        return mappings.filter(mapping => mapping.actor_id === actorId);
      }

      return [];
    },

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