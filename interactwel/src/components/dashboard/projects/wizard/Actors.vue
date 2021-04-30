<template>
  <b-col lg="12">
    <ol class="progress-bar">
      <li class="col-md-2">
        <div
          id="active"
          class="step-progress-bar"
        >
          <div class="step-no">
            1
          </div>
          <h4 class="list-group-item-heading">
            Goals
          </h4>
          <h4r class="list-group-item-heading">
            &#10003;
          </h4r>
          <p class="list-group-item-text">
            {{ adaptationPlan.selectedGoals.length }} Goals Selected
          </p>
        </div>
      </li>
      <li class="col-md-2 active">
        <div class="step-progress-bar">
          <div class="step-no">
            2
          </div>
          <h4 class="list-group-item-heading">
            Actors
          </h4>
          <h4r class="list-group-item-heading">
            &#10003;
          </h4r>
          <p class="list-group-item-text">
            {{ selectedActors.length }} Actors Selected
          </p>
        </div>
      </li>
      <li class="col-md-2">
        <div class="step-progress-bar">
          <div class="step-no">
            3
          </div>
          <h4 class="list-group-item-heading">
            Actions
          </h4>
          <h4r class="list-group-item-heading">
            &#10003;
          </h4r>
          <p class="list-group-item-text">
            0 Actions Selected
          </p>
        </div>
      </li>
      <li class="col-md-2">
        <div class="step-progress-bar">
          <div class="step-no">
            4
          </div>
          <h4 class="list-group-item-heading">
            Visualize and Evaluate
          </h4>
          <h4r class="list-group-item-heading">
            &#10003;
          </h4r>
          <p class="list-group-item-text">
            Adaptation Plans
          </p>
        </div>
      </li>
      <!--<li class="col-md-2">
        <div class="step-progress-bar">
          <div class="step-no">5</div>
          <h4 class="list-group-item-heading">Feedback</h4>
          <h4r class="list-group-item-heading">&#10003;</h4r>
          <p class="list-group-item-text">Rate each plan</p>
        </div>
      </li>-->
      <li class="col-md-2">
        <div class="step-progress-bar">
          <div class="step-no">
            5
          </div>
          <h4 class="list-group-item-heading">
            Wrap Up
          </h4>
          <h4r class="list-group-item-heading">
            &#10003;
          </h4r>
          <p class="list-group-item-text">
            Save and Print Plans
          </p>
        </div>
      </li>
    </ol>
    <div
      id="step2"
      title="Step 2"
      icon="ti-settings"
    >
      <div class="help-block-actors">
        <b-collapse
          id="collapse-what_are_actors"
          visible
        >
          <b-card
            tag="article"
            style="max-width: 25rem;"
            class="mb-2"
          >
            <div class="row">
              <div class="col">
                <h4 class="card-title">
                  "Who are Actors?"
                </h4>
              </div>
              <div class="col-1 mr-3">
                <h5 class="text-right font-weight-light">
                  <i
                    v-b-toggle.collapse-what_are_actors
                    class="fas fa-times"
                    style="cursor: pointer"
                  />
                </h5>
              </div>
            </div>
            <!--<b-card-text><strong>Who are Actors?</strong></b-card-text><br/>-->
            <b-card-text>
              <p align="justify">
                <b>Actors</b>
                are groups of individuals, institutions, and organizations in a community who are most impacted, directly and/or indirectly, by the changes and stresses in the water, energy, and land resources they depend on.
              </p>

              <p align="justify">
                In <b>Step 2</b>, think about which group of actors would be of interest to you and your stakeholders. Then choose from the options available in this list by clicking on the options that reflect your group’s interest. Note that even though you may decide to choose only a few actors, your adaptation plans (in Step 4) may include additional actors who would need to also take actions in conjunction with you. But more on that when you reach Step 4!
              </p>
            </b-card-text>
          </b-card>
        </b-collapse>
      </div>
      <b-card
        no-body
        footer-tag="footer"
      >
        <div
          slot="header"
          class="step-header"
        >
          Choose Actors
          <em slot="header">
            <i
              v-b-toggle.collapse-what_are_actors
              class="far fa-question-circle"
              title="Show instructions"
              style="cursor: pointer"
            />
          </em>
        </div>
        <b-card-body>
          <p class="card-text">
            <i>
              Choose the actors whose adaptation actions you want to visualize.
            </i>
          </p>
        </b-card-body>
        <b-list-group-item>
          <b-form-checkbox-group>
            <label class="form-checkbox">
              <input
                v-model="selectAllActors"
                type="checkbox"
                @click="selectActors"
              >
              Select All
              <!-- <div class="text-uppercase text-bold">id selected: {{selectedActors}}</div> -->
            </label>
            <!--<div class="text-uppercase text-bold">id selected: {{selectedActors}}</div>-->
          </b-form-checkbox-group>
        </b-list-group-item>
        <b-list-group flush>
          <b-form>
            <div class="list-group">
              <li
                v-for="actor in actors"
                :key="actor.actor_id"
                class="list-group-item"
              >
                <label class="form-checkbox">
                  <input
                    v-model="selectedActors"
                    type="checkbox"
                    :value="actor"
                    :disabled="actor.readonly"
                  >
                  {{ actor.name }}
                  <b-collapse :id="'collapse_'+actor.actor_id">
                    <p class="item-info">
                      <small>{{ actor.description }}</small>
                    </p>
                  </b-collapse>
                </label>
                <b-badge
                  v-b-toggle="'collapse_' + actor.actor_id"
                  class="info-button"
                  pill
                  variant="secondary"
                >
                  i
                </b-badge>
              </li>
            </div>
          </b-form>
        </b-list-group>
        <em slot="footer">
          <!--<b-button-group>
              <b-button id="step2-back-btn" @click="tabIndex--" variant="outline-success" size="sm">
                  Back
              </b-button>
              <b-button id="step2-next-btn" @click="step2NextClicked" variant="success" size="sm">Next
              </b-button>
          </b-button-group>-->
          <b-button
            id="step2-next-btn"
            variant="next"
            size="sm"
            @click="submit"
          >Next</b-button>
          <b-button
            id="step2-back-btn"
            variant="back"
            size="sm"
            @click="back"
          >Back</b-button>
        </em>
      </b-card>
    </div>
    <b-modal v-model="showInfoModal">
      <template slot="modal-title">
        <strong>No selections were made</strong>
      </template>
      You forgot to select any actors. We filled that for you.
      <template
        slot="modal-footer"
        slot-scope="{ ok, cancel, hide }"
      >
        <b-button
          size="sm"
          variant="next"
          @click="onConfirm"
        >
          Ok
        </b-button>
      </template>
    </b-modal>
  </b-col>
</template>
<script>
import ActorsOpts from './../../../../../public/static/actors.json';

export default {
  name: 'Actors',
  props: ['goalsAssignedToThisProject'],
  data() {
    return {
      itemInfoVisibility: false,
      selectAllActors: false,
      selectedActors: [],
      actors: [], //ActorsOpts
      adaptationPlan: [],
      showInfoModal: false,
    };
  },

  watch: {
    selectedActors: {
      handler() {
        this.actors.id;
      },
      deep: true,
    },
  },
  mounted() {
    this.adaptationPlan = this.$store.state.currentAdaptationPlan;
    if (this.adaptationPlan){
      this.selectedActors = this.adaptationPlan.selectedActors;
    }

    // if (localStorage.getItem('adaptationPlan')) this.selectedActors = JSON.parse(localStorage.getItem('adaptationPlan')).selectedActors;

    const { utils } = AiravataAPI;
    this.projectId = this.$route.params.projectId;
    utils.FetchUtils.get('/interactwel/api/actors/')
      .then(data => {
        this.actors = data;
      })
      .catch(error => {
        alert("Could not get the actors list. API error! " + error);
      });

  },

  methods: {
    selectActors() {
      this.selectedActors = [];
      if (!this.selectAllActors) {
        this.actors.forEach(element => {
          this.selectedActors.push(element);
        });
      } else {
        this.selectedActors = [];
      }
    },
    submit() {
      if (this.selectedActors.length < 1){
        this.showInfoModal = true;
        return;
      }
      this.$store.commit("setSelectedActors", this.selectedActors);
      this.$store.commit("step2", true);
      this.$router.push('/adaptation-plans/' + this.projectId + '/actions');
    },

    back(){
      this.$router.push('/adaptation-plans/' + this.$route.params.projectId + '/goals');
    },
    onConfirm() {
      this.selectActors();
      this.$store.commit("setSelectedActors", this.selectedActors);
      this.$store.commit("step2", true);
      this.$router.push('/adaptation-plans/' + this.projectId + '/actions');
    },
  },

};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  h3 {
    margin: 40px 0 0;
  }
  ul {
    list-style-type: none;
    padding: 0;
  }
  li {
    display: inline-block;
    margin: 0 10px;
  }
  a {
    color: #42b983;
  }
</style>
