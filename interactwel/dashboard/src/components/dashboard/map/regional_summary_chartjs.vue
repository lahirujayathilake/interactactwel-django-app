<template>
    <div id="regionalSummary" class="card">

        <div class="card-header"><strong>Subbasin ID : {{subbasinID}}</strong><span v-on:click="dismiss" class="close"><font-awesome-icon
                icon="times-circle"/> Close</span></div>
        <div class="card-body no-padding">
            <b-tabs card>
                <b-tab title="Overview" active>
                        <b-row>
                            <b-col>
                                <table class="table table-striped table-sm">
                                    <thead>
                                    <tr>
                                        <th>General Info</th>
                                        <th></th>
                                    </tr>
                                    </thead>
                                    <tbody>
                                    <tr>
                                        <td>Basin area (acres)</td>
                                        <td><span class="badge badge-secondary">{{ subbasinInfo[subbasinID].area}}</span></td>
                                    </tr>
                                    <tr>
                                        <td>Agricultural land (acres)</td>
                                        <td><span class="badge badge-secondary">{{ subbasinInfo[subbasinID].agrland}}</span></td>
                                    </tr>
                                    <tr>
                                        <td>Hydrologic response units (HRUs)</td>
                                        <td><span class="badge badge-secondary">{{ subbasinInfo[subbasinID].numHRUs}}</span></td>
                                    </tr>
                                    </tbody>
                                </table>
                            </b-col>
                            <b-col cols="7">
                                <chart-bar :chart-data="datacollectionlnd" :options="optionslnd" :width="5"
                                           :height="4"></chart-bar>
                            </b-col>
                        </b-row>
                        <!--<regional-waterrights-graph :subbasinID ="this.subbasinID"></regional-waterrights-graph>-->
                </b-tab>
                <b-tab title="Water Rights">
                        <b-row>
                            <b-col>
                                <chart-pie :chart-data="datacollectionwr" :options="optionswr" :width="5"
                                           :height="4"></chart-pie>
                            </b-col>
                            <b-col>
                                <chart-pie :chart-data="datacollectionirr" :options="optionsirr" :width="5"
                                           :height="4"></chart-pie>
                            </b-col>
                        </b-row>
                </b-tab>
                <b-tab title="Precipitation">
                    <div class="card-body">

                    </div>
                </b-tab>
            </b-tabs>
        </div>
    </div>
</template>

<script>
    import EventBus from './../../../event-bus';
    import {FontAwesomeIcon} from '@fortawesome/vue-fontawesome';
    import {faTimesCircle} from '@fortawesome/free-solid-svg-icons';
    //import RegionalWRGraph from './../charts/regional-waterrights-graph.vue'
    import axios from 'axios';
    import ChartPie from "../../../chartPie";
    import ChartBar from "../../../chartBarH";
    //import 'chartjs-plugin-labels';

    export default {
        name: 'regional_summary',

        components: {
            'chart-pie': ChartPie,
            'chart-bar': ChartBar,
            //'regional-waterrights-graph': RegionalWRGraph,
        },

        data() {
            return {
                subbasinID: null,
                wrdata: null,

                subbasinInfo: [
                    {id: "1", area: '94,090', numHRUs: '501', agrland: '1,022'},
                    {id: "2", area: '81,975', numHRUs: '582', agrland: '1,022'},
                    {id: "3", area: '146,020', numHRUs: '768', agrland: '1,022'},
                    {id: "4", area: '162,546', numHRUs: '821', agrland: '1,022'},
                    {id: "5", area: '70,672', numHRUs: '794', agrland: '1,022'}
                ],

                datacollectionwr: null,
                datacollectionirr: null,
                datacollectionlnd: null,
                optionswr: {
                    responsive: true,
                    title: {
                        display: true,
                        text: 'Total water rights volume (ac-ft) by water source',
                    },
                    labels: {
                        render: 'percentage',
                        precision: 2
                    },

                    tooltips: {
                        mode: 'point',
                        intersect: false,
                    },
                    hover: {
                        mode: 'nearest',
                        intersect: true
                    },
                    scales: {
                        xAxes: [{
                            display: false,
                        }],
                        yAxes: [{
                            display: false,
                        }]
                    }
                },
                optionsirr: {
                    responsive: true,
                    title: {
                        display: true,
                        text: 'Total area of irrigated land (acres) by water source',
                    },
                    labels: {
                        render: 'percentage',
                        precision: 2
                    },

                    tooltips: {
                        mode: 'point',
                        intersect: false,
                    },
                    hover: {
                        mode: 'nearest',
                        intersect: true
                    },
                    scales: {
                        xAxes: [{
                            display: false,
                        }],
                        yAxes: [{
                            display: false,
                        }]
                    }
                },
                optionslnd: {
                    responsive: true,
                    title: {
                        display: true,
                        text: 'Distribution of land use area (acre)',
                    },
                    legend: {
                        display: false,
                    },
                    labels: {
                        render: 'percentage',
                        precision: 2
                    },

                    tooltips: {
                        mode: 'point',
                        intersect: false,
                    },
                    hover: {
                        mode: 'nearest',
                        intersect: true
                    },
                    scales: {
                        xAxes: [{
                            display: true,
                            stacked: false,
                            scaleLabel: {
                                display: true,
                                labelString: 'Area (acres)'
                            }
                        }],
                        yAxes: [{
                            display: true,
                            stacked: false,

                        }]
                    }
                }
            };
        },

        mounted() {
            let $this = this;
            EventBus.$on('CREATE_REGION_SUMMARY', function (selectedBasinID) {
                $this.subbasinID = selectedBasinID;
                this.subbasinID = selectedBasinID;
                //console.log(this.subbasinID);
                axios.get("/static/BASIN_Water_Rights.json").then(response => {
                    $this.buildDataCollectionwr(response.data, $this.subbasinID);
                });

                axios.get("/static/BASIN_LandUse_chartjs.json").then(response => {
                    $this.buildDataCollectionlnd(response.data, $this.subbasinID);
                });

                axios.get("/static/BASIN_IrrLand_chartjs.json").then(response => {
                    $this.buildDataCollectionirr(response.data, $this.subbasinID);
                });

            })
        },

        created() {
            // axios.get("/static/BASIN_Irrigation_(acre-ft)_data.json").then(response => {
            //     this.buildDataCollectionwr(response.data);
            // });
        },

        computed: {
            jsonData() {
                var data = JSONData[this.subbasinID];

                return data;
            },
        },
        methods: {
            dismiss() {
                EventBus.$emit('CLOSE');
            },

            buildDataCollectionwr(data, subbasinID) {
                let $this = this
                this.datacollectionwr = {};
                this.datacollectionwr.labels = [];
                for (let legend in data.Legend) {
                    this.datacollectionwr.labels.push(data.Legend[legend]);
                }
                this.datacollectionwr.datasets = [];
                let dataIndex = subbasinID;
                //for (let dataIndex in data.Data){
                let dataPoint = data.Data[dataIndex];

                let dataset = {};
                dataset.label = dataPoint.Name;
                dataset.backgroundColor = ["#4e85eb", "#eb4e4e", "#186a3b"];
                dataset.data = [];
                for (let dataValue in dataPoint.Data) {
                    //dataset.data.label = $this.getColorwr(dataValue);
                    dataset.data.push(dataPoint.Data[dataValue]);
                }
                //console.log(dataset);
                this.datacollectionwr.datasets.push(dataset);
                //}
            },

            buildDataCollectionirr(data, subbasinID) {
                let $this = this
                this.datacollectionirr = {};
                this.datacollectionirr.labels = [];
                for (let legend in data.Legend) {
                    this.datacollectionirr.labels.push(data.Legend[legend]);
                }
                this.datacollectionirr.datasets = [];
                let dataIndex = subbasinID;
                //for (let dataIndex in data.Data){
                let dataPoint = data.Data[dataIndex];

                let dataset = {};
                dataset.label = dataPoint.Name;
                dataset.backgroundColor = ["#fca650", "#4e85eb", "#eb4e4e", "#186a3b"];
                dataset.data = [];
                for (let dataValue in dataPoint.Data) {
                    //dataset.data.label = $this.getColorwr(dataValue);
                    dataset.data.push(dataPoint.Data[dataValue]);
                }
                //console.log(dataset);
                this.datacollectionirr.datasets.push(dataset);
                //}
            },

            buildDataCollectionlnd(data, subbasinID) {
                let $this = this
                this.datacollectionlnd = {};
                this.datacollectionlnd.labels = [];
                for (let legend in data.Legend) {
                    this.datacollectionlnd.labels.push(data.Legend[legend]);
                }
                this.datacollectionlnd.datasets = [];
                let dataIndex = subbasinID;
                //for (let dataIndex in data.Data){
                let dataPoint = data.Data[dataIndex];

                let dataset = {};
                dataset.label = dataPoint.Name;
                dataset.backgroundColor = ["#073b4c", "#ef476f", "#3f7cff", "#ccd7c5", "#06d6a0", "#415a77", "#fca650", "#368bd3"];
                dataset.data = [];
                for (let dataValue in dataPoint.Data) {
                    dataset.data.push(dataPoint.Data[dataValue]);
                }
                //console.log(dataset);
                this.datacollectionlnd.datasets.push(dataset);
                //}
            },

            getRandomColor() {
                let letters = '0123456789ABCDEF';
                let color = '#';
                for (let i = 0; i < 6; i++) {
                    color += letters[Math.floor(Math.random() * 16)];
                }
                return color;
            },

        }
    };
</script>

<style>
    #regionalSummary {
        position: absolute !important;
        top: 40px;
        right: 50px;
        z-index: 1000;
        width: 700px;
    }

    #canvas {
        font-size: 15px;
        font-weight: bold;
    }

    .close {
        font-size: 15px !important;
    }

    .card-header {
        font-size: 17px;
    }

    .chart_div1 {
        width: 350px;
        float: left;
    }

    .chart_div2 {
        width: 350px;
        float: right;

    }

    #regionalSummary .nav-item a {
        color: #28a645;
        text-decoration: none;
        font-weight: 500;
        background-color: transparent;
        font-size: 14px;
    }

    #regionalSummary .nav-item .nav-link.active {
        color: #5e6b7e;
        font-weight: 500;
        background-color: #FFFFFF;
        font-size: 14px;
        border-top: 2px solid #28a645;
    }

    #regionalSummary table{
        font-size:12px;
    }
</style>