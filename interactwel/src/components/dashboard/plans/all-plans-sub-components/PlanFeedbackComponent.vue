<template>
  <div>
    <b-card v-if="feedback">
      <b-button
        v-b-toggle.collapse-1
        size="sm"
        class="float-right"
        variant="light"
      >
        View More <i class="fa fa-chevron-down" />
      </b-button>
      <h5 class="mb-1">
        Feedback
      </h5>
      <div>
        <small>Feedback Provided on: {{ new Date(feedback.date_modified)| dateFormat('YYYY.MM.DD : HH.mm') }}</small>
      </div>
      <div v-if="feedback.rating != null">
        <star-rating
          :rating="feedback.rating"
          read-only
        />
      </div>
      <b-collapse
        id="collapse-1"
        class="mt-2"
      >
        <small>
          <hr>
          <div>
            Question: Do you think the actions and timeframes presented in this plan are feasible?
            <br>
            Answer: {{ feedback.feasibilty === 1 ? 'Yes' : 'No' }}
          </div>
          <hr>
          <div
            v-for="feedbackItem in feedback.feedback_answers"
            :key="feedbackItem.id"
          >
            Question: {{ feedbackItem.question }}
            <br>
            Answer: {{ feedbackItem.answer }}
            <hr>
          </div>
          <div v-if="feedback.comments != null">
            Comment: {{ feedback.comments }}
          </div>
        </small>
      </b-collapse>
    </b-card>
    <b-card v-if="!feedback">
      No feedback provided yet
    </b-card>
  </div>
</template>

<script>
export default {
  name: "PlanFeedbackComponent",
  props: {
    selectedPlan: {
      type: Object,
    },
  },
  data() {
    return {
      feedback: null,
    };
  },
  mounted() {
    const {utils} = AiravataAPI;
    utils.FetchUtils.get("/interactwel/api/feedbacks/?plan_id=" + this.selectedPlan.plan_id).then(result => {
      if (result.length > 0) {
        this.feedback = result[0];
      }
    }
    ).catch(error => {
      alert("Failed to fetch feedbacks " + error);
    });
  },
};
</script>

<style scoped>

</style>