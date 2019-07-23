<template>
    <div>
   <!-- <horizontal-bar-chart :chart-data="datacollectionH" :options="optionsH"></horizontal-bar-chart>-->
    <line-chart :chart-data="datacollection" :options="options" :width="600" :height="400"></line-chart>
    </div>
</template>

<script>
    import HorizontalBarChart from "./../lib/HorizontalBarChart";
    import LineChart from "./../lib/LineChart";

    export default {
        name: 'gannt-chart',

        components: {
            HorizontalBarChart,LineChart
        },

        data() {
            return {
                datacollection: {
                    datasets: [
                        {

                            label: 'Action 0',
                            backgroundColor: "#dd434e",
                            borderColor: "#de3131",
                            fill: false,
                            borderWidth : 40,
                            pointRadius : 0,
                            data: [
                                {
                                    x: "Jan",
                                    y: "Increase amount of SW"
                                }, {
                                    x: "Feb",
                                    y: "Increase amount of SW"
                                }
                            ]
                        },
                        {

                            label: 'Action 1',
                            backgroundColor: "#0f9c31",
                            borderColor: "#0f9c31",
                            fill: false,
                            borderWidth : 40,
                            pointRadius : 0,
                            data: [
                                {
                                    x: "Jan",
                                    y: "Increase amount of SW"
                                }, {
                                    x: "Apr",
                                    y: "Increase amount of SW"
                                }
                            ]
                        },
                        {
                            label: 'Action 2',
                            backgroundColor: "#0f9c31",
                            borderColor: "#0f9c31",
                            fill: false,
                            borderWidth : 40,
                            pointRadius : 0,
                            data: [
                                {
                                    x: "Apr",
                                    y: "Increase amount of GW"
                                }, {
                                    x: "Jul",
                                    y: "Increase amount of GW"
                                }
                            ]
                        },
                        {

                            label: 'Action 3',
                            backgroundColor: "#0f9c31",
                            borderColor: "#0f9c31",
                            fill: false,
                            borderWidth : 40,
                            pointRadius : 0,
                            data: [
                                {
                                    x: "Jul",
                                    y: "Decrease amount of SW"
                                }, {
                                    x: "Sep",
                                    y: "Decrease amount of SW"
                                }
                            ]
                        },
                        {
                            label: 'Action 4',
                            backgroundColor: "#0f9c31",
                            borderColor: "#0f9c31",
                            fill: false,
                            borderWidth : 40,
                            pointRadius : 0,
                            data: [
                                {
                                    x: "Sep",
                                    y: "Decrease amount of SW"
                                }, {
                                    x: "Dec",
                                    y: "Decrease amount of SW"
                                }
                            ]
                        }
                    ],
                    labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
                },
                options: {
                    responsive: false,
                    legend : {
                        display : false
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
                            ticks : {
                                beginAtzero :true,
                                stepSize : 1
                            }
                        }],
                        yAxes : [{
                            type: 'category',
                            scaleLabel: {
                                display: true,
                                labelString: 'Actions'
                            },
                            ticks : {
                                beginAtZero :true,
                                max : 7
                            },
                            labels: ["Business as usual", "Increase amount of SW", "Decrease amount of SW", "Increase amount of GW", "Decrease amount of GW", "Increase amount of CR", "Decrease amount of CR"],
                        }]
                    }
                },

               /* datacollectionH: {
                    labels: ["1", "2", "3", "4"],

                    datasets: [
                        {
                            data: [50, 150, 300, 400, 500],
                            backgroundColor: "rgba(63,103,126,0)",
                            hoverBackgroundColor: "rgba(50,90,100,0)"
                        },
                        {
                            data: [100, 100, 200, 200, 100],
                            backgroundColor: ['red', 'green', 'blue', 'yellow'],
                        }
                    ]
                },
                optionsH: {
                    hover: {
                        animationDuration: 10
                    },
                    scales: {
                        xAxes: [
                            {
                                label: "Duration",
                                ticks: {
                                    beginAtZero: true,
                                    fontFamily: "'Open Sans Bold', sans-serif",
                                    fontSize: 11
                                },
                                scaleLabel: {
                                    display: false
                                },
                                gridLines: {},
                                stacked: true
                            }],
                        yAxes: [{
                            gridLines: {
                                display: false,
                                color: "#fff",
                                zeroLineColor: "#fff",
                                zeroLineWidth: 0
                            },
                            ticks: {
                                fontFamily: "'Open Sans Bold', sans-serif",
                                fontSize: 11
                            },
                            stacked: true
                        }]
                    },
                    legend: {
                        display: false
                    }
                }*/
            }
        }

    }
</script>