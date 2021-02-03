<template>
    <pie-chart :chart-data="datacollection" :options="options" :width="600" :height="400"></pie-chart>
</template>

<script>
    import axios from 'axios';
    import PieChart from "../lib/PieChart";

    export default {
        name: 'RegionalWRGraph',

        components: {
            PieChart
        },

        props: {
            subbasinID: String,
        },

        data() {
            return {
                datacollection: null,
                subbasinIDu: this.subbasinID,
                options: {
                    responsive: false,
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
                    this.datacollection.datasets.push(dataset);
                //}
            },
        }
    }
</script>