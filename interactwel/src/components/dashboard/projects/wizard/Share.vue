<template>
  <b-col lg="12">
    <ol class="progress-bar">
      <li class="col-md-2">
        <div id="active" class="step-progress-bar">
          <div class="step-no">1</div>
          <h4 class="list-group-item-heading">Goals</h4>
          <h4r class="list-group-item-heading">&#10003;</h4r>
          <p class="list-group-item-text">{{ adaptationPlan.selectedGoals.length }} goals selected</p>
        </div>
      </li>
      <li class="col-md-2">
        <div class="step-progress-bar">
          <div class="step-no">2</div>
          <h4 class="list-group-item-heading">Actors</h4>
          <h4r class="list-group-item-heading">&#10003;</h4r>
          <p class="list-group-item-text">{{ adaptationPlan.selectedActors.length }} Actores selected</p>
        </div>
      </li>
      <li class="col-md-2">
        <div class="step-progress-bar">
          <div class="step-no">3</div>
          <h4 class="list-group-item-heading">Actions</h4>
          <h4r class="list-group-item-heading">&#10003;</h4r>
          <p class="list-group-item-text">{{ adaptationPlan.selectedActions.length }} Actions selected</p>
        </div>
      </li>
      <li class="col-md-2">
        <div class="step-progress-bar">
          <div class="step-no">4</div>
          <h4 class="list-group-item-heading">Visualize and Evaluate</h4>
          <h4r class="list-group-item-heading">&#10003;</h4r>
          <p class="list-group-item-text">Adaptation Plans</p>
        </div>
      </li>
      <!--<li class="col-md-2">
          <div class="step-progress-bar">
              <div class="step-no">5</div>
              <h4 class="list-group-item-heading">Feedback</h4>
              <h4r class="list-group-item-heading">&#10003;</h4r>
              <p class="list-group-item-text">Rate each plan</p>
          </div>
      </li>-->
      <li class="col-md-2">
        <div class="step-progress-bar active">
          <div class="step-no">5</div>
          <h4 class="list-group-item-heading">Wrap Up</h4>
          <h4r class="list-group-item-heading">&#10003;</h4r>
          <p class="list-group-item-text">Save and print Plans</p>
        </div>
      </li>
    </ol>
    <div id="step5" title="Step 5">
      <b-card no-body footer-tag="footer">
        <div class="step-header" slot="header">Share</div>
        <b-card-body>
          <b-table class="card-text" bordered small hover :items="tableRow" :fields="fields">
            <template v-slot:cell(rating)="data">
              <star-rating :rating="data.item.rating" read-only></star-rating>
            </template>
            <!--<template v-slot:cell(download)="data">
                <b-button pill size="sm"
                          variant="primary">Print
                </b-button>
            </template>-->
            <template v-slot:cell(save)="data">
              <b-button @click="savePlan()" pill size="sm" variant="secondary">
                Save
              </b-button>
            </template>
          </b-table>
        </b-card-body>
        <em slot="footer">
          <!--<b-button-group>
              <b-button id="step6-next-btn" @click="step6BackClicked" variant="outline-success" size="sm">
                  Back
              </b-button>
              <b-button id="step6-next-btn" @click="tabIndex++" variant="success" size="sm">Finish
              </b-button>
          </b-button-group>-->
          <b-button id="step6-next-btn" @click="exitWizard" variant="next" size="sm">Finish</b-button>
          <b-button id="step6-next-btn" @click="back" variant="back" size="sm">Back</b-button>
        </em>
      </b-card>
    </div>
  </b-col>
</template>

<script>

export default {
  name: 'Goals',
  props: {},
  data() {
    return {
      fields: [
        {
          key: 'plan',
          label: 'Adaptation Plan',
          sortable: true
        },
        {
          key: 'q1',
          label: 'Do you think the actions and time frames presented in this plan are feasible?',
          sortable: false
        },
        {
          key: 'q2',
          label: 'Please share any additional thoughts about the alternative plans or the plan builder tool',
          sortable: false
        },
        {
          key: 'rating',
          label: 'Overall rating',
          sortable: true
        },
        /*{key: 'download', label: ''},*/
        {key: 'save', label: ''},
      ],
      tableRow: [],
      adaptationPlan: [],
      projectId: null,
      planList: [],
      planId: null,
    }
  },
  async mounted() {
    const {utils} = AiravataAPI;
    this.adaptationPlan = this.$store.state.currentAdaptationPlan;
    if (localStorage.getItem('selectedGoals')) this.selectedGoals = JSON.parse(localStorage.getItem('selectedGoals'));
    let user = await this.getLoggedInUser();
    this.planList = this.$store.state.planList;
    this.planList.forEach(plan => {
      utils.FetchUtils.get("/interactwel/api/feedbacks/?plan_id=" + plan.plan_id + "&user_id=" + user.id).then(result => {
          if (result.length > 0) {
            let feedback = result[0]; //assuming that one user can have one feedback for one plan
            this.planId = feedback.plan_id;
            let row = {};
            row.plan = "Plan " + this.planId;
            row.q1 = feedback.feasibility === true ? "Yes" : "No";
            row.q2 = feedback.comments;
            row.rating = feedback.rating;
            this.tableRow.push(row);
          }

        }
      ).catch(error => {
        alert("Failed to fetch questions " + error);
      })
    })
  },

  watch: {},

  methods: {

    exitWizard() {
      this.$toast.success("Thank You for evaluating plans.");
      this.$router.push('/all-plans/' + this.$route.params.projectId);
      localStorage.setItem('adaptation_wizardStarted', false);
    },

    back() {
      this.$router.push('/adaptation-plans/' + this.$route.params.projectId + '/plans/overview')
    },

    async savePlan() {
      let user = await this.getLoggedInUser();
      let goals = this.adaptationPlan['selectedGoals'];
      let selectedActions = this.adaptationPlan['selectedActions'];

      const {utils} = AiravataAPI;
      utils.FetchUtils.post(
        '/interactwel/api/selectedplans/',
        {
          timestamp: new Date(),
          user_id: user.id,
          plan_id: this.planId,
          goals: goals.map(goal => goal.goal_id),
        }).then(selectedPlan => {
          utils.FetchUtils.post(
          '/interactwel/api/projectselectedplans/',
          {
            project_id: this.adaptationPlan['projectId'],
            selected_plan_id: selectedPlan.selected_plan_id,
          })
          .catch(error => {
            this.$toast.error("API error while saving the data! " + error);
          });
          selectedActions.forEach(action => {
            utils.FetchUtils.post(
              '/interactwel/api/selectedplanactoraction/',
              {
                selected_plan_id: selectedPlan.selected_plan_id,
                actor_id: action.actor.actor_id,
                action_id: action.action.action_id,
              })
              .catch(error => {
                this.$toast.error("API error while saving the selected actor action mapping! " + error);
              });
          });
          this.$toast.success("Successfully Saved the plan.");
          this.exitWizard();
        }
      ).catch(error => {
        this.$toast.error("API error while saving the selected plan! " + error);
      });
    },
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
