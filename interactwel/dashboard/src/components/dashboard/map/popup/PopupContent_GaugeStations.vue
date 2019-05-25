<template>
<div id="PopupContentGaugeStations" class="card">
<div class="card-header"><strong>Weather station</strong></div>
    <div class="card-body no-padding">
    <b-tabs card>
        <b-tab title="Info" active>
        <div class="card-body">
            <strong>Name: </strong>{{ data.name }}<br>
            <strong>Data Availability: </strong> {{ data.data_Range}}<br>
            <strong>Observation Type: </strong>{{ data.obs_type}}<br>
            <strong>Num. of Precipitation Obs.: </strong>{{ data.num_flowobs}}<br>
            </div>
        </b-tab>
        <b-tab title="Overview">
        <div class="card-body">
        <div class="card-body">
                    <GChart :resizeDebounce="5" type="ColumnChart" :data="jsonData" :options="chartOptions"/>
                    </div>
                    </div>
        </b-tab>
    </b-tabs>
        </div>
        </div>

</template>

<script>
    import {GChart} from 'vue-google-charts';

    export default {
        name: "PopupContentGaugeStations",
        components: {
            GChart
        },
        props: {
            data: {
                name: String
            },
            pcpdata: {

            }
        },
        
    chartOptions: {
                chart: {
                    title: "Aveage monthly streamflow (cfs)",
                    subtitle: "Aveage monthly streamflow (cfs)",
                },
                width: 500,
                height: 250,
                legend: {position: 'top', maxLines: 3},
                chartArea: {width: "90%", height: "90%"}
                },
    computed:{
        jsonData() {
            var data = this.pcpdata[this.data.id];
            console.log(data)
            return data;
            },
        },
    };
</script>

<style>
#PopupContentGaugeStations {
    width: 500px;
    height: 300px;
    z-index: 1000;
}

.leaflet-popup-content{
    width: 500px;
}
.leaflet-popup-content-wrapper{
    width: 550px;
}
</style>