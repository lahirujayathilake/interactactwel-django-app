<template>
    <div id="graph" class="card">
        <div class="card-header">
            <strong>Evaluate Adaptation Plan {{$route.params.planId}}</strong>
        </div>
        <div class="card-body no-padding">
            <div v-show="feedbackVisibility" class="">
                <div v-show="feedbackBlock" id="feedback-block">
                    <b-form v-show="initialFeedback" @submit="submitFeedback" @reset="onReset">
                        <b-form-group label="Do you think the actions and timeframes presented in this plan are feasible?">
                            <b-form-radio-group required v-model="feasibility" value="1" name="feasibility-choice" :options="feasibilityChoice"></b-form-radio-group>
                        </b-form-group>
                        <div v-if="feasibility === '0'">
                            <b-form-group label="Please state why this plan is infeasible">
                                <b-form-textarea
                                        id="textarea"
                                        v-model="comment"
                                        rows="3"
                                        max-rows="6"
                                ></b-form-textarea>
                            </b-form-group>
                        </div>
                        <div v-if="feasibility === '1'">
                            <b-form-group v-for="question in questions" :key="question.question_id"
                                          :label="question.question_text">
                                <b-form-radio-group v-if="question.question_type === 'multi_choice'"
                                                    :id="question.question_id.toString()"
                                                    v-model="answers[question.question_id]"
                                                    :options="question.options"
                                ></b-form-radio-group>
                                <b-form-textarea v-if="question.question_type === 'text'"
                                                 :id="question.question_id.toString()"
                                                 v-model="answers[question.question_id]"
                                                 rows="3"
                                                 max-rows="6"
                                ></b-form-textarea>
                            </b-form-group>
                            <b-form-group label="How do you rate this plan?">
                                <star-rating v-model="rating"></star-rating>
                            </b-form-group>
                            <b-form-group label="Please share any additional thoughts about the alternative plans or the plan builder tool">
                                <b-form-textarea
                                        id="textarea"
                                        v-model="comment"
                                        rows="3"
                                        max-rows="6"
                                ></b-form-textarea>
                            </b-form-group>
                        </div>
                        <b-button type="submit">Submit</b-button>
                    </b-form>
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
                comment: null,
                feasibilityChoice: [
                    {text:"Yes", value: "1"},
                    {text:"No", value: "0"}
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
                SelectedFactors: [],
                questions: [],
                answers: new Map(),
                rating: null
            }
        },
        mounted() {
            const {utils} = AiravataAPI;

            if(!localStorage.feedbackProvided){
                localStorage.setItem('feedbackProvided', false);
            }else{
                let $this = this
                $this.feedbackProvided = localStorage.feedbackProvided;
            }
            let projectId = this.$route.params.projectId;

            //get the list of questions for this project. First fetches all questions and joins it with the project questions result.
            //TODO: Ideally this join should happen in db level
            utils.FetchUtils.get("/interactwel/api/questions/").then(
                allQuestions => {
                    utils.FetchUtils.get("/interactwel/api/projectquestions/?project_id="+projectId)
                        .then(questions => {
                            if (questions != null) {
                                let sortedQuestions = questions.sort((x, y) => x.id - y.id);
                                let projectQuestions = []
                                for (let sortedQuestion of sortedQuestions) {
                                    for (let question of allQuestions) {
                                        if (question.question_id === sortedQuestion.question_id){
                                            this.addQuestionOptions(question);
                                            projectQuestions.push(question);
                                        }
                                    }
                                }
                                this.questions = projectQuestions;
                            }
                        })
                        .catch(error => {
                            alert("Could not get the projects list. API error! " + error);
                        });
                }
            ).catch(error => {
                alert("Failed to fetch questions");
            })
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
            async submitFeedback(evt) {
                evt.preventDefault()
                //let adaptationPlan = JSON.parse(localStorage.getItem("adaptationPlan"));
                //adaptationPlan.planId = this.$route.params.planId;
                //localStorage.setItem('adaptationPlan', JSON.stringify(adaptationPlan));
                let user = await this.getLoggedInUser();
                let planId = this.$route.params.planId;
                let projectId = this.$route.params.projectId;
                debugger;
                const {utils} = AiravataAPI;
                utils.FetchUtils.post(
                    '/interactwel/api/feedbacks/',
                    {
                        date_created: new Date(),
                        date_modified: new Date(),
                        feasibilty: this.feasibility,
                        comments: this.comment,
                        rating: this.rating,
                        user_id: user.id,
                        project_id: projectId,
                        plan_id: planId
                    })
                    .then(feedback => {
                        if (feedback.error != null && feedback.error === true) {
                            alert("Error while posting the feedback.");
                            return;
                        }
                        //feedback posted successfully. now post the questions and answers
                        //prepare the answers body
                        let answerBody = [];
                        for (var element in this.answers) {
                            if (this.answers.hasOwnProperty(element)) {
                                let question = this.getQuestionById(element);
                                if (question === null || question === undefined) {
                                    continue;
                                }
                                answerBody.push({
                                    question:question.question_text,
                                    answer:this.answers[element],
                                    feedback_id:feedback.feedback_id
                                })
                            }
                        }
                        utils.FetchUtils.post("/interactwel/api/feedbackanswers",
                            answerBody).then( result => {
                                if (result.error != null && result.error === true) {
                                    alert("Error while posting the answers. " + feedback.error)
                                }
                        });
                    })
                    .catch(error => {
                        alert("API error while posting the feedback! " + error)
                    });

                localStorage.feedbackProvided = true
                this.feedbackProvided = true
                this.thankyouBlock = true
                this.feedbackBlock = false
            },
            addQuestionOptions(question) {

                let options = [];
                question.possible_answers.forEach(answer => {
                    options.push({
                        text:answer,
                        value:answer
                    })
                })
                question.options = options;

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
            },
            getQuestionById(id) {
                for (const question of this.questions) {
                    if (question.question_id == id) {
                        return question;
                    }
                }
            }
        },

    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>