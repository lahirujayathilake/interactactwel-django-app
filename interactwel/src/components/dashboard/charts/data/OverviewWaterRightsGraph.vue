<template>
        <vertical-bar-chart :chart-data='datacollection' :options="options" :width="320" :height="400"></vertical-bar-chart>
</template>
<script>
    import axios from 'axios';
    import VerticalBarChart from "../lib/VerticalBarChart";
    import EventBus from '../../../../event-bus';
    
    export default {
        name: 'OverviewWaterRightsGraph',
        components: {
            VerticalBarChart
        },
        data() {
            return {
                planName: "Adaptation Plan 1",
                JSONData: null,
                datacollection: null,
                graphColors: [
                    "#3d71ff",
                    "#00b3eb",
                    "#61cf94"
                ],
                options: {
                    responsive: false,
                    title: {
                        display: true,
                        text: 'Total water rights volume (ac-ft)'
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
                                labelString: '(ac-ft)'
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
            axios.get("/static/interactwel/BASIN_Water_Rights_plans.json").then(response => {
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

            showChart: function (selectedPlan) {
                this.planName = selectedPlan;
            },

            getColor(i) {
                let color;
                color = this.graphColors[i];
                return color;
            },
        }
    };
</script>
