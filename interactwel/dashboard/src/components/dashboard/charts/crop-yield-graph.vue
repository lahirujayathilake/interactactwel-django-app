<template>
    <div>
        <chart :chart-data='datacollection' :width="5" :height="3"></chart>
    </div>
</template>
<script>
    import axios from 'axios';
    import Chart from "../../../chart";

    export default {
        name: 'CropYieldGraph',
        components: {
            Chart
        },
        data() {
            return {
                datacollection: null,
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    scales: {
                        xAxes: [{ stacked: true }],
                        yAxes: [{ stacked: true }]
                    }
                }
            };
        },
        mounted() {

        },

        created(){
            axios.get("/static/BASIN_Crop_yield_(kg)_data.json").then(response => {
                this.buildDataCollection(response.data);
                });
        },

        methods: {
            buildDataCollection(data){
                this.datacollection = {};
                this.datacollection.labels = [];
                for (let legend in data.Legend) {
                    this.datacollection.labels.push(data.Legend[legend]);
                }

                this.datacollection.datasets = [];
                for (let dataIndex in data.Data){
                    let dataPoint = data.Data[dataIndex];
                    let dataset = {};
                    dataset.label = dataPoint.Name;
                    dataset.backgroundColor = this.getRandomColor();
                    dataset.data = [];
                    for(let dataValue in dataPoint.Data) {
                        dataset.data.push(dataPoint.Data[dataValue]);
                    }
                    this.datacollection.datasets.push(dataset);
                }
            },

            getRandomColor() {
                let letters = '0123456789ABCDEF';
                let color = '#';
                for (let i = 0; i < 6; i++) {
                    color += letters[Math.floor(Math.random() * 16)];
                }
                return color;
            }
        }
    };
</script>
