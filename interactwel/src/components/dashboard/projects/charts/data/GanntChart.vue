<template>
  <div>
    <line-chart
      :chart-data="datacollectionHHH"
      :options="optionsHHH"
      :width="687"
      :height="120"
    />
    <line-chart
      :chart-data="datacollectionHH"
      :options="optionsHH"
      :width="687"
      :height="120"
    />
    <line-chart
      :chart-data="datacollectionH"
      :options="optionsH"
      :width="700"
      :height="145"
    />
    <!--<horizontal-bar-chart :chart-data="data" :options="optionsdata" :width="5"
                              :height="3"></horizontal-bar-chart>-->

    <!--<horizontal-bar-chart :chart-data="datax" :options="optx" :width="5"
                              :height="3"></horizontal-bar-chart>-->
    <!-- <horizontal-bar-chart :chart-data="modelData" :options="modelOptions"></horizontal-bar-chart>-->
  </div>
</template>

<script>
import HorizontalBarChart from "./../lib/HorizontalBarChart";
import LineChart from "./../lib/LineChart";
//import chartjsPluginAnnotation from "chartjs-plugin-annotation";

export default {
  name: 'GanntChart',

  components: {
    HorizontalBarChart,
    LineChart,
  },

  data() {
    return {
      datacollection: null,

      datacollectionHHH: {
        labels: ["2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010"],

        datasets: [
          {

            label: 'Action 0',
            backgroundColor: "#dd434e",
            borderColor: "#de3131",
            fill: false,
            borderWidth: 20,
            pointRadius: 0,
            data: [
              {
                x: "2001",
                y: "Actor 1",
              }, {
                x: "2004",
                y: "Actor 1",
              },
            ],
          },
          {

            label: 'Action 1',
            backgroundColor: "#ff8905",
            borderColor: "#ff6a07",
            fill: false,
            borderWidth: 20,
            pointRadius: 0,
            data: [
              {
                x: "2004",
                y: "Actor 1.1",
              }, {
                x: "2008",
                y: "Actor 1.1",
              },
            ],
          },
          {

            label: 'Action 2',
            backgroundColor: "#8d0c0d",
            borderColor: "#640c0d",
            fill: false,
            borderWidth: 20,
            pointRadius: 0,
            data: [
              {
                x: "2008",
                y: "Actor 1.5",
              }, {
                x: "2010",
                y: "Actor 1.5",
              },
            ],
          },
        ],
      },

      optionsHHH: {
        responsive: false,
        legend: {
          display: false,
        },
        title: {
          display: false,
          text: 'Farmers: Surface water',
        },

        tooltips: {
          callbacks: {
            title: function(tooltipItem, datacollectionHHH) {
              return datacollectionHHH['labels'][tooltipItem[0]['index']];
            },
            label: function(tooltipItem, datacollectionHHH) {
              return datacollectionHHH['datasets'][0]['data'][tooltipItem['index']];
            },
          },
          backgroundColor: '#FFF',
          titleFontSize: 16,
          titleFontColor: '#0066ff',
          bodyFontColor: '#000',
          bodyFontSize: 14,
          displayColors: false,
        },

        /*tooltips: {
                        mode: 'nearest',
                        intersect: false,
                        axis: 'x',
                        position: 'nearest',
                    },*/
        scales: {
          xAxes: [{
            type: 'category',
            position: 'bottom',
            scaleLabel: {
              display: false,
              labelString: 'Time',
            },
            ticks: {
              display: false,
            },
          }],
          yAxes: [{
            gridLines: {
              display: false,
              color: "#fff",
              zeroLineColor: "#fff",
              zeroLineWidth: 0,
            },
            type: 'category',
            scaleLabel: {
              display: true,
              labelString: 'Farmers: SW',
            },
            ticks: {
              display: false,
            },
            labels: ["", "Actor 1", "Actor 1.1", "Actor 1.2", "Actor 1.3", "Actor 1.4", "Actor 1.5", "Actor 1.6", ""],
          }],
        },
        annotation: {
          drawTime: 'afterDraw',
          events: ['dblclick'],
          annotations: [
            {
              type: 'box',
              xScaleID: 'x-axis-0',
              yScaleID: 'y-axis-0',
              backgroundColor: 'rgba(96, 125, 139, 0.2)',
              borderColor: 'rgba(96, 125, 139, 0.3)',
              borderWidth: 1,
            },
          ],
        },
      },

      datacollectionHH: {
        labels: ["2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010"],

        datasets: [
          {

            label: 'Action 0',
            backgroundColor: "#ff8905",
            borderColor: "#ff6a07",
            fill: false,
            borderWidth: 20,
            pointRadius: 0,
            data: [
              {
                x: "2001",
                y: "Actor 1.1",
              }, {
                x: "2005",
                y: "Actor 1.1",
              },
            ],
          },
          {

            label: 'Action 1',
            backgroundColor: "#8d0c0d",
            borderColor: "#640c0d",
            fill: false,
            borderWidth: 20,
            pointRadius: 0,
            data: [
              {
                x: "2005",
                y: "Actor 1.5",
              }, {
                x: "2008",
                y: "Actor 1.5",
              },
            ],
          },
          {

            label: 'Action 2',
            backgroundColor: "#dd434e",
            borderColor: "#de3131",
            fill: false,
            borderWidth: 20,
            pointRadius: 0,
            data: [
              {
                x: "2008",
                y: "Actor 1",
              }, {
                x: "2010",
                y: "Actor 1",
              },
            ],
          },
        ],
      },

      optionsHH: {
        responsive: false,
        legend: {
          display: false,
        },
        title: {
          display: false,
          text: "Farmers: Groundwater (GW)",
        },
        tooltips: {
          mode: 'nearest',
          intersect: false,
          axis: 'x',
          position: 'nearest',
          callbacks: {
            label: function(tooltipItem, data) {
              let start = 0;
              for (var i = 0; i < tooltipItem.datasetIndex; i++) {
                start += data.datasets[i].data[tooltipItem.index];
              }
              return tooltipItem.yLabel;
            },
          },
        },
        scales: {
          xAxes: [{
            type: 'category',
            position: 'bottom',
            scaleLabel: {
              display: false,
              labelString: 'Time',
            },
            ticks: {
              display: false,
            },
          }],
          yAxes: [{
            gridLines: { display: false },
            type: 'category',
            scaleLabel: {
              display: true,
              labelString: 'Farmers: GW',
            },
            ticks: {
              display: false,
            },
            labels: ["", "Actor 1", "Actor 1.1", "Actor 1.2", "Actor 1.3", "Actor 1.4", "Actor 1.5", "Actor 1.6", ""],
          }],
        },
        annotation: {
          drawTime: 'afterDraw',
          events: ['dblclick'],
          annotations: [
            {
              type: 'box',
              xScaleID: 'x-axis-0',
              yScaleID: 'y-axis-0',
              backgroundColor: 'rgba(126, 50, 139, 0.2)',
              borderColor: 'rgba(126, 50, 139, 0)',
              borderWidth: 1,
            },
          ],
        },
      },

      datacollectionH: {
        labels: ["2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010"],

        datasets: [
          {

            label: 'Action 0',
            backgroundColor: "#8d0c0d",
            borderColor: "#640c0d",
            fill: false,
            borderWidth: 20,
            pointRadius: 0,
            data: [
              {
                x: "2001",
                y: "Actor 1.5",
              }, {
                x: "2004",
                y: "Actor 1.5",
              },
            ],
          },
          {

            label: 'Action 1',
            backgroundColor: "#fffd62",
            borderColor: "#fffd62",
            fill: false,
            borderWidth: 20,
            pointRadius: 0,
            data: [
              {
                x: "2004",
                y: "Actor 1.4",
              }, {
                x: "2010",
                y: "Actor 1.4",
              },
            ],
          },
        ],
      },

      optionsH: {
        responsive: false,
        legend: {
          display: false,
        },
        title: {
          display: false,
          text: 'Actions taken by each actor through time',
        },
        tooltips: {
          mode: 'nearest',
          intersect: false,
          axis: 'x',
          position: 'nearest',
          callbacks: {
            label: function(tooltipItem, data) {
              let start = 0;
              for (var i = 0; i < tooltipItem.datasetIndex; i++) {
                start += data.datasets[i].data[tooltipItem.index];
              }
              return tooltipItem.yLabel;
            },
          },
        },
        scales: {
          xAxes: [{
            type: 'category',
            position: 'bottom',
            scaleLabel: {
              display: false,
              labelString: 'Time',
            },
          }],
          yAxes: [{
            gridLines: { display: false },
            type: 'category',
            scaleLabel: {
              display: true,
              labelString: 'Farmers: CR',
            },
            ticks: {
              display: false,
            },
            labels: ["", "Actor 1", "Actor 1.1", "Actor 1.2", "Actor 1.3", "Actor 1.4", "Actor 1.5", "Actor 1.6", ""],
          }],
        },
        annotation: {
          drawTime: 'afterDraw',
          events: ['dblclick'],
          annotations: [
            {
              type: 'box',
              xScaleID: 'x-axis-0',
              yScaleID: 'y-axis-0',
              backgroundColor: 'rgba(126, 50, 139, 0.2)',
              borderColor: 'rgba(126, 50, 139, 0)',
              borderWidth: 1,
            },
          ],
        },
      },

      datax: {
        labels: ["1", "2", "3", "4"],

        datasets: [{
          data: [50, 150, 300, 400, 500],
          backgroundColor: "rgba(63,103,126,0)",
          hoverBackgroundColor: "rgba(50,90,100,0)",

        }, {
          data: [100, 100, 200, 200, 100],
          backgroundColor: ['red', 'green', 'blue', 'yellow'],
        }],
      },
      optx: {
        hover: {
          animationDuration: 10,
        },
        scales: {
          xAxes: [{
            label: "Duration",
            ticks: {
              beginAtZero: true,
              fontFamily: "'Open Sans Bold', sans-serif",
              fontSize: 11,
            },
            scaleLabel: {
              display: false,
            },
            gridLines: {
            },
            stacked: true,
          }],
          yAxes: [{
            gridLines: {
              display: false,
              color: "#fff",
              zeroLineColor: "#fff",
              zeroLineWidth: 0,
            },
            ticks: {
              fontFamily: "'Open Sans Bold', sans-serif",
              fontSize: 11,
            },
            stacked: true,
          }],
        },
        legend: {
          display: false,
        },
      },

      data: {
        datasets: [
          {
            label: 'Business as usual',
            data: [ 25, 35, 50],
            backgroundColor: "#0f39de",
            hoverBackgroundColor: "#286bde",
            hoverBorderWidth: 0,
          },
          {
            label: 'Increase amount of SW',
            data: [
              {
                x: 25,
                y: '',
              }, {
                x: 35,
                y: "Farmer with other surface water rights",
              },
              {x: 25},
            ],
            backgroundColor: "#FFA000",
            hoverBackgroundColor: "#FFCA28",
            hoverBorderWidth: 0,
          },
          {
            label: 'Decrease amount of SW',
            data: [10, 20, 20],
            backgroundColor: "#D32F2F",
            hoverBackgroundColor: "#EF5350",
            hoverBorderWidth: 0,
          },
        ],
      },
      optionsdata: {
        animation: {
          duration: 10,
        },
        title: {
          display: true,
          text: 'Actions taken by each actor through time',
        },
        tooltips: {
          mode: 'point',
          intersect: false,
        },
        scales: {
          xAxes: [{
            stacked: true,
            gridLines: {display: false},
            scaleLabel: {
              display: true,
              labelString: 'Time',
            },
            labels: ["2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010"],
          }],
          yAxes: [{
            type: 'category',
            stacked: false,
            scaleLabel: {
              display: true,
              labelString: 'Actors',
            },
            labels: ["Farmer with Columbia river water rights", "Farmer with other surface water rights", "Farmer with groundwater rights"],
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
        },
      },

      modelData: {
        labels: ["Job 1", "Job 2", "Job 3"],
        datasets: [{
          // first dataset for blank gab
          backgroundColor: "rgba(255,255,255,0)",
          hoverBackgroundColor: "rgba(255,255,255,0)",
          tooltipHidden: true,
          data: [100000, 300000, 500000], // one value for each job
        }, {
          // second dataset for real data (bar 1)
          backgroundColor: "#9dc6dd",
          hoverBackgroundColor: "#9dc6dd",
          tooltipHidden: false,
          data: [50000, 100000, 50000], // one value for each job
        }, {
          // third dataset for blank gab
          backgroundColor: "rgba(255,255,255,0)",
          hoverBackgroundColor: "rgba(255,255,255,0)",
          tooltipHidden: true,
          data: [100000, 0, 0], // one value for each job
        }, {
          // fourth dataset for real data (bar 2)
          backgroundColor: "#9dc6dd",
          hoverBackgroundColor: "#9dc6dd",
          tooltipHidden: false,
          data: [200000, 0, 0], // one value for each job
        }],
      },
      modelOptions: {
        hover: {
          animationDuration: 10,
        },
        scales: {
          xAxes: [{
            ticks: {
              userCallback: function(v) {
                return "hello";
              },
              beginAtZero: false,
            },
            scaleLabel: {
              display: false,
            },
            gridLines: {},
            stacked: true,
            labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"],
          }],
          yAxes: [{
            gridLines: {
              display: false,
              color: "#fff",
              zeroLineColor: "#fff",
              zeroLineWidth: 0,
            },
            stacked: true,
          }],
        },
        tooltips: {
          custom: function(tooltipModel) {
            // EXTENSION: filter is not enough! Hide tooltip frame
            if (!tooltipModel.body || tooltipModel.body.length < 1) {
              tooltipModel.caretSize = 0;
              tooltipModel.xPadding = 0;
              tooltipModel.yPadding = 0;
              tooltipModel.cornerRadius = 0;
              tooltipModel.width = 0;
              tooltipModel.height = 0;
            }
          },
          // Hide tooltips of blank gabs
          filter: function(tooltipItem, data) {
            return !data.datasets[tooltipItem.datasetIndex].tooltipHidden;
          },
          callbacks: {
            label: function(tooltipItem, data) {
              var start = 0;
              for (var i = 0; i < tooltipItem.datasetIndex; i++) {
                start += data.datasets[i].data[tooltipItem
                  .index];
              }
              return tooltipItem.xLabel;
            },
          },
        },
        legend: {
          display: false,
        },
        responsive: true,
        maintainAspectRatio: false,
      },

    };
  },

  methods: {
  },
};
</script>