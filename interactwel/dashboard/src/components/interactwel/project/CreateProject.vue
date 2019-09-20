<template>
    <b-card-group>
        <b-card footer-tag="footer">
            <div class="step-header" slot="header">Create New Project
            </div>
            <b-card-text>
                <div class="p-3">
                    <b-col lg="6">
                        <b-form @submit="onSubmit" @reset="onReset" v-if="show">
                            <b-form-group
                                    id="input-group-1"
                                    label="Project Name"
                                    label-for="input-1"
                                    description=""
                            >
                                <b-form-input
                                        id="input-1"
                                        v-model="form.project"
                                        type="text"
                                        required
                                        placeholder=""
                                ></b-form-input>
                            </b-form-group>

                            <b-form-group id="input-group-2" label="Description" label-for="input-2">
                                <b-form-input
                                        id="input-2"
                                        v-model="form.description"
                                        required
                                        placeholder=""
                                ></b-form-input>
                            </b-form-group>

                            <b-form-group id="input-group-2" label="Location" label-for="input-2">
                                <b-form-input
                                        id="input-2"
                                        v-model="form.description"
                                        required
                                        placeholder=""
                                ></b-form-input>
                            </b-form-group>

                            <b-form-group id="input-group-2" label="Location" label-for="input-2">
                                <b-form-input
                                        id="input-2"
                                        v-model="form.creator"
                                        required
                                        placeholder=""
                                ></b-form-input>
                            </b-form-group>

                            <b-form-group id="input-group-3" label="Perturbation" label-for="input-3">
                                <b-form-select
                                        id="input-3"
                                        v-model="form.perturbation"
                                        :options="perturbation"
                                        required
                                ></b-form-select>
                            </b-form-group>

                            <b-form-group id="input-group-3" label="Who will get affected" label-for="input-3">
                                <b-form-select
                                        id="input-3"
                                        v-model="form.perturbation"
                                        :options="perturbation"
                                        required
                                ></b-form-select>
                            </b-form-group>

                            <b-form-group id="input-group-3" label="Natural Systems" label-for="input-3">
                                <b-form-select
                                        id="input-3"
                                        v-model="form.perturbation"
                                        :options="perturbation"
                                        required
                                ></b-form-select>
                            </b-form-group>

                            <b-form-group id="input-group-3" label="Societal Drivers" label-for="input-3">
                                <b-form-select
                                        id="input-3"
                                        v-model="form.perturbation"
                                        :options="perturbation"
                                        required
                                ></b-form-select>
                            </b-form-group>

                            <b-button type="submit" variant="success">Submit</b-button>
                            <b-button type="reset" class="mr-2" variant="dark">Reset</b-button>
                        </b-form>
                    </b-col>
                    <!--<b-card class="mt-3" header="Form Data Result">
                        <pre class="m-0">{{ form }}</pre>
                    </b-card>-->
                </div>
            </b-card-text>
        </b-card>
    </b-card-group>
</template>

<script>
    import EventBus from './../../../event-bus';

    export default {
        components: {

        },
        name: 'CreateProject',

        data() {
            return {
                form: {
                    email: '',
                    name: '',
                    food: null,
                    checked: []
                },
                perturbation: [{ text: 'Select One', value: null }, 'Surface Water Allocation', 'perturbation 1', 'perturbation 2', 'perturbation 3'],
                show: true
            }
        },

        mounted() {
        },

        methods: {
            onSubmit(evt) {
                evt.preventDefault()
                alert(JSON.stringify(this.form))
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
</style>

