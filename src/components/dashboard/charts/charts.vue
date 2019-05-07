<template>
    <b-container class="bv-example-row chart-container">
        <b-row>
            <component v-bind:is="component=this.currentChartComponent"></component>
        </b-row>
        <b-row>
            <component v-bind:is="component='actions-graph'"></component>
        </b-row>
    </b-container>
</template>

<script>
    import JSONData from "../../../assets/result_action_plans.json";
    import MyChart from "./MyChart";
    import ActionsGraph from './actions-graph.vue'
    import StreamsflowGraph from './streamflow-graph.vue'
    import FertilizerGraph from './fertilizer-graph.vue'
    import CostGraph from './cost-graph.vue'
    import CropsGraph from './crops-graph.vue'
    import PrecipitationGraph from './precipitation-graph.vue'
    import IrrigationGraph from './irrigation-graph.vue'
    import GroudWaterGraph from './groudwater-graph.vue'

    import EventBus from './../../../event-bus';

    export default {
        name: 'Charts',

        components: {
            'MyChart': MyChart,
            'actions-graph': ActionsGraph,
            'streamsflow-graph': StreamsflowGraph,
            'fertilizer-graph': FertilizerGraph,
            'costs-graph': CostGraph,
            'crops-graph': CropsGraph,
            'precipitation-graph': PrecipitationGraph,
            'irrigation-graph': IrrigationGraph,
            'groundwater-graph': GroudWaterGraph,
        },

        data() {
            return {

                currentChartComponent: 'null',
                colorIndex : 0,
                isPlanGraphActive: false,
                isCostGraphActive: false,
                planName: "POPSWAT_0",
                selectedKeyList: [],

                costVisibility: true,
                planVisibility: true,

                pathColors: [
                    "#0176b8",
                    "#7b549c",
                    "#c73431",
                    "#d2701b",
                    "#219b9f",
                    "#d2a02f",
                    "#dc4b8a",
                    "#6ba629",
                    "#737478"
                ]
            };
        },
        computed: {
            jsonData() {
                return JSONData;
            },

            actions() {
                return this.jsonData["Actions_map"];
            },

            adaptationPlans() {
                return this.jsonData["Adaptation_plans"]
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
            actors() {
                return Object.keys(this.jsonData["Actors_map"]).map(key => {
                    return {
                        key: parseInt(key, 10) + 1,
                        value: this.jsonData["Actors_map"][key]
                    };
                });
            },

            actions1() {
                return Object.keys(this.jsonData["Actions_map"]).map(key => {
                    return {
                        key: parseInt(key, 10) + 1,
                        value: this.jsonData["Actions_map"][key]
                    };
                });
            }
        },

        mounted(){
            let $this = this;
            EventBus.$on('CLICK_ITEM_SIDEBAR', function (planName) {
                $this.showChart(planName);
            })
            EventBus.$on('CLICK_ITEM_PLAN', function () {
                $this.showPlanGraph();
            })
            EventBus.$on('CLICK_ITEM_COST', function () {
                $this.showCostGraph();
            })
            EventBus.$on('CLICK_ITEM', function (currentChartComponent) {
                $this.showGraph(currentChartComponent);
            })
        },

        methods: {
            inputChanged(event, item) {
                if (event.target.checked) {
                    this.selectedKeyList.push(event.target.value);
                    item.active = !item.active;

                } else {
                    const index = this.selectedKeyList.findIndex(
                        k => k === event.target.value
                    );
                    this.selectedKeyList.splice(index, 1);

                }
            },

            showChart: function (selectedPlan) {
                this.planName = selectedPlan;
            },

            showGraph: function (selectedChart) {
                this.currentChartComponent = selectedChart;
            },

            showCostGraph(){
                this.isCostGraphActive = true;
                this.isPlanGraphActive = false;
                this.costVisibility = false;
                this.planVisibility = false;
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
        width: 800px;
        max-width: 830px !important;
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
    .active a{
        color: rgba(255,255,255,0.8);
    }

    .active a:hover{
        color: #fff
    }

    .filter-options input {
        margin-left: 10px !important;
    }

    #graph .card {
        width: 800px;
        max-width: 830px !important;
    }
</style>