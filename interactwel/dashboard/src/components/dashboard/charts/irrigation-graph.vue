<template>
    <div>
    <chart :chart-data="datacollection" :width="5" :height="2"></chart>
    </div>
</template>

<script>
    import axios from 'axios';
    import Chart from "./lib/chart";

    export default {
        name: 'IrrigationGraph',

        components: {
            Chart
        },

        data() {
            return {
                datacollection: null,
            };
        },

        mounted() {
            this.fillData()
        },

        methods: {

            fillData() {
                this.datacollection = {
                    labels: [ "2008", "2009", "2010"],
                    datasets: [
                        {
                            label: "Surface Water",
                            backgroundColor: "#ff8c1c",
                            data: [1664.97, 1687.5, 1653.23]
                        },
                        {
                            label: "Groundwater",
                            backgroundColor: "#ccbf23",
                            data: [5427.46, 5353.44, 5868.54]
                        },

                        {
                            label: "Columbia River",
                            backgroundColor: "#4d45b0",
                            data: [2412.1, 2328.64, 2327.24]
                        }
                    ]
                };
            },
        }
    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>

    .chart-container {
        position: absolute;
        top: 30px;
        left: 30px;
        z-index: 1000;
        background-color: #4cae4c;
        height: auto;
        width: 800px;
        max-width: 830px !important;
    }

    .nav-pills .nav-link.active, .nav-pills .show > .nav-link {
        color: #fff;
        background-color: #4cae4c !important;
    }

    .chart-inner {
        position: absolute !important;
        width: 100% !important;
        bottom: 0 !important;
    }

    .filter-options-container {
        text-align: left;
    }

    .filter-options {
        padding: 10px;
        color: #FFFFFF;
        background-color: #EFEFEF;
        margin: 5px !important;
        border-radius: 5px;
    }

    #sidebar .active {
        color: #FFF !important;
        background-color: #4cae4c;
        margin: 5px !important;
        border-radius: 5px;
    }

    .active a {
        color: rgba(255, 255, 255, 0.8);
    }

    .active a:hover {
        color: #fff
    }

    .filter-options input {
        margin-left: 10px !important;
    }

    #graph .card {
        width: 800px;
        max-width: 830px !important;
    }
</style>