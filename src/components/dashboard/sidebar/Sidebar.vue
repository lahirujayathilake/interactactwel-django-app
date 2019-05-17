<template>
    <div id="sidebar" role="tablist">
        <div v-for="(key, value) in adaptationPlans" v-bind:key="key">
            <b-nav header-tag="header" class="p-1" role="tab">
                <b-nav-item v-on:click="showChart(value)" block href="#" v-b-toggle="value" variant="info">{{value}}
                </b-nav-item>
            </b-nav>
            <b-collapse :id="value" accordion="my-accordion" role="tabpanel">
                <b-nav vertical class="w-100" v-for="chart in chartTypes">
                    <b-nav-item class="collapse-item" v-on:click="showGraph(chart.id)">{{chart.name}}</b-nav-item>
                </b-nav>
            </b-collapse>
        </div>
    </div>
</template>

<script>

    import JSONData from "../../../assets/result_action_plans.json";

    import EventBus from './../../../event-bus';

    export default {
        name: 'Sidebar',

        data() {
            return {
                isPlanGraphActive: false,
                isCostGraphActive: false,

                currentChart: null,

                chartTypes: [
                    /*{id:"actions-graph", name: "Actions"},*/
                    {id: "overview-graph", name: "Overview"},
                    {id: "fertilizer-graph", name: "Detailed"},
                    {id: "costs-graph", name: "Costs"},
                    {id: "streamsflow-graph", name: "Streams"},
                   /* {id: "crops-graph", name: "Crops"},*/
                    {id: "precipitation-graph", name: "Precipitation"},
                    /*{id: "irrigation-graph", name: "Irrigation"},*/
                    {id: "groundwater-graph", name: "Groundwater"},
                ]
            }


        },

        computed: {
            jsonData() {
                return JSONData;
            },
            adaptationPlans() {
                return this.jsonData["Adaptation_plans"]
            },
        },

        methods: {

            showChart(planName) {
                this.onClickSidebarItem(planName);
                this.currentChart = null;
            },

            showGraph(chart) {
                this.currentChart = chart;
                EventBus.$emit('CLICK_ITEM', this.currentChart);

            },

            showPlanGraph() {
                EventBus.$emit('CLICK_ITEM_PLAN');
            },

            showCostGraph() {
                EventBus.$emit('CLICK_ITEM_COST');
            },

            onClickSidebarItem(planName) {
                EventBus.$emit('CLICK_ITEM_SIDEBAR', planName);
            },

        }
    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
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

    #sidebar {
        background-color: #263238;
    }

    #sidebar .collapse .nav-item {
        border-bottom: 1px solid #37474f !important;
    }

    #sidebar .collapse .nav-item a {
        color: rgba(255, 255, 255, 0.8);
    }

    #sidebar .p-1 {
        border-bottom: 1px solid #37474f !important;
        font-size: 14px;
    }

    #sidebar .p-1:hover {
        background-color: #000;
        border-right: 5px solid #4cae4c;
    }

    #sidebar .list-header a {
        color: #fff;
    }

    #sidebar .collapse-item a{
        font-size: 12px;
        text-indent: 15px;
    }

    #sidebar .collapsing-section{
        background-color: #000;
    }

    #sidebar .nav-link:hover{
        background-color: #000 ;
    }

</style>