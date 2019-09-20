<template>
    <div>
        <component v-bind:is="component='Header'"></component>
        <b-container fluid class="main">
            <b-breadcrumb :items="breadcrumb"></b-breadcrumb>
            <b-row>
                <b-col lg="2">
                    <b-card no-body class="mb-1" v-for="project in projects">
                        <b-card-header header-tag="header" class="p-1" role="tab">
                            <b-button block href="#" v-b-toggle="project.id" variant="success">{{project.name}}</b-button>
                        </b-card-header>
                        <b-collapse :id="project.id" visible accordion="my-accordion" role="tabpanel">
                            <b-card-body>
                                <b-form inline>
                                    <label class="mr-sm-2" for="inline-form-custom-select-pref">Sort By</label>
                                    <b-form-select
                                            class="mb-2 mr-sm-2 mb-sm-0"
                                            :value="null"
                                            :options="{ '1': 'Cost', '2': 'Sustainability', '3': 'Resilience', '4': 'Rating' }"
                                            id="inline-form-custom-select-pref"
                                    >
                                        <template v-slot:first>
                                            <option :value="null">Choose...</option>
                                        </template>
                                    </b-form-select>
                                </b-form>
                                <b-list-group>
                                    <b-list-group-item><router-link v-bind:to="'/visualization/' + project.name"><b-button block size="sm">Visualize</b-button></router-link></b-list-group-item>
                                    <router-link v-bind:to="'/plans/' + project.id +'/overview'"><b-list-group-item>Overview</b-list-group-item></router-link>
                                </b-list-group>
                                <b-list-group v-for="item in feedbacks">
                                    <router-link v-bind:to="'/plans/' + project.id +'/feedback/' + item.id"><b-list-group-item>{{item.plan}}</b-list-group-item></router-link>
                                </b-list-group>
                            </b-card-body>
                        </b-collapse>
                    </b-card>
                </b-col>
                <b-col lg="10">
                    <h5>Project: Umatilla</h5>
                    <b-card no-body>
                        <router-view></router-view>
                    </b-card>
                </b-col>
            </b-row>
        </b-container>
        <component v-bind:is="component='Footer'"></component>
    </div>
</template>

<script>
    import Header from './Header.vue';
    import Footer from './Footer.vue';
    import CreateProject from './project/CreateProject.vue';
    import Overview from './plans/Overview.vue';
    import Feedback from './plans/Feedback.vue';
    import LeafletMap from './../dashboard/map/LeafletMap.vue'

    export default {
        components: {
            Header, Footer, LeafletMap, CreateProject, Overview, Feedback
        },
        name: 'Plans',

        props: {
            adaptationPlan: {
                type: String,
                default: ""
            },
        },

        data() {
            return {
                projectId: 1,

                feed:{},

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

                projects: [
                    {id:1, name: "Umatilla"},
                    {id:2, name: "Texas"},
                    {id:3, name: "Colarado"}
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

    #main{
        display: -webkit-box;
        display: -ms-flexbox;
        display: flex;
        min-height: 60vh;
    }

    #main > nav {
        -webkit-box-flex: 0;
        -ms-flex: 0 0 auto;
        flex: 0 0 auto;
        min-width: 200px;
        overflow: auto;
        background-color: #37474f;
        -webkit-box-ordinal-group: 0;
        -ms-flex-order: -1;
        order: -1;
        height: calc(92vh - 20px);
    }

    #main > article {
        -webkit-box-flex: 1;
        -ms-flex: 1;
        flex: 1;
        height: calc(92vh - 20px);
    }

    #main > aside {
        -webkit-box-flex: 0;
        -ms-flex: 0 0 400px;
        flex: 0 0 400px;
        height: calc(92vh - 20px);
        overflow: auto;
        padding: 1rem;
        background-color: #fff;
    }

    .main {
        background-color: #efefef;
        padding: 1rem;
        min-height: 90vh;
    }

    .map-wrapper {
        -webkit-box-flex: 1;
        -ms-flex: 1;
        flex: 1;
        min-height: calc(60vh);
    }

    .widget {
        background-color: #f7f7f7;
        padding: 1rem;
        border: 1px solid #efefef;
        border-radius: 5px;
        margin-bottom: 10px;
    }

    .widget-title {
        font-size: 16px;
        font-weight: 700;
    }
</style>

