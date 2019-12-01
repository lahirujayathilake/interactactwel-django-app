<template>
    <div id="graph" class="card">
        <div class="card-header">
            <span v-on:click="dismiss" class="close">Close</span>
            <div class="row">
                <div class="col-8"><strong>Sub-basins</strong></div>
                <div class="col-4"><div class="form-group">
                    <select class="form-control form-control-sm" v-model="selected" @change="changeBasin">
                        <option v-for="option in options" v-bind:key="option.value" v-bind:value="option.value">{{ option.text }}</option>
                    </select>
                </div></div>
            </div>
        </div>
        <div class="card-body no-padding">
            <b-tabs card>
                <b-tab title="Irrigation" active>
                    <div class="card-body">
                        <vertical-bar-chart :chart-data="datacollection" :options="optionsirr" :width="5"
                                    :height="3"></vertical-bar-chart>
                    </div>
                </b-tab>
                <b-tab title="Water Rights">
                    <div class="card-body">
                        <img class="img-fluid" src="../../../../assets/graph-placeholder.png"/>
                    </div>
                </b-tab>
                <b-tab title="Crop yield">
                    <div class="card-body">
                    <img class="img-fluid" src="../../../../assets/graph-placeholder.png"/>
                    </div>
                </b-tab>
                <b-tab title="Groundwater Recharge">
                    <div class="card-body">
                        <img class="img-fluid" src="../../../../assets/graph-placeholder.png"/>
                    </div>
                </b-tab>
                <b-tab title="N fertilizer">
                    <div class="card-body">
                        <img class="img-fluid" src="../../../../assets/graph-placeholder.png"/>
                    </div>
                </b-tab>
            </b-tabs>
        </div>
    </div>
</template>


<script>

    import EventBus from './../../../../event-bus';
    import axios from 'axios';
    import VerticalBarChart from "./lib/VerticalBarChart";

    export default {
        name: 'SubBasins',

        components: {
           VerticalBarChart
        },

        data() {
            return {
                selected: '1',
                selectedBasinID: '1',
                planName: 'Adaptation Plan 1',
                JSONData: null,
                options: [
                    {text: 'Sub-basin: 1', value: '1'},
                    {text: 'Sub-basin: 2', value: '2'},
                    {text: 'Sub-basin: 3', value: '3'},
                    {text: 'Sub-basin: 4', value: '4'},
                    {text: 'Sub-basin: 5', value: '5'}
                ],
                datacollection: null,
                graphColors: [
                    "#3d71ff",
                    "#00b3eb",
                    "#61cf94"
                ],
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
        computed: {},

        mounted() {
            let $this = this;
            EventBus.$on('CLICK_ITEM_SIDEBAR', function (planName) {
                $this.planName = planName;
                $this.buildDataCollection($this.JSONData, $this.planName, $this.selectedBasinID)
            });

        },

        created() {
            axios.get("/static/BASIN_Irrigation_basins_data.json").then(response => {
                this.JSONData = response.data;
                this.buildDataCollection(this.JSONData, this.planName, this.selectedBasinID);
            })
        },

        methods: {
            dismiss() {
                EventBus.$emit('CLOSE');
            },

            buildDataCollection(data, adaptationPlan, basinID) {
                this.datacollection = {};
                this.datacollection.labels = [];
                for (let legend in data.Legend) {
                    this.datacollection.labels.push(data.Legend[legend]);
                }
                this.datacollection.datasets = [];
                let i= 0;
                for (let dataIndex in data.Adaptation_plans[adaptationPlan][basinID]["Data"]) {
                    let dataPoint = data.Adaptation_plans[adaptationPlan][basinID]["Data"][dataIndex];
                    let dataset = {};
                    dataset.label = dataPoint.Name;
                    dataset.backgroundColor = this.getColor(i++);
                    dataset.data = [];
                    for (let dataValue in dataPoint.Data) {
                        dataset.data.push(dataPoint.Data[dataValue]);
                    }
                    this.datacollection.datasets.push(dataset);
                }
                i++;
            },

            getColor(i) {
                let color;
                color = this.graphColors[i];
                return color;
            },

            changeBasin() {
                this.selectedBasinID = this.selected;
                this.buildDataCollection(this.JSONData, this.planName, this.selectedBasinID)
            },
        },
        //props: ["jsonData"]

    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
