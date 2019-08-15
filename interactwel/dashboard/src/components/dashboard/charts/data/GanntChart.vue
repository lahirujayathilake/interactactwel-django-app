<template>
    <div>
        <!--<line-chart :chart-data="data2" :options="options2" :width="600" :height="400"></line-chart>-->
        <horizontal-bar-chart :chart-data="data" :options="optionsdata" :width="5"
                              :height="3"></horizontal-bar-chart>
    </div>
</template>

<script>
    import HorizontalBarChart from "./../lib/HorizontalBarChart";
    import LineChart from "./../lib/LineChart";
    import chartjsPluginAnnotation from "chartjs-plugin-annotation";

    export default {
        name: 'gannt-chart',

        components: {
            HorizontalBarChart, LineChart
        },

        data() {
            return {
                data: {
                    labels: ["Farmer with Columbia river water rights", "Farmer with other surface water rights", "Farmer with groundwater rights"],
                    datasets: [
                        {
                            label: 'Business as usual',
                            data: [10, 30, 10],
                            backgroundColor: "#0f39de",
                            hoverBackgroundColor: "#286bde",
                            hoverBorderWidth: 0
                        },
                        {
                            label: 'Increase amount of SW',
                            data: [
                                {
                                    x: 23,
                                    y: "Farmer with other surface water rights"
                                }, {
                                    x: 35,
                                    y: "Farmer with other surface water rights"
                                },
                                {x: 25},
                            ],
                            backgroundColor: "#FFA000",
                            hoverBackgroundColor: "#FFCA28",
                            hoverBorderWidth: 0
                        },
                        {
                            label: 'Decrease amount of SW',
                            data: [
                                {
                                    x: 35,
                                    y: "Farmer with other surface water rights"
                                }, {
                                    x: 50,
                                    y: "Farmer with other surface water rights"
                                }, {
                                    x: 25
                                }
                            ],
                            backgroundColor: "#D32F2F",
                            hoverBackgroundColor: "#EF5350",
                            hoverBorderWidth: 0
                        },
                    ]
                },
                optionsdata: {
                    animation: {
                        duration: 10,
                    },
                    title: {
                        display: true,
                        text: 'Actions taken by each actor through time'
                    },
                    scales: {
                        xAxes: [{
                            stacked: true,
                            gridLines: {display: false},
                            scaleLabel: {
                                display: true,
                                labelString: 'Time'
                            },
                        }],
                        yAxes: [{
                            stacked: false,
                            scaleLabel: {
                                display: true,
                                labelString: 'Actors'
                            },
                        }],
                    }, // scales
                    legend: {display: true},
                    annotation: {
                        drawTime: 'afterDraw',
                        events: ['dblclick'],
                        /*annotations: [
                            {
                                type: 'box',
                                xScaleID: 'x-axis-0',
                                yScaleID: 'y-axis-0',
                                yMin: "Farmer with Columbia river water rights",
                                yMax: "Farmer with other surface water rights",
                                backgroundColor: 'rgba(96, 125, 139, 0.1)',
                                borderWidth: 0,
                                onDblclick: function (e) {
                                    console.log('Box', e.type, this);
                                }
                            },
                            {
                                type: 'box',
                                xScaleID: 'x-axis-0',
                                yScaleID: 'y-axis-0',
                                yMin: "Farmer with other surface water rights",
                                yMax: "Farmer with groundwater rights",
                                backgroundColor: 'rgba(96, 125, 139, 0.3)',
                                borderWidth: 0,
                                onDblclick: function (e) {
                                    console.log('Box', e.type, this);
                                }
                            }
                        ]*/
                    }
                },

                /*data2: {
                    labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
                    datasets: [{
                        label: "Farmer with Columbia river water rights",
                        backgroundColor: "#286bde",
                        borderColor: "#286bde",
                        borderJoinStyle: 'round',
                        borderWidth: 6,
                        pointRadius: 0,
                        data: [
                            'Increase amount of SW', 'Increase amount of SW', 'Increase amount of SW', 'Increase amount of SW', 'Increase amount of SW', 'Increase amount of SW', 'Increase amount of SW', 'Increase amount of SW', 'Increase amount of SW', 'Increase amount of SW', 'Increase amount of SW', 'Increase amount of SW' ],
                        steppedLine: true,
                        fill: false,
                    }, {
                        label: "Farmer with other surface water rights",
                        fill: false,
                        backgroundColor: "#dd434e",
                        borderColor: "#dd434e",
                        borderJoinStyle: 'round',
                        borderWidth: 6,
                        pointRadius: 0,
                        data: [
                            'Increase amount of CR', 'Decrease amount of GW', 'Decrease amount of GW', 'Decrease amount of GW', 'Decrease amount of GW', 'Decrease amount of GW', 'Decrease amount of GW','Decrease amount of GW','Decrease amount of GW','Decrease amount of GW','Decrease amount of GW','Decrease amount of GW'
                        ],
                        steppedLine: true,
                    }]
                },
                options2: {
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
                },*/
            }
        }
    }
</script>