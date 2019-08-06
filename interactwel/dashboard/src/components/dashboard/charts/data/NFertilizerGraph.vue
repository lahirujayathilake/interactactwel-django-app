<template>
    <vertical-bar-chart :chart-data='datacollection' :options="options" :width="300" :height="400"></vertical-bar-chart>
</template>
<script>
    import axios from 'axios';
    import VerticalBarChart from "../lib/VerticalBarChart";
    import EventBus from '../../../../event-bus';

    export default {
        name: 'NFertilizerGraph',
        components: {
            VerticalBarChart
        },
        data() {
            return {
                planName: "Adaptation Plan 1",
                JSONData: null,
                datacollection: null,
                graphColors: [
                    "#a500a8",
                    "#c900cc",
                    "#af00e9",
                    "#7500e9",
                    "#571ee9",
                    "#0f39de",
                    "#286bde",
                    "#5a7ede",
                    "#79b7fb",
                    "#56b3d3",
                    "#1999a1",
                    "#3aa16d",
                    "#69b079",
                    "#8dbf88",
                    "#aece9a",
                    "#ccddaf",
                    "#e7edc7",
                    "#fffee2",
                    "#f3e4ba",
                    "#ecc895",
                    "#e8aa76",
                    "#ffa600",
                    "#ff8905",
                    "#ff6a07",
                    "#dd434e",
                    "#de3131",
                    "#b72b39",
                    "#8d0c0d"
                ],
                options: {
                    responsive: false,
                    title: {
                        display: true,
                        text: 'Amount of N fertilizer applied automatically in watershed'
                    },
                    legend: {
                        display: true,
                        position: 'top',
                        labels: {
                            fontSize: 10,
                            boxWidth: 10

                        }
                    },
                    tooltips: {
                        mode: 'point',
                        intersect: false,
                    },
                    hover: {
                        mode: 'nearest',
                        intersect: false
                    },
                    scales: {
                        xAxes: [{
                            display: true,
                            stacked: true,
                            scaleLabel: {
                                display: true,
                                labelString: 'Years'
                            }
                        }],
                        yAxes: [{
                            display: true,
                            stacked: true,
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

        created() {
            axios.get("/static/BASIN_N_fertilizer_(kg_N)_data.json").then(response => {
                this.JSONData = response.data;
                this.buildDataCollection(this.JSONData, this.planName);
            });
        },

        methods: {
            buildDataCollection(data, adaptationPlan) {
                this.datacollection = {};
                this.datacollection.labels = [];
                for (let legend in data.Legend) {
                    this.datacollection.labels.push(data.Legend[legend]);
                }

                this.datacollection.datasets = [];
                let i= 0;
                for (let dataIndex in data.Adaptation_plans[adaptationPlan]["Data"]) {
                    let dataPoint = data.Adaptation_plans[adaptationPlan]["Data"][dataIndex];
                    let dataset = {};
                    dataset.label = dataPoint.Name;
                    dataset.backgroundColor = this.getColor(i++);
                    dataset.data = [];
                    for (let dataValue in dataPoint.Data) {
                        dataset.data.push(dataPoint.Data[dataValue]);
                    }
                    this.datacollection.datasets.push(dataset);
                }
                i++;
            },

            getColor(i) {
                let color;
                color = this.graphColors[i];
                return color;
            },
        }
    };
</script>
