<template>
    <div>
        <component v-bind:is="component='Header'"></component>
        <b-container fluid class="main">
            <b-row>
                <b-col>
                    <h3 class="mb-3">Plans</h3>
                </b-col>
            </b-row>
            <b-row>
                <b-col lg="12">
                    <b-card v-if="projects" no-body>
                        <b-tabs vertical nav-wrapper-class="w-25">
                            <b-tab
                                    v-for="project in projects"
                                    :title="project.name"
                                    v-on:click="projectSelected(project.project_id)">
                                <!--<router-view></router-view>-->
                                <b-card-body class="no-padding">
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
                                    <div class="mt-3">
                                        <b-tabs>
                                            <b-tab
                                                v-for="plan in plans"
                                                v-if="project.project_id == plan.project_id"
                                                :title="'Plan '+plan.plan_id">
                                                <div class="d-lg-flex d-sm-block py-3">
                                                    <b-button size="sm" variant="outline-success">Visualize this Plan
                                                    </b-button>
                                                </div>
                                                <div class="d-lg-flex d-sm-block">
                                                    <b-list-group>
                                                        <b-list-group-item class="flex-column align-items-start">
                                                            <div class="d-flex w-100 justify-content-between">
                                                                <h5 class="mb-1">Goals</h5>
                                                                <small>{{project.goals.length}} Goals selected</small>
                                                            </div>
                                                            <small>
                                                                <ul class="no-padding">
                                                                    <li v-for="goal in project.goals">{{goal.name}}</li>
                                                                </ul>
                                                            </small>
                                                        </b-list-group-item>

                                                        <b-list-group-item class="flex-column align-items-start">
                                                            <div class="d-flex w-100 justify-content-between">
                                                                <h5 class="mb-1">Actors</h5>
                                                                <small class="text-muted">{{project.actors.length}} Actors Selected</small>
                                                            </div>
                                                            <small>
                                                                <ul class="no-padding">
                                                                    <li v-for="actor in project.actors">{{actor.description}}</li>
                                                                </ul>
                                                            </small>
                                                        </b-list-group-item>

                                                        <b-list-group-item class="flex-column align-items-start">
                                                            <div class="d-flex w-100 justify-content-between">
                                                                <h5 class="mb-1">Actions</h5></div>

                                                            <small>
                                                                <ul class="no-padding">
                                                                  <li v-for="actor in project.actors">{{actor.description}}
                                                                        <ul>
                                                                            <li v-for="action in actions" v-if="action.actor_id == actor.actor_id && action.plan_id == plan.plan_id">
                                                                                {{action.name}}
                                                                            </li>
                                                                        </ul>
                                                                    </li>
                                                                </ul>
                                                            </small>
                                                        </b-list-group-item>
                                                    </b-list-group>
                                                    <div class="d-block mx-3">
                                                        <b-card>
                                                          <actions-graph-stepped-lines></actions-graph-stepped-lines>
                                                        </b-card>
                                                    </div>
                                                </div>
                                                <div class="d-block my-3">
                                                    <b-card>
                                                      <b-list-group-item class="flex-column align-items-start">
                                                        <div class="d-flex w-100 justify-content-between">
                                                          <h5 class="mb-1">Feedbacks</h5>
                                                        </div>
                                                        <small>
                                                          <ul class="no-padding">
                                                            <li v-for="feedback in plan.feedbacks">{{feedback.comments}}</li>
                                                          </ul>
                                                        </small>
                                                      </b-list-group-item>
                                                    </b-card>
                                                </div>
                                            </b-tab>
                                        </b-tabs>
                                    </div>
                                </b-card-body>
                            </b-tab>
                        </b-tabs>
                    </b-card>
                </b-col>
            </b-row>
        </b-container>
        <component v-bind:is="component='Footer'"></component>
    </div>
</template>

<script>

    import Header from './../../Header.vue';
    import Footer from './../../Footer.vue';
    import GanntChart from "@/components/dashboard/projects/charts/data/GanntChart";
    import ActionsGraphSteppedLines from "@/components/dashboard/projects/charts/data/ActionsGraphSteppedLines";

    export default {
        components: {},
        name: "AllPlans",
        components: {
            Header, Footer,
          'actions-graph-stepped-lines': ActionsGraphSteppedLines
        },

        data() {
            return {
                projects: [],
                projectsUsers: [],
                plans: [],
                actions: [],
                feedbacks: []
            };
        },

        async mounted() {
          const {utils} = AiravataAPI;
            this.projects = await this.getProjectsListWithPlansOfLoggedInUser();
            for (let project of this.projects){
              let plans = await this.getProjectPlans(project.project_id);
              plans.forEach(plan => {
                plan.feedbacks = [];
                utils.FetchUtils.get("/interactwel/api/feedbacks/?plan_id="+ plan.plan_id).then(result => {
                      if (result.length > 0) {
                        plan.feedbacks.push(result[0]);
                      }
                    }
                ).catch(error => {
                  alert("Failed to fetch feedbacks " + error);
                })
              });
              this.plans = this.plans.concat(plans);
              project.goals = await this.getProjectGoals(project.project_id);
              project.actors = await this.getProjectActors(project.project_id);
              // project.actions = await this.getProjectActions(project.project_id);
              for (let actor of project.actors){
                for (let plan of plans){
                  let actions = await this.getActorActions(plan.plan_id, actor.actor_id);
                  for (let action of actions){
                    action.actor_id = actor.actor_id;
                    action.plan_id = plan.plan_id;
                    this.actions.push(action);
                  }
                }
              }
            }
            localStorage.setItem('currentPlanId','');
            if (this.plans.length > 0){
              localStorage.setItem('currentPlanId', this.plans[0].plan_id);
              ActionsGraphSteppedLines.mounted();
            }
        },

        methods: {},
        computed: {}
    };
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
    .main {
        background-color: #efefef;
        padding: 1rem 2rem;
        min-height: 90vh;
        text-align: left;
    }

</style>
