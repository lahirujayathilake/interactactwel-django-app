<template>
    <div class="feedback-container">
        <div class="header-container">
            <h5>Evaluate Adaptation Plan</h5>
        </div>
        <div id="feedback-block" class="ui form">
            <b-form @submit="onSubmit" @reset="onReset">
                <b-form-group label="Do you think this Alternative plan is feasible?">
                    <b-form-radio v-model="checked" name="some-radios" value="A">Yes</b-form-radio>
                    <b-form-radio v-model="checked" name="some-radios" value="B">No</b-form-radio>
                    <b-form-radio v-model="checked" name="some-radios" value="C">May Be</b-form-radio>
                </b-form-group>
                <b-form-group id="input-group-4" label="Why is this plan not feasible? (Check all that apply)">
                    <b-form-checkbox v-model="selected" value="1">Unlikely to be profitable / financially sustainable</b-form-checkbox>
                    <b-form-checkbox v-model="selected" value="2">Infrastructure costs</b-form-checkbox>
                    <b-form-checkbox v-model="selected" value="3">Permits or other regulatory approval processes and cost
                    </b-form-checkbox>
                    <b-form-checkbox v-model="selected" value="4">Reliance on other stakeholders to take action</b-form-checkbox>
                    <b-form-checkbox v-model="selected" value="5">Long time period before seeing positive results</b-form-checkbox>
                    <b-form-checkbox v-model="selected" value="6">Public disapproval of the actions listed in the plans
                    </b-form-checkbox>
                    <b-form-checkbox v-model="selected" value="7">Other</b-form-checkbox>
                </b-form-group>
                <b-form-textarea
                        id="textarea"
                        v-model="comment"
                        placeholder="Provide your feedback"
                        rows="3"
                        max-rows="6"
                ></b-form-textarea>
                <b-button id="submit-btn" type="submit" variant="success">Submit</b-button>
            </b-form>
        </div>
    </div>
</template>

<script>

    export default {
        name: 'Feedback',

        data() {
            return {
            }
        },
        methods: {
            onSubmit(evt) {
                evt.preventDefault()
                alert(JSON.stringify(this.form))
            },
            onReset(evt) {
                evt.preventDefault()
                // Reset our form values
                this.form.comment = null
                this.form.checked = []
                this.form.selected = []
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

    }

    #feedback-block legend{
        font-weight: bold;
        font-size: 14px;
    }

    .header-container {
        padding: 0 10px;
    }

    #submit-btn{
        margin-top:10px;
    }

</style>