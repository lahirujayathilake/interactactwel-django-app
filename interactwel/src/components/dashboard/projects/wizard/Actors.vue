<template>
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
          </label>
          <!--<div class="text-uppercase text-bold">id selected: {{selectedActors}}</div>-->
        </b-form-checkbox-group>
      </b-list-group-item>
      <b-list-group flush>
        <b-form>
          <div class="list-group">
            <li class="list-group-item" v-for="actor in actors" v-bind:key="actor.id">
              <label class="form-checkbox">
                <input type="checkbox" :value="actor" v-model="selectedActors"
                       :disabled="actor.readonly">
                {{actor.actor}}
              </label>
              <b-badge class="info-button" pill variant="secondary" v-b-tooltip.hover
                       :title="actor.info">i
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
        <b-button id="step2-next-btn" @click="submit" variant="next" size="sm">Next</b-button>
        <b-button id="step2-back-btn" @click="back" variant="back" size="sm">Back</b-button>
      </em>
    </b-card>
  </div>
</template>
<script>
    import ActorsOpts from './../../../../../public/static/actors.json';

    export default {
  name: 'Actors',
  props: {

  },
    data() {
        return {
            itemInfoVisibility: false,
            selectAllActors: false,
            selectedActors: [],
            actors: ActorsOpts,
        }
    },
        mounted() {
            if (localStorage.getItem('selectedActors')) this.selectedActors = JSON.parse(localStorage.getItem('selectedActors'));
        },

        watch: {
            selectedActors: {
                handler() {
                    localStorage.setItem('selectedActors', JSON.stringify(this.selectedActors));
                },
                deep: true,
            }
        },

        methods: {
            selectActors() {
                this.selectedActors = [];
                if (!this.selectAllActors) {
                    this.actors.forEach(element => {
                        if (element.readonly == false) {
                            this.selectedActors.push(element);
                        }
                    });
                }
            },
            submit() {
                localStorage.setItem('step2', true);
                let adaptationPlan = JSON.parse(localStorage.getItem("adaptationPlan"));
                adaptationPlan.selectedActors = this.selectedActors;
                localStorage.setItem('adaptationPlan', JSON.stringify(adaptationPlan));
                this.$router.push('/adaptation-plans/1/actions')
            },

            back(){
                this.$router.push('/adaptation-plans/1/goals')
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
