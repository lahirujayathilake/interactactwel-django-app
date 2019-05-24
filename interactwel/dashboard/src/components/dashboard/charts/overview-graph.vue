<template>
    <div id="graph" class="card">
        <div class="card-header">
            <strong>Overview</strong>
        </div>
        <div class="card-body no-padding">
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
                        <irridation-graph></irridation-graph>
                    </div>
                </b-tab>
                <b-tab title="Crop Area">
                    <div class="card-body">
                        <crop-area-graph></crop-area-graph>
                    </div>
                </b-tab>
                <b-tab title="Crop yield">
                    <div class="card-body">
                        <crops-yield-graph></crops-yield-graph>
                    </div>
                </b-tab>
            </b-tabs>
        </div>
    </div>
</template>

<script>
    import JSONData from "../../../assets/result_action_plans.json";
    import IrrigationGraph from './irrigation-graph.vue'
    import CropsGraph from './crops-graph.vue'
    import CropAreaGraph from './crop-area-graph.vue'
    import NFertilizerGraph from './n-fertilizer-graph.vue'
    import PFertilizerGraph from './p-fertilizer-graph.vue'

    export default {
        name: 'StreamsflowGraph',

        components: {
            'irridationGraph' : IrrigationGraph,
            'cropsYieldGraph' :CropsGraph,
            'cropAreaGraph' :CropAreaGraph,
            'nFertilizerGraph' :NFertilizerGraph,
            'pFertilizerGraph' :PFertilizerGraph,
        },

        data() {
            return {};
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

        methods: {},
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

    .active a {
        color: rgba(255, 255, 255, 0.8);
    }

    .active a:hover {
        color: #fff
    }

    .filter-options input {
        margin-left: 10px !important;
    }

    #graph{
        width: 900px;
        max-width: 830px !important;
    }
</style>