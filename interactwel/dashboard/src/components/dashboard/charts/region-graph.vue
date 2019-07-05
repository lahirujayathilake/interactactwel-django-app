<template>
    <div id="graph" class="card">
        <div class="card-header"><span v-on:click="dismiss" class="close"><font-awesome-icon
                icon="times-circle"/> Close</span>
            <strong>Region</strong>
        </div>
        <div class="card-body no-padding">
            <b-tabs card>
                <b-tab title="P Fertilizer" active>
                    <div class="card-body">
                        <img class="img-fluid" src="../../../assets/graph-placeholder.png"/>
                    </div>
                </b-tab>
                <b-tab title="N Fertilizer">
                    <div class="card-body">
                        <img class="img-fluid" src="../../../assets/graph-placeholder.png"/>
                    </div>
                </b-tab>
                <b-tab title="Irrigation">
                    <div class="card-body">
                        <img class="img-fluid" src="../../../assets/graph-placeholder.png"/>
                    </div>
                </b-tab>
                <b-tab title="Crop Area">
                    <div class="card-body">
                        <img class="img-fluid" src="../../../assets/graph-placeholder.png"/>
                    </div>
                </b-tab>
                <b-tab title="Crop Yield">
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
    import EventBus from './../../../event-bus';

    export default {
        name: 'RegionGraph',

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

    #graph{
        width: 750px;
        max-width: 750px !important;
    }
</style>
