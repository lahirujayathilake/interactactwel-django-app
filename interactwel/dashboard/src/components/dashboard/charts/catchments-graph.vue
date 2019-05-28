<template>
    <div id="graph" class="card">
        <div class="card-header"><span v-on:click="dismiss" class="close"><font-awesome-icon
                icon="times-circle"/> Close</span>
            <strong>Sub-basins</strong>
        </div>
        <div class="card-body no-padding">
            <select v-model="selected" @click="selectCatchment">
                <option v-for="option in options" v-bind:value="option.value">{{ option.text }}</option>
            </select>
            <!--<span>Sub-basin: {{ selected }}</span>-->

            <b-tabs card>
                <b-tab title="N fertilizer" active>
                    <div class="card-body">
                        <n-fertilizer-graph></n-fertilizer-graph>
                    </div>
                </b-tab>
                <b-tab title="P fertilizer">
                    <div class="card-body">
                        <p-fertilizer-graph></p-fertilizer-graph>
                    </div>
                </b-tab>
                <b-tab title="Irrigation">
                    <div class="card-body">
                        <chart-barv :chart-data="datacollectionirr" :options="optionsirr" :width="5" :height="3"></chart-barv>
                    </div>
                </b-tab>
                <b-tab title="Crop Area">
                    <div class="card-body">
                        <crop-area-graph></crop-area-graph>
                    </div>
                </b-tab>
                <b-tab title="Crop yield">
                    <div class="card-body">
                        <crop-yield-graph></crop-yield-graph>
                        <!--<crops-yield-graph></crops-yield-graph>-->
                    </div>
                </b-tab>
            </b-tabs>
        </div>
    </div>
</template>

<script>
    import JSONData from "../../../assets/result_action_plans.json";
    import IrrigationGraph from './irrigation-graph.vue'
    import CropAreaGraph from './crop-area-graph.vue'
    import CropYieldGraph from './crop-yield-graph.vue'
    import NFertilizerGraph from './n-fertilizer-graph.vue'
    import PFertilizerGraph from './p-fertilizer-graph.vue'
    import EventBus from './../../../event-bus';
    import axios from 'axios';
    import ChartBarV from "../../../chart";

    export default {
        name: 'CatchmentsGraph',

        components: {
            'irridationGraph' : IrrigationGraph,
            'cropAreaGraph' :CropAreaGraph,
            'cropYieldGraph' :CropYieldGraph,
            'nFertilizerGraph' :NFertilizerGraph,
            'pFertilizerGraph' :PFertilizerGraph,
            'chart-barv': ChartBarV,
        },
        
        selectedBasinID: '1',
        planName: 'Adaptation Plan 1',

        data() {
            return {
                selected: '1',
                selectedBasinID: '1',

                
            options: [
                { text: 'Sub-basin: 1', value: '1' },
                { text: 'Sub-basin: 2', value: '2' },
                { text: 'Sub-basin: 3', value: '3' },
                { text: 'Sub-basin: 4', value: '4' },
                { text: 'Sub-basin: 5', value: '5' }
                ],
            datacollectionirr:null,
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
            let $this = this;

            EventBus.$on('CLICK_ITEM_SIDEBAR', function (planName) {
                this.planName = planName;
            
            axios.get("/static/BASIN_Irrigation_basins_data.json").then(response => {
                //this.jsonData["Adaptation_plans"][adaptationPlan]
                var adaptationPlan = this.planName
                var selectedBasinID = this.selected
                
                //console.log(selectedBasinID);
                //console.log(response.data.Adaptation_plans.adaptationPlan);
                //console.log(this.planName);
                //debugger;
                $this.buildDataCollectionirr(response.data,adaptationPlan,selectedBasinID);
                })
            });

        },

        methods: {
            dismiss() {
                EventBus.$emit('CLOSE');
            },

            buildDataCollectionirr(data,adaptationPlan,selectedBasinID){
                //debugger;
                this.datacollectionirr = {};
                this.datacollectionirr.labels = [];
                for (let legend in data.Legend) {
                    this.datacollectionirr.labels.push(data.Legend[legend]);
                }

                this.datacollectionirr.datasets = [];
                for (let dataIndex in data.Adaptation_plans[adaptationPlan][selectedBasinID]["Data"]){
                    let dataPoint = data.Adaptation_plans[adaptationPlan][selectedBasinID]["Data"][dataIndex];
                    let dataset = {};
                    dataset.label = dataPoint.Name;
                    dataset.backgroundColor = this.getRandomColor();
                    dataset.data = [];
                    for(let dataValue in dataPoint.Data) {
                        dataset.data.push(dataPoint.Data[dataValue]);
                    }
                    this.datacollectionirr.datasets.push(dataset);
                }
            },

            
            selectCatchment() {
                this.selectedBasinID = this.selected
                console.log(this.selected)
            },
        },
        //props: ["jsonData"]
        
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

    .active a {
        color: rgba(255, 255, 255, 0.8);
    }

    .active a:hover {
        color: #fff
    }

    .filter-options input {
        margin-left: 10px !important;
    }

    #graph {
        width: 750px;
        max-width: 750px !important;
    }
</style>
