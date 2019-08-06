<template>
    <div class="card">
        <div class="card-header">
            <strong>Compare</strong>
        </div>
        <div class="card-body">
            <div class="row">
                <div class="col-6">
                    <div class="card-body">
                        Base line chart goes here
                    </div>
                </div>
                <div class="col-6">
                    <div class="card-body">
                        <div class="row">
                            <div class="col-4"><strong>Plan</strong></div>
                            <div class="col-8">
                                <div class="form-group">
                                    <select class="form-control form-control-sm" v-model="selected"
                                            @change="changeBasin">
                                        <option v-for="option in options" v-bind:key="option.value"
                                                v-bind:value="option.value">{{ option.text }}
                                        </option>
                                    </select>
                                </div>
                            </div>
                        </div>
                        <b-row>
                            <b-col lg="12">
                                chart goes here
                            </b-col>
                        </b-row>
                    </div>
                </div>
            </div>
        </div>
    </div>
    </div>
</template>

<script>

    export default {
        name: 'Compare',

        components: {},

        data() {
            return {
                options: [
                    {text: 'Adaptaion Plan 1', value: '1'},
                    {text: 'Adaptaion Plan: 2', value: '2'},
                    {text: 'Adaptaion Plan: 3', value: '3'},
                    {text: 'Adaptaion Plan: 4', value: '4'},
                    {text: 'Adaptaion Plan: 5', value: '5'}
                ],
                datacollection: null,
                optionsirr: {
                    responsive: true,
                    title: {
                        display: true,
                        text: 'Irrigation - Yearly totals per water source'
                    },
                    tooltips: {
                        mode: 'point',
                        intersect: false,
                    },
                    hover: {
                        mode: 'nearest',
                        intersect: true
                    },
                    scales: {
                        xAxes: [{
                            display: true,
                            stacked: false,
                            scaleLabel: {
                                display: true,
                                labelString: 'Years'
                            }
                        }],
                        yAxes: [{
                            display: true,
                            stacked: false,
                            scaleLabel: {
                                display: true,
                                labelString: 'acre-ft'
                            }
                        }]
                    }
                }
            };
        },
        computed: {
            jsonData() {
                return JSONData;
            },

            graphData() {
                var adaptationPlan = this.planName;

                return Object.keys(this.jsonData["Adaptation_plans"][adaptationPlan])
                    .map(key => {
                        return {
                            key: key,
                            value: this.jsonData["Adaptation_plans"][adaptationPlan][key]
                        };
                    })
                    .filter(d => {
                        if (this.selectedKeyList.findIndex(k => k === d.key) > -1) {
                            //console.log(this.selectedKeyList.findIndex(k => k === d.key) > -1);
                            return true;
                        } else {
                            return false;
                        }
                    });

            },
        },

        mounted() {
        },

        methods: {}

    }
</script>


<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>

    .chart-container {
        position: absolute;
        top: 30px;
        left: 30px;
        z-index: 1000;
        background-color: #4cae4c;
        height: auto;
        width: 750px;
        max-width: 750px !important;
    }

    .nav-pills .nav-link.active, .nav-pills .show > .nav-link {
        color: #fff;
        background-color: #4cae4c !important;
    }

    #sidebar .active {
        color: #FFF !important;
        background-color: #4cae4c;
        margin: 5px !important;
        border-radius: 5px;
    }

    .filter-options input {
        margin-left: 10px !important;
    }

    #graph {
        width: 750px;
        max-width: 750px !important;
    }
</style>
