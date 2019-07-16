<template>
    <div id="graph" class="card">
        <div class="card-header"><span v-on:click="dismiss" class="close"><font-awesome-icon
                icon="times-circle"/> Close</span>
            <strong>Region</strong>
        </div>
        <div class="card-body no-padding">
            <b-tabs card>
                <b-tab title="Water Rights" active>
                    <div class="card-body no-padding">
                        <overview-water-rights-graph></overview-water-rights-graph>
                    </div>
                </b-tab>
                <b-tab title="Crop yield">
                    <div class="card-body no-padding">
                        <crop-yield-graph></crop-yield-graph>
                    </div>
                </b-tab>
                <b-tab title="N fertilizer">
                    <div class="card-body no-padding">
                        <n-fertilizer-graph></n-fertilizer-graph>
                    </div>
                </b-tab>
                <b-tab title="P fertilizer">
                    <div class="card-body no-padding">
                        <p-fertilizer-graph></p-fertilizer-graph>
                    </div>
                </b-tab>
                <b-tab title="Irrigation">
                    <div class="card-body no-padding">
                        <irrigation-graph></irrigation-graph>
                    </div>
                </b-tab>
                <b-tab title="Groundwater Recharge">
                    <div class="card-body no-padding">
                        <img class="img-fluid" src="../../../assets/graph-placeholder2.png"/>
                    </div>
                </b-tab>

            </b-tabs>
        </div>
    </div>
</template>

<script>
    import JSONData from "../../../assets/result_action_plans.json";
    import IrrigationGraph from './data/IrrigationGraph.vue'
    import CropYieldGraph from './data/CropYieldGraph.vue'
    import NFertilizerGraph from './data/NFertilizerGraph.vue'
    import PFertilizerGraph from './data/PFertilizerGraph.vue'
    import OverviewWaterRightsGraph from './data/OverviewWaterRightsGraph.vue'
    import EventBus from './../../../event-bus';

    export default {
        name: 'Region',

        components: {
            'irrigationGraph' : IrrigationGraph,
            'cropYieldGraph' :CropYieldGraph,
            'nFertilizerGraph' :NFertilizerGraph,
            'pFertilizerGraph' :PFertilizerGraph,
            'overviewWaterRightsGraph' :OverviewWaterRightsGraph,
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

        methods: {
            dismiss() {
                EventBus.$emit('CLOSE');
            },
        },
        //props: ["jsonData"]

    }
</script>


<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>

</style>
