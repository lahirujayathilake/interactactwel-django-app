<template>
    <div id="regionalSummary" class="card">

        <div class="card-header">Subbasin ID : {{subbasinID}}<span v-on:click="dismiss" class="close"><font-awesome-icon icon="times-circle"/>Close</span></div>
        <div class="card-body">
            <GChart :resizeDebounce="400"
                    type="BarChart"
                    :data="chartData"
                    :options="chartOptions"/>
        </div>
    </div>
</template>

<script>
    import {GChart} from 'vue-google-charts'
    import EventBus from './../../../event-bus';
    import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
    import { faTimesCircle } from '@fortawesome/free-solid-svg-icons'

    export default {
        name: 'regional_summary',

        components: {
            GChart,
        },

        data() {
            return {
                subbasinID : null,

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
                    width: 500,
                    legend: {position: 'top', maxLines: 3},
                    chartArea: {width: "400", height: "80%"}
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
        top: 20px;
        right:30px;
        z-index: 1000;
    }

    .close{
        font-size: 10px !important;
    }
</style>