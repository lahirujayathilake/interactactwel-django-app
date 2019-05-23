<template>
    <div>
        <chart :chart-data='datacollection' :width="5" :height="2"></chart>
    </div>
</template>
<script>
    import axios from 'axios';
    import Chart from "../../../chart";

    export default {
        name: 'NFertilizerGraph',
        components: {
            Chart
        },
        data() {
            return {
                datacollection: null,
                xLabels: [],
            };
        },
        mounted() {
            this.fillData();
        },

        created(){
            axios.get("/BASIN_N_fertilizer_(kg_N)_data.json").then(response => {
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
                    dataset.label = dataIndex;
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
            },

            fillData() {
                this.datacollection = {
                    labels: [
                        "2008",
                        "2009",
                        "2010"
                    ],
                    datasets: [
                        {
                            label: "CWGR",
                            backgroundColor: "#f87979",
                            data: [7.35, 48.18, 0]
                        },
                        {
                            label: "POTA",
                            backgroundColor: "#A5CC82",
                            data: [182, 134.1, 1691.96]
                        },
                        {
                            label: "OAK",
                            backgroundColor: "#7266ba",
                            data: [0, 0, 0]
                        },
                        {
                            label: "PEAS",
                            backgroundColor: "#ccb949",
                            data: [0, 0, 0]
                        },
                        {
                            label: "GRSG",
                            backgroundColor: "#2470cc",
                            data: [40.95, 191.58, 685.35]
                        },
                        {
                            label: "AGRL",
                            backgroundColor: "#12cc6c",
                            data: [11148.51, 38010.32, 8793.48]
                        },
                    ]
                };
            },
        }
    };
</script>
