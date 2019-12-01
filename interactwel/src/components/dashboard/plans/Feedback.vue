<template>
    <b-card-group>
        <b-card footer-tag="footer" v-for="item in filteredFeedbacks" v-bind:key="item">
            <div class="step-header" slot="header">{{item.plan}}
                <em slot="header">
                    <b-button size="sm">Share</b-button>
                    <b-button class="mr-2" size="sm">Edit</b-button>
                </em>
            </div>
            <b-card-text>
                <ol class="list-group list-group-flush">
                    <li class="list-group-item">{{item.q1.q}}<br/>
                        <small>{{item.q1.a}}</small>
                    </li>
                    <li class="list-group-item">{{item.q2.q}}<br/>
                        <small>{{item.q2.a}}</small>
                    </li>
                    <li class="list-group-item">{{item.q3.q}}<br/>
                        <small>{{item.q3.a}}</small>
                    </li>
                    <li class="list-group-item">{{item.q4.q}}<br/>
                        <small>{{item.q4.a}}</small>
                    </li>
                    <li class="list-group-item">{{item.q5.q}}<br/>
                        <small>{{item.q5.a}}</small>
                    </li>
                    <li class="list-group-item">{{item.q6.q}}<br/>
                        <div v-for="answers in item.q6.a" v-bind:key="answers">
                            <ul>
                                <li>
                                    <small>{{answers}}</small>
                                </li>
                            </ul>
                        </div>
                    </li>
                    <li class="list-group-item">Rating<br/>
                        <small>
                            <star-rating v-model="item.rating" read-only show-rating star-size='30'></star-rating>
                        </small>
                    </li>
                </ol>
            </b-card-text>
        </b-card>
    </b-card-group>
</template>

<script>
    import StarRating from 'vue-star-rating'


    export default {
        components: {
            StarRating
        },
        name: 'Feedback',

        props: {
            adaptationPlan: {
                type: String,
                default: ""
            },
        },

        data() {
            return {

                rating: 2,

                //adaptationPlanId : route.params.planId,

                feedbacks: [
                    {
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
                            q: 'What factors might prevent you from taking the recommended actions listed in this plan?',
                            a: {
                                1: 'Infrastructure costs',
                                2: 'Permits or other regulatory approval processes and cost'
                            }
                        },
                        rating: '5'
                    },
                    {
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
                            q: 'What factors might prevent you from taking the recommended actions listed in this plan?',
                            a: {
                                1: 'Infrastructure costs',
                            }
                        },
                        rating: '3'
                    },
                ],
            }
        },

        computed: {
            filteredFeedbacks() {
                return this.feedbacks.filter(item => item.plan === 'Adaptation Plan ' + this.$route.params.planId)
            }
        },

        mounted() {

        },


        methods: {}

    }

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
    .top-fixed-nav a, button a {
        color: #fff;
    }

    .router-link-exact-active {
        color: #4cae4c;
    }
</style>

