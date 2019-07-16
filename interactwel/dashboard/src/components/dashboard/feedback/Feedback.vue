<template>
    <div class="feedback-container">
        <div class="header-container">
            <h5>Evaluate Adaptation Plan</h5>
        </div>
        <div id="feedback-block" class="ui form">
            <b-form v-show="feedbackStep1" @submit="onSubmit" @reset="onReset">
                <b-form-group label="Do you think this Adaptation Plan is feasible?">
                    <b-form-radio v-model="feasibility" name="some-radios" value="Yes">Yes</b-form-radio>
                    <b-form-radio v-model="feasibility" name="some-radios" value="No">No</b-form-radio>
                </b-form-group>
            </b-form>
            <b-button id="submit-btn" type="submit" variant="success" disabled="readonly">Submit</b-button>
            <b-form v-show="feedbackStep2">
                <b-form-group id="input-group-4" label="Why is this plan NOT feasible? (Check all that apply)">
                    <b-form-checkbox v-model="selected" value="1">Unlikely to be profitable or financially sustainable
                    </b-form-checkbox>
                    <b-form-checkbox v-model="selected" value="2">Infrastructure costs</b-form-checkbox>
                    <b-form-checkbox v-model="selected" value="3">
                        Challenging permit or other regulatory approval processes
                    </b-form-checkbox>
                    <b-form-checkbox v-model="selected" value="4">Reliance on other actors to make this plan work
                    </b-form-checkbox>
                    <b-form-checkbox v-model="selected" value="5">Positive impacts take a long time to accrue
                    </b-form-checkbox>
                    <b-form-checkbox v-model="selected" value="6">Potential public disapproval of actions listed in the plan
                    </b-form-checkbox>
                    <b-form-checkbox v-model="selected" value="7">Other</b-form-checkbox>
                </b-form-group>
                <b-form-textarea
                        id="textarea"
                        v-model="comment"
                        placeholder="Please provide feedback (positive or negative)"
                        rows="3"
                        max-rows="6"
                ></b-form-textarea>
            </b-form>
        </div>
    </div>
</template>

<script>

    export default {
        name: 'Feedback',

        data() {
            return {
                feedbackStep1: true,
                feedbackStep2: false,
                feasibility: [],
                selected: [],
                comment: null
            }
        },
        methods: {
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

    #feedback-block {
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