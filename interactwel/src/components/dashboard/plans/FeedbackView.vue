<template>
    <b-card title="Feedback">
        <b-card-text>
            <div v-if="feedback == null">
                No feedback is provided for this plan yet.
            </div>
            <div v-if="feedback != null">
                <div>
                    Feedback Provided Date: {{feedback.date_modified }}
                </div>
                <hr>
                <div>
                    Question: Do you think the actions and timeframes presented in this plan are feasible?
                    <br>
                    Answer: {{feedback.feasibilty==1 ? 'Yes' : 'No' }}
                </div>
                <hr>
                <div v-for="feedbackItem in feedback.feedback_answers" :key="feedback.id">
                    Question: {{feedbackItem.question}}
                    <br>
                    Answer: {{feedbackItem.answer}}
                    <hr>
                </div>
            </div>
        </b-card-text>
    </b-card>
</template>

<script>
    export default {
        name: "FeedbackView",
        props: {
            projectId: String,
            planId: Number
        },

        data() {
            return {
                feedback: null,
            };
        },

        async mounted() {
            const {utils} = AiravataAPI; // eslint-disable-line
            let user = await this.getLoggedInUser();
            utils.FetchUtils.get("/interactwel/api/feedbacks/?plan_id="+ this.planId + "&user_id="+user.id).then(result => {

                if (result.length > 0) {
                    this.feedback = result[0]; //assuming that one user can have one feedback for one plan
                }

                }
            ).catch(error => {
                alert("Failed to fetch questions " + error);
            })

        }
    }
</script>

<style scoped>

</style>