<template>
    <div>
        <form-wizard @on-complete="onComplete"
                     shape="tab"
                     color="#28a645"
        title="Data Visualization Wizard"
        subtitle="Umatilla Region Adapts to New Water Allocation">
            <tab-content title="Step 1"
                         icon="ti-user" :before-change="beforeTabSwitch">
                <b-card no-body>
                    <h4 slot="header">Choose Goals</h4>
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
                            <div class="text-uppercase text-bold">id selected: {{selectedGoals}}</div>
                        </b-form-checkbox-group>
                    </b-list-group-item>
                    <b-list-group flush>
                        <b-list-group-item>
                            <b-form>
                                <div v-for="goal in goals">
                                    <label class="form-checkbox">
                                        <input type="checkbox" :value="goal.id" v-model="selectedGoals">
                                        {{goal.goal}}
                                    </label>
                                    <b-badge pill variant="secondary">Info</b-badge>
                                </div>
                            </b-form>
                        </b-list-group-item>
                    </b-list-group>
                </b-card>
            </tab-content>
            <tab-content title="Step 2"
                         icon="ti-settings">
                <b-card no-body>
                    <h4 slot="header">Choose Actors</h4>
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
                            <div class="text-uppercase text-bold">id selected: {{selectedActors}}</div>
                        </b-form-checkbox-group>
                    </b-list-group-item>
                    <b-list-group flush>
                        <b-list-group-item>
                            <b-form>
                                <div v-for="actor in actors">
                                    <label class="form-checkbox">
                                        <input type="checkbox" :value="actor.id" v-model="selectedActors">
                                        {{actor.actor}}
                                    </label>
                                    <b-badge pill variant="secondary">Info</b-badge>
                                </div>
                            </b-form>
                        </b-list-group-item>
                    </b-list-group>
                </b-card>
            </tab-content>
            <tab-content title="Step 3"
                         icon="ti-check">
                <b-card no-body>
                    <h4 slot="header">Choose Actions</h4>
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

                        <div class="text-uppercase text-bold">id selected: {{selectedActions}}</div>
                        <table class="table table-striped table-hover table-responsive">
                            <thead>
                            <tr>
                                <th>Action</th>
                                <th v-for="actor in actors">
                                    {{actor.name}}
                                </th>
                            </tr>
                            </thead>
                            <tbody>

                            <tr v-for="action in actions">
                                <td>
                                    {{action.action}}
                                </td>
                                <td v-for="actor in actors">
                                    <label class="form-checkbox">
                                        <input type="checkbox" :value="actor.id + ',' + action.id" v-model="selectedActions">
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

    import {FormWizard, TabContent} from 'vue-form-wizard'

    export default {

        components: {
            'form-wizard': FormWizard,
            'tab-content': TabContent
        },


        name: 'Step1Content',

        data: () => ({

            selectedActions: [],
            selectAllActions: false,

            selectedGoals: [],
            selectAllGoals: false,

            selectedActors: [],
            selectAllActors: false,

            goals: [
                { id: "0", goal: 'Improve surface water quality'},
                { id: "1", goal: 'Increase ground water supply'},
                { id: "2", goal: 'Minimize land use change'},
                { id: "3", goal: 'Improve economy'},
                { id: "4", goal: 'Increase energy production'},
                { id: "5", goal: 'Improve ecological habitat'},
                { id: "6", goal: 'Other'},

            ],

            actions: [
                { id: 0, name: "act1", action: 'Business as usual' },
                { id: 1, name: "act2", action: 'Increase capacity by 20%' },
                { id: 2, name: "act3", action: 'Decrease total capacity by 20%' },
                { id: 3, name: "act4", action: 'Increase amount of SW' },
                { id: 4, name: "act5", action: 'Increase amount of GW' },
                { id: 5, name: "act6", action: 'Increase amount of RW' },
                { id: 6, name: "act7", action: 'Decrease amount of SW' },
                { id: 7, name: "act8", action: 'Decrease amount of GW' },
                { id: 8, name: "act9", action: 'Invest in renewable energy sources' },
                { id: 9, name: "act10", action: 'Pump RW to farmers/daries' },
                { id: 10, name: "act11", action: 'Increase surface storage' },
                { id: 11, name: "act12", action: 'Invest in infra to pump RW' }
            ],

            actors: [
                { id: 0, name: "F_SW_GW", actor: 'Farmer with surface water and ground water right' },
                { id: 1, name: "F_SW", actor: 'Farmer with surface water right (F_SW)' },
                { id: 2, name: "F_GW", actor: 'Farmer with ground water right (F_GW)' },
                { id: 3, name: "EP", actor: 'Solar_Power_Plants' },
                { id: 4, name: "DC", actor: 'Coal_Power_Plants' },
                { id: 5, name: "TRI", actor: 'Data_Centers' },
                { id: 6, name: "MUN", actor: 'Dairies' }
            ],
        }),

        methods: {
            selectGoals() {
                this.selectedGoals = [];
                if (!this.selectAllGoals) {
                    for (let goal in this.goals) {
                        this.selectedGoals.push(this.goals[goal].id);
                    }
                }
            },

            selectActors() {
                this.selectedActors = [];
                if (!this.selectAllActors) {
                    for (let actor in this.actors) {
                        this.selectedActors.push(this.actors[actor].id);
                    }
                }
            },

            selectActions() {
                this.selectedActions = [];
                if (!this.selectAllActions) {
                    for (let action in this.actions) {
                        for (let actor in this.actors) {
                            this.selectedActions.push(this.actors[actor].id + ',' + this.actions[action].id);
                        }
                    }
                }
            },

            onComplete: function(){
                alert('Yay. Done!');
            },
            beforeTabSwitch: function(){
                alert("This is called before switchind tabs")
                return true;
            }
        }

    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

    @import '../../static/css/vue-form-wizard.min.css';

    .vue-form-wizard{
        width: 50%;
        max-width: 600px;
        background-color: #ECEFF1;
    }

</style>
