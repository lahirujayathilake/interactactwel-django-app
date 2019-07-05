<template>
    <div id="regionalSummary" class="card">

        <div class="card-header">Subbasin ID : {{subbasinID}}<span v-on:click="dismiss" class="close"><font-awesome-icon icon="times-circle"/>Close</span></div>
        <div class="card-body no-padding">
            <b-tabs card>
                <b-tab title="N fertilizer" active>
                <div class="card-body">
                <d3-pie
                :data="d3data"
                width="100%"
                height="400px">
                </d3-pie>
                    </div>
                </b-tab>
                
                <b-tab title="N fertilizer" active>
                    <div class="card-body">
            <GChart :resizeDebounce="400"
                    type="BarChart"
                    :data="chartData"
                    :options="chartOptions"/>
                    </div>
                </b-tab>
                </b-tabs>
        </div>
        </div>
    </div>
</template>

<script>
    import {GChart} from 'vue-google-charts';
    import EventBus from './../../../event-bus';
    import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
    import { faTimesCircle } from '@fortawesome/free-solid-svg-icons';
    import {Vs, d3Pie} from 'd3-vs';
    //Vue.use(Vs);

    export default {
        name: 'regional_summary',

        components: {
            GChart,
        },

        data() {
            return {
                subbasinID : null,
                d3data: [{"label":"one", "value":20}, 
                        {"label":"two", "value":50}, 
                        {"label":"three", "value":30}],

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
                    width: 700,
                    height: 300,
                    legend: {position: 'top', maxLines: 3},
                    chartArea: {width: "100%", height: "80%"}
                }
            };
        },

        mounted() {
            let $this = this;
            EventBus.$on('CREATE_REGION_SUMMARY', function (selectedBasinID) {
                $this.subbasinID = selectedBasinID;
            })
        },

        methods: {
            dismiss() {
                EventBus.$emit('CLOSE');
            },
        },
    };
</script>

<style>
    #regionalSummary {
        position: absolute !important;
        top: 80px;
        right: 50px;
        z-index: 1000;
    }

    .close{
        font-size: 15px !important;
    }
</style>