<template>
    <div id="graph" class="card">
        <div class="card-header">
            <strong>Compare</strong>
        </div>
        <div class="card-body">
            <div class="row">
                <div class="col-8"><strong>Sub-basins</strong></div>
                <div class="col-4"><div class="form-group">
                    <select class="form-control form-control-sm" v-model="selected" @change="changeBasin">
                        <option v-for="option in options" v-bind:key="option.value" v-bind:value="option.value">{{ option.text }}</option>
                    </select>
                </div></div>
            </div>
            <div class="row">
            <div class="col-6">
                <b-tabs card>
                    <b-tab title="Irrigation" active>
                        <div class="card-body">
                            <chart-barv :chart-data="datacollection" :options="optionsirr" :width="5"
                                        :height="3"></chart-barv>
                        </div>
                    </b-tab>
                </b-tabs>
            </div>
            <div class="col-6">
                <b-tabs card>
                    <b-tab title="Irrigation" active>
                        <div class="card-body">
                            chart goes here
                        </div>
                    </b-tab>
                </b-tabs>
            </div>
            </div>
        </div>
    </div>
</template>

<script>

    export default {
        name: 'Compare',

        components: {

        },

        data() {
            return {
                options: [
                    {text: 'Sub-basin: 1', value: '1'},
                    {text: 'Sub-basin: 2', value: '2'},
                    {text: 'Sub-basin: 3', value: '3'},
                    {text: 'Sub-basin: 4', value: '4'},
                    {text: 'Sub-basin: 5', value: '5'}
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

        methods: {
        }
        
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

    .chart-inner {
        position: absolute !important;
        width: 100% !important;
        bottom: 0 !important;
    }

    .filter-options-container {
        text-align: left;
    }

    .filter-options {
        padding: 10px;
        color: #FFFFFF;
        background-color: #EFEFEF;
        margin: 5px !important;
        border-radius: 5px;
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
