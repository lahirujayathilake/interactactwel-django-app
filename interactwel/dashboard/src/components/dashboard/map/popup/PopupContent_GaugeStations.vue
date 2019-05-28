<template>
    <div id="PopupContentGaugeStations" class="card">
        <div class="card-header"><strong>Gauge Station: <small>{{ data.name }}</small></strong></div>
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
                                <th>USGS ID</th>
                                <td><span class="badge badge-secondary">{{ data.id}}</span></td>
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
                                <td><span class="badge badge-secondary">{{ data.num_flowobs}}</span></td>
                            </tr>
                            </tbody>
                        </table>
                    </div>
                </b-tab>
                <b-tab title="Data">
                        <line-chart :chart-data="datacollection" :options="options" :width="5" :height="3"></line-chart>
                </b-tab>
            </b-tabs>
        </div>
</template>

<script>
    import axios from 'axios';
    import LineChart from '../../../../chartLine';

    export default {
        name: "PopupContentGaugeStations",
        components: {
            LineChart
        },
        props: {
            data: {},
            pcpdata: {}
        },

        data() {
            return {
                datacollection: null,
                options: {
                    responsive: true,
                    title: {
                        display: true,
                        text: 'Aveage monthly streamflow (cfs)'
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
                                labelString: 'Streamflow (cfs)'
                            }
                        }]
                    }
                }
            };
        },

        mounted() {

        },

        created() {
            axios.get("/static/streamflow_station_data.json").then(response => {
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
                    if (dataPoint.Name != this.data.id) {
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
    #PopupContentGaugeStations {
        width: 450px;
        height: auto;
        z-index: 1000;
    }

    #PopupContentGaugeStations .card-body{
        padding:0.5em;
    }

    .leaflet-popup-content {
        width: 450px;
    }

    .leaflet-popup-content-wrapper {
        width: 490px;
    }

    #PopupContentGaugeStations .nav-item a{
        color: #28a645;
        text-decoration: none;
        font-weight: 500;
        background-color: transparent;
        font-size: 14px;
    }

    #PopupContentGaugeStations .nav-item .nav-link.active{
        color: #5e6b7e;
        font-weight: 500;
        background-color: #FFFFFF;
        font-size: 14px;
        border-top:2px solid #28a645;
    }
</style>