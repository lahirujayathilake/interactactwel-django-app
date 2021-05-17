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
    <b-card v-if="false">
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
            @click="loadTabContent(plan.plan_id)"
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
              <b-list-group class="col-lg-3 col-md-12 col-sm-12">
                <b-list-group-item class="flex-column align-items-start">
                  <div class="d-flex w-100 justify-content-between">
                    <h5 class="mb-1">
                      Goals
                    </h5>
                    <small>{{ plan.goals.length }} Goals selected</small>
                  </div>
                  <small>
                    <ul class="no-padding">
                      <li
                        v-for="goalId in plan.goals"
                        :key="goalId"
                      >{{ getGoalName(goalId).name }}</li>
                    </ul>
                  </small>
                </b-list-group-item>

                <b-list-group-item class="flex-column align-items-start">
                  <div class="d-flex w-100 justify-content-between">
                    <h5 class="mb-1">
                      Actors
                    </h5>
                    <small class="text-muted"> {{ plan.actors.length }} Actors Selected</small>
                  </div>
                  <small>
                    <ul class="no-padding">
                      <li
                        v-for="actorId in plan.actors"
                        :key="actorId"
                      >{{ getActorName(actorId).name }}</li>
                    </ul>
                  </small>
                </b-list-group-item>

                <b-list-group-item class="flex-column align-items-start">
                  <div class="d-flex w-100 justify-content-between">
                    <h5 class="mb-1">
                      Actions
                    </h5>
                  </div>
                  <small>
                    <ul class="no-padding">
                      <li
                        v-for="actorId in plan.actors"
                        :key="actorId"
                      >
                        {{ getActorName(actorId).name }}
                        <ul>
                          <li
                            v-for="action_mapping in getActionMappings(actorId, plan.action_mapping)"
                            :key="action_mapping.id"
                          >
                            {{ getActionName(action_mapping.action_id).name }}
                          </li>
                        </ul>
                      </li>
                      <li>Farmers: Surface Water (SW)
                        <ul>
                          <li>Increase the volume of non-Columbia surface water</li>
                        </ul>
                      </li>
                    </ul>
                  </small>
                </b-list-group-item>
              </b-list-group>
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

export default {
  name: "SavedPlansProjectComponent",
  components: {
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
    loadTabContent(planId) {
      this.$router.push('/all-plans/' + planId);
    },

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
        return this.actors.filter(actor => actorIds.includes(actor.actor_id))
      }

      return {};

    },
  },
};
</script>

<style scoped>

</style>