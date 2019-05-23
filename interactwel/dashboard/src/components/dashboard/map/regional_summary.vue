<template>
    <div id="regionalSummary" class="card">

        <div class="card-header">Subbasin ID : {{subbasinID}}<span v-on:click="dismiss" class="close"><font-awesome-icon icon="times-circle"/>Close</span></div>
        <div class="card-body no-padding">
            <b-tabs card>
                <b-tab title="N fertilizer" active>
                <div class="card-body">
                <div id="chart_div">
            <GChart :resizeDebounce="500"
                    type="PieChart"
                    :data="pieData"
                    :options="chartOptions1"
                    @readay="onChartReady"/>
                    </div>
                    <div id="chart_div2">
                <GChart :resizeDebounce="500"
                    type="PieChart"
                    :data="pieData"
                    :options="chartOptions2"/>
                    </div>
                    </div>
                </b-tab>
                
                <b-tab title="N fertilizer" active>
                    <div class="card-body">
            <GChart :resizeDebounce="500"
                    type="BarChart"
                    :data="chartData"
                    :options="chartOptions"/>
                    </div>
                </b-tab>
                </b-tabs>
        </div>
        </div>
    </div>
</template>

<script>
    import {GChart} from 'vue-google-charts';
    import EventBus from './../../../event-bus';
    import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
    import { faTimesCircle } from '@fortawesome/free-solid-svg-icons';
    import JSONData from "../../../assets/BASIN_Water_Rights.json";
    import {Vs,d3Pie,d3Metric} from 'd3-vs';

    export default {
        name: 'regional_summary',

        components: {
            GChart,
            'd3-metric': d3Metric,
            'd3-pie': d3Pie,
        },

        data() {
            return {
                subbasinID : null,
                wrdata: null,
                pieData: [['Task', 'Hours per Day'],
                         ['Work', 11],
                         ['Eat',  2],
                         ['Commute',  2],
                         ['Watch TV', 2],
                         ['Sleep',    7]
                ],
                chartData: [
                    ["Year", "Surface water", "Groundwater", "Columbia River"],
                    ["2008", 1664.97, 5427.46, 2412.1],
                    ["2009", 1687.5, 5353.44, 2328.64],
                    ["2010", 1653.23, 5868.54, 2327.24]
                ],
                chartOptions: {
                    chart: {
                        title: "Total Irrigation",
                        subtitle: "Irrigation: 2008-2010",
                    },
                    width: 700,
                    height: 300,
                    legend: {position: 'top', maxLines: 3},
                    chartArea: {width: "80%", height: "80%"}
                },
                chartOptions1: {
                    chart: {
                        title: "Total Irrigation",
                        subtitle: "Irrigation: 2008-2010",
                    },
                    width: 350,
                    height: 300,
                    legend: {position: 'left', maxLines: 3},
                    chartArea: {width: "80%", height: "70%"}
                },
                chartOptions2: {
                    chart: {
                        title: "Total Irrigation",
                        subtitle: "Irrigation: 2008-2010",
                    },
                    width: 350,
                    height: 300,
                    legend: {position: 'rigth', maxLines: 3},
                    chartArea: {width: "80%", height: "70%"}
                }
            };
        },

        mounted() {
            let $this = this;
            EventBus.$on('CREATE_REGION_SUMMARY', function (selectedBasinID) {
                $this.subbasinID = selectedBasinID;
            })
        },
        computed:{
            jsonData() {
                const myObjStr = JSON.stringify(JSONData);
                console.log(myObjStr)
                return JSON.parse(JSONData);
            },
            adaptationPlans() {
                console.log(this.jsonData)
                var tempdata = this.jsonData
                return new google.visualization.DataTable(JSON.parse(JSONData));
            },
        },
        methods: {
            dismiss() {
                EventBus.$emit('CLOSE');
            },
            onChartReady(chart, google) {
                //this.wrdata = new google.visualization.DataTable(JSON.parse(JSONData));
                //console.log(wrdata)
                const data = google.visualization.arrayToDataTable([['Task', 'Hours per Day'],
                         ['Work', 11],
                         ['Eat',  2],
                         ['Commute',  2],
                         ['Watch TV', 2],
                         ['Sleep',    7]
                ]);
                console.log(data)
                chart.draw(data, options);
        },
        },
    };
</script>

<style>
    #regionalSummary {
        position: absolute !important;
        top: 80px;
        right: 50px;
        z-index: 1000;
    }

    .close{
        font-size: 15px !important;
    }

    #chart_div{
    width:350px;
    float:left;
    } 
    #chart_div2{
    width:350px;
    float:right;
   
    } 
</style>