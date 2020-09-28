<template>
    <div>
        <b-card no-body>
            <b-tabs card pills vertical>
                <b-tab :key="plan.plan_id" :title="'Plan ' + plan.plan_id" active v-for="plan in plans">
                    <b-row>
                        <b-col lg="6">
                            <b-card title="Overview">
                                <b-row>
                                    <b-col lg="6">
                                        <span class="chart-title"><strong>This section is under construction</strong></span>
                                    </b-col>
                                </b-row>
                            </b-card>
                        </b-col>
                        <b-col lg="6">
                            <feedback-view :plan-id="plan.plan_id" :project-id="projectId"></feedback-view>
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

        async mounted() {
            this.projectId = this.$route.params.projectId
            this.plans = await this.getProjectPlans(this.projectId)

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
