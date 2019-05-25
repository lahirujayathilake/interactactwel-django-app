<template>
    <div id="PopupContentReservoirs" class="card">
        <div class="card-header"><strong>{{ data.name }}</strong></div>
        <div class="card-body no-padding">
            <b-tabs card>
                <b-tab title="Info" active>
                    <div class="card-body">
                        <strong><u>Principal Spillway: </u></strong><br>
                        <strong>Volume: </strong>{{ data.spillway_vol}}<br>
                        <strong>Surface Area: </strong>{{ data.spillway_sfarea}}<br>
                        <br>
                        <strong><u>Emergency Principal Spillway: </u></strong><br>
                        <strong>Volume: </strong>{{ data.espillway_vol}}<br>
                        <strong>Surface Area: </strong>{{ data.espillway_sfarea}}<br>

                    </div>
                </b-tab>
                <b-tab title="Data">
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
        name: "PopupContentReservoirs",
        components: {
            GChart
        },
        props: {
            data: {
                name: String
            },
            pcpdata: {}
        },

        data(){
            return{
                chartOptions: {
                    chart: {
                        title: "Aveage monthly releases volume (ac-ft)",
                        subtitle: "Aveage monthly release volume (ac-ft)",
                    },
                    width: 500,
                    height: 250,
                    legend: {position: 'top', maxLines: 3},
                    chartArea: {width: "90%", height: "90%"}
                },
            }
        },

        computed: {
            jsonData() {
                var data = this.pcpdata[this.data.id];
                console.log(data)
                return data;
            },
        },
    };
</script>

<style>
    #PopupContentReservoirs {
        width: 500px;
        height: 300px;
        z-index: 1000;
    }

    .leaflet-popup-content {
        width: 500px;
    }

    .leaflet-popup-content-wrapper {
        width: 550px;
    }
</style>