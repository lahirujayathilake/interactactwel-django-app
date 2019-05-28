<template>
    <div>
        <form-wizard v-show="!stepWizardVisibility" @on-complete="onComplete"
                     shape="tab"
                     color="#28a645">
            <tab-content title="Step 1"
                         icon="ti-user" :before-change="beforeTabSwitchStep1">
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
                            <p align="justify"> In <b>Step 1</b>, think about what goals would be of interest to you and your stakeholders. Then choose from the options available in this list by clicking on the goals that reflect your priorities and interests.</p>
                            <p aling="justify"> You will be able to visualize how each adaptation plan meets the goals in <strong>Step 4</strong>. </p>
                            

                        </b-card-text>
                    </b-card>
                </div>
                <b-card no-body>
                    <div class="step-header" slot="header">Choose Goals</div>
                    <b-card-body>
                        <p class="card-text">
                            Choose adaptation goals that are important to you
                        </p>
                    </b-card-body>
                    <b-list-group-item>
                        <b-form-checkbox-group>
                            <label class="form-checkbox">
                                <input type="checkbox" v-model="selectAllGoals" @click="selectGoals">
                                Select All
                            </label>
                            <!--<div class="text-uppercase text-bold">id selected: {{selectedGoals}}</div>-->
                        </b-form-checkbox-group>
                    </b-list-group-item>
                    <b-list-group flush>
                        <b-form>
                            <div class="list-group">
                                <li class="list-group-item" v-for="goal in goals" v-bind:key="goal.id">
                                    <label class="form-checkbox" :disabled="goal.readonly">
                                        <input type="checkbox" :value="goal.id" v-model="selectedGoals" :disabled="goal.readonly"/>
                                        {{goal.goal}}
                                    </label>
                                    <b-badge class="info-button" pill variant="secondary" v-b-tooltip.hover :title="goal.info">i</b-badge>
                                </li>
                            </div>
                        </b-form>
                    </b-list-group>
                </b-card>
            </tab-content>
            <tab-content title="Step 2"
                         icon="ti-settings" :before-change="beforeTabSwitchStep2">
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
                <b-card no-body>
                    <div class="step-header" slot="header">Choose Actors</div>
                    <b-card-body>
                        <p class="card-text">
                            Choose the actors whose adaptation actions you want to visualize
                        </p>
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
                                        <input type="checkbox" :value="actor.id" v-model="selectedActors"
                                               :disabled="actor.readonly">
                                        {{actor.actor}}
                                    </label>
                                    <b-badge class="info-button" pill variant="secondary" v-b-tooltip.hover :title="actor.info">i</b-badge>
                                </li>
                            </div>
                        </b-form>
                    </b-list-group>
                </b-card>
            </tab-content>
            <tab-content title="Step 3"
                         icon="ti-check" :before-change="beforeTabSwitchStep3">
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
                <b-card style="height: 470px; width: 580px" no-body>
                    <div class="step-header" slot="header">Choose Actions</div>
                    <b-card-body>
                        <p class="card-text">
                            Choose the actors whose adaptation actions you want to visualize
                        </p>
                    </b-card-body>
                    <b-list-group-item>
                        <b-form-checkbox-group>
                            <label class="form-checkbox">
                                <input type="checkbox" v-model="selectAllActions" @click="selectActions">
                                Select All
                            </label>
                        </b-form-checkbox-group>
                    </b-list-group-item>
                    <b-card-body>

                        <!--<div class="text-uppercase text-bold">id selected: {{selectedActions}}</div>-->
                        <table style="height:270px; width: 550px"
                               class="table table-bordered table-striped table-hover table-responsive">
                            <thead>
                            <tr>
                                <th></th>
                                <th v-for="actor in actors" v-bind:key="actor.id">
                                    {{actor.actor}}
                                </th>
                            </tr>
                            </thead>
                            <tbody>

                            <tr v-for="action in actions" v-bind:key="action.id">
                                <td>
                                    {{action.action}}
                                    <b-badge class="info-button" pill variant="secondary" v-b-tooltip.hover :title="action.info">i</b-badge>
                                </td>
                                
                                <td v-for="actor in actors" v-bind:key="actor.id">
                                    <label class="form-checkbox">
                                        <input type="checkbox" :value="actor.id + ',' + action.id"
                                               v-model="selectedActions" :disabled="action.readonly || actor.readonly">
                                        <i class="form-icon"></i>
                                    </label>
                                </td>

                            </tr>

                            </tbody>
                        </table>

                    </b-card-body>
                </b-card>
            </tab-content>
        </form-wizard>
    </div>


</template>

<script>

    //import {FormWizard, TabContent} from 'vue-form-wizard'

    import FormWizard from './../formWizard/FormWizard.vue'
    import TabContent from './../formWizard/TabContent.vue'
    import EventBus from './../../event-bus';

    export default {

        components: {
            'tab-content': TabContent,
            'form-wizard': FormWizard,

        },


        name: 'Step1Content',

        data: () => ({

            fromparent: "",

            stepWizardVisibility: false,

            selectedActions: [],
            selectAllActions: false,

            selectedGoals: [],
            selectAllGoals: false,

            selectedActors: [],
            selectAllActors: false,

            goals: [
                {id: "0", goal: 'Improve surface water quality', readonly: false, tooltip: true, info: "Surface water quality is assessed for each stream, based on total nitrogen loading, temperature, and dissolved oxygen."},
                {id: "1", goal: 'Increase recharge to shallow aquifer', readonly: false, tooltip: true, info: "Shallow aquifer recharge is assessed for each sub-basin, based on millimeters of water infiltrated."},
                //{id: "2", goal: 'Minimize land use change', readonly: true},
                {id: "2", goal: 'Increase agriculture productivity', readonly: false, tooltip: true, info: "Agriculture productivity is assessed for each sub-basin based on area planted, crop yields, and net income."},
                {id: "3", goal: 'Increase energy production', readonly: true, tooltip: false, info:""},
                {id: "4", goal: 'Improve ecological habitat', readonly: false, tooltip: true, info:"Ecological habitat is assessed in each stream based on stream flow, temperature and dissolved oxygen."},
                {id: "5", goal: 'Other', readonly: true, tooltip: false, info:""},

            ],

            actions: [
                {id: 0, name: "act1", action: 'No changes to current water right allocations', readonly: false, info:""},
                //{id: 1, name: "act2", action: 'Increase water right volume by 20%', readonly: false},
                //{id: 2, name: "act3", action: 'Decrease water right volume by 20%', readonly: false},
                {id: 1, name: "act2", action: 'Increase the volume of non-Columbia surface water', readonly: false, info:'Increase the volume of non-Columbia surface water, while reducing the same total volume of ground water and/or Columbia  water.'},
                {id: 2, name: "act3", action: 'Decrease the volume of non-Columbia surface water', readonly: false, info: 'Decrease the volume of non-Columbia surface water, while increasing the same total volume of ground water and/or Columbia water.'},
                //{id: 5, name: "act6", action: 'Increase amount of RW', readonly: true},
                {id: 3, name: "act4", action: 'Increase the volume of groundwater', readonly: false, info:"Increase the volume of ground water, while reducing the same total volume of non-Columbia surface water and/or Columbia  water."},
                {id: 4, name: "act5", action: 'Decrease the volume of groundwater', readonly: false, info:"Decrease the volume of ground water, while increasing the same total volume of non-Columbia surface water and/or Columbia water."},
                //{id: 5, name: "act6", action: 'Invest in renewable energy sources', readonly: true, info:""},
                {id: 5, name: "act7", action: 'Increase the volume of Columbia surface water', readonly: true, info:"Increase the volume of Columbia surface water, while reducing the same total volume of ground water and/or non-Columbia water."},
                {id: 6, name: "act8", action: 'Decrease the volume of Columbia surface water', readonly: true, info: "Decrease the volume of Columbia surface water, while increasing the same total volume of ground water and/or non-Columbia water."},
                //{id: 11, name: "act12", action: 'Invest in infra to pump RW', readonly: false}
            ],

            actors: [
                {id: 0, name: "F_SW_GW", actor: 'Farmer with Columbia river water rights', readonly: false, info: "Actors that currently produce agricultural products and have the right to use Columbia River water."},
                {id: 1, name: "F_SW", actor: 'Farmer with other surface water rights', readonly: false, info: 'Actors that currently produce agricultural products and have the right to use surface water (excluding Columbia River).'},
                {id: 2, name: "F_GW", actor: 'Farmer with groundwater rights', readonly: false, info:'Actors that currently produce agricultural products and have the right to use ground water.'}
                //{id: 3, name: "EP", actor: 'Solar Power Plants', readonly: true},
                //{id: 4, name: "DC", actor: 'Coal Power Plants', readonly: true},
                //{id: 5, name: "TRI", actor: 'Data Centers', readonly: true},
                //{id: 6, name: "MUN", actor: 'Dairies', readonly: true}
            ],
        }),

        methods: {
            selectGoals() {
                this.selectedGoals = [];
                if (!this.selectAllGoals) {
                    for (let goal in this.goals) {
                        if (this.goals[goal].readonly == false) {
                            this.selectedGoals.push(this.goals[goal].id);
                        }
                    }
                }
            },

            selectActors() {
                this.selectedActors = [];
                if (!this.selectAllActors) {
                    for (let actor in this.actors) {
                        if (this.actors[actor].readonly == false) {
                            this.selectedActors.push(this.actors[actor].id);
                        }
                    }
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

            onComplete: function () {
                this.stepWizardVisibility = true,
                    this.$emit('finish-wizard');

            },

            beforeTabSwitchStep1: function (selectedGoalsCount) {
                selectedGoalsCount = this.selectedGoals.length;
                EventBus.$emit('MOVE_TO_STEP2', selectedGoalsCount);
                return true
            },

            beforeTabSwitchStep2: function (selectedActorsCount) {
                selectedActorsCount = this.selectedActors.length;
                EventBus.$emit('MOVE_TO_STEP3', selectedActorsCount);
                return true
            },

            beforeTabSwitchStep3: function (selectedActionsCount) {
                selectedActionsCount = this.selectedActions.length;
                EventBus.$emit('MOVE_TO_STEP4', selectedActionsCount);
                return true
            },
        }

    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

    @import '../../static/css/vue-form-wizard.min.css';

    .vue-form-wizard {
        max-height: 700px;
        overflow: visible;
        background-color: #ECEFF1;
        position: absolute;
        left: 90px;
        z-index: 1000;
        max-width: 800px;
        top: 20px;
        border-radius: 10px;
        height: auto;
        width: auto;
    }

    td, th {
        font-size: 12px;
        text-align: left;
        padding: .5rem;
    }

    th {
        width: auto;
    }

    .vue-form-wizard .wizard-header {
        display: none;
    }

    b-list-group-item {
        paddding: 0 !important;
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


</style>
