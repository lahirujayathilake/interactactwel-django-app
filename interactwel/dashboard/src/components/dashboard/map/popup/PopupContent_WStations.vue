<template>
    <div id="PopupContentWStations" class="card">
        <div class="card-header"><strong>Weather station : <small>{{ data.name }}</small></strong></div>
        <b-tabs card>
            <b-tab title="Info" active>
                <div class="card-body">
                    <table class="table table-borderless table-sm">
                        <tbody>
                        <tr>
                            <th>Name</th>
                            <td>{{ data.name}}</td>
                        </tr>
                        <tr>
                            <th>Data Availability</th>
                            <td><span class="badge badge-secondary">{{ data.data_Range}}</span></td>
                        </tr>
                        <tr>
                            <th>Observation Type</th>
                            <td><span class="badge badge-secondary">{{ data.obs_type}}</span></td>
                        </tr>
                        <tr>
                            <th>Num. of Precipitation Obs.</th>
                            <td><span class="badge badge-secondary">{{ data.num_Pobs}}</span></td>
                        </tr>
                        <tr>
                            <th>Num. of Temperature Obs.</th>
                            <td><span class="badge badge-secondary">{{ data.num_Tobs}}</span></td>
                        </tr>
                        </tbody>
                    </table>
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
    //import LineChart from '../../../../chartLine'

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
                        text: 'Average Monthly Precipitation'
                    },
                    legend: {
                        display: false,
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
                                labelString: 'Precipitation depth (mm)'
                            }
                        }]
                    }
                }
            };
        },

        mounted() {

        },

        created() {
            axios.get("/static/weather_station_data.json").then(response => {
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
                this.datacollection.title = jsonData["Data type"];
                this.datacollection.datasets = [];
                for (let dataIndex in jsonData.Data) {
                    let dataPoint = jsonData.Data[dataIndex];
                    if (dataPoint.Name != this.data.name) {
                        continue;
                    }
                    let dataset = {};
                    dataset.label = dataPoint.Name;
                    //dataset.backgroundColor = this.getRandomColor();
                    dataset.backgroundColor ='#4e85eb';
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
        font-size: 14px;
    }

    .leaflet-popup-content {
        width: 450px;
    }

    .leaflet-popup-content-wrapper {
        width: 490px;
    }

    #PopupContentWStations .nav-item a{
        color: #28a645;
        text-decoration: none;
        font-weight: 500;
        background-color: transparent;
        font-size: 14px;
    }

    #PopupContentWStations .nav-item .nav-link.active{
        color: #5e6b7e;
        font-weight: 500;
        background-color: #FFFFFF;
        font-size: 14px;
        border-top:2px solid #28a645;
    }

    #PopupContentWStations table{
        font-size:14px;
    }
</style>
