<template>
    <div>
        <b-card no-body>
            <b-tabs card pills vertical>
                <b-tab :key="plan.id" :title="'Plan ' + plan.plan_id" active v-for="plan in plans">
                    <b-row>
                        <b-col lg="6">
                            <b-card title="Overview">
                                <b-row>
                                    <b-col lg="6">
                                        <h6 class="chart-title"><strong>Selected Goals</strong></h6>
                                    </b-col>
                                </b-row>
                            </b-card>
                        </b-col>
                        <b-col lg="6">
                            <feedback-view :plan-id="plan.id" :project-id="projectId"></feedback-view>
                        </b-col>
                        <b-col lg="12">
                            <b-card title="Adaptation Pathways">
                                <b-card-text>
                                    <actions-graph-stepped-lines></actions-graph-stepped-lines>
                                </b-card-text>
                            </b-card>
                        </b-col>
                    </b-row>
                </b-tab>
            </b-tabs>
        </b-card>
    </div>
</template>


<script>
    import ActionsGraphSteppedLines from "./../projects/charts/data/ActionsGraphSteppedLines.vue";
    import FeedbackView from "./FeedbackView";

    export default {
        components: {
            FeedbackView,
            ActionsGraphSteppedLines,
        },
        name: "ProjectPlansList",

        data() {
            return {
                plans: [],
                projectId: ''
            };
        },

        mounted() {
            const {utils} = AiravataAPI;
            this.projectId = this.$route.params.projectId
            utils.FetchUtils.get("/interactwel/api/projectplans/")
                .then(projectPlansList => {
                    //filter by project id todo: ideally this filtration should happen at DB level
                    if (projectPlansList != null) {
                        projectPlansList.forEach(projectPlan => {
                            if (projectPlan.project_id == this.projectId) {
                                this.plans.push(projectPlan);
                            }
                        });
                    }
                })
                .catch(error => {
                    alert("Could not get the projects list. API error! " + error);
                });

        },

        methods: {
            projectSelected: function (projectId) {
                this.$router.push('/plans/saved-plans/' + projectId);
            }

        },
        computed: {}
    };
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
</style>
