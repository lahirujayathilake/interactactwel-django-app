<template>
    <div class="feedback-container">
        <span v-on:click="hideAside" class="close"><font-awesome-icon
                icon="times-circle"/></span>
        <div class="header-container">
            <h5>Evaluate Adaptation Plan</h5>
        </div>
        <div v-show="feedbackBlock" id="feedback-block">
            <b-form v-show="initialFeedback" @submit="onSubmit" @reset="onReset">
                <b-form-group label="Do you think this Adaptation Plan is feasible?">
                    <b-form-radio v-model="feasibility" name="some-radios" value="1">Yes</b-form-radio>
                    <b-form-radio v-model="feasibility" name="some-radios" value="0">No</b-form-radio>
                </b-form-group>
            </b-form>
            <b-form v-if="feasibility === '0'">
                <b-form-group label="Why is this plan NOT feasible? (Check all that apply)">
                    <b-form-checkbox v-for="question in ifFeasibleQuestions" v-model="ifFeasible" :value="question.id">
                        {{question.question}}
                    </b-form-checkbox>
                </b-form-group>
                <b-form-textarea
                        id="textarea"
                        v-model="ifFeasiblecomment"
                        placeholder="Please provide feedback (positive or negative)"
                        rows="3"
                        max-rows="6"
                ></b-form-textarea>
            </b-form>
            <b-form v-if="feasibility === '1'">
                <b-form-group id="input-group-4" label="Oh great!. We would love to hear your feedback.">
                    <b-form-checkbox v-for="question in ifNotFeasibleQuestions" v-model="ifNotFeasible"
                                     :value="question.id">{{question.question}}
                    </b-form-checkbox>
                </b-form-group>
                <b-form-textarea
                        id="textarea"
                        v-model="ifNotFeasiblecomment"
                        placeholder="Please provide feedback (positive or negative)"
                        rows="3"
                        max-rows="6"
                ></b-form-textarea>
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

    export default {
        name: 'Feedback',

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

                ifFeasibleQuestions: [
                    {id: 0, question: "Unlikely to be profitable or financially sustainable"},
                    {id: 1, question: "Infrastructure costs"},
                    {id: 2, question: "Challenging permit or other regulatory approval processes"},
                    {id: 3, question: "Reliance on other actors to make this plan work"},
                    {id: 4, question: "Positive impacts take a long time to accrue"},
                    {id: 4, question: "Potential public disapproval of actions listed in the plan"},
                    {id: 4, question: "Other"},
                ],

                ifNotFeasibleQuestions: [
                    {id: 0, question: "blah blah blah"},
                    {id: 1, question: "Infrastructure costs"},
                    {id: 2, question: "Challenging permit or other regulatory approval processes"},
                    {id: 3, question: "Reliance on other actors to make this plan work"},
                    {id: 4, question: "Positive impacts take a long time to accrue"},
                    {id: 4, question: "Potential public disapproval of actions listed in the plan"},
                    {id: 4, question: "Other"},
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
        padding: 1rem;
    }

    #feedback-block {
        background-color: #f5f8fa;
        padding: 20px;
        border-radius: 10px;
        margin-top: 20px;
        font-size: 12px;
        width: 100%;
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