<template>
    <div>
        <component v-bind:is="component='Header'"></component>
        <b-container fluid class="main">
            <b-breadcrumb :items="breadcrumb"></b-breadcrumb>
            <b-row>
                <b-col lg="8">
                    <h2>Select Project to Proceed</h2>
                    <b-card no-body>
                        <b-tabs pills card vertical nav-wrapper-class="w-50">
                            <b-tab title="Tab 1" active><b-card-text>Tab Contents 1</b-card-text></b-tab>
                            <b-tab title="Tab 2"><b-card-text>Tab Contents 2</b-card-text></b-tab>
                            <b-tab title="Tab 3"><b-card-text>Tab Contents 3</b-card-text></b-tab>
                        </b-tabs>
                    </b-card>
                    <b-list-group>
                        <b-list-group-item href="#some-link">Awesome link</b-list-group-item>
                        <b-list-group-item href="#" active>Link with active state</b-list-group-item>
                        <b-list-group-item href="#">Action links are easy</b-list-group-item>
                        <b-list-group-item href="#foobar" disabled>Disabled link</b-list-group-item>
                    </b-list-group>
                </b-col>
            </b-row>
        </b-container>
        <component v-bind:is="component='Footer'"></component>
    </div>
</template>

<script>
    import Header from './../Header.vue';
    import Footer from './../Footer.vue';
    import CreateProject from './../project/CreateProject.vue';
    import Overview from './../plans/Overview.vue';
    import Feedback from './../plans/Feedback.vue';
    import LeafletMap from './../../dashboard/map/LeafletMap.vue'

    export default {
        components: {
            Header, Footer, LeafletMap, CreateProject, Overview, Feedback
        },
        name: 'VisualizationOverview',

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

