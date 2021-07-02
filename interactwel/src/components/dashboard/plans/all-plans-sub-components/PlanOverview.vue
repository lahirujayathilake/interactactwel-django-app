<template>
  <b-list-group>
    <b-list-group-item class="flex-column align-items-start">
      <div class="d-flex w-100 justify-content-between">
        <h5 class="mb-1">
          Goals
        </h5>
        <small v-if="plan.goals">{{ plan.goals.length }} Goals selected</small>
      </div>
      <small>
        <ul class="no-padding">
          <li
            v-for="goalId in plan.goals"
          >{{ getGoalName(goalId).name }}</li>
        </ul>
      </small>
    </b-list-group-item>

    <b-list-group-item class="flex-column align-items-start">
      <div class="d-flex w-100 justify-content-between">
        <h5 class="mb-1">
          Actors
        </h5>
        <small v-if="plan.actors" class="text-muted"> {{ plan.actors.length }} Actors Selected</small>
      </div>
      <small>
        <ul class="no-padding">
          <li
            v-for="actorId in plan.actors"
          >{{ getActorName(actorId).name }}</li>
        </ul>
      </small>
    </b-list-group-item>

    <b-list-group-item class="flex-column align-items-start">
      <div class="d-flex w-100 justify-content-between">
        <h5 class="mb-1">
          Actions
        </h5>
      </div>
      <small>
        <ul class="no-padding">
          <li
            v-for="actorId in plan.actors"
          >
            {{ getActorName(actorId).name }}
            <ul>
              <li
                v-for="action_mapping in getActionMappings(actorId, plan.action_mapping)"
              >
                {{ getActionName(action_mapping.action_id).name }}
              </li>
            </ul>
          </li>
          <li>Farmers: Surface Water (SW)
            <ul>
              <li>Increase the volume of non-Columbia surface water</li>
            </ul>
          </li>
        </ul>
      </small>
    </b-list-group-item>
  </b-list-group>
</template>

<script>
export default {
  name: "PlanOverview",
  props: {
    plan: {
      type: Object,
    },
    goals: {
      type: Array,
    },
    actors: {
      type: Array,
    },
    actions: {
      type: Array,
    },
  },
  methods: {
    getGoalName(goalId) {
      if (this.goals) {
        return this.goals.find(goal => goal.goal_id === goalId);
      }
      return {};
    },

    getActorName(actorId) {
      if (this.actors) {
        return this.actors.find(actor => actor.actor_id === actorId);
      }
      return {};
    },

    getActionName(actionId) {
      if (this.actions) {
        return this.actions.find(action => action.action_id === actionId);
      }
      return {};
    },

    getActionMappings(actorId, mappings) {
      if (mappings) {
        return mappings.filter(mapping => mapping.actor_id === actorId);
      }

      return [];
    },

    getActorsList(actorIds) {
      if (actorIds && this.actors) {
        return this.actors.filter(actor => actorIds.includes(actor.actor_id));
      }

      return {};

    },
  },
};
</script>

<style scoped>

</style>