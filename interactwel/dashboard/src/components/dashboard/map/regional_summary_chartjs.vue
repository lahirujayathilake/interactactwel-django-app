<template>
    <div id="regionalSummary" class="card">

        <div class="card-header"><strong>Subbasin ID : {{subbasinID}}</strong><span v-on:click="dismiss" class="close"><font-awesome-icon icon="times-circle"/>Close</span></div>
        <div class="card-body no-padding">
            <b-tabs card>
                <b-tab title="Overview" active>
                    <div class="card-body">
                    <div id="chart_div1">
                    </div>
                        <!--<regional-waterrights-graph :subbasinID ="this.subbasinID"></regional-waterrights-graph>-->
                    <div id="chart_div2">
                    </div>
                    </div>
                </b-tab>
                <b-tab title="Water Rights">
                    <div class="card-body">
                        <div id="chart_div1">
                             <chart :chart-data="datacollectionwr" :options="optionswr" :width="5" :height="4"></chart>
                        </div>
                        
                        <div id="chart_div2">
                            
                        </div>
                    </div>
                </b-tab>
                
                <b-tab title="N fertilizer">
                    <div class="card-body">
                        
                    </div>
                </b-tab>
            </b-tabs>
        </div>
        </div>
    </div>
</template>

<script>
    import EventBus from './../../../event-bus';
    import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
    import { faTimesCircle } from '@fortawesome/free-solid-svg-icons';
    //import RegionalWRGraph from './../charts/regional-waterrights-graph.vue'
    import axios from 'axios';
    import Chart from "../../../chartPie";
    import 'chartjs-plugin-labels';

    export default {
        name: 'regional_summary',

        components: {
            Chart,
            //'regional-waterrights-graph': RegionalWRGraph,
        },

        data() {
            return {
                subbasinID : null,
                wrdata: null,
                
                datacollectionwr: null,
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
                $this.buildDataCollectionwr(response.data,$this.subbasinID);
            });
                
            })
        },

        created(){
            // axios.get("/static/BASIN_Irrigation_(acre-ft)_data.json").then(response => {
            //     this.buildDataCollectionwr(response.data);
            // });
        },

        computed:{
            jsonData() {
                var data = JSONData[this.subbasinID];

                return data;
            },
        },
        methods: {
            dismiss() {
                EventBus.$emit('CLOSE');
            },
            
            buildDataCollectionwr(data, subbasinID){
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
                    dataset.backgroundColor = ["#4e85eb","#eb4e4e","#186a3b"];
                    dataset.data = [];
                    for(let dataValue in dataPoint.Data) {
                        //dataset.data.label = $this.getColorwr(dataValue);
                        dataset.data.push(dataPoint.Data[dataValue]);
                    }
                    //console.log(dataset);
                    this.datacollectionwr.datasets.push(dataset);
                //}
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
    }

    #canvas{
        font-size: 15px;
        font-weight: bold;
    }

    .close{
        font-size: 15px !important;
    }

    .card-header{
        font-size: 17px;
    }

    #chart_div1{
    width: 350px;
    float: left;
    } 

    #chart_div2{
    width: 350px;
    float: right;
   
    } 
</style>