<template>
    <div>
        <line-chart :chart-data="datacollection" :options="options" :width="650" :height="400"></line-chart>
    </div>
</template>

<script>
    import axios from 'axios';
    import LineChart from "../lib/LineChart";
    import chartjsPluginAnnotation from "chartjs-plugin-annotation";
    import EventBus from '../../../../../event-bus';

    export default {
        name: 'actions-graph-stepped-lines',

        components: {
            LineChart
        },

        data() {
            return {
                planName: "Adaptation Plan 1",
                JSONData: null,
                datacollection: null,
                cr_data: null,

                options: {
                    responsive: false,
                    legend: {
                        display: true
                    },
                    title: {
                        display: false,
                        text: 'Actions taken by each actor through time'
                    },
                    scales: {
                        xAxes: [{
                            type: 'category',
                            position: 'bottom',
                            scaleLabel: {
                                display: true,
                                labelString: 'Time'
                            },
                            ticks: {
                                beginAtzero: false,
                                stepSize: 1
                            }
                        }],
                        yAxes: [{
                            type: 'category',
                            scaleLabel: {
                                display: true,
                                labelString: 'Actions'
                            },
                            ticks: {
                                beginAtZero: false,
                                max: 9
                            },
                            labels: ["Business as usual", "Increase amount of SW", "Decrease amount of SW", "Increase amount of GW", "Decrease amount of GW", "Increase amount of CR", "Decrease amount of CR"],
                        }]
                    }
                },
            }
        },
        mounted() {
            let $this = this;
            EventBus.$on('CLICK_ITEM_SIDEBAR', function (planName) {
                $this.planName = planName;
                $this.buildDataCollection($this.JSONData, $this.planName);
            });

        },

        created(){
            axios.get("/static/BASIN_Action_Plans.json").then(response => {
                this.JSONData = response.data;
                this.buildDataCollection(this.JSONData, this.planName);
            });
        },

        methods: {
            buildDataCollection(data, adaptationPlan){
                this.datacollection = {
                    labels: ["2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010"],
                    datasets: [{
                        label: "Farmers: Columbia River (CR)",
                        backgroundColor: "#186a3b",
                        borderColor: "#186a3b",
                        borderJoinStyle: 'round',
                        borderWidth: 6,
                        data: [
                                'Increase amount of SW','Increase amount of SW', 'Increase amount of SW', 'Increase amount of SW','Increase amount of CR','Increase amount of CR','Increase amount of CR','Business as usual','Business as usual','Business as usual'],
                        steppedLine: true,
                        fill: false,
                    },
                        {
                            label: "Farmers: Groundwater (GW)",
                            backgroundColor: "#286bde",
                            borderColor: "#286bde",
                            borderJoinStyle: 'round',
                            borderWidth: 6,
                            data: [
                                'Increase amount of CR', 'Increase amount of CR', 'Increase amount of CR', 'Increase amount of CR', 'Decrease amount of GW', 'Decrease amount of GW', 'Decrease amount of GW', 'Decrease amount of GW', 'Decrease amount of GW', 'Decrease amount of GW'],
                            steppedLine: true,
                            fill: false,
                        },
                        {
                        label: "Farmers: Surface water (SW)",
                        fill: false,
                        backgroundColor: "#dd434e",
                        borderColor: "#dd434e",
                        borderJoinStyle: 'round',
                        borderWidth: 6,
                        data: [
                            'Business as usual', 'Business as usual', 'Business as usual', 'Business as usual', 'Increase amount of SW', 'Increase amount of SW', 'Increase amount of SW','Increase amount of SW','Increase amount of CR','Increase amount of CR'],
                        steppedLine: true,
                    }]
                };



                //this.datacollection.labels = [];
                //this.cr_data = [];
                //for (let legend in data.Legend) {
                //    this.datacollection.labels.push(data.Legend[legend]);
                //}
                //this.datacollection.datasets = [];
                //let i= 0;
                //this.cr_data.datasets = [];

                this.datacollection.datasets[0].data =[];


                for (let dataIndex in data.Adaptation_plans[adaptationPlan]["Data"]) {
                    
                    let dataPoint = data.Adaptation_plans[adaptationPlan]["Data"][dataIndex];
                    let dataset = [];
                    //dataset.label = dataPoint.Name;
                    //dataset.backgroundColor = this.getColor(i++);
                    
                    //dataset.data = [];
                    if (dataIndex == 1){
                        //console.log(dataPoint);
                    for (let dataValue in dataPoint.Data) {
                        dataset.push(dataPoint.Data[dataValue]);
                    }
                    this.datacollection.datasets[0].data.push(dataset[0]);
                    console.log(this.datacollection.datasets[0].data);
                    }
                }
                //i++;
            }
        }
    };
</script>