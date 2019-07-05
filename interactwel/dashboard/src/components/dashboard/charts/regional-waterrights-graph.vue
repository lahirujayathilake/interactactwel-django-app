<template>
    <chart :chart-data="datacollection" :options="options" :width="10" :height="10"></chart>
</template>

<script>
    import axios from 'axios';
    import Chart from "../../../chartPie";

    export default {
        name: 'RegionalWRGraph',

        components: {
            Chart
        },

        props: {
            subbasinID: String,
        },

        data() {
            return {
                datacollection: null,
                subbasinIDu: this.subbasinID,
                options: {
                    responsive: true,
                    title: {
                        display: true,
                        text: 'Total water rights volume (ac-ft) by water source',
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
                        }],
                        yAxes: [{
                            display: true,
                        }]
                    }
                }
            };
        },

        mounted() {

        },

        created(){
                axios.get("/static/BASIN_Water_Rights.json").then(response => { 
                this.buildDataCollection(response.data,this.subbasinIDu);
            });
        },

        methods: {
            buildDataCollection(data, subbasinID){
                console.log(subbasinID);
                this.datacollection = {};
                this.datacollection.labels = [];
                for (let legend in data.Legend) {
                    this.datacollection.labels.push(data.Legend[legend]);
                }
                this.datacollection.datasets = [];
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
                    this.datacollection.datasets.push(dataset);
                //}
            },
        }
    }
</script>

<style>
    #regionalSummary {
        position: absolute !important;
        top: 40px;
        right: 50px;
        z-index: 1000;
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