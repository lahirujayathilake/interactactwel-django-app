<template>
    <b-card-group>
        <b-card footer-tag="footer" v-show="isStep1Active">
            <div class="step-header" slot="header">Create New Project</div>
            <b-card-text>
                <div class="p-3">
                    <b-col lg="6">
                        <b-form>
                            <b-form-group
                                    id="input-group-1"
                                    label="Project Name"
                                    label-for="input-1"
                                    description=""
                            >
                                <b-form-input
                                        id="input-1"
                                        v-model="form.projectName"
                                        type="text"
                                        required
                                        placeholder=""
                                ></b-form-input>
                            </b-form-group>

                            <b-form-group id="input-group-3" label="Location" label-for="input-3">
                                <b-form-input
                                        id="input-3"
                                        v-model="form.location"
                                        required
                                        placeholder="City, Region, Country"
                                ></b-form-input>

                            </b-form-group>

                            <b-form-group id="input-group-4" label="Coordinates" label-for="input-4">
                                <b-form inline>
                                    <b-input
                                            id="input-4"
                                            v-model="form.latitude"
                                            required
                                            placeholder="Latitude (degrees)"
                                    ></b-input>

                                    <b-input
                                            id="input-5"
                                            v-model="form.longtitude"
                                            required
                                            placeholder="Longitude (degrees)"
                                    ></b-input>
                                </b-form inline>

                            </b-form-group>

                            <b-form-group id="input-group-2" label="Description" label-for="input-2">
                                <b-form-textarea
                                        id="input-2"
                                        v-model="form.description"
                                        required
                                        placeholder=""
                                ></b-form-textarea>
                            </b-form-group>

                            <b-button @click="createProjectAction" type="submit" variant="success">Next</b-button>
                            <!--<b-button type="reset" class="mr-2" variant="dark">Reset</b-button>-->
                        </b-form>
                    </b-col>
                    <!--<b-card class="mt-3" header="Form Data Result">
                        <pre class="m-0">{{ form }}</pre>
                    </b-card>-->
                </div>
            </b-card-text>
        </b-card>


        <b-card footer-tag="footer" v-show="isStep2Active">
            <div class="step-header" slot="header">Create Conceptual System Diagram
            </div>
            <b-card-text>
                <div class="p-3">
                    <b-card-text class="text-justify">Build a Conceptual System Diagram of your communities's adaptation plans
                        to manage food, energy, water and land resources stressed by perturbation of concern. </b-card-text>
                    <br>

                    <b-button @click="stepStartCSD" class="btn-upload" type="submit" variant="success">Start</b-button>

                    <!--<b-card class="mt-3" header="Form Data Result">
                        <pre class="m-0">{{ form }}</pre>
                    </b-card>-->
                </div>
            </b-card-text>
            <template v-slot:footer>
                <b-button @click="step2BackClicked" type="reset" class="btn-upload" variant="dark">Back</b-button>
            </template>
        </b-card>


        <b-card footer-tag="footer" v-show="isStep2Active">
            <div class="step-header" slot="header">Upload Map Spatial Layers
            </div>
            <b-card-text>
                <div class="p-3">
                    <b-col lg="6">
                        <b-form>
                            <b-form-group id="input-group-2" label="Select GeoJson Files " label-for="input-2">
                                <label class="file-select">
                                    <div class="large-12 medium-12 small-12 cell">
                                        <input type="file" id="files" ref="files" multiple v-on:change="handleFilesUpload()"/>
                                    </div>
                                    <div class="large-12 medium-12 small-12 cell">
                                        <div v-for="(file, key) in geojson_files" class="file-listing">{{ file.name }}
                                            <span class="remove-file" v-on:click="removeFile( key )">Remove</span></div>
                                    </div>
                                    <!--<br>
                                    <div class="large-12 medium-12 small-12 cell">
                                        <button v-on:click="addFiles()">Add Files</button>
                                    </div>
                                    <br>
                                    <div class="large-12 medium-12 small-12 cell">
                                        <button v-on:click="submitFiles()">Submit</button>
                                    </div>-->

                                </label>
                            </b-form-group>

                            <b-button @click="" class="btn-upload" type="submit" variant="success">Submit</b-button>

                        </b-form>
                    </b-col>
                    <!--<b-card class="mt-3" header="Form Data Result">
                        <pre class="m-0">{{ form }}</pre>
                    </b-card>-->
                </div>
            </b-card-text>

            <template v-slot:footer>
                <b-button @click="step3NextClicked" type="submit" variant="success">Next</b-button>
            </template>
        </b-card>


        <b-card footer-tag="footer" v-show="isStep2CSD">
            <div class="step-header" slot="header">Natural Resources and Societal Drivers</div>
            <b-card-text>
                <div class="p-3">
                    <b-col lg="8">
                        <b-form>
                            <b-form-group
                                    id="input-group-1"
                                    label="Identify Natural Resources and Societal Drivers"
                                    label-for="input-1"
                                    description=""
                            >
                                <b-card-text>How important are the following factors to you in supporting the social, environmental, and economic well-being of your community?
                                </b-card-text>
                            </b-form-group>

                            <b-card-group deck>
                                <b-card header="Select Natural Resources">
                                    <div class="list-group">
                                        <li class="list-group-item" v-for="ns in naturalsystems" v-bind:key="ns.id">
                                            <label class="form-checkbox" :disabled="ns.readonly">
                                                <input type="checkbox" :value="ns.id"
                                                       v-model="selectedActions"
                                                       :disabled="ns.readonly"/>
                                                {{ns.name}}
                                            </label>
                                        </li>
                                    </div>
                                </b-card>

                                <b-card class="card-nb" header="Natural Resources in System Diagram">
                                    <!--<b-card no-body style="max-width: 20rem;" img-src="https://placekitten.com/380/200" img-alt="Image" img-top>-->
                                    <img src="./../../../../public/static/img/Natural_systems.svg" width="200" height="121" class="center"></img>
                                </b-card>

                            </b-card-group>

                            <b-card-group deck>
                                <b-card header="Select Societal Drivers">
                                    <div class="list-group">
                                        <li class="list-group-item" v-for="sd in societaldrivers" v-bind:key="sd.id">
                                            <label class="form-checkbox" :disabled="sd.readonly">
                                                <input type="checkbox" :value="sd.id"
                                                       v-model="selectedActions"
                                                       :disabled="sd.readonly"/>
                                                {{sd.name}}
                                            </label>

                                        </li>
                                    </div>
                                </b-card>
                                <b-card class="card-nb" header="Societal Drivers in System Diagram">
                                    <img src="./../../../../public/static/img/societal_drivers.svg" width="200" height="121" class="center"></img>
                                </b-card>
                            </b-card-group>

                        </b-form>
                    </b-col>
                </div>
            </b-card-text>
            <template v-slot:footer>
                <b-button @click="stepBackStartCSD" type="reset" class="btn-upload" variant="dark">Back</b-button>
                <b-button @click="step2CSD" type="submit" variant="success">Next</b-button>
            </template>
        </b-card>


        <b-card footer-tag="footer" v-show="isStep1CSD">
            <div class="step-header" slot="header">Perturbations</div>
            <b-card-text>
                <div class="p-3">
                    <b-col lg="8">
                        <b-form>
                            <b-form-group
                                    id="input-group-1"
                                    label="Identify Perturbations and Stresses"
                                    label-for="input-1"
                                    description=""
                            >
                                <b-card-text>What chronic and/or sudden stresses threaten your community's land, energy, and water resources?
                                </b-card-text>
                            </b-form-group>

                            <b-card-group deck>
                                <b-card header="Potential Perturbations">
                                    <div class="list-group">
                                        <li class="list-group-item" v-for="ps in perturbations" v-bind:key="ps.id">
                                            <label class="form-checkbox" :disabled="ps.readonly">
                                                <input type="checkbox" :value="ps.id"
                                                       v-model="selectedActions"
                                                       :disabled="ps.readonly"/>
                                                {{ps.name}}
                                            </label>
                                        </li>
                                    </div>
                                </b-card>

                                <b-card class="card-nb" header="Perturbations in the System Diagram">
                                    <!--<b-card no-body style="max-width: 20rem;" img-src="https://placekitten.com/380/200" img-alt="Image" img-top>-->
                                    <img src="./../../../../public/static/img/perturbations.svg" width="200" height="200" class="center"></img>
                                </b-card>

                            </b-card-group>

                        </b-form>
                    </b-col>
                </div>
            </b-card-text>
            <template v-slot:footer>
                <b-button @click="stepBackStartCSD" type="reset" class="btn-upload" variant="dark">Back</b-button>
                <b-button @click="step2CSD" type="submit" variant="success">Next</b-button>
            </template>
        </b-card>




    </b-card-group>
</template>

<script>
    import EventBus from './../../../event-bus';
    import NaturalSystems from './../../../../public/static/natural_systems.json';
    import SocietalDrivers from './../../../../public/static/societal_drivers.json';
    import Image1 from './../../../../public/static/img/Natural_systems.svg';
    import axios from 'axios';

    export default {

        name: 'CreateProject',

        data() {
            return {
                form: {
                    projectName: null,
                    description: null,
                    location: null,
                    latitude: null,
                    longtitude: null,
                    feedbackProvided: false
                },

                naturalsystems: NaturalSystems,
                societaldrivers: SocietalDrivers,

                tabIndex: 0,
                isStep1Active: true,
                isStep2Active: false,
                isStep1CSD: false,
                isStep2CSD: false,

                geojson_files: [],

                perturbations: [{id: "0", name: "Drought"},{id: "1", name: "Increase precipitation"},
                    {id: "2", name: "Wild fires"},{id: "3", name: "Decrease in total precipitation"},{id: "4", name: "Reduction of snow pack"}],
                perturbation: [{ text: 'Select One', value: null }, 'Surface Water Allocation', 'perturbation 1', 'perturbation 2', 'perturbation 3'],
                show: true
            }
        },

        mounted() {
        },

        methods: {
            handleFileChange(e) {
                //this.$emit('input', e.target.files[0])
                this.$emit('input', e.target.files[0])
            },

            addFiles(){
                this.$refs.files.click();
            },

            onSubmit(evt) {
                evt.preventDefault()
                alert(JSON.stringify(this.form))
            },

            createProjectAction() {

                const { utils } = AiravataAPI;
                utils.FetchUtils.post(
                    '/interactwel/api/projects/',
                    {
                        name: this.form.projectName,
                        description: this.form.description,
                        location: this.form.location,
                        latitude: this.form.latitude,
                        longtitude: this.form.longtitude,
                        feedbackProvided: this.form.feedbackProvided
                    })
                    .then(data => {
                        this.projects = data;
                    })
                    .catch(error => {
                        alert("Create the Projects. API error! " + error)
                    });

                this.isStep1Active = false;
                this.isStep2Active = true;
                return true
            },

            step2NextClicked() {
                this.isStep1Active = false;
                this.isStep2Active = false;
                return true
            },

            stepStartCSD() {
                this.isStep1Active = false;
                this.isStep2Active = false;
                this.isStep1CSD = true;
                return true
            },

            step2CSD() {
                this.isStep2Active = false;
                this.isStep1CSD = false;
                this.isStep2CSD = true;
                return true
            },

            stepBackStartCSD() {
                this.isStep2CSD = false;
                this.isStep1Active = false;
                this.isStep2Active = true;
                return true
            },

            step2BackClicked() {
                this.isStep1Active = true;
                this.isStep2Active = false;
                return true
            },

            handleFilesUpload(){
                let uploadedFiles = this.$refs.files.files;

                /*
                Adds the uploaded file to the files array
                */
                for( var i = 0; i < uploadedFiles.length; i++ ){
                    //console.log(uploadedFiles[i]);
                    this.geojson_files.push( uploadedFiles[i] );
                }
            },

            /*
                Removes a select file the user has uploaded
            */
            removeFile( key ){
                this.geojson_files.splice( key, 1 );
            },

            onReset(evt) {
                evt.preventDefault()
                // Reset our form values
                this.form.email = ''
                this.form.name = ''
                this.form.food = null
                this.form.checked = []
                // Trick to reset/clear native browser form validation state
                this.show = false
                this.$nextTick(() => {
                    this.show = true
                })
            }
        }

    }

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
    .map-container{
        height: 400px;
        overflow:auto;
    }
</style>

