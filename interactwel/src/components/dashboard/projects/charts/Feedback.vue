<template>
    <div id="graph" class="card">
        <div class="card-header">
            <strong>Evaluate Adaptation Plan {{$route.params.planId}}</strong>
        </div>
        <div class="card-body no-padding">
            <div v-show="feedbackVisibility" class="">
                <div v-show="feedbackBlock" id="feedback-block">
                    <b-form v-show="initialFeedback" @submit="onSubmit" @reset="onReset">
                        <b-form-group label="Do you think the actions and timeframes presented in this plan are feasible?">
                            <b-form-radio v-model="feasibility" value="1" name="some-radios">Yes</b-form-radio>
                            <b-form-radio v-model="feasibility" value="0" name="some-radios">No</b-form-radio>
                        </b-form-group>
                    </b-form>
                    <b-form v-if="feasibility === '0'">
                        <b-form-group label="Please state why this plan is infeasible">
                            <b-form-textarea
                                    id="textarea"
                                    v-model="ifNotFeasiblecomment"
                                    rows="3"
                                    max-rows="6"
                            ></b-form-textarea>
                        </b-form-group>
                    </b-form>
                    <b-form v-if="feasibility === '1'">

                        <b-form-group
                                label="How well does this plan (alternative plan 1, 2, etc.) meet the management goals you identified in Step 1?">
                            <b-form-radio-group
                                    id="radio-group-1"
                                    v-model="q1Selected"
                                    :options="options"
                                    name="q1"
                            ></b-form-radio-group>
                        </b-form-group>

                        <b-form-group
                                label="Do you think that the projected results/impacts from this plan will occur if the proposed actions are implemented?">
                            <b-form-radio-group
                                    id="radio-group-2"
                                    v-model="q2Selected"
                                    :options="options"
                                    name="q2"
                            ></b-form-radio-group>
                        </b-form-group>

                        <b-form-group label="What factors might prevent you from taking the recommended actions listed in this plan? (check all that apply)">
                            <b-form-checkbox-group
                                    id="checkbox-group-1"
                                    v-model="SelectedFactors"
                                    :options="factors"
                                    name="q3"
                            ></b-form-checkbox-group>
                        </b-form-group>

                        <b-form-group
                                label="What factors might prevent you from taking the recommended actions listed in this plan? (check all that apply)">
                            <b-form-radio-group
                                    id="radio-group-3"
                                    v-model="q3Selected"
                                    :options="options"
                                    name="q4"
                            ></b-form-radio-group>
                        </b-form-group>

                        <b-form-group
                                label="How likely are you to implement the actions recommended in this plan?">
                            <b-form-radio-group
                                    id="radio-group-4"
                                    v-model="q4Selected"
                                    :options="options"
                                    name="q5"
                            ></b-form-radio-group>
                        </b-form-group>

                        <b-form-group
                                label="How likely are you to work with other stakeholder groups to implement this plan?">
                            <b-form-radio-group
                                    id="radio-group-5"
                                    v-model="q5Selected"
                                    :options="options"
                                    name="q6"
                            ></b-form-radio-group>
                        </b-form-group>
                        <b-form-group label="Rate this plan">
                            <star-rating star-size="30  "></star-rating>
                        </b-form-group>

                        <b-form-group label="Please share any additional thoughts about the alternative plans or the plan builder tool">
                            <b-form-textarea
                                    id="textarea"
                                    v-model="ifNotFeasiblecomment"
                                    rows="3"
                                    max-rows="6"
                            ></b-form-textarea>
                        </b-form-group>

                    </b-form>
                    <b-button @click="submitFeedback">Submit</b-button>
                </div>
                <div id="thankyou-block" v-show="thankyouBlock">
                    Thank you
                </div>
            </div>
        </div>
    </div>
</template>
<script>

    export default {
        name: 'Feedback',
        props: {},
        data() {
            return {
                feedbackVisibility: true,
                feedbackBlock: true,
                thankyouBlock: false,
                feasibility: false,
                initialFeedback: true,
                ifFeasible: [],
                ifNotFeasible: [],
                ifFeasiblecomment: null,
                ifNotFeasiblecomment: null,

                options: [
                    {text: 'Not at all', value: 1},
                    {text: 'Satisfactory', value: 2},
                    {text: 'Neutral', value: 3},
                    {text: 'Well', value: 4},
                    {text: 'Very Well', value: 5},
                ],

                factors: [
                    {text: 'Infrastructure costs', value: 'Infrastructure costs'},
                    {text: 'Permits or other regulatory approval processes and cost', value: 'Permits or other regulatory approval processes and cost'},
                    {text: 'Reliance on other stakeholders to take action', value: 'Reliance on other stakeholders to take action'},
                    {text: 'Long time period before seeing positive results', value: 'Long time period before seeing positive results'},
                    {text: 'Public disapproval of the actions listed in the plan', value: 'Public disapproval of the actions listed in the plan'},
                ],

                feedbackProvided: false,
                currentRouteName: '',

                q1Selected: [],
                q2Selected: [],
                q3Selected: [],
                q4Selected: [],
                q5Selected: [],
                SelectedFactors: [],

                questions: [],
            }
        },
        mounted() {
            if(!localStorage.feedbackProvided){
                localStorage.setItem('feedbackProvided', false);
            }else{
                let $this = this
                $this.feedbackProvided = localStorage.feedbackProvided;
            }

        },
        watch: {},
        methods: {
            submit(){
                localStorage.setItem('step4', true);
                this.feedbackVisibility = false

            },
            back(){
                this.$router.push('/adaptation-plans/1/actions')
            },
            submitFeedback() {
                let adaptationPlan = JSON.parse(localStorage.getItem("adaptationPlan"));
                adaptationPlan.planId = this.$route.params.planId;
                localStorage.setItem('adaptationPlan', JSON.stringify(adaptationPlan));

                localStorage.feedbackProvided = true
                this.feedbackProvided = true
                this.thankyouBlock = true
                this.feedbackBlock = false
            },
            onSubmit(evt) {
                evt.preventDefault()
                alert(JSON.stringify(this))
            },
            onReset(evt) {
                evt.preventDefault()
                // Reset our form values
                this.comment = null
                this.feasibility = []
                this.selected = []
                // Trick to reset/clear native browser form validation state
                this.show = false
                this.$nextTick(() => {
                    this.show = true
                })
            }
        }
    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
