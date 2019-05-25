<template>
    <div id="PopupContentWStations" class="card">
        <div class="card-header"><strong>Weather station : {{ data.name }}</strong></div>
        <b-tabs card>
            <b-tab title="Info" active>
                <div class="card-body">
                    <strong>Name: </strong>{{ data.name }}<br>
                    <strong>Data Availability: </strong> {{ data.data_Range}}<br>
                    <strong>Observation Type: </strong>{{ data.obs_type}}<br>
                    <strong>Num. of Precipitation Obs.: </strong>{{ data.num_Pobs}}<br>
                    <strong>Num. of Temperature Obs.: </strong>{{ data.num_Tobs}}
                </div>
            </b-tab>
            <b-tab title="Data">
                <div class="card-body">
                    <chart :chart-data="datacollection" :options="options" :width="5" :height="3"></chart>
                </div>
            </b-tab>
        </b-tabs>
    </div>
</template>

<script>
    import axios from 'axios';
    import Chart from "../../../../chart";

    export default {
        name: "PopupContentWStations",
        components: {
            Chart
        },
        props: {
            data: {},
            pcpdata: {}
        },

        chartOptions: {
            chart: {
                title: "Aveage monthly precipitation depth (mm)",
                subtitle: "Aveage monthly precipitation depth (mm)",
            },
            width: 500,
            height: 250,
            legend: {position: 'top', maxLines: 3},
            chartArea: {width: "90%", height: "90%"}
        },

        data() {
            return {
                datacollection: null,
                options: {
                    responsive: true,
                    title: {
                        display: true,
                        text: 'Average Precipitation Depth'
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
                                labelString: 'Months'
                            }
                        }],
                        yAxes: [{
                            display: true,
                            stacked: false,
                            scaleLabel: {
                                display: true,
                                labelString: 'mm'
                            }
                        }]
                    }
                }
            };
        },

        mounted() {

        },

        created() {
            axios.get("/static/SUB_Irrigation_data.json").then(response => {
                this.buildDataCollection(response.data);
            });
        },

        methods: {
            buildDataCollection(jsonData) { //todo: need to move this method to an upper layer since it is getting called for each weather station
                this.datacollection = {};
                this.datacollection.labels = [];
                for (let legend in jsonData.Legend) {
                    this.datacollection.labels.push(jsonData.Legend[legend]);
                }

                this.datacollection.datasets = [];
                for (let dataIndex in jsonData.Data) {
                    let dataPoint = jsonData.Data[dataIndex];
                    if (dataPoint.Name != this.data.name) {
                        continue;
                    }
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

<style>
    #PopupContentWStations {
        width: 450px;
        height: auto;
        z-index: 1000;
    }

    #PopupContentWStations .card-body{
        padding:0.5em;
    }

    .leaflet-popup-content {
        width: 450px;
    }

    .leaflet-popup-content-wrapper {
        width: 490px;
    }
</style>
