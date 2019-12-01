<template>
    <div id="graph" class="card">
        <div class="card-header">
            <strong>Feedback</strong>
        </div>
        <div class="card-body no-padding">
            <div class="feedback-container">
                <div class="header-container">
                    <h5>Evaluate Adaptation Plan {{$route.params.planId}}</h5>
                </div>
                <div id="feedback-block">
                    <b-form @submit="onSubmit" @reset="onReset">
                        <b-form-group label="Do you think the actions and timeframes presented in this plan are feasible?">
                            <b-form-radio v-model="feasibility" name="some-radios" value="1">Yes</b-form-radio>
                            <b-form-radio v-model="feasibility" name="some-radios" value="0">No</b-form-radio>
                        </b-form-group>
                    </b-form>
                    <b-form>
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
            return {}
        },
        mounted() {

        },
        watch: {},
        methods: {}
    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
