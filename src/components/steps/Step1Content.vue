<template>
    <div>
        <!--<component :fromparent="fromparent" v-bind:is="component='progress-bar'"></component>-->
        <form-wizard v-show="!stepWizardVisibility" v-on:next-step="nextStep" @on-complete="onComplete"
                     shape="tab"
                     color="#28a645">
            <tab-content title="Step 1"
                         icon="ti-user" :before-change="beforeTabSwitchStep1">
                <div class="help-block">
                    <b-card
                            title=""
                            tag="article"
                            style="max-width: 25rem;"
                            class="mb-2"
                    >
                        <b-card title><strong>What are Goals?</strong></b-card title>
                        <b-card-text>
                            <p align="justify">A community can suffer severe consequences from not effectively managing its water, energy, and land resources, especially when slow and sudden changes in the environment (e.g., changing climate, new policies, etc.) impair the quality, quantity, and accessibility of these resources over time.</p> 

                            <p align="justify"> Before choosing an appropriate plan of response (called <b>Adaptation Plan</b>), community members must choose what types of goals are important for them to achieve. 
                            <ul><li>These goals, also called <b>Adaptation Goals</b>, allow different groups within the community to evaluate how an adaptation plan may impact the bottom-line of each group, as well as that of the community in whole.</li> 
                            <li>Further, many of these goals may be short-term goals, while others may need to be accomplished over a longer period of time.</li></ul></p>

                            <p align="justify"> In <b>Step 1</b>, think about what goals would be of interest to you and your stakeholders. Then choose from the options available in this list by clicking on the goals that reflect your priorities and interests. </p>

                        </b-card-text>
                        <!-- <br/> -->
                        <!-- <br/> -->
                        <!-- <b-card-text>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed tempus urna id turpis faucibus fermentum.</b-card-text> -->
                    </b-card>
                </div>
                <b-card no-body>
                    <div class="step-header" slot="header">Choose Goals</div>
                    <b-card-body>
                        <p class="card-text">
                            Choose the adaptation goals that are important to you
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
                                        <input type="checkbox" :value="goal.id" v-model="selectedGoals" :disabled="goal.readonly"></input>
                                        {{goal.goal}}
                                    </label>
                                    <b-badge class="info-button" pill variant="secondary">i</b-badge>
                                </li>
                            </div>
                        </b-form>
                    </b-list-group>
                </b-card>
            </tab-content>
            <tab-content title="Step 2"
                         icon="ti-settings" :before-change="beforeTabSwitchStep2">
                <div class="help-block">
                    <b-card
                            title=""
                            tag="article"
                            style="max-width: 20rem;"
                            class="mb-2"
                    >
                        <b-card-text><strong>Who are Actors?</strong></b-card-text><br/>
                        <b-card-text class="small">
                            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed tempus urna id turpis faucibus fermentum.
                            Proin feugiat semper nunc eget porta. Etiam felis velit, congue sed eros eu, hendrerit tempus urna.
                        </b-card-text>
                        <br/>
                        <br/>
                        <b-card-text>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed tempus urna id turpis faucibus fermentum.</b-card-text>
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
                                        <input type="checkbox" :value="actor.id" v-model="selectedActors" :disabled="actor.readonly">
                                        {{actor.actor}}
                                    </label>
                                    <b-badge class="info-button" pill variant="secondary">i</b-badge>
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
                            title=""
                            tag="article"
                            style="max-width: 20rem;"
                            class="mb-2"
                    >
                        <b-card-text><strong>Why select Actions?</strong></b-card-text><br/>
                        <b-card-text class="small">
                            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed tempus urna id turpis faucibus fermentum.
                            Proin feugiat semper nunc eget porta. Etiam felis velit, congue sed eros eu, hendrerit tempus urna.
                        </b-card-text>
                        <br/>
                        <br/>
                        <b-card-text>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed tempus urna id turpis faucibus fermentum.</b-card-text>
                    </b-card>
                </div>
                <b-card style="height: 570px; width: 610px" no-body>
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
                        <table style="height: 370px; width: 580px" class="table table-bordered table-striped table-hover table-responsive">
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
                                </td>
                                <td v-for="actor in actors" v-bind:key="actor.id">
                                    <label class="form-checkbox">
                                        <input type="checkbox" :value="actor.id + ',' + action.id" v-model="selectedActions" :disabled="action.readonly || actor.readonly">
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
                {id: "0", goal: 'Improve surface water quality', readonly: false},
                {id: "1", goal: 'Increase ground water supply', readonly: false},
                {id: "2", goal: 'Minimize land use change', readonly: true},
                {id: "3", goal: 'Improve regional economy', readonly: false},
                {id: "4", goal: 'Increase energy production', readonly: true},
                {id: "5", goal: 'Improve ecological habitat', readonly: false},
                {id: "6", goal: 'Other', readonly: true},

            ],

            actions: [
                {id: 0, name: "act1", action: 'Business as usual', readonly: false},
                //{id: 1, name: "act2", action: 'Increase water right volume by 20%', readonly: false},
                //{id: 2, name: "act3", action: 'Decrease water right volume by 20%', readonly: false},
                {id: 1, name: "act2", action: 'Increase volume of SW water rights', readonly: false},
                {id: 2, name: "act3", action: 'Increase volume of GW water rights', readonly: false},
                //{id: 5, name: "act6", action: 'Increase amount of RW', readonly: true},
                {id: 3, name: "act4", action: 'Decrease volume of SW water rights', readonly: false},
                {id: 4, name: "act5", action: 'Decrease volume of GW water rights', readonly: false},
                {id: 5, name: "act6", action: 'Invest in renewable energy sources', readonly: true},
                {id: 6, name: "act7", action: 'Pump RW to farmers/daries', readonly: true},
                {id: 7, name: "act8", action: 'Increase surface storage', readonly: true},
                //{id: 11, name: "act12", action: 'Invest in infra to pump RW', readonly: false}
            ],

            actors: [
                {id: 0, name: "F_SW_GW", actor: 'Farmer with surface water and ground water rights', readonly: false},
                {id: 1, name: "F_SW", actor: 'Farmer with surface water rights', readonly: false},
                {id: 2, name: "F_GW", actor: 'Farmer with ground water rights', readonly: false},
                {id: 3, name: "EP", actor: 'Solar Power Plants', readonly: true},
                {id: 4, name: "DC", actor: 'Coal Power Plants', readonly: true},
                {id: 5, name: "TRI", actor: 'Data Centers', readonly: true},
                { id: 6, name: "MUN", actor: 'Dairies' , readonly: true}
            ],
        }),

        methods: {
            selectGoals() {
                this.selectedGoals = [];
                if (!this.selectAllGoals) {
                    for (let goal in this.goals) {
                        if (this.goals[goal].readonly == false){
                        this.selectedGoals.push(this.goals[goal].id, this.goals[goal].readonly);
                        }
                    }
                }
            },

            selectActors() {
                this.selectedActors = [];
                if (!this.selectAllActors) {
                    for (let actor in this.actors) {
                        if (this.actors[actor].readonly == false){
                        this.selectedActors.push(this.actors[actor].id, this.actors[actor].readonly);
                        }
                    }
                }
            },

            selectActions() {
                this.selectedActions = [];
                if (!this.selectAllActions) {
                    for (let action in this.actions) {
                        for (let actor in this.actors) {
                            if (this.actors[actor].readonly == false && this.actions[action].readonly == false){
                            this.selectedActions.push(this.actors[actor].id + ',' + this.actions[action].id);
                            }
                        }
                    }
                }
            },

            onComplete: function () {
                //alert('Yay. Done!'),
                this.stepWizardVisibility = true,
                    this.$emit('finish-wizard');
                //EventBus.$emit('MOVE_TO_STEP4');

            },

            beforeTabSwitchStep1: function () {
                EventBus.$emit('MOVE_TO_STEP2');
                //alert("This is called before switchind tabs")
                return true
            },

            beforeTabSwitchStep2: function () {
                EventBus.$emit('MOVE_TO_STEP3');
                //alert("This is called before switchind tabs")
                return true
            },

            beforeTabSwitchStep3: function () {
                EventBus.$emit('MOVE_TO_STEP4');
                //alert("This is called before switchind tabs")
                return true
            },

            beforeTabSwitch: function () {
                //EventBus.$emit('CLICK_NEXT_STEP');
                //alert("This is called before switchind tabs")
                return true
            },

            nextStep() {
                //alert("next tab clicked")
                //this.$emit('next-click')
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
        left: 60px;
        z-index: 1000;
        max-width: 800px;
        top: 20px;
        border-radius: 10px;
        height: auto;
        width: auto;
    }

    td, th {
        font-size: 12px;
        padding: .5rem;
    }

    .vue-form-wizard .wizard-header {
        display: none;
    }

    b-list-group-item {
        paddding: 0 !important;
    }

    .info-button{
        float: right !important;
    }

    .help-block{
        position: absolute;
        border: none;
        right: -440px;
        z-index: 1000;
    }
    
    .help-block-actions{
        position: absolute;
        right: -450px;
        z-index: 1000;
    }

    .step-header{
        font-size: 16px;
        font-weight: bold;
    }

    .card-text{
        font-size:12px;
    }


</style>