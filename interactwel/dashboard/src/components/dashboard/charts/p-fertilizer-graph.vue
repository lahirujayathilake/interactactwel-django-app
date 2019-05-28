<template>
        <chart :chart-data='datacollection' :options="options" :width="600" :height="500"></chart>
</template>
<script>
    import axios from 'axios';
    import Chart from "../../../chart";
       import EventBus from './../../../event-bus';

    export default {
        name: 'PFertilizerGraph',
        components: {
            Chart
        },
        data() {
            return {
                planName: "Adaptation Plan 1",
                JSONData: null,
                datacollection: null,
                options: {
                    responsive: false,
                    title: {
                        display: true,
                        text: 'Amount of P fertilizer applied automatically in watershed'
                    },
                    legend: {
                        position: 'top',
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
                            display: true,
                            stacked: false,
                            scaleLabel: {
                                display: true,
                                labelString: 'kg_N'
                            }
                        }]
                    }
                }
            };
        },
        mounted() {
            let $this = this;
            EventBus.$on('CLICK_ITEM_SIDEBAR', function (planName) {
                $this.planName = planName;
                $this.buildDataCollection($this.JSONData, $this.planName);
            });

        },

        created(){
            axios.get("/static/BASIN_P_fertilizer_(kg_N)_data.json").then(response => {
                this.JSONData = response.data;
                this.buildDataCollection(this.JSONData, this.planName);
            });
        },

        methods: {
            buildDataCollection(data, adaptationPlan){
                this.datacollection = {};
                this.datacollection.labels = [];
                for (let legend in data.Legend) {
                    this.datacollection.labels.push(data.Legend[legend]);
                }

                this.datacollection.datasets = [];
                for (let dataIndex in data.Adaptation_plans[adaptationPlan]["Data"]) {
                    let dataPoint = data.Adaptation_plans[adaptationPlan]["Data"][dataIndex];
                    let dataset = {};
                    dataset.label = dataPoint.Name;
                    dataset.backgroundColor = this.getRandomColor();
                    dataset.data = [];
                    for (let dataValue in dataPoint.Data) {
                        dataset.data.push(dataPoint.Data[dataValue]);
                    }
                    this.datacollection.datasets.push(dataset);
                }
            },

            showChart: function (selectedPlan) {
                this.planName = selectedPlan;
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
