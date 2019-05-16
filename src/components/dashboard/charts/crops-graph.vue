<template>
    <GChart :resizeDebounce="500"
            type="BarChart"
            :data="chartData"
            :options="chartOptions"
    />
</template>

<script>
    import JSONData from "../../../assets/result_action_plans.json";
    import { GChart } from 'vue-google-charts'

    export default {
        name: 'CropsGraph',

        components: {
            GChart,
        },

        data() {
            return {
                    chartData: [
                            ['Crested Wheatgrass', 'Potato', 'Oak', 'Garden or Canning Peas', 'Grain Sorghum', 'Agricultural Land-Generic', 'Spring Canola-Polish', 'Spring Barley', 'Winter Wheat', 'Onion', 'Celery', 'Slender Wheatgrass', 'Wetlands-Non-Forested', 'Orchard', 'Bell Pepper', 'Eastern Gamagrass', 'Alfalfa','Western Wheatgrass', 'Corn', 'Sorghum Hay', 'Sweetpotato', 'Spring Wheat', 'Hay', 'Head Lettuce','Sweet Corn',{ role: 'annotation' } ],
                        ['2008', 82573.95, 61873.27, 1539608.51, 95688.8, 144604.26, 2694706.07, 843445.87, 14850424.78, 134840.35, 2780199.76, 24792.54, 222207.72,715169.67, 0, 49907.47, 190787120.12, 34302225.1, 15355557.62, 5499.29,68822.49,36447.29,2180468.22, 10208509.11,461105.45,''],
                        ['2009', 58765.5, 37596.97, 2088141.41, 54869.65, 55776.33, 2779259.8, 609319.26, 14681356.24, 28604.78, 2002433.5,25023.61, 217204.51, 96585.23, 4.1, 96136.4, 140139535.96, 27650419.33, 23060147.560000002, 	4925.93,171859.84,	133370.06,1259651.02,6337729.99,648344.14, ''],
                        ['2010', 62972.19, 420562.1, 1073763.05, 18350.12, 111001.2, 538192.26, 138652.8, 11421278.53, 0, 1409647.42, 24954.51, 119372.18, 704879.92,1.64, 13053.75, 199777453.9, 21984849.56, 	6493385.22,11195.85,27921.54, 15147.97,2904656.63,8295234.46,128238.04,'']

                    ],
                    chartOptions: {
                        chart: {
                            title: "Total yield of planted crops in watershed (kg)",
                            subtitle: "Total yield of planted crops in watershed (kg): 2008-2010",
                        },
                        width:700,
                        chartArea: {  width: "65%", height: "80%" },
                        legend: { position: 'right', maxLines: 3 },
                        bar: { groupWidth: '70%' },
                        isStacked: true
                    }
                };
        },
        computed: {
            jsonData() {
                return JSONData;
            },
        },

        mounted() {
        },

        methods: {},
        //props: ["jsonData"]
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