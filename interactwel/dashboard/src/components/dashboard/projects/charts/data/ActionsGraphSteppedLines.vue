<template>
    <div>
        <line-chart :chart-data="data" :options="options" :width="600" :height="400"></line-chart>
    </div>
</template>

<script>
    import LineChart from "./../lib/LineChart";
    import chartjsPluginAnnotation from "chartjs-plugin-annotation";

    export default {
        name: 'actions-graph-stepped-lines',

        components: {
            LineChart
        },

        data() {
            return {

                data: {
                    labels: ["2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010"],
                    datasets: [{
                        label: "Farmers: Columbia River (CR)",
                        backgroundColor: "#186a3b",
                        borderColor: "#186a3b",
                        borderJoinStyle: 'round',
                        borderWidth: 6,
                        data: [
                            'Increase amount of SW', 'Increase amount of SW', 'Increase amount of SW', 'Increase amount of SW', 'Increase amount of CR', 'Increase amount of CR', 'Increase amount of CR', 'Business as usual', 'Business as usual', 'Business as usual'],
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
                },
                options: {
                    responsive: true,
                    legend: {
                        display: true
                    },
                    title: {
                        display: true,
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
                                max: 7
                            },
                            labels: ["Business as usual", "Increase amount of SW", "Decrease amount of SW", "Increase amount of GW", "Decrease amount of GW", "Increase amount of CR", "Decrease amount of CR"],
                        }]
                    }
                },
            }
        }
    }
</script>