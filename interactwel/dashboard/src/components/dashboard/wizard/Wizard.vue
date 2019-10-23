<template>
    <div class="wizard-container">
        <b-tabs v-model="tabIndex" fill>
            <!-- Step 1-->
            <b-tab active>
                <template slot="title">
                    <div class="step-progress-bar">
                        <div class="step-no">1</div>
                        <h4 class="list-group-item-heading">Goals</h4>
                        <h4r v-if="isStep1Active" class="list-group-item-heading">&#10003;</h4r>
                        <p class="list-group-item-text">{{step1_desc}}</p>
                    </div>
                </template>
                <div id="step1" title="Step 1" icon="ti-user">
                    <div class="help-block">
                    <b-collapse visible id="collapse-1">
                        <b-card class="mb-2"
                                tag="article"
                                style="max-width: 25rem;"
                        >
                        <h4 class="card-title"> "What are Goals?"<b-button v-b-toggle.collapse-1 variant="outline-info" class="m-1b" size="sm"><i>Hide panel</i></b-button></h4>
                        
                            <!--<b-card title><strong>What are Goals?</strong></b-card title> -->
                            <!--<b-card-text v-if="isHelpStep1Active">-->
                            <b-card-text>
                                <!--<p align="justify">
                                    A community can suffer severe consequences from not effectively managing its water, energy, and land resources, especially when slow and sudden changes in the environment (e.g., changing climate, new policies, etc.) impair the quality, quantity, and accessibility of these resources over time.</p>-->
                                <p align="justify">Before choosing an appropriate plan of response (called <b>Adaptation Plan</b>), community members must choose what types of goals are important for them to achieve.
                                </p>
                                <ul>
                                    <li>These goals, also called <b>Adaptation Goals</b>, allow different groups within the community to evaluate how an adaptation plan may impact the bottom-line of each group, as well as that of the community at large.
                                    </li>
                                    <li>
                                        Further, many of these goals may be short-term goals, while others may need to be accomplished over a longer period of time.
                                    </li>
                                </ul>
                                <p align="justify"> In <b>Step 1</b>, think about what goals would be of interest to you and your stakeholders. Then choose from the options available in this list by clicking on the goals that reflect your priorities and interests.
                                </p>
                                <p aling="justify">
                                    You will be able to visualize how each adaptation plan meets the goals in <strong>Step 4</strong>.
                                </p>
                            </b-card-text>
                            
                        </b-card>
                    </b-collapse>
                    </div>
                    <b-card no-body footer-tag="footer">
                        <div class="step-header" slot="header">Choose Goals
                            <em slot="header">
                                <b-button v-b-toggle.collapse-1 class="m-1" size="sm"> Show instructions </b-button>
                            </em>
                            </div>
                            <b-card-body>
                                <p class="card-text"><i>
                                    Choose adaptation goals that are important to you.
                                </i></p>
                            </b-card-body>
                        <b-list-group-item>
                            <b-form-checkbox-group>
                                <label class="form-checkbox">
                                    <input type="checkbox" v-model="selectAllGoals" @click="selectGoals">
                                    Select All
                                </label>
                                <!-- <div class="text-uppercase text-bold">id selected: {{selectedGoals}}</div>-->
                            </b-form-checkbox-group>
                        </b-list-group-item>
                        <b-list-group flush>
                            <b-form>
                                <div class="list-group">
                                    <li class="list-group-item" v-for="goal in goals" v-bind:key="goal.id">
                                        <label class="form-checkbox" :disabled="goal.readonly">
                                            <input type="checkbox" :value="goal" v-model="selectedGoals"
                                                   :disabled="goal.readonly"/>
                                            {{goal.goal}}
                                            <p v-show="itemInfoVisibility" class="item-info">
                                                <small>{{goal.info}}</small>
                                            </p>
                                        </label>
                                        <b-badge class="info-button" pill variant="secondary" @click="showItemInfo">i
                                        </b-badge>
                                        <!--<b-badge class="info-button" pill variant="secondary" v-b-tooltip.hover
                                                 :title="goal.info">i
                                        </b-badge>-->
                                    </li>
                                </div>
                            </b-form>
                        </b-list-group>
                        <em slot="footer">
                            <b-button @click="step1NextClicked" variant="next" size="sm">Next</b-button>
                        </em>
                    </b-card>
                </div>
            </b-tab>
            <!-- Step 2 -->
            <b-tab :disabled="isStep1Active === false">
                <template slot="title">
                    <div class="step-progress-bar">
                        <div class="step-no">2</div>
                        <h4 class="list-group-item-heading">Actors</h4>
                        <h4r v-if="isStep2Active" class="list-group-item-heading">&#10003;</h4r>
                        <p class="list-group-item-text">{{step2_desc}}</p>
                    </div>
                </template>
                <div id="step2" title="Step 2"
                     icon="ti-settings">
                    <div class="help-block-actors">
                    <b-collapse visible id="collapse-2">
                        <b-card
                                tag="article"
                                style="max-width: 25rem;"
                                class="mb-2"
                        >
                        <h4 class="card-title">"Who are Actors?"<b-button v-b-toggle.collapse-2 variant="outline-info" class="m-1b" size="sm"><i>Hide panel</i></b-button></h4>
                            <!--<b-card-text><strong>Who are Actors?</strong></b-card-text><br/>-->
                            <b-card-text>
                                <p align="justify"><b>Actors</b>
                                    are groups of individuals, institutions, and organizations in a community who are most impacted, directly and/or indirectly, by the changes and stresses in the water, energy, and land resources they depend on.
                                </p>

                                <p align="justify">In <b>Step 2</b>, think about which group of actors would be of interest to you and your stakeholders. Then choose from the options available in this list by clicking on the options that reflect your group’s interest. Note that even though you may decide to choose only a few actors, your adaptation plans (in Step 4) may include additional actors who would need to also take actions in conjunction with you. But more on that when you reach Step 4!
                                </p>

                            </b-card-text>
                            
                        </b-card>
                        </b-collapse>
                    </div>
                    <b-card no-body footer-tag="footer">
                        <div class="step-header" slot="header">Choose Actors
                        <em slot="header">
                                <b-button v-b-toggle.collapse-2 class="m-1" size="sm"> Show instructions </b-button>
                        </em>
                        </div>
                        <b-card-body>
                            <p class="card-text"><i>
                                Choose the actors whose adaptation actions you want to visualize.
                            </i></p>
                        </b-card-body>
                        <b-list-group-item>
                            <b-form-checkbox-group>
                                <label class="form-checkbox">
                                    <input type="checkbox" v-model="selectAllActors" @click="selectActors">
                                    Select All
                                </label>
                                <!--<div class="text-uppercase text-bold">id selected: {{selectedActors}}</div>-->
                            </b-form-checkbox-group>
                        </b-list-group-item>
                        <b-list-group flush>
                            <b-form>
                                <div class="list-group">
                                    <li class="list-group-item" v-for="actor in actors" v-bind:key="actor.id">
                                        <label class="form-checkbox">
                                            <input type="checkbox" :value="actor" v-model="selectedActors"
                                                   :disabled="actor.readonly">
                                            {{actor.actor}}
                                        </label>
                                        <b-badge class="info-button" pill variant="secondary" v-b-tooltip.hover
                                                 :title="actor.info">i
                                        </b-badge>
                                    </li>
                                </div>
                            </b-form>
                        </b-list-group>
                        <em slot="footer">
                            <!--<b-button-group>
                                <b-button id="step2-back-btn" @click="tabIndex--" variant="outline-success" size="sm">
                                    Back
                                </b-button>
                                <b-button id="step2-next-btn" @click="step2NextClicked" variant="success" size="sm">Next
                                </b-button>
                            </b-button-group>-->
                                <b-button id="step2-next-btn" @click="step2NextClicked" variant="next" size="sm">Next</b-button>
                                <b-button id="step2-back-btn" @click="tabIndex--" variant="back" size="sm">Back</b-button>
                        </em>
                    </b-card>
                </div>
            </b-tab>

            <!-- Step 3 -->
            <b-tab :disabled="isStep2Active === false">
                <template slot="title">
                    <div class="step-progress-bar">
                        <div class="step-no">3</div>
                        <h4 class="list-group-item-heading">Actions</h4>
                        <h4r v-if="isStep3Active" class="list-group-item-heading">&#10003;</h4r>
                        <p class="list-group-item-text">{{step3_desc}}</p>
                    </div>
                </template>
                <div id="step3" title="Step 3"
                     icon="ti-check">
                    <div class="help-block-actions">
                    <b-collapse visible id="collapse-3">
                        <b-card
                                tag="article"
                                style="max-width: 25rem;"
                                class="mb-2">
                                <h4 class="card-title">"What are Actions?"<b-button v-b-toggle.collapse-3 variant="outline-info" class="m-1b" size="sm"><i>Hide panel</i></b-button></h4>
                            <!-- <b-card-text><strong>Why select Actions?</strong></b-card-text><br/> -->
                            <b-card-text>
                                <p align="justify"><b>Adaptation Actions</b>
                                    are management actions that adjust the allocation of resources, operations, and assets.  These management actions are formulated to adapt to changing basin conditions that effect quality, quantity, and accessibility of water, energy, and land resources. These actions include a variety of approaches – from infrastructure building, adopting new technologies to raising awareness.
                                </p>
                                <p align="justify">In <b>Step 3</b>, think about types of actions would be of interest to the actors you selected in Step 2 and select from the options available on the list. Please note that your adaptation plans (in Step 4) may include additional actions. But more on that when you reach Step 4!
                                </p>
                            </b-card-text>
                        </b-card>
                        </b-collapse>
                    </div>
                    <b-card style="width: 700px" no-body footer-tag="footer">
                        <div class="step-header" slot="header">Choose Actions
                            <em slot="header">
                                <b-button v-b-toggle.collapse-3 class="m-1" size="sm"> Show instructions </b-button>
                            </em>
                        </div>
                        <b-list-group-item>
                            <b-form-checkbox-group>
                                <label class="form-checkbox">
                                    <input type="checkbox" v-model="selectAllActions" @click="selectActions">
                                    Select All
                                </label>
                                <!-- <div class="text-uppercase text-bold">id selected: {{selectedActions}}</div>-->

                            </b-form-checkbox-group>
                        </b-list-group-item>
                        <b-card-body>
                        <p class="card-text"><i> Please choose from the drop-down menu the actor for which you want to define the possible actions.</i></p>
                        <h4>Selected actors         Available actions</h4>
                            <b-tabs card vertical content-class="mt-3" style="margin-top: 0px">
                                <b-tab :title="actor.actor" v-for="actor in selectedActors" v-bind:key="actor.id">
                                    <div class="list-group">
                                        <li class="list-group-item" v-for="action in actions" v-bind:key="action.id">
                                            <label class="form-checkbox" :disabled="action.readonly">
                                                <input type="checkbox" :value="actor.id + ',' + action.id"
                                                       v-model="selectedActions"
                                                       :disabled="action.readonly"/>
                                                {{action.action}}
                                            </label>
                                            <b-badge class="info-button" pill variant="secondary" v-b-tooltip.hover
                                                     :title="action.info">
                                            </b-badge>
                                        </li>
                                    </div>
                                </b-tab>
                            </b-tabs>
                            
                            <!--<b-form-select v-model="selected">
                                <option :value="null"disabled>-- Please select an actor --</option>
                                <option :value="actor.id" v-for="actor in selectedActors" v-bind:key="actor.id">{{actor.actor}}</option>
                            </b-form-select>
                            <div class="list-group">
                                <li class="list-group-item" v-for="action in actions" v-bind:key="action.id">
                                    <label class="form-checkbox" :disabled="action.readonly">
                                        <input type="checkbox" :value="selected + ',' + action.id"
                                                v-model="selectedActions"
                                                :disabled="action.readonly"/>
                                        {{action.action}}
                                    </label>
                                    <b-badge class="info-button" pill variant="secondary" v-b-tooltip.hover
                                                :title="action.info">
                                    </b-badge>
                                </li>
                            </div>-->

                        </b-card-body>
                        <em slot="footer">
                            <!--<b-button-group>
                                <b-button id="step3-back-btn" @click="tabIndex--" variant="back" size="sm">
                                    Back
                                </b-button>
                                <b-button id="step3-next-btn" @click="step3NextClicked" variant="next"
                                          size="sm">Next
                                </b-button>
                            </b-button-group>-->
                            <b-button id="step3-next-btn" @click="step3NextClicked" variant="next" size="sm">Next</b-button>
                            <b-button id="step3-back-btn" @click="tabIndex--" variant="back" size="sm">Back</b-button>
                        </em>
                    </b-card>
                </div>
            </b-tab>
            <!-- Step 4 -->
            <b-tab :disabled="isStep3Active === false">
                <template slot="title">
                    <div class="step-progress-bar">
                        <div class="step-no">4</div>
                        <h4 class="list-group-item-heading">Visualization</h4>
                        <!--<h4r v-if="isStep4Active" class="list-group-item-heading">&#10003;</h4r>-->
                        <p class="list-group-item-text">{{step4_desc}}</p>
                    </div>
                </template>
                <div id="step4" title="Step 4">
                <div class="help-block-viz">
                    <b-collapse visible id="collapse-4">
                        <b-card
                                tag="article"
                                style="max-width: 33rem;"
                                class="mb-2"
                        >
                        <h4 class="card-title">"What are Adaptation Plans?"<b-button v-b-toggle.collapse-4 variant="outline-info" class="m-1b" size="sm"><i>Hide panel</i></b-button></h4>
                            <!--<b-card-text><strong>Who are Actors?</strong></b-card-text><br/>-->
                            <b-card-text>
                                <p align="justify">In this section you will be able to view multiple adaptation plans that incorporate the actors <strong>(Step 2)</strong> and actions <strong>(Step 3)</strong> that you selected.  You can compare how each adaptation plan meets the goals you selected in <strong>Step 1</strong> for the entire basin, sub-basins, and individual streams.  You can also compare the actions and their timeframes included within each plan.</p>
                                <p aling="justify">Remember that you can click the map to visualize the data. </p>
                            </b-card-text>
                            
                        </b-card>
                        </b-collapse>
                    </div>

                    <b-card no-body footer-tag="footer">
                        <div class="step-header" slot="header">Visualization
                            <em slot="header">
                                <b-button v-b-toggle.collapse-4 class="m-1" size="sm"> Show instructions </b-button>
                            </em>
                        </div>
                        <b-card-body class="no-padding">
                            <b-container>
                                <b-row>
                                    <nav>
                                        <sidebar></sidebar>
                                    </nav>
                                    <article>
                                        <!--<router-view></router-view>-->
                                        <charts :goals="goals" :actors="actors" :actions="actions"
                                                :selectedGoals="selectedGoals" :selectedActors="selectedActors"
                                                :selectedActions="selectedActions"></charts>
                                    </article>
                                </b-row>
                            </b-container>
                        </b-card-body>
                        <em slot="footer">
                            <!--<b-button-group>
                                <b-button id="step2-back-btn" @click="step4BackClicked" variant="outline-success" size="sm">
                                    Back
                                </b-button>
                                <b-button id="step2-next-btn" @click="step4NextClicked" variant="success" size="sm">Next
                                </b-button>
                            </b-button-group>-->
                            <b-button id="step2-next-btn" @click="step4NextClicked" variant="next" size="sm">Next</b-button>
                            <b-button id="step2-back-btn" @click="step4BackClicked" variant="back" size="sm">Back</b-button>
                            
                        </em>
                    </b-card>
                    
                </div>
            </b-tab>
            <!-- Step 5 -->
            <b-tab :disabled="isStep3Active === false">
                <template slot="title">
                    <div class="step-progress-bar">
                        <div class="step-no">5</div>
                            <h4 class="list-group-item-heading">Feedback</h4>
                        <p class="list-group-item-text">{{step5_desc}}</p>
                    </div>
                </template>
                <div id="step5" title="Step 5"
                     icon="ti-check">

                    <b-card no-body footer-tag="footer">
                        <b-card-body class="no-padding">
                            <b-container>
                                <b-row>
                                    <nav>
                                        <sidebar></sidebar>
                                    </nav>
                                    <article>
                                        <charts :goals="goals" :actors="actors" :actions="actions"
                                                :selectedGoals="selectedGoals" :selectedActors="selectedActors"
                                                :selectedActions="selectedActions"></charts>
                                        <feedback :feedbackOn="feedbackOn"></feedback>
                                    </article>
                                </b-row>
                            </b-container>
                        </b-card-body>
                        <em slot="footer">
                            <!--<b-button-group>
                                <b-button id="step3-back-btn" @click="step5BackClicked" variant="outline-success" size="sm">
                                    Back
                                </b-button>
                                <b-button id="step3-next-btn" @click="step5NextClicked" variant="success" size="sm">Next
                                </b-button>
                            </b-button-group>-->
                            <b-button id="step3-next-btn" @click="step5NextClicked" variant="next" size="sm">Next</b-button>
                            <b-button id="step3-back-btn" @click="step5BackClicked" variant="back" size="sm">Back</b-button>
                        </em>
                    </b-card>
                </div>
            </b-tab>
            <!-- Step 6 -->
            <b-tab :disabled="isStep3Active === false">
                <template slot="title">
                    <div class="step-progress-bar">
                        <div class="step-no">6</div>
                        <h4 class="list-group-item-heading">Share</h4>
                        <p class="list-group-item-text">{{step6_desc}}</p>
                    </div>
                </template>
                <div id="step6" title="Step 6"
                     icon="ti-user">
                    <b-card no-body footer-tag="footer">
                        <div class="step-header" slot="header">Share</div>
                        <b-card-body>
                            <b-table class="card-text" bordered small hover :items="items" :fields="fields">
                                <template slot="rating" slot-scope="data">
                                    <star-rating star-size="20"></star-rating>
                                </template>
                                <template v-slot:cell(download)="data">
                                    <b-button pill size="sm"
                                              variant="primary">Download
                                    </b-button>
                                </template>
                                <template v-slot:cell(save)="data">
                                    <b-button pill size="sm"
                                              variant="secondary">Save
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
                            <b-button id="step6-next-btn" @click="tabIndex++" variant="next" size="sm">Next</b-button>
                            <b-button id="step6-next-btn" @click="step6BackClicked" variant="back" size="sm">Back</b-button>
                        </em>
                    </b-card>
                </div>
            </b-tab>
        </b-tabs>

        <b-modal v-model="showInfoModal" ok-only>
            <template slot="modal-title">
                <strong>No selections were made</strong>
            </template>
            Please be advised that all available choices will be selected.
            <template slot="modal-footer" slot-scope="{ ok, cancel, hide }">
                <b-button size="sm" variant="next" @click="ok()">Ok</b-button>
            </template>
        </b-modal>

        <b-modal v-model="showInfoModalActions" ok-only>
            <template slot="modal-title">
                <strong>No selections were made</strong>
            </template>
            
            <ul id="example-1">
                <li v-for="i in missingActionsActors">
                   Please be advised that all available choices will be selected for actor: {{ actors[i].actor }}
                </li>
            </ul>

            <template slot="modal-footer" slot-scope="{ ok, cancel, hide }">
                <b-button size="sm" variant="next" @click="ok()">Ok</b-button>
            </template>
        </b-modal>


    </div>
</template>

<script>
    import axios from 'axios';

    import Charts from '../charts/ChartContainer.vue';
    import Sidebar from '../sidebar/Sidebar.vue';
    import Feedback from '../feedback/Feedback.vue';
    import Compare from '../feedback/Compare.vue';
    import EventBus from './../../../event-bus';
    

    import ActionsOpts from './../../../../public/static/actions.json';
    import GoalsOpts from './../../../../public/static/goals.json';
    import ActorsOpts from './../../../../public/static/actors.json';

    import StarRating from 'vue-star-rating'

    export default {

        name: 'wizard',
        components: {
            Compare,
            Feedback,
            Sidebar,
            Charts,
            StarRating
            
        },

        data() {
            return {
                tabIndex: 0,
                itemInfoVisibility: false,

                show: true,
                showInfoModal: false,
                showInfoModalActions: false,

                step1_desc: "Choose Goals",
                step2_desc: "Choose Actors",
                step3_desc: "Choose Actions",
                step4_desc: "Visualize Adaptation plans",
                step5_desc: "Rate Adaptation plans",
                step6_desc: "Share",

                isStep1Active: false,
                isStep2Active: false,
                isStep3Active: false,
                isStep4Active: false,
                isStep5Active: false,

                isHelpStep1Active: true,

                selectedActions: [],
                selectedActionsActors: [],
                missingActionsActors: [],
                selectAllActions: false,

                selectedGoals: [],
                selectAllGoals: false,

                selectedActors: [],
                selectAllActors: false,

                goals: GoalsOpts,
                actions: ActionsOpts,
                actors: ActorsOpts,
                actor: [],
                selected: null,

                fields: [
                    {
                        key: 'plan',
                        label: 'Plan',
                        sortable: true
                    },
                    {
                        key: 'q1',
                        label: 'Meet Management Goals?',
                        sortable: false
                    },
                    {
                        key: 'q2',
                        label: 'Expectations of projected impacts',
                        sortable: false
                    },
                    {
                        key: 'q3',
                        label: 'Likely to implement recommended actions',
                        sortable: false
                    },
                    {
                        key: 'q4',
                        label: 'Likely to collaborate with others to implement plan',
                        sortable: false
                    },
                    {
                        key: 'rating',
                        label: 'Overall rating',
                        sortable: true
                    },
                    {key: 'download', label: ''},
                    {key: 'save', label: ''},
                ],
                items: [
                    { isActive: true, plan: 1, q1: 'yes', q2: 'Satisfactory', q3: 'yes', q4: 'yes'},
                    { isActive: false, plan: 2, q1: 'yes', q2: 'Well' , q3: 'yes', q4: 'yes'},
                    { isActive: false, plan: 3, q1: 'yes', q2: 'Very well' , q3: 'yes', q4: 'yes'},
                    { isActive: true, plan: 4, q1: 'yes', q2: 'Neutral', q3: 'yes', q4: 'yes' }
                ],
                itemsX: [
                    { 'plan': 1, 'Meet Management Goals?' : 'yes', 'Expectations of projected impacts' : 'Dickerson', 'Likely to implement recommended actions': 'Macdonald' },
                ],
                fieldX: [
                    {key: 'plan', label: 'Plan'},
                    {key: 'Meet Management Goals?', label: 'Meet Management Goals?'},
                    {key: 'Expectations of projected impacts', label: 'Expectations of projected impacts'},
                    {key: 'Likely to implement recommended actions', label: 'Likely to implement recommended actions'},
                    {key: 'Likely to collaborate with others to implement plan', label: 'Likely to collaborate with others to implement plan'},
                    {key: 'Overall rating', label: 'Overall rating'},
                    {key: 'download', label: ''},
                    {key: 'save', label: ''},
                ],

                feedbackOn: "hello"
            }
        },

        mounted() {
            let $this = this;
            EventBus.$on('CLICK_ITEM_SIDEBAR', function (planName) {
                $this.feedbackOn == planName;
            })
        },

        methods: {
            selectGoals() {
                this.selectedGoals = [];
                if (!this.selectAllGoals) {
                    this.goals.forEach(element => {
                        if (element.readonly == false) {
                            this.selectedGoals.push(element);
                        }
                    });
                }
            },

            selectActors() {
                this.selectedActors = [];
                if (!this.selectAllActors) {
                    this.actors.forEach(element => {
                        if (element.readonly == false) {
                            this.selectedActors.push(element);
                        }
                    });
                }
            },

            CheckActorsACtions(){
                this.selectedActionsActors = [];
                this.missingActionsActors = [];
                if (!this.selectAllActions) {
                    for (var i = 0; i < this.selectedActions.length; i++) {
                        if(this.selectedActionsActors.includes(this.selectedActions[i][0]) == false){
                            this.selectedActionsActors.push(this.selectedActions[i][0]);
                            //console.log(this.selectedActions[i][0]);
                        }
                    }
                    for (let actor in this.selectedActors) {
                        if(this.selectedActionsActors.includes(actor) == false){
                            this.missingActionsActors.push(actor);
                            //console.log(actor);
                        } 
                    }
                }
            },

            selectActions() {
                if (this.selectAllActions) {
                    this.selectedActions = [];
                    for (let actor in this.actors) {
                        for (let action in this.actions) {
                            if (this.actors[actor].readonly == false && this.actions[action].readonly == false) {
                                this.selectedActions.push(this.actors[actor].id + ',' + this.actions[action].id);
                            }
                        }
                    }
                }
                
                if (this.missingActionsActors.length !== 0) {
                    for (var i = 0; i < this.missingActionsActors.length; i++) {
                        //console.log(this.missingActionsActors[i])
                        for (let action in this.actions) {
                            if (this.actors[this.missingActionsActors[i]].readonly == false && this.actions[action].readonly == false) {
                                //console.log(this.actors[this.missingActionsActors[i]].id + ',' + this.actions[action].id)
                                this.selectedActions.push(this.actors[this.missingActionsActors[i]].id + ',' + this.actions[action].id);
                            }
                        }
                    }
                }
            },

            step1NextClicked() {
                if (this.selectedGoals.length == 0) {
                    this.selectGoals()
                    this.selectAllGoals = true
                    this.showInfoModal = true
                    this.tabIndex++
                    this.isStep1Active = true
                }
                else {
                    this.tabIndex++
                    this.isStep1Active = true
                    return true
                }

            },

            step2NextClicked() {
                if (this.selectedActors.length == 0) {
                    this.selectActors()
                    this.selectAllActors = true
                    this.showInfoModal = true
                    this.tabIndex++
                    this.isStep2Active = true
                }
                else {
                    this.tabIndex++
                    this.isStep2Active = true
                    return true
                }

            },

            step3NextClicked() {
                this.CheckActorsACtions()
                
                if (this.selectedActions.length == 0) {
                    this.selectActions()
                    this.selectAllActions = true
                    this.showInfoModalActions = true
                    this.tabIndex++
                    this.isStep3Active = true

                }else if(this.missingActionsActors.length !== 0) {
                    this.selectActions()
                    this.showInfoModalActions = true
                    this.tabIndex++
                    this.isStep3Active = true
                    return true
                }
                else {
                    this.tabIndex++
                    this.isStep3Active = true
                   // this.$router.push({ name: 'Plan', params: { planId: 1 } })
                    return true
                }

            },

            step4NextClicked() {
                //EventBus.$emit('SHOW_ASIDE');
                this.tabIndex++
            },

            step5NextClicked() {
                EventBus.$emit('HIDE_ASIDE');
                this.tabIndex++
            },

            step5BackClicked() {
                EventBus.$emit('HIDE_ASIDE');
                this.tabIndex--
            },

            step4BackClicked() {
                EventBus.$emit('HIDE_ASIDE');
                this.tabIndex--
            },

            step6BackClicked() {
                EventBus.$emit('SHOW_ASIDE');
                this.tabIndex--
            },

            showItemInfo() {
                if (this.itemInfoVisibility == true) {
                    this.itemInfoVisibility = false
                } else {
                    this.itemInfoVisibility = true
                }

            }

        }
    }
</script>

<style>
    .wizard-container {
        /* position: absolute;*/
        /*background-color: #0000007a;
        width: 100%;
        height: 100%;*/
        z-index: 10000;
    }

    #step1 {
        position: absolute;
        z-index: 1000;
        left: 30px;
        top: 80px;
        min-width: 350px;
    }

    #step2 {
        position: absolute;
        z-index: 1000;
        left: 30px;
        top: 80px;
        min-width: 350px;
    }

    #step3 {
        position: absolute;
        z-index: 1000;
        left: 30px;
        top: 80px;
    }

    #step4 {
        display: flex;
        position: absolute;
        z-index: 1000;
        left: 30px;
        top: 80px;
        width: 1000px;
    }

    #step5 {
        position: absolute;
        z-index: 1000;
        left: 100px;
        top: 100px;
    }

    #step6 {
        position: absolute;
        z-index: 1000;
        left: 100px;
        top: 100px;
        width:900px;
    }

    .step-progress-bar h4 {
        font-size: 1em;
        font-weight: 700;
        color: #5f6c73;
        margin-bottom: .05rem;
        text-align: left;
    }

    .step-progress-bar h4r {
        float: right;
        font-size: 1em;
        font-weight: 700;
        color: #5f6c73;
        margin-bottom: .05rem;
        text-align: right;
    }

    .step-progress-bar p {
        font-weight: 400;
        font-size: .72857143em;
        color: #5f6c73;
        margin-bottom: 0;
        text-align: left;
    }

    .step-progress-bar .step-no {
        float: left;
        font-size: 25px;
        font-weight: 700;
        color: #28a745;
        width: 30px;
    }

    .step-progress-bar .active {
        background: #DCEDC8;
    }

    .wizard-container .nav-tabs .nav-item.show .nav-link, .nav-tabs .nav-link.active {
        background: #DCEDC8 !important;
        border: none;
    }

    .wizard-container .nav-tabs .nav-item.show .nav-link, .nav-tabs .nav-link:hover {
        background: #e4f5d0 !important;
        border: none;
    }

    .arrow_box {
        position: relative;
        background: #DCEDC8;
        border-right: 2px solid #28a745;
        border-left: none;
    }

    .arrow_box:after, .arrow_box:before {
        left: 100%;
        top: 50%;
        border: solid transparent;
        content: " ";
        height: 0;
        width: 0;
        position: absolute;
        pointer-events: none;
    }

    .arrow_box:after {
        border-color: rgba(136, 183, 213, 0);
        border-left-color: #28a745;
        border-width: 11px;
        margin-top: -11px;
    }

    .arrow_box:before {
        border-color: rgba(95, 108, 115, 0);
        border-left-color: #28a745;
        border-width: 10px;
        margin-top: -10px;
        z-index: 1 !important;
    }

    .info-button {
        float: right !important;
    }

    .help-block {
        position: absolute;
        border: none;
        right: -440px;
        z-index: 1000;
    }

    .help-block-actors {
        position: absolute;
        border: none;
        right: -440px;
        z-index: 1000;
    }

    .help-block-viz {
        position: absolute;
        border: none;
        right: -530px;
        z-index: 1000;
    }

    .help-block-actions {
        position: absolute;
        right: -450px;
        z-index: 1000;
    }

    .help-block .card-body, .help-block-actors .card-body, .help-block-actions .card-body {
        padding: 1.5rem;
    }

    .step-header {
        font-size: 18px;
        font-weight: bold;
    }

    .card-text {
        font-size: 13px;
        color: #5e6b7e;
    }

    .card-title {
        font-size: 25px;
        font-weight: bold;
        color: #5e6b7e;
        border-bottom: 2px solid #28a645;
        padding-bottom: 5px;
    }

    #step4 > article {
        flex: 1;
        height: calc(60vh - 20px);
    }

    #step4 nav,#step5 nav {
        flex: 0 0 auto;
        min-width: 200px;
        overflow: auto;
        background-color: #263238;
        height: inherit;
    }

    .item-info {
        margin-top: 5px;
        max-width: 250px;
    }

    .nav-pills .nav-link.active, .nav-pills .show > .nav-link {
        color: #fff;
        background-color: #4cae4c !important;
    }

    #step3 .nav-item a {
        color: #28a645;
        text-decoration: none;
        font-weight: 500;
        background-color: transparent;
        font-size: 14px;
    }

    #step3 .nav-item .nav-link.active {
        color: #5e6b7e;
        font-weight: 500;
        background-color: #FFFFFF;
        font-size: 14px;
        border-top: 2px solid #28a645;
    }

    .btn{
        float: right;
        margin-right: 0px;
    }

    .btn.m-1{
        margin: -0.05rem !important;
    }

    .btn-next{
        color: #fff !important;
        background-color: #28a745 !important;
        border-color: #28a745 !important;
        padding: .25rem 3rem !important;
        float: right !important;
        margin-right: 0px !important;
    }

    .btn-back{
        color: #28a745 !important;
        background-color: transparent !important;
        border-color: #28a745 !important;
        padding: .25rem 3rem !important;
        float: left !important;
        margin-left: 0px !important;
    }

    .btn-outline-info{
        margin: .05rem !important;
        background-color: #FFFFFF;
        border-color: #FFF !important;
    }

</style>
