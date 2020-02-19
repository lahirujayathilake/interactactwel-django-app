<template>
    <div>
        <b-card no-body>
            <div class="col-4 p-3">
                <b-form-select v-model="selectedProject" :options="projects" size="sm" class="mt-3"></b-form-select>
                <b-form-select v-model="selectedUser" :options="users" size="sm" class="mt-3"></b-form-select>
                <b-form-select v-model="selectedStatus" :options="statusList" size="sm" class="mt-3"></b-form-select>
                <b-form-select v-model="selectedRole" :options="roles" size="sm" class="mt-3"></b-form-select>
                <b-form-select v-model="selectedSector" :options="sectors" size="sm" class="mt-3"></b-form-select>
                <b-form-select v-model="selectedActor" :options="actors" size="sm" class="mt-3"></b-form-select>

                <b-button @click="submitAction" type="submit" variant="success"  size="sm" class="mt-3" style="float:right">Assign</b-button>

            </div>
        </b-card>
        <b-card v-show="">
        <b-card-body title="You don't have access to any projects">
            <b-card-text>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque luctus purus sit amet massa hendrerit semper at eu dui.
            </b-card-text>
        </b-card-body>
        </b-card>


    </div>
</template>

<script>
    import L from 'leaflet';
    import {LMap, LTileLayer, LMarker} from 'vue2-leaflet';
    import axios from 'axios';

    export default {
        components: {
            LMap, LTileLayer, LMarker

        },
        name: 'AssignProjects',

        data() {
            return {
                selectedProject: null,
                selectedUser: null,
                selectedStatus: null,
                selectedRole: null,
                selectedSector: null,
                selectedActor: null,
                projects: [
                    { value: null, text: 'Please select a Project' }
                ],
                users: [
                    { value: null, text: 'Please select an User' }
                ],

                //todo: verify these values
                statusList: [
                    { value: null, text: 'Please select a Status' },
                    { value: "Active", text: 'Active' },
                    { value: "Inactive", text: 'Inactive' }
                ],

                roles: [
                    { value: null, text: 'Please select a Role' },
                    { value: "Admin", text: 'Admin' },
                    { value: "Non-Admin", text: 'Non-Admin' }
                ],
                sectors: [
                    { value: null, text: 'Please select a Sector' },
                    { value: "Sector-1", text: 'Sector-1' },
                    { value: "Sector-2", text: 'Sector-2' }


                ],
                actors: [
                    { value: null, text: 'Please select an Actor' },
                    { value: "Actor-1", text: 'Actor-1' },
                    { value: "Actor-2", text: 'Actor-2' }
                ]
            }

        },

        mounted() {

            axios.get( process.env.VUE_APP_API_BASE_URL + '/interactwel/api/projects/',
                {
                    headers: {
                        "X-CSRFTOKEN" : "RtR4hQtbuve5i4RLgvWDkuWwIFwsS9WIcQNCSm4wlk9AHoTQtk2ekNcqBOQOvbhW"
                    }
                })
                .then(response => {
                    response.data.forEach( projectItem => {
                        this.projects.push({value: projectItem.id, text: projectItem.name});
                    });
                })
                .catch(error => {
                    alert("Could not create the new project. API error! " + error)
                });

            axios.get(process.env.VUE_APP_API_BASE_URL + '/interactwel/api/users/',
                {
                    headers: {
                        "X-CSRFTOKEN" : "RtR4hQtbuve5i4RLgvWDkuWwIFwsS9WIcQNCSm4wlk9AHoTQtk2ekNcqBOQOvbhW"
                    }
                })
                .then(response => {
                    response.data.forEach( userItem => {
                        this.users.push({value: userItem.id, text: userItem.username});
                    });
                })
                .catch(error => {
                    alert("Could not create the new project. API error! " + error)
                });

        },


        methods: {

            submitAction() {
                axios.post(process.env.VUE_APP_API_BASE_URL + '/interactwel/api/projectuserss/', {
                        user_id: this.selectedUser.id,
                        project_id: this.selectedProject.id,
                        status : this.selectedStatus,
                        role: this.selectedRole,
                        sector: this.selectedSector,
                        actor: this.selectedActor

                    },
                    {
                        headers: {
                           // "X-CSRFTOKEN" :  process.env.VUE_APP_X_CSRFTOKEN
                            "X-CSRFTOKEN" :  "IJ3optOBMDCJ7cZDbjNH3t6Fn3rttsFKx79lyhx2maMsyL7FoEu8skYkst2v8rhS"
                        }
                    })
                    .then(response => {
                        this.responseData = response.data; console.log(response);
                        alert (response);
                    })
                    .catch(error => {
                        alert("API error! " + error)
                    });
                return true
            },

        }

    }

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
    @import '../../../assets/vendor/Vue2Leaflet/leaflet.css';
    .map-container{
        height: 400px;
        overflow:auto;
    }
</style>

