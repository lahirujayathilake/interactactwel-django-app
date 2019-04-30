<template>
    <l-map ref="myMap" :zoom="zoom" :center="center">
        <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>
        <l-marker :lat-lng="marker"></l-marker>
    </l-map>
</template>

<script>

    import {L, LMap, LTileLayer, LMarker} from 'vue2-leaflet';
    import axios from 'axios';

    export default {

        components: {
            'l-map': LMap,
            'l-tile-layer': LTileLayer,
            'l-marker': LMarker
        },

        name: 'Map',

        delete: L.Icon.Default.prototype._getIconUrl,

        L: L.Icon.Default.mergeOptions({
            iconRetinaUrl: require('leaflet/dist/images/marker-icon-2x.png'),
            iconUrl: require('leaflet/dist/images/marker-icon.png'),
            shadowUrl: require('leaflet/dist/images/marker-shadow.png')
        }),


        data() {
            return {
                geoJson: null,
                zoom: 10,
                maxZoom: 17,
                minZoom: 3,
                center: L.latLng(45.6735777, -118.8455003),
                url: 'https://stamen-tiles-{s}.a.ssl.fastly.net/terrain/{z}/{x}/{y}{r}.png',
                attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
                marker: L.latLng(45.6735777, -118.8455003),
                detectRetina: true,
            }
        },

        mounted (){
            this.loadJson();
        },

        methods: {

            loadJson() {

                axios.get('/basin.geojson').then(response => {
                    this.geoJson = response.data;
                });


                let Farm = null;
                //Farm = L.geoJSON().addData(this.geoJson);


            }
        }


    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
    @import '../../../static/vendor/Vue2Leaflet/leaflet.css';

    .leaflet-control-zoom{
        display:none;
    }

</style>