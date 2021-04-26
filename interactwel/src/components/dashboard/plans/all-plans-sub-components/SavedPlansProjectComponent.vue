<template>
  <b-card-body>
    <div class="d-lg-flex d-sm-block">
      <h5 class="mr-auto">{{project.name}}</h5>
      <b-button size="sm" variant="success" @click="$router.push('/adaptation-plans/'+ project.project_id)">Generate New Plan</b-button>
      <b-button size="sm" variant="outline-success" @click="$router.push('/visualize/'+ project.project_id)">View Project Data</b-button>
    </div>
    <b-card v-if="false">
      <b-card-body title="You don't have access to any saved plans">
        <b-card-text>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque luctus purus sit amet massa hendrerit semper at eu dui.
        </b-card-text>
      </b-card-body>
    </b-card>
    <div class="mt-3 pl-2">
      <b-tabs vertical nav-wrapper-class="plan-tabs bg-light px-0">
        <section v-for="plan in plans" v-bind:key="plan.selected_plan_id">
          <b-tab class="p-3 bg-light border"
                 :title="'Plan '+plan.plan_id"
                 v-on:click='loadTabContent(plan.plan_id)'
          >
            <div class="d-lg-flex d-sm-block pb-3">
              <b-button size="sm" @click="visualizePlan(plan.plan_id)" variant="dark">Visualize this Plan
              </b-button>
            </div>
            <div class="d-lg-flex d-sm-block">
              <b-list-group class="col-lg-3 col-md-12 col-sm-12">
                <b-list-group-item class="flex-column align-items-start">
                  <div class="d-flex w-100 justify-content-between">
                    <h5 class="mb-1">Goals</h5>
                    <small>{{plan.goals.length}} Goals selected</small>
                  </div>
                  <small>
                    <ul class="no-padding">
                      <li v-for="goal in plan.goals" v-bind:key="goal.goal_id">{{goal.name}}</li>
                    </ul>
                  </small>
                </b-list-group-item>

                <b-list-group-item class="flex-column align-items-start">
                  <div class="d-flex w-100 justify-content-between">
                    <h5 class="mb-1">Actors</h5>
                    <small class="text-muted"> 2 Actors Selected</small>
                  </div>
                  <small>
                    <ul class="no-padding">
                      <li>Farmers: Ground Water (GW)</li>
                      <li>Farmers: Surface Water (SW)</li>
                    </ul>
                  </small>
                </b-list-group-item>

                <b-list-group-item class="flex-column align-items-start">
                  <div class="d-flex w-100 justify-content-between">
                    <h5 class="mb-1">Actions</h5></div>
                  <small>
                    <ul class="no-padding">
                      <li>Farmers: Ground Water (GW)
                        <ul>
                          <li>Increase the volume of non-Columbia surface water</li>
                          <li>Decrease the volume of non-Columbia surface water</li>
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
                  <actions-graph v-bind:adaptation-plan-id="plan.plan_id"></actions-graph>
                </b-card>
              </div>
              <div class="d-block col-lg-3 col-md-12 col-sm-12">
                <PlanFeedbackComponent v-bind:selected-plan="plan"/>
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
    }
  },
  data() {
    return {
      plans: [],
    };
  },
  mounted() {
    const {utils} = AiravataAPI;

    this.plans = utils.FetchUtils.get("/interactwel/api/selectedplans/").then(
      result => {
        this.plans = result.filter(plan => plan.user_id === this.user.id);//todo: do this filtering in backend
      }
    )
  },

  methods: {
    loadTabContent(planId) {
      this.$router.push('/all-plans/' + planId);
    },

    visualizePlan(planId) {
      this.$router.push('/adaptation-plans/1/plans/' + planId + '/actions');
    }
  },
}
</script>

<style scoped>

</style>