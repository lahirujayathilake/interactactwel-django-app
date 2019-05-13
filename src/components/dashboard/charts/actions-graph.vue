<template>
    <div id="graph" class="card">
        <b-card no-body>
            <div class="card-header">
                <strong>Actions</strong>
            </div>
            <div class="card-body">
                <div class="filter-options-container">
                    <div v-for="actor in actors" v-bind:key="actor.key"
                         class="form-check form-check-inline filter-options"
                         :style="{ 'background-color': pathColors[actor.key]}">
                        <input class="form-check-input"
                               type="checkbox"
                               :name="actor.value"
                               :value="actor.key"
                               :id="actor.key"
                               @change="inputChanged($event , actor)">
                        <label class="form-check-label small" :for="actor.key">{{actor.value}}</label>
                    </div>
                </div>
            </div>
            <div class="card-body">
                <MyChart :actions="actions" :data="graphData"></MyChart>
            </div>
        </b-card>
    </div>
</template>

<script>
    import JSONData from "../../../assets/result_action_plans.json";
    import MyChart from "./MyChart";
    import EventBus from './../../../event-bus';

    export default {
        name: 'ActionsGraph',

        components: {
            'MyChart': MyChart
        },

        data() {
            return {
                colorIndex: 0,
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

        mounted() {
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
                this.showPlanGraph()
            },

            showCostGraph() {
                this.isCostGraphActive = true;
                this.isPlanGraphActive = false;
                this.costVisibility = false;
                this.planVisibility = false;
            },

            showPlanGraph() {
                this.isPlanGraphActive = true;
                this.isCostGraphActive = false;
                this.costVisibility = true;
                this.planVisibility = true;
            }


            /*toggleActive: function(item) {
                item.active = !item.active;
            }*/
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
        width: 850px;
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
        width: 850px;
        max-width: 850px !important;
    }
</style>