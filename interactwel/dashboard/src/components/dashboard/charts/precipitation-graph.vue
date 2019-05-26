<template>
    <div id="graph" class="card">
        <div class="card-header">
            <strong>Precipitation</strong>
        </div>
        <div class="card-body no-padding">
            <b-tabs card>
                <b-tab title="Total Precipitation" active>
                    <div class="card-body">
                        <img class="img-fluid" src="../../../assets/graph-placeholder.png"/>
                    </div>
                </b-tab>
                <b-tab title="Monthly Precipitation">
                    <div class="card-body">
                        <img class="img-fluid" src="../../../assets/graph-placeholder.png"/>
                    </div>
                </b-tab>
            </b-tabs>
        </div>
    </div>
</template>

<script>
    import JSONData from "../../../assets/result_action_plans.json";
    import MyChart from "./pathways-graph";

    import EventBus from './../../../event-bus';

    export default {
        name: 'PrecipitationGraph',

        components: {
            'MyChart': MyChart
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
