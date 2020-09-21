<template>
  <b-col lg="12">
    <ol class="progress-bar">
      <li class="col-md-2">
        <div id="active" class="step-progress-bar">
          <div class="step-no">1</div>
          <h4 class="list-group-item-heading">Goals</h4>
          <h4r class="list-group-item-heading">&#10003;</h4r>
          <p class="list-group-item-text">{{adaptationPlan.selectedGoals.length}} Goals Selected</p>
        </div>
      </li>
      <li class="col-md-2 active">
        <div class="step-progress-bar">
          <div class="step-no">2</div>
          <h4 class="list-group-item-heading">Actors</h4>
          <h4r class="list-group-item-heading">&#10003;</h4r>
          <p class="list-group-item-text">{{selectedActors.length}} Actors Selected</p>
        </div>
      </li>
      <li class="col-md-2">
        <div class="step-progress-bar">
          <div class="step-no">3</div>
          <h4 class="list-group-item-heading">Actions</h4>
          <h4r class="list-group-item-heading">&#10003;</h4r>
          <p class="list-group-item-text">0 Actions Selected</p>
        </div>
      </li>
      <li class="col-md-2">
        <div class="step-progress-bar">
          <div class="step-no">4</div>
          <h4 class="list-group-item-heading">Visualize and Evaluate</h4>
          <h4r class="list-group-item-heading">&#10003;</h4r>
          <p class="list-group-item-text">Adaptation Plans</p>
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
          <div class="step-no">5</div>
          <h4 class="list-group-item-heading">Wrap Up</h4>
          <h4r class="list-group-item-heading">&#10003;</h4r>
          <p class="list-group-item-text">Save and Print Plans</p>
        </div>
      </li>
    </ol>
    <div id="step2" title="Step 2"
         icon="ti-settings">
      <div class="help-block-actors">
        <b-collapse visible id="collapse-2">
          <b-card
                  tag="article"
                  style="max-width: 25rem;"
                  class="mb-2"
          >
            <h4 class="card-title">"Who are Actors?"<b-button v-b-toggle.collapse-2 variant="outline-info" class="m-1b" size="sm"><i>Hide panel</i></b-button></h4>
            <!--<b-card-text><strong>Who are Actors?</strong></b-card-text><br/>-->
            <b-card-text>
              <p align="justify"><b>Actors</b>
                are groups of individuals, institutions, and organizations in a community who are most impacted, directly and/or indirectly, by the changes and stresses in the water, energy, and land resources they depend on.
              </p>

              <p align="justify">In <b>Step 2</b>, think about which group of actors would be of interest to you and your stakeholders. Then choose from the options available in this list by clicking on the options that reflect your group’s interest. Note that even though you may decide to choose only a few actors, your adaptation plans (in Step 4) may include additional actors who would need to also take actions in conjunction with you. But more on that when you reach Step 4!
              </p>

            </b-card-text>

          </b-card>
        </b-collapse>
      </div>
      <b-card no-body footer-tag="footer">
        <div class="step-header" slot="header">Choose Actors
          <em slot="header">
            <b-button v-b-toggle.collapse-2 class="m-1" size="sm"> Show instructions </b-button>
          </em>
        </div>
        <b-card-body>
          <p class="card-text"><i>
            Choose the actors whose adaptation actions you want to visualize.
          </i></p>
        </b-card-body>
        <b-list-group-item>
          <b-form-checkbox-group>
            <label class="form-checkbox">
              <input type="checkbox" v-model="selectAllActors" @click="selectActors">
              Select All
              <!-- <div class="text-uppercase text-bold">id selected: {{selectedActors}}</div> -->
            </label>
            <!--<div class="text-uppercase text-bold">id selected: {{selectedActors}}</div>-->
          </b-form-checkbox-group>
        </b-list-group-item>
        <b-list-group flush>
          <b-form>
            <div class="list-group">
              <li class="list-group-item" v-for="actor in actors" v-bind:key="actor.actor_id">
                <label class="form-checkbox">
                  <input type="checkbox" :value="actor" v-model="selectedActors"
                         :disabled="actor.readonly">
                  {{actor.name}}
                  <b-collapse :id="'collapse_'+actor.actor_id">
                    <p class="item-info">
                      <small>{{actor.description}}</small>
                    </p>
                  </b-collapse>
                </label>
                <b-button v-b-toggle="'collapse_' + actor.actor_id" variant="outline-secondary">
                  <b-badge class="info-button" pill variant="secondary" >i</b-badge>
                </b-button>
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
          <b-button id="step2-next-btn" @click="submit" variant="next" size="sm">Next</b-button>
          <b-button id="step2-back-btn" @click="back" variant="back" size="sm">Back</b-button>
        </em>
      </b-card>
    </div>
    <b-modal v-model="showInfoModal">
      <template slot="modal-title">
        <strong>No selections were made</strong>
      </template>
      You forgot to select any actors. We filled that for you.
      <template slot="modal-footer" slot-scope="{ ok, cancel, hide }">
        <b-button size="sm" variant="next" @click="onConfirm">Ok</b-button>
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
      }
    },
    mounted() {
      this.adaptationPlan = this.$store.state.currentAdaptationPlan;
      if(this.adaptationPlan){
        this.selectedActors=this.adaptationPlan.selectedActors;
      }

      // if (localStorage.getItem('adaptationPlan')) this.selectedActors = JSON.parse(localStorage.getItem('adaptationPlan')).selectedActors;

      const { utils } = AiravataAPI;
      this.projectId = this.$route.params.projectId
      utils.FetchUtils.get('/interactwel/api/actors/')
              .then(data => {
                this.actors = data;
              })
              .catch(error => {
                alert("Could not get the actors list. API error! " + error)
              });

    },

    watch: {
      selectedActors: {
        handler() {
          this.actors.id;
        },
        deep: true,
      }
    },

    methods: {
      selectActors() {
        this.selectedActors = [];
        if (!this.selectAllActors) {
          this.actors.forEach(element => {
            this.selectedActors.push(element);
          });
        }else{
          this.selectedActors = [];
        }
      },
      submit() {
        if(this.selectedActors.length<1){
          this.showInfoModal = true;
          return;
        }
        this.$store.commit("setSelectedActors", this.selectedActors);
        this.$store.commit("step2", true);
        this.$router.push('/adaptation-plans/'+this.projectId+'/actions');
      },

      back(){
        this.$router.push('/adaptation-plans/1/goals')
      },
      onConfirm() {
        this.selectActors();
        this.$store.commit("setSelectedActors", this.selectedActors);
        this.$store.commit("step2", true);
        this.$router.push('/adaptation-plans/'+this.projectId+'/actions');
      }
    }

  }
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
