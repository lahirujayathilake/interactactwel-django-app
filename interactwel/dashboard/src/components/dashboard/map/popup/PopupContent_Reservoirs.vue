<template>
    <div id="PopupContentReservoirs" class="card">
        <div class="card-header"><strong>Reservoir : {{ data.name }}</strong></div>
        <b-tabs card>
            <b-tab title="Info" active>
                <div class="card-body">
                    <strong><u>Principal Spillway: </u></strong><br>
                    <strong>Volume: </strong>{{ data.spillway_vol}}<br>
                    <strong>Surface Area: </strong>{{ data.spillway_sfarea}}<br>
                    <br>
                    <strong><u>Emergency Principal Spillway: </u></strong><br>
                    <strong>Volume: </strong>{{ data.espillway_vol}}<br>
                    <strong>Surface Area: </strong>{{ data.espillway_sfarea}}<br>

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
    import Chart from "../../../../chart";

    export default {
        name: "PopupContentReservoirs",
        components: {
            Chart
        },
        props: {
            data: {
                name: String
            },
            pcpdata: {}
        },

        data() {
            return {
                datacollection: null,
                options: {
                    responsive: true,
                    title: {
                        display: true,
                        text: 'Average monthly releases volume (ac-ft)'
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
                                labelString: 'ac-ft'
                            }
                        }]
                    }
                }
            };
        },

        mounted() {
            this.fillData();
        },

        methods: {
            fillData() {
                this.datacollection = {
                    labels: [
                        "Jan",
                        "Feb",
                        "Mar",
                        "Apr",
                        "May",
                        "Jun",
                        "Jul",
                        "Aug",
                        "Sep",
                        "Oct",
                        "Nov",
                        "Dec"],
                    datasets: [
                        {
                            label: 'Willow Creek Reservoir',
                            data: [0.0, 0.0, 0.0, 50.0, 375.0, 450.0, 625.0, 550.0, 400.0, 50.0, 0.0, 0.0],
                            backgroundColor: '#D6E9C6',
                        }
                    ]
                }
            },
        }
    };
</script>

<style>
    #PopupContentReservoirs {
        width: 450px;
        height: auto;
        z-index: 1000;
    }

    #PopupContentReservoirs .card-body{
        padding:0.5em;
    }

    .leaflet-popup-content {
        width: 450px;
    }

    .leaflet-popup-content-wrapper {
        width: 490px;
    }
</style>