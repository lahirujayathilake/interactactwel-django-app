<template>
    <div class="wizard-container">
        <b-tabs v-model="tabIndex" fill>
            <!-- Step 1-->
            <b-tab active>
                <template slot="title">
                    <div class="step-progress-bar">
                        <div class="step-no">1</div>
                        <h4 class="list-group-item-heading">Goals</h4>
                        <h4r class="list-group-item-heading">&#10003;</h4r>
                        <p class="list-group-item-text">{{step1_desc}}</p>
                        
                    </div>
                    
                </template>
                <div id="step1" title="Step 1"
                     icon="ti-user">
                    <div class="help-block">
                        <b-card class="mb-2"
                                title="What are Goals?"
                                tag="article"
                                style="max-width: 25rem;"

                        >
                            <!--<b-card title><strong>What are Goals?</strong></b-card title> -->
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
                    </div>
                    <b-card no-body footer-tag="footer">
                        <div class="step-header" slot="header">Choose Goals</div>
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
                            <b-button @click="step1NextClicked" variant="success" size="sm">Next</b-button>
                        </em>
                    </b-card>
                </div>
            </b-tab>
            <!-- Step 2 -->
            <b-tab>
                <template slot="title">
                    <div class="step-progress-bar">
                        <div class="step-no">2</div>
                        <h4 class="list-group-item-heading">Actors</h4>
                        <p class="list-group-item-text">{{step2_desc}}</p>
                    </div>
                </template>
                <div id="step2" title="Step 2"
                     icon="ti-settings">
                    <div class="help-block-actors">
                        <b-card
                                title="Who are Actors?"
                                tag="article"
                                style="max-width: 25rem;"
                                class="mb-2"
                        >
                            <!--<b-card-text><strong>Who are Actors?</strong></b-card-text><br/>-->
                            <b-card-text>
                                <p align="justify"><b>Actors</b>
                                    are groups of individuals, institutions, and organizations in a community who are most impacted, directly and/or indirectly, by the changes and stresses in the water, energy, and land resources they depend on.
                                </p>

                                <p align="justify">In <b>Step 2</b>, think about which group of actors would be of interest to you and your stakeholders. Then choose from the options available in this list by clicking on the options that reflect your group’s interest. Note that even though you may decide to choose only a few actors, your adaptation plans (in Step 4) may include additional actors who would need to also take actions in conjunction with you. But more on that when you reach Step 4!
                                </p>

                            </b-card-text>
                        </b-card>
                    </div>
                    <b-card no-body footer-tag="footer">
                        <div class="step-header" slot="header">Choose Actors</div>
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
                            <b-button-group>
                                <b-button id="step2-back-btn" @click="tabIndex--" variant="outline-success" size="sm">
                                    Back
                                </b-button>
                                <b-button id="step2-next-btn" @click="step2NextClicked" variant="success" size="sm">Next
                                </b-button>
                            </b-button-group>
                        </em>
                    </b-card>
                </div>
            </b-tab>
            <!-- Step 3 -->
            <b-tab>
                <template slot="title">
                    <div class="step-progress-bar">
                        <div class="step-no">3</div>
                        <h4 class="list-group-item-heading">Actions</h4>
                        <p class="list-group-item-text">{{step3_desc}}</p>
                    </div>
                </template>
                <div id="step3" title="Step 3"
                     icon="ti-check">
                    <div class="help-block-actions">
                        <b-card
                                title="What are Actions?"
                                tag="article"
                                style="max-width: 25rem;"
                                class="mb-2"
                        >
                            <!-- <b-card-text><strong>Why select Actions?</strong></b-card-text><br/> -->
                            <b-card-text>
                                <p align="justify"><b>Adaptation Actions</b>
                                    are management actions that adjust the allocation of resources, operations, and assets.  These management actions are formulated to adapt to changing basin conditions that effect quality, quantity, and accessibility of water, energy, and land resources. These actions include a variety of approaches – from infrastructure building, adopting new technologies to raising awareness.
                                </p>
                                <p align="justify">In <b>Step 3</b>, think about types of actions would be of interest to the actors you selected in Step 2 and select from the options available on the list. Please note that your adaptation plans (in Step 4) may include additional actions. But more on that when you reach Step 4!
                                </p>
                            </b-card-text>
                        </b-card>
                    </div>
                    <b-card style="width: 580px" no-body footer-tag="footer">
                        <div class="step-header" slot="header">Choose Actions</div>
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
                            <b-tabs content-class="mt-3">
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

                        </b-card-body>
                        <em slot="footer">
                            <b-button-group>
                                <b-button id="step3-back-btn" @click="tabIndex--" variant="outline-success" size="sm">
                                    Back
                                </b-button>
                                <b-button id="step3-next-btn" @click="step3NextClicked" variant="success"
                                          size="sm">Next
                                </b-button>
                            </b-button-group>
                        </em>
                    </b-card>
                </div>
            </b-tab>
            <!-- Step 4 -->
            <b-tab>
                <template slot="title">
                    <div class="step-progress-bar">
                        <div class="step-no">4</div>
                        <h4 class="list-group-item-heading">Visualization</h4>
                        <p class="list-group-item-text">{{step4_desc}}</p>
                    </div>
                </template>
                <div id="step4" title="Step 4">
                    <b-card no-body footer-tag="footer">
                        <div class="step-header" slot="header">Visualization</div>
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
                                    </article>
                                </b-row>
                            </b-container>
                        </b-card-body>
                        <em slot="footer">
                            <b-button-group>
                                <b-button id="step2-back-btn" @click="step4BackClicked" variant="outline-success" size="sm">
                                    Back
                                </b-button>
                                <b-button id="step2-next-btn" @click="step4NextClicked" variant="success" size="sm">Next
                                </b-button>
                            </b-button-group>
                        </em>
                    </b-card>
                </div>
            </b-tab>
            <!-- Step 5 -->
            <!--<b-tab>
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
                                        <compare></compare>
                                    </nav>
                                    <article>
                                        <feedback></feedback>
                                    </article>
                                </b-row>
                            </b-container>
                        </b-card-body>
                        <em slot="footer">
                            <b-button-group>
                                <b-button id="step3-back-btn" @click="tabIndex&#45;&#45;" variant="outline-success" size="sm">
                                    Back
                                </b-button>
                                <b-button id="step3-next-btn" @click="tabIndex++" variant="success" size="sm">Next
                                </b-button>
                            </b-button-group>
                        </em>
                    </b-card>
                </div>
            </b-tab>-->
            <!-- Step 6 -->
            <b-tab>
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
                            <p class="card-text">
                                Print and Save
                            </p>
                            <b-button variant="info">Print Report</b-button>
                            <b-button variant="success">Save Report</b-button>
                        </b-card-body>
                        <em slot="footer">
                            <b-button-group>
                                <b-button id="step6-next-btn" @click="tabIndex--" variant="outline-success" size="sm">
                                    Back
                                </b-button>
                                <b-button id="step6-next-btn" @click="tabIndex++" variant="success" size="sm">Finish
                                </b-button>
                            </b-button-group>
                        </em>
                    </b-card>
                </div>
            </b-tab>
        </b-tabs>
        <b-modal v-model="showInfoModal" ok-only>
            <template slot="modal-title">
                No selections were made.
            </template>
            Please be advised that all available choices are being considered.
            <template slot="modal-footer" slot-scope="{ ok, cancel, hide }">
                <b-button size="sm" variant="success" @click="ok()">Ok</b-button>
            </template>
        </b-modal>
    </div>
</template>

<script>

    import Charts from '../charts/ChartContainer.vue'
    import Sidebar from '../sidebar/Sidebar.vue'
    import Feedback from '../feedback/Feedback.vue'
    import Compare from '../feedback/Compare.vue'
    import EventBus from './../../../event-bus';

    export default {

        name: 'wizard',
        components: {
            Compare,
            Feedback,
            Sidebar,
            Charts
        },

        data() {
            return {
                tabIndex: 0,
                itemInfoVisibility: false,

                show: true,
                showInfoModal: false,

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

                selectedActions: [],
                selectAllActions: false,

                selectedGoals: [],
                selectAllGoals: false,

                selectedActors: [],
                selectAllActors: false,

                goals: [
                    {
                        id: "0",
                        goal: 'Improve surface water quality',
                        readonly: false,
                        tooltip: true,
                        info: "Surface water quality is assessed for each stream, based on total nitrogen loading, temperature, and dissolved oxygen."
                    },
                    {
                        id: "1",
                        goal: 'Increase recharge to shallow aquifer',
                        readonly: false,
                        tooltip: true,
                        info: "Shallow aquifer recharge is assessed for each sub-basin, based on millimeters of water infiltrated."
                    },
                    //{id: "2", goal: 'Minimize land use change', readonly: true},
                    {
                        id: "2",
                        goal: 'Increase agriculture productivity',
                        readonly: false,
                        tooltip: true,
                        info: "Agriculture productivity is assessed for each sub-basin based on area planted, crop yields, and net income."
                    },
                    {id: "3", goal: 'Increase energy production', readonly: true, tooltip: false, info: ""},
                    {
                        id: "4",
                        goal: 'Improve ecological habitat',
                        readonly: false,
                        tooltip: true,
                        info: "Ecological habitat is assessed in each stream based on stream flow, temperature and dissolved oxygen."
                    },
                    {id: "5", goal: 'Other', readonly: true, tooltip: false, info: ""},

                ],

                actions: [
                    {
                        id: 0,
                        name: "act1",
                        action: 'No changes to current water right allocations',
                        readonly: false,
                        info: ""
                    },
                    //{id: 1, name: "act2", action: 'Increase water right volume by 20%', readonly: false},
                    //{id: 2, name: "act3", action: 'Decrease water right volume by 20%', readonly: false},
                    {
                        id: 1,
                        name: "act2",
                        action: 'Increase the volume of non-Columbia surface water',
                        readonly: false,
                        info: 'Increase the volume of non-Columbia surface water, while reducing the same total volume of ground water and/or Columbia  water.'
                    },
                    {
                        id: 2,
                        name: "act3",
                        action: 'Decrease the volume of non-Columbia surface water',
                        readonly: false,
                        info: 'Decrease the volume of non-Columbia surface water, while increasing the same total volume of ground water and/or Columbia water.'
                    },
                    //{id: 5, name: "act6", action: 'Increase amount of RW', readonly: true},
                    {
                        id: 3,
                        name: "act4",
                        action: 'Increase the volume of groundwater',
                        readonly: false,
                        info: "Increase the volume of ground water, while reducing the same total volume of non-Columbia surface water and/or Columbia  water."
                    },
                    {
                        id: 4,
                        name: "act5",
                        action: 'Decrease the volume of groundwater',
                        readonly: false,
                        info: "Decrease the volume of ground water, while increasing the same total volume of non-Columbia surface water and/or Columbia water."
                    },
                    //{id: 5, name: "act6", action: 'Invest in renewable energy sources', readonly: true, info:""},
                    {
                        id: 5,
                        name: "act7",
                        action: 'Increase the volume of Columbia surface water',
                        readonly: true,
                        info: "Increase the volume of Columbia surface water, while reducing the same total volume of ground water and/or non-Columbia water."
                    },
                    {
                        id: 6,
                        name: "act8",
                        action: 'Decrease the volume of Columbia surface water',
                        readonly: true,
                        info: "Decrease the volume of Columbia surface water, while increasing the same total volume of ground water and/or non-Columbia water."
                    },
                    //{id: 11, name: "act12", action: 'Invest in infra to pump RW', readonly: false}
                ],

                actors: [
                    {
                        id: 0,
                        name: "F_SW_GW",
                        actor: 'Farmer with Columbia river water rights',
                        readonly: false,
                        info: "Actors that currently produce agricultural products and have the right to use Columbia River water."
                    },
                    {
                        id: 1,
                        name: "F_SW",
                        actor: 'Farmer with other surface water rights',
                        readonly: false,
                        info: 'Actors that currently produce agricultural products and have the right to use surface water (excluding Columbia River).'
                    },
                    {
                        id: 2,
                        name: "F_GW",
                        actor: 'Farmer with groundwater rights',
                        readonly: false,
                        info: 'Actors that currently produce agricultural products and have the right to use ground water.'
                    }
                    //{id: 3, name: "EP", actor: 'Solar Power Plants', readonly: true},
                    //{id: 4, name: "DC", actor: 'Coal Power Plants', readonly: true},
                    //{id: 5, name: "TRI", actor: 'Data Centers', readonly: true},
                    //{id: 6, name: "MUN", actor: 'Dairies', readonly: true}
                ],
            }
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

            selectActions() {
                this.selectedActions = [];
                if (!this.selectAllActions) {
                    for (let action in this.actions) {
                        for (let actor in this.actors) {
                            if (this.actors[actor].readonly == false && this.actions[action].readonly == false) {
                                this.selectedActions.push(this.actors[actor].id + ',' + this.actions[action].id);
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
                }
                else {
                    this.tabIndex++
                    return true
                }

            },

            step2NextClicked() {
                if (this.selectedActors.length == 0) {
                    this.selectActors()
                    this.selectAllActors = true
                    this.showInfoModal = true
                    this.tabIndex++
                }
                else {
                    this.tabIndex++
                    return true
                }

            },

            step3NextClicked() {
                if (this.selectedActions.length == 0) {
                    this.selectActions()
                    this.selectAllActions = true
                    this.showInfoModal = true
                    this.tabIndex++
                }
                else {
                    this.tabIndex++
                    return true
                }

            },

            step4NextClicked() {
                EventBus.$emit('HIDE_ASIDE');
                this.tabIndex++
            },

            step4BackClicked() {
                EventBus.$emit('HIDE_ASIDE');
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
        left: 100px;
        top: 100px;
        min-width: 350px;
    }

    #step2 {
        position: absolute;
        z-index: 1000;
        left: 100px;
        top: 100px;
        min-width: 350px;
    }

    #step3 {
        position: absolute;
        z-index: 1000;
        left: 100px;
        top: 100px;
    }

    #step4 {
        display: flex;
        position: absolute;
        z-index: 1000;
        left: 100px;
        top: 60px;
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

    #step4 nav {
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


</style>
