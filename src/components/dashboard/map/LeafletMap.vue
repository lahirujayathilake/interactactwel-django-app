<template>
    <l-map ref="myMap" :zoom="zoom" :center="center">
        <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>
        <l-geo-json
                v-if="show"
                :geojson="geoJson2"
                :options="options"
                :options-style="styleFunction"
        />
        <l-geo-json
                v-if="show"
                :geojson="geoJson"
                :options="options"
                :options-style="styleFunction"
        />
        <l-marker :lat-lng="marker"></l-marker>
    </l-map>
</template>

<script>

    import {L, LMap, LTileLayer, LMarker, LGeoJson} from 'vue2-leaflet';
    import axios from 'axios';

    export default {

        components: {
            'l-map': LMap,
            'l-tile-layer': LTileLayer,
            'l-marker': LMarker,
            'l-geo-json': LGeoJson
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
                geoJson2: null,
                zoom: 10,
                maxZoom: 17,
                minZoom: 3,
                center: L.latLng(45.4435777, -119.9455003),
                url: 'https://stamen-tiles-{s}.a.ssl.fastly.net/terrain/{z}/{x}/{y}{r}.png',
                attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
                marker: L.latLng(45.6735777, -118.8455003),
                detectRetina: true,
                enableTooltip: true,
                loading: true,
                show: true,
                fillColor: "rgba(76, 175, 80, 0.44)"
            }
        },

        computed: {
            options() {
                return {
                    onEachFeature: this.onEachFeatureFunction
                };
            },
            styleFunction() {
                const fillColor = this.fillColor; // important! need touch fillColor in computed for re-calculate when change fillColor
                return () => {
                    return {
                        weight: 2,
                        color: "#3386ff",
                        opacity: 1,
                        fillColor: fillColor,
                        fillOpacity: 1
                    };
                };
            },

            onEachFeatureFunction() {
                if (!this.enableTooltip) {
                    return () => {
                    };
                }

                return (feature, layer) => {
                    layer.bindTooltip(
                        "<div>tooltip :)</div>",
                        {permanent: false, sticky: true}
                    );
                    layer.on({
                        click: this.layerClicked
                    });
                };
            }
        },

        created() {
            this.loading = true;
            axios.get("/reaches.geojson")
                .then(response => {
                    this.geoJson = response.data;
                    this.loading = true;
                    })

            axios.get("/subbasins.geojson")
                .then(response => {
                    this.geoJson2 = response.data;
                    this.loading = true;
                });

        },
        methods: {

            layerClicked() {
                alert("clicked me ;)");
            }

        }
    };
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
    @import '../../../static/vendor/Vue2Leaflet/leaflet.css';

    .leaflet-control-zoom {
        display: none;
    }

</style>