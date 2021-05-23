<template>
  <div>
    <component :is="component='Header'" />
    <b-container
      fluid
      class="main"
    >
      <b-container>
        <b-row>
          <b-col>
            <b-card-group deck>
              <b-card
                class="mb-2 learn-block"
                tag="article"
                style="max-width: 25rem"
              >
                <template
                  #header
                  style="background-color: #4caf50 !important;"
                >
                  <div class="h2 font-weight-bold">
                    Learn
                  </div>
                  <p>Learn about how adaptation can help FEW actors in watershed communities be resilient</p>
                </template>
                <b-card-text>
                  <div class="d-flex flex-column p-4">
                    <div class="p-1">
                      <b-button
                        pill
                        block
                        variant="outline-secondary"
                        @click="$router.push('learn/videos/1')"
                      >
                        Instructional Videos
                      </b-button>
                    </div>
                    <div class="p-1">
                      <b-button
                        pill
                        block
                        variant="outline-secondary"
                        @click="$router.push('learn/stories')"
                      >
                        Adaptation Stories
                      </b-button>
                    </div>
                    <div class="p-1">
                      <b-button
                        pill
                        block
                        variant="outline-secondary"
                        @click="$router.push('learn/docs')"
                      >
                        Documentation
                      </b-button>
                    </div>
                    <div class="p-1">
                      <b-button
                        pill
                        block
                        variant="outline-secondary"
                        @click="$router.push('learn/support')"
                      >
                        Support
                      </b-button>
                    </div>
                  </div>
                </b-card-text>
              </b-card>
              <b-card
                class="mb-2 prepare-block"
                tag="article"
                style="max-width: 25rem"
              >
                <template
                  #header
                  style="background-color: #4caf50 !important;"
                >
                  <div class="h2 font-weight-bold">
                    Prepare
                  </div>
                  <p>Create portfolios of community wide adaptation strategies using advanced scientific models and machine learning</p>
                </template>
                <b-card-text>
                  <div class="d-flex flex-column p-4">
                    <div class="p-1">
                      <b-button
                        pill
                        block
                        variant="outline-secondary"
                        @click="$router.push('projects/explore-projects')"
                      >
                        Join a New Project
                      </b-button>
                    </div>
                    <div class="p-1">
                      <b-button
                        pill
                        block
                        variant="outline-secondary"
                        @click="$router.push('all-plans')"
                      >
                        Generate New Plans
                      </b-button>
                    </div>
                    <div class="p-1">
                      <b-button
                        pill
                        block
                        variant="outline-secondary"
                        @click="$router.push('all-plans')"
                      >
                        Review Saved Plans
                      </b-button>
                    </div>
                  </div>
                </b-card-text>
              </b-card>
              <b-card
                class="mb-2 act-block"
                tag="article"
                style="max-width: 25rem"
              >
                <template
                  #header
                  style="background-color: #4caf50 !important;"
                >
                  <div class="h2 font-weight-bold">
                    Act
                  </div>
                  <p>Visualize, evaluate, recommend, identify and adopt community preffered adaptation plans</p>
                </template>
                <b-card-text>
                  <div class="d-flex flex-column p-4">
                    <div class="p-1">
                      <b-button
                        pill
                        block
                        variant="outline-secondary"
                        @click="$router.push('plans/saved-plans')"
                      >
                        Share Plans
                      </b-button>
                    </div>
                    <div class="p-1">
                      <b-button
                        pill
                        block
                        variant="outline-secondary"
                        @click="$router.push('community/groups')"
                      >
                        Participate in Group
                      </b-button>
                    </div>
                    <div class="p-1">
                      <b-button
                        pill
                        block
                        variant="outline-secondary"
                        @click="$router.push('community/events')"
                      >
                        Participate in Events
                      </b-button>
                    </div>
                  </div>
                </b-card-text>
              </b-card>
            </b-card-group>
          </b-col>
        </b-row>
      </b-container>
    </b-container>
    <component :is="component='Footer'" />
  </div>
</template>

<script>
import Header from './Header.vue';
import Footer from './Footer.vue';

export default {
  name: 'Dashboard',
  components: {
    Header, Footer,
  },
  props: {
    msg: String,
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    .main {
        background-color: #efefef;
        padding: 3rem 1rem;
        min-height: 90vh;
        text-align: center;
    }

     .card-title {
         font-size: 25px;
         font-weight: bold;
         color: #5e6b7e;
         border-bottom: 2px solid #28a645;
         padding-bottom: 5px;
     }

    .card-text {
        font-size: 13px;
        color: #5e6b7e;
    }

    .learn-block .card-header{
        background-color: #daf0d4;
        padding:2rem;
     }
    .learn-block .h2, .learn-block p{
        color: #446b3a;
    }

    .prepare-block .card-header{
        background-color: #ffe6db;
        padding:2rem;
    }
    .prepare-block .h2, .prepare-block p{
        color: #b74949;
    }
    .act-block .card-header{
        background-color: #d1e4f5;
        padding:2rem;
    }
    .act-block .h2, .act-block p{
        color: #2b689f;
    }
</style>
