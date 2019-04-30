<template>
    <b-container class="bv-example-row chart-container">
        <b-row>
            <div id="sidebar" role="tablist">
                <div class="accordion-header" v-for="(key, value) in adaptationPlans" v-bind:key="key">
                    <b-nav header-tag="header" class="p-1" role="tab">
                        <b-nav-item class="list-header" v-on:click="showChart(value)" block href="#" v-b-toggle="value" variant="info">{{value}}</b-nav-item>
                    </b-nav>
                    <b-collapse :id="value" accordion="my-accordion" role="tabpanel">
                        <b-nav vertical class="w-100">
                            <b-nav-item v-on:click="showPlanGraph()" v-bind:class="{active: isPlanGraphActive}">Plans</b-nav-item>
                            <b-nav-item v-on:click="showCostGraph()" v-bind:class="{active: isCostGraphActive}">Cost</b-nav-item>
                        </b-nav>
                    </b-collapse>
                </div>
            </div>
            <div id="graph" class="card">
                <div class="card-header">
                    <strong>{{planName}}</strong>
                </div>
                <div v-show="planVisibility" id="plans" class="card-body">
                    <b-card no-body>
                        <b-tabs card>
                            <b-tab title="Actors" active>
                                <div class="card-body no-padding">
                                    <div class="filter-options-container">
                                        <div v-for="actor in actors" v-bind:key="actor.key"
                                             class="form-check form-check-inline filter-options" :style="{ 'background-color': pathColors[actor.key]}">
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
                            </b-tab>
                            <b-tab title="Actions">
                                <div class="card-body no-padding">
                                    <div class="filter-options-container">
                                        <div class="form-check form-check-inline filter-options" :style="{ 'background-color': '#999999'}">
                                            <input class="form-check-input"
                                                   type="checkbox">
                                            <label class="form-check-label small" for="">Business as Usual</label>
                                        </div>
                                        <div class="form-check form-check-inline filter-options" :style="{ 'background-color': '#999999'}">
                                            <input class="form-check-input"
                                                   type="checkbox">
                                            <label class="form-check-label small" for="">Increase capacity by 20%</label>
                                        </div>
                                        <div class="form-check form-check-inline filter-options" :style="{ 'background-color': '#999999'}">
                                            <input class="form-check-input"
                                                   type="checkbox">
                                            <label class="form-check-label small" for="">Decrease total capacity by 20%</label>
                                        </div>
                                        <div class="form-check form-check-inline filter-options" :style="{ 'background-color': '#999999'}">
                                            <input class="form-check-input"
                                                   type="checkbox">
                                            <label class="form-check-label small" for="">Increase amount of SW</label>
                                        </div>
                                        <div class="form-check form-check-inline filter-options" :style="{ 'background-color': '#999999'}">
                                            <input class="form-check-input"
                                                   type="checkbox">
                                            <label class="form-check-label small" for="">Increase amount of GW</label>
                                        </div>
                                    </div>
                                </div>
                                <div class="card-body">
                                    <MyChart :actions="actions" :data="graphData"></MyChart>
                                </div>
                            </b-tab>
                        </b-tabs>
                    </b-card>

                </div>
                <div v-show="!costVisibility" id="costs" class="card-body">Cost
                <div class="card-body">
                    <img class="img-fluid" src="../../../assets/cost-graph.png"/>
                </div>
                </div>
            </div>
        </b-row>
    </b-container>
</template>

<script>
    import JSONData from "../../../assets/result_action_plans.json";
    import MyChart from "./MyChart";

    export default {
        name: 'Charts',

        components: {
            'MyChart': MyChart
        },

        data() {
            return {
                colorIndex : 0,
                isPlanGraphActive: false,
                isCostGraphActive: false,
                planName: "POPSWAT_0",
                strokeColor: {
                    backgroundColor: "#16a085"
                },

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
                ],

                colors: [
                    {
                        id: 'ssmf',
                        hex: ['#297afb','#2898fb','#01d8fd'],
                        title: 'Sleek, Sophisticated, Mature & Formal'
                    },
                    {
                        id: 'hlfss',
                        hex: ['#297afb','#2898fb','#01d8fd'],
                        title: 'Honest, Loyal, Friendly, Stable, & Strong'
                    }]
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

            getPathColor(key) {
                const color = this.pathColors[key];
                backgroundColor:color;
                return backgroundColor;
            },

            showChart: function (selectedPlan) {
                this.planName = selectedPlan;
                showPlanGraph()
            },

            showCostGraph(){
                this.isCostGraphActive = true;
                this.isPlanGraphActive = false;
                this.costVisibility = false;
                this.planVisibility = false;
            },

            showPlanGraph(){
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
        /*top: 100px;
        left: 30px;*/
        z-index: 1000;
        background-color: #4cae4c;
        height: 400px;
        width: 800px;
        max-width: 1000px !important;
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

    #sidebar {
        width: 20%;
        background-color: #263238;
    }

    #graph {
        width: 80%;
    }

    #sidebar .collapse .nav-item{
        border-bottom: 1px solid #37474f !important;
    }

    #sidebar .collapse .nav-item a{
        color: rgba(255,255,255,0.8);
    }


    #sidebar .p-1 {
        border-bottom: 1px solid #263238 !important;
    }

    #sidebar .p-1:hover{
        background-color: #000;
        border-right:5px solid #4cae4c;
    }

    #sidebar .list-header a{
        color:#fff;
    }

    .accordion-header{
        border-bottom: 1px solid #ffffff4d;
    }
</style>