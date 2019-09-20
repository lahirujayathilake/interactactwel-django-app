<template>
    <div>
                    <h2>Project {{$route.params.projectId}}</h2>
                    <h2>Project {{$route.params.projectId}}</h2>
    </div>
</template>

<script>

    export default {
        components: {

        },
        name: 'Project',

        props: {
            adaptationPlan: {
                type: String,
                default: ""
            },
        },

        data() {
            return {
                feedbacks: [
                    {
                        id: 1,
                        plan: 'Adaptation Plan 1',
                        q1: {
                            q: 'How well does this plan (alternative plan 1, 2, etc.) meet the management goals you identified in Step 1?',
                            a: 'Good'
                        },
                        q2: {
                            q: 'Do you think that the projected results/impacts from this plan will occur if the proposed actions are implemented?',
                            a: 'Satisfactory'
                        },
                        q3: {
                            q: 'What factors might prevent you from taking the recommended actions listed in this plan? (check all that apply)',
                            a: 'Satisfactory'
                        },
                        q4: {
                            q: 'How likely are you to implement the actions recommended in this plan?',
                            a: 'bad'
                        },
                        q5: {
                            q: 'How likely are you to work with other stakeholder groups to implement this plan?',
                            a: 'Satisfactory'
                        },
                        q6: {
                            q: 'What factors might prevent you from taking the recommended actions listed in this plan? (check all that apply)',
                            a: {
                                1: 'Infrastructure costs',
                                2: 'Permits or other regulatory approval processes and cost'
                            }
                        },
                        rating: '5'
                    },
                    {
                        id: 3,
                        plan: 'Adaptation Plan 3',
                        q1: {
                            q: 'How well does this plan (alternative plan 1, 2, etc.) meet the management goals you identified in Step 1?',
                            a: 'bad'
                        },
                        q2: {
                            q: 'Do you think that the projected results/impacts from this plan will occur if the proposed actions are implemented?',
                            a: 'Satisfactory'
                        },
                        q3: {
                            q: 'What factors might prevent you from taking the recommended actions listed in this plan? (check all that apply)',
                            a: 'Satisfactory'
                        },
                        q4: {
                            q: 'How likely are you to implement the actions recommended in this plan?',
                            a: 'Well'
                        },
                        q5: {
                            q: 'How likely are you to work with other stakeholder groups to implement this plan?',
                            a: 'Satisfactory'
                        },
                        q6: {
                            q: 'What factors might prevent you from taking the recommended actions listed in this plan? (check all that apply)',
                            a: {
                                1: 'Infrastructure costs',
                            }
                        },
                        rating: '3'
                    },
                ],

                breadcrumb: [
                    {
                        text: 'Home',
                        to: { name: 'Home' }
                    },
                    {
                        text: 'Plans',
                        to: { name: 'Plans' }
                    },
                    {
                        text: 'Overview',
                        to: { name: 'Overview' }
                    }
                ]
            }
        },

        mounted() {
        },


        methods: {
            showFeedback(currentComponent, planId) {
                    this.adaptationPlan = 'Adaptation Plan '+planId;
                    this.currentComponent = currentComponent;
                    //EventBus.$emit('PLAN_FEEDBACK', this.currentComponent);

            },
        }

    }

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>

    .main{
        background-color: #efefef;
        padding: 1rem;
        min-height: 90vh;
    }

    .map-container {
        -webkit-box-flex: 1;
        -ms-flex: 1;
        flex: 1;
        height: calc(92vh - 20px);
    }
</style>

