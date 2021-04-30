<template>
  <div>
    <b-card title="My Feedback">
      <b-card-text>
        <div>
          Feedback Provided DateTime: {{ new Date(feedback.date_modified)| dateFormat('YYYY.MM.DD : HH.mm') }}
        </div>
        <hr>
        <div>
          Question: Do you think the actions and timeframes presented in this plan are feasible?
          <br>
          Answer: {{ feedback.feasibilty==1 ? 'Yes' : 'No' }}
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
        <hr>
        <div v-if="feedback.rating != null">
          How do you rate this plan?
          <star-rating
            :rating="feedback.rating"
            read-only
          />
        </div>
      </b-card-text>
    </b-card>
  </div>
</template>

<script>
export default {
  name: "OldFeedbackView",
  props: {
    feedback: null,
  },
};
</script>

<style scoped>

</style>