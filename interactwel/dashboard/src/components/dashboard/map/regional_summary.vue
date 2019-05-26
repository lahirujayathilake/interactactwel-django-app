<template>
    <div id="regionalSummary" class="card">
        <div class="card-header"><strong>Subbasin ID : {{subbasinID}}</strong><span v-on:click="dismiss" class="close"><font-awesome-icon
                icon="times-circle"/> Close</span></div>
        <div class="card-body no-padding">
            <b-tabs card>
                <b-tab title="N fertilizer" active>
                    <n-fertilizer-graph></n-fertilizer-graph>
                </b-tab>
                <b-tab title="P fertilizer">
                    <p-fertilizer-graph></p-fertilizer-graph>
                </b-tab>
                <b-tab title="Irrigation">
                    <irridation-graph></irridation-graph>
                </b-tab>
                <b-tab title="Crop Area">
                    <crop-area-graph></crop-area-graph>
                </b-tab>
                <b-tab title="Crop yield">
                    <crop-yield-graph></crop-yield-graph>
                    <!--<crops-yield-graph></crops-yield-graph>-->
                </b-tab>
            </b-tabs>
        </div>
    </div>
</template>

<script>
    import EventBus from './../../../event-bus';
    import {FontAwesomeIcon} from '@fortawesome/vue-fontawesome';
    import {faTimesCircle} from '@fortawesome/free-solid-svg-icons';
    import JSONData from "../../../assets/BASIN_Water_Rights.json";
    //import {Vs, d3Pie, d3Metric} from 'd3-vs';

    import IrrigationGraph from './../charts/irrigation-graph.vue'
    import CropAreaGraph from './../charts/crop-area-graph.vue'
    import CropYieldGraph from './../charts/crop-yield-graph.vue'
    import NFertilizerGraph from './../charts/n-fertilizer-graph.vue'
    import PFertilizerGraph from './../charts/p-fertilizer-graph.vue'


    export default {
        name: 'regional_summary',

        components: {
            'irridationGraph': IrrigationGraph,
            'cropAreaGraph': CropAreaGraph,
            'cropYieldGraph': CropYieldGraph,
            'nFertilizerGraph': NFertilizerGraph,
            'pFertilizerGraph': PFertilizerGraph,
        },

        data() {
            return {
                subbasinID: null,
                wrdata: null,

                WaterRigthData: {
                    "cols": [
                        {"id": "", "label": "Water Source", "pattern": "", "type": "string"},
                        {"id": "", "label": "Total Volume (acre-ft)", "pattern": "", "type": "number"}
                    ],
                    "rows": [
                        {"c": [{"v": "Water Source", "f": null}, {"v": 21664, "f": null}]},
                        {"c": [{"v": "Surface water", "f": null}, {"v": 14466, "f": null}]},
                        {"c": [{"v": "Columbia River", "f": null}, {"v": 2368, "f": null}]}
                    ]
                },

                d3WaterRigthData: [{"key": "Surface water", "value": 14466}, {
                    "key": "Groundwater",
                    "value": 2368
                }, {"key": "Columbia River", "value": 21664}],

                d3WaterRigthOptions: {
                    axisXLabel: "string",
                },

            };
        },

        mounted() {
            let $this = this;
            EventBus.$on('CREATE_REGION_SUMMARY', function (selectedBasinID) {
                $this.subbasinID = selectedBasinID;
            })
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
            //onChartReady(chart, google) {
            //const data = JSONData;
            //const data = new google.visualization.DataTable(this.WaterRigthData);
            //console.log(data['cols'])
            // const data = google.visualization.arrayToDataTable([['Task', 'Hours per Day'],
            //          ['Work', 11],
            //          ['Eat',  2],
            //          ['Commute',  2],
            //          ['Watch TV', 2],
            //          ['Sleep',    7]
            // ]);
            //console.log(data)
            // chart.draw(data, options);
            //},
        },
    };
</script>

<style>
    #regionalSummary {
        position: absolute !important;
        top: 40px;
        right: 50px;
        z-index: 1000;
    }

    .close {
        font-size: 15px !important;
    }

    .card-header {
        font-size: 17px;
    }

    #chart_div1 {
        width: 350px;
        float: left;
    }

    #chart_div2 {
        width: 350px;
        float: right;

    }

    #regionalSummary .card {
        width: 700px;
        max-width: 750px !important;
    }

    #regionalSummary .nav-item a{
        color: #28a645;
        text-decoration: none;
        font-weight: 500;
        background-color: transparent;
        font-size: 14px;
    }

    #regionalSummary .nav-item .nav-link.active{
        color: #5e6b7e;
        font-weight: 500;
        background-color: #FFFFFF;
        font-size: 14px;
        border-top:2px solid #28a645;
    }
</style>