<template>
    <div>
      <b-card-group>
        <b-card footer-tag="footer">
          <div class="step-header" slot="header">Groups
          </div>
          <b-card-text>
            <b-row>
              <b-col lg="8">
                <b-container>
                  <b-row>
                    <b-col>
                      <b-button class="mr-2" size="sm" data-toggle="modal" data-target="#createGroupModal">Create Group</b-button>
                    </b-col>
                  </b-row>
                </b-container>
                <b-container class="mt-3">
                  <b-row>
                    <b-col>
                      <b-list-group>
                        <b-list-group-item v-for="group in groups">{{group.group_name}} <b-button size="sm">Leave</b-button><b-button size="sm" class="mr-2">Add Friend</b-button></b-list-group-item>
                      </b-list-group>
                    </b-col>
                  </b-row>
                </b-container>
              </b-col>
              <b-col lg="4">
                <b-container>
                  <b-row>
                    <b-col class="widget">
                      <div class="widget-title">Groups you manage</div>
                      <b-list-group class="mt-2">
                        <b-list-group-item>Group 1
                          <b-button size="sm">Manage</b-button>
                        </b-list-group-item>
                        <b-list-group-item>Group 1
                          <b-button size="sm">Manage</b-button>
                        </b-list-group-item>
                      </b-list-group>
                    </b-col>
                  </b-row>
                  <b-row>
                    <b-col class="widget">
                      <div class="widget-title">
                        Groups you may like
                      </div>
                      <b-list-group class="mt-2">
                        <b-list-group-item>Group 1
                          <b-button size="sm">Join</b-button>
                        </b-list-group-item>
                        <b-list-group-item>Group 2
                          <b-button size="sm">Join</b-button>
                        </b-list-group-item>
                        <b-list-group-item>Group 3
                          <b-button size="sm">Join</b-button>
                        </b-list-group-item>
                        <b-list-group-item>Group 4
                          <b-button size="sm">Join</b-button>
                        </b-list-group-item>
                        <b-list-group-item>Group 5
                          <b-button size="sm">Join</b-button>
                        </b-list-group-item>
                      </b-list-group>
                    </b-col>
                  </b-row>
                </b-container>
              </b-col>
            </b-row>
          </b-card-text>
        </b-card>
      </b-card-group>
      <div class="modal fade" id="createGroupModal" tabindex="-1" role="dialog" aria-labelledby="createGroupModalLabel" aria-hidden="true">
        <div class="modal-dialog" role="document">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" id="createGroupModalLabel">Create Group</h5>
              <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <div class="modal-body">
              <b-form>
                <b-form-group
                    id="input-group-1"
                    label="Group Name"
                    label-for="input-1"
                    description=""
                >
                  <b-form-input
                      id="input-1"
                      v-model="form.group_name"
                      type="text"
                      required
                      placeholder=""
                  ></b-form-input>
                </b-form-group>

                <b-form-group
                    id="input-group-2"
                    label="Group Description"
                    label-for="input-1"
                    description=""
                >
                  <b-form-input
                      id="input-1"
                      v-model="form.group_description"
                      type="text"
                      required
                      placeholder=""
                  ></b-form-input>
                </b-form-group>
              </b-form>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
              <button type="button" class="btn btn-primary" @click="createGroupAction">Create</button>
            </div>
          </div>
        </div>
      </div>
    </div>
</template>

<script>
    import Header from './../../Header.vue';
    import Footer from './../../Footer.vue';

    export default {
        components: {
            Header, Footer
        },
        name: 'Groups',

        data() {
            return {
              form: {
                group_name: null,
                group_description: null,
              },
              groups: [],
            }
        },

        mounted() {
          this.getAllGroups();
        },


        methods: {
          createGroupAction() {
            if (this.form.group_name){
              const { utils } = AiravataAPI;
              utils.FetchUtils.post(
                  '/interactwel/api/groups/',
                  {
                    group_name: this.form.group_name,
                    group_description: this.form.group_description,
                  })
                  .then(data => {
                    this.projects = data;
                    $('#createGroupModal').modal('hide');
                  })
                  .catch(error => {
                    alert("Create Group. API error! " + error)
                  });
              return true
            }
          },

          getAllGroups() {
            const { utils } = AiravataAPI;
            utils.FetchUtils.get("/interactwel/api/groups/").then(result => {
                  if (result.length > 0) {
                    this.groups = result;
                  }
                }
            ).catch(error => {
              alert("Failed to fetch groups " + error);
            })
          }
        }

    }

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
    .map-wrapper {
        -webkit-box-flex: 1;
        -ms-flex: 1;
        flex: 1;
        min-height: calc(60vh);
    }

    .widget {
        background-color: #f7f7f7;
        padding: 1rem;
        border: 1px solid #efefef;
        border-radius: 5px;
        margin-bottom: 10px;
    }

    .widget-title {
        font-size: 16px;
        font-weight: 700;
    }
</style>

