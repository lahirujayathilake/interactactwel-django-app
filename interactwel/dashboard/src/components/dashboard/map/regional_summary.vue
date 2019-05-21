<template>
    <GChart :resizeDebounce="500"
            type="BarChart"
            :data="chartData"
            :options="chartOptions"
    />
</template>

<script>
    import { GChart } from 'vue-google-charts'

    export default {
        name: 'regional_summary',

        components: {
            GChart,
        },

        data() {
            return {
                chartData: [
                    ["Year", "Surface water", "Groundwater", "Columbia River"],
                    ["2008", 1664.97, 5427.46, 2412.1],
                    ["2009", 1687.5, 5353.44, 2328.64],
                    ["2010", 1653.23, 5868.54, 2327.24]
                ],
                chartOptions: {
                    chart: {
                        title: "Total Irrigation",
                        subtitle: "Irrigation: 2008-2010",
                    },
                    width:700,
                    chartArea: {  width: "400", height: "80%" }
                }
            };
        },

        methods: {
            close() {
                this.$emit('close');
            },
        },
    };
</script>