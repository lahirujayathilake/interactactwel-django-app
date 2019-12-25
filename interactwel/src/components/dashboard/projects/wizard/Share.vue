<template>
    <b-col lg="12">
        <ol class="progress-bar">
            <li class="col-md-2">
                <div id="active" class="step-progress-bar">
                    <div class="step-no">1</div>
                    <h4 class="list-group-item-heading">Goals</h4>
                    <h4r class="list-group-item-heading">&#10003;</h4r>
                    <p class="list-group-item-text"># golas selected</p>
                </div>
            </li>
            <li class="col-md-2">
                <div class="step-progress-bar">
                    <div class="step-no">2</div>
                    <h4 class="list-group-item-heading">Actors</h4>
                    <h4r class="list-group-item-heading">&#10003;</h4r>
                    <p class="list-group-item-text"># Actores selected</p>
                </div>
            </li>
            <li class="col-md-2">
                <div class="step-progress-bar">
                    <div class="step-no">2</div>
                    <h4 class="list-group-item-heading">Actions</h4>
                    <h4r class="list-group-item-heading">&#10003;</h4r>
                    <p class="list-group-item-text"># Actions selected</p>
                </div>
            </li>
            <li class="col-md-2">
                <div class="step-progress-bar">
                    <div class="step-no">2</div>
                    <h4 class="list-group-item-heading">Visualization</h4>
                    <h4r class="list-group-item-heading">&#10003;</h4r>
                    <p class="list-group-item-text">Adaptation Plans</p>
                </div>
            </li>
            <li class="col-md-2">
                <div class="step-progress-bar">
                    <div class="step-no">2</div>
                    <h4 class="list-group-item-heading">Feedback</h4>
                    <h4r class="list-group-item-heading">&#10003;</h4r>
                    <p class="list-group-item-text">Rate each plan</p>
                </div>
            </li>
            <li class="col-md-2">
                <div class="step-progress-bar active">
                    <div class="step-no">2</div>
                    <h4 class="list-group-item-heading">Share</h4>
                    <h4r class="list-group-item-heading">&#10003;</h4r>
                    <p class="list-group-item-text">Share with community</p>
                </div>
            </li>
        </ol>
        <div id="step5" title="Step 5">
        <b-card no-body footer-tag="footer">
            <div class="step-header" slot="header">Share</div>
            <b-card-body>
                <b-table class="card-text" bordered small hover :items="items" :fields="fields">
                    <template slot="rating" slot-scope="data">
                        <star-rating star-size="20"></star-rating>
                    </template>
                    <template v-slot:cell(download)="data">
                        <b-button pill size="sm"
                                  variant="primary">Print
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
                <b-button id="step6-next-btn" @click="submit" variant="next" size="sm">Finish</b-button>
                <b-button id="step6-next-btn" @click="back" variant="back" size="sm">Back</b-button>
            </em>
        </b-card>
        </div>
    </b-col>
</template>

<script>
    import GoalsOpts from './../../../../../public/static/goals.json';

    export default {
        name: 'Goals',
        props: {},
        data() {
            return {
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
            }
        },
        mounted() {

            if (localStorage.getItem('selectedGoals')) this.selectedGoals = JSON.parse(localStorage.getItem('selectedGoals'));

            /*let adaptationPlan = JSON.parse(localStorage.getItem("adaptationPlan"));
            if (adaptationPlan) {
                this.selectedGoals = adaptationPlan.selectedGoals;
                this.$route.params.projectId = adaptationPlan.projectId;

            } else {
                localStorage.setItem('adaptationPlan', JSON.stringify({'selectedGoals': this.selectedGoals}));
            }*/
        },

        watch: {

        },

        methods: {
            submit(){
                localStorage.setItem('step4', true);
                this.feedbackVisibility = false

            },
            back(){
                this.$router.push('/adaptation-plans/1/plans/overview')
            },
        }

    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
