<template>
    <div id="graph" class="card">
        <div class="card-header">
            <strong>Streams</strong>
        </div>
        <div class="card-body no-padding">
            <b-tabs card>
                <b-tab title="Stream Flows" active>
                    <div class="card-body">
                        <img class="img-fluid" src="../../../assets/graph-placeholder.png"/>
                    </div>
                </b-tab>
                <b-tab title="Stream Temparature">
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

    export default {
        name: 'StreamsflowGraph',

        components: {
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

    #graph .card {
        width: 800px;
        max-width: 830px !important;
    }
</style>