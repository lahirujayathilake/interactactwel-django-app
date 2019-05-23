<template>
    <div>
        <chart :chart-data="datacollection" :width="5" :height="2"></chart>
    </div>
</template>
<script>
    import axios from 'axios';
    import Chart from "../../../chart";

    export default {
        name: 'NFertilizerGraph',
        components: {
            Chart
        },
        data() {
            return {
                datacollection: null,
                xLabels: [],
                BASIN_N_Fertilizer_Data: [],
            };
        },
        mounted() {
            var $this = this;
            axios.get("/BASIN_N_fertilizer_(kg_N)_data.json").then(function (response) {
                $this.BASIN_N_Fertilizer_Data = response.data;
                for (var i = 0; i < 10; i++) {
                    $this.xLabelsComputed($this.BASIN_N_Fertilizer_Data["Data Labels"][i]);
                }

            }).catch(function (error) {
                console.log(error);
            });

            this.fillData();
        },

        methods: {
            xLabelsComputed(v) {
                return this.xLabels.push(v);
            },

            fillData() {
                this.datacollection = {
                    labels: [
                        "2008",
                        "2009",
                        "2010"
                    ],
                    datasets: [
                        {
                            label: "CWGR",
                            backgroundColor: "#f87979",
                            data: [7.35, 48.18, 0]
                        },
                        {
                            label: "POTA",
                            backgroundColor: "#A5CC82",
                            data: [182, 134.1, 1691.96]
                        },
                        {
                            label: "OAK",
                            backgroundColor: "#7266ba",
                            data: [0, 0, 0]
                        },
                        {
                            label: "PEAS",
                            backgroundColor: "#ccb949",
                            data: [0, 0, 0]
                        },
                        {
                            label: "GRSG",
                            backgroundColor: "#2470cc",
                            data: [40.95, 191.58, 685.35]
                        },
                        {
                            label: "AGRL",
                            backgroundColor: "#12cc6c",
                            data: [11148.51, 38010.32, 8793.48]
                        },
                    ]
                };
            },
        }
    };
</script>