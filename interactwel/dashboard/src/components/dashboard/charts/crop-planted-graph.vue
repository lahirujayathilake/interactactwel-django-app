<template>
    <chart :chart-data="datacollection" :options="options" :width="5" :height="3"></chart>
</template>

<script>
    import axios from 'axios';
    import Chart from "../../../chart";

    export default {
        name: 'IrrigationGraph',

        components: {
            Chart
        },

        data() {
            return {
                datacollection: null,
                options: {
                    responsive: true,
                    title: {
                        display: true,
                        text: 'Irrigation - Yearly totals per water source'
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
                                labelString: 'Years'
                            }
                        }],
                              yAxes: [{
                                id: 'A',
                                type: 'linear',
                                position: 'left',
                                display: true,
                            stacked: false,
                            scaleLabel: {
                                display: true,
                                labelString: 'acre-ft'
                            }
                            }, {
                                id: 'B',
                                type: 'linear',
                                position: 'right',
                                gridLines:{display: false},
                                ticks: {
                                max: 10,
                                min: 0
                                }
                            }]

                    }
                }
            };
        },

        mounted() {

        },

        created(){
            axios.get("/static/BASIN_Irrigation_(acre-ft)_data.json").then(response => {
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
                    dataset.yAxisID = 'A';
                    dataset.backgroundColor = this.getRandomColor();
                    dataset.data = [];
                    for(let dataValue in dataPoint.Data) {
                        dataset.data.push(dataPoint.Data[dataValue]);
                    }
                    this.datacollection.datasets.push(dataset);
                }

                    let dataset = {};
                    dataset.label = 'TEST';
                    dataset.yAxisID = 'B';
                    dataset.backgroundColor = this.getRandomColor();
                    dataset.data = [1, 6, 3]
                    this.datacollection.datasets.push(dataset);

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
    }
</script>