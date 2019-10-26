<template>
    <div class="feedback-container">
        <span v-on:click="hideAside" class="close"><font-awesome-icon
                icon="times-circle"/></span>
        <div class="header-container">
            <h5>Evaluate Adaptation Plan {{feedbackOn}}</h5>
        </div>
        <div v-show="feedbackBlock" id="feedback-block">
            <b-form v-show="initialFeedback" @submit="onSubmit" @reset="onReset">
                <b-form-group label="Do you think the actions and timeframes presented in this plan are feasible?">
                    <b-form-radio v-model="feasibility" name="some-radios" value="1">Yes</b-form-radio>
                    <b-form-radio v-model="feasibility" name="some-radios" value="0">No</b-form-radio>
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
</template>

<script>

    import EventBus from './../../../event-bus';
    import StarRating from 'vue-star-rating'

    export default {
        name: 'Feedback',

        components: {
            StarRating
        },

        props: {
            feedbackOn: {
                type: String,
                default: ""
            }
        },


        data() {
            return {
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
            }
        },
        methods: {

            hideAside() {
                EventBus.$emit('HIDE_ASIDE');
            },

            submitFeedback() {
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
<style>

    .feedback-container {
        background-color: #ffffff;
        padding: 1rem;
        position: absolute;
        top: -52px;
        left: 124%;
        width: 400px;
    }

    #feedback-block {
        background-color: #f5f8fa;
        padding: 20px;
        border-radius: 10px;
        margin-top: 20px;
        font-size: 12px;
        width: 100%;
        height: 81vh;
        overflow: auto;
    }

    #thankyou-block {
        background-color: #f5f8fa;
        padding: 20px;
        border-radius: 10px;
        margin-top: 20px;
        font-size: 12px;
        width: 100%;
    }

    #feedback-block legend {
        font-weight: bold;
        font-size: 14px;
    }

    .header-container {
        padding: 0 10px;
    }

    #submit-btn {
        margin-top: 10px;
    }

</style>