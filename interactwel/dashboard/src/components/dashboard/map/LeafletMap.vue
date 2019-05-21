<template>
    <l-map ref="myMap" :zoom="zoom" :center="center">
        <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>
        <l-control-layers position="topleft" ref="layersControl" :sort-layers="true">
        </l-control-layers>
        <l-layer-group layer-type="overlay" name="Sub-basins">
        <l-geo-json
                v-if="show"
                :geojson="geoJson_subbasin"
                :options="options"
                :options-style="styleFunction_subbasin"
        />
        </l-layer-group>
        <l-layer-group layer-type="overlay" name="Streams">
        <l-geo-json
                v-if="show"
                :geojson="geoJson_reach"
                :options="options"
                :options-style="styleFunction_reach"
        />
        </l-layer-group>
        
        <l-tile-layer
        v-for="tileProvider in tileProviders"
        :key="tileProvider.name"
        :name="tileProvider.name"
        :visible="tileProvider.visible"
        :url="tileProvider.url"
        :attribution="tileProvider.attribution"
        :token="token"
        layer-type="base"/>

        <!--<template slot-scope="props"> 
            <l-info-control
                item="props.currentItem" 
                unit="props.unit"
                title="Department" 
                placeholder="Hover over sub-basins"
                position="topright"
            />

       </template> -->
    <l-control-scale position="bottomleft" :maxWidth="200" imperial="imperial"/>
    </l-map>
    
    
</template>

<script>

    import {L, LMap, LTileLayer, LMarker, LGeoJson, LControlLayers, LControlScale, LLayerGroup} from 'vue2-leaflet';
    import { InfoControl, ReferenceChart, ChoroplethLayer } from 'vue-choropleth';
    import axios from 'axios';
    import regional_summary from './regional_summary.vue';

    export default {
        name: 'Map',
        components: {
            'overview_graph': regional_summary,
            'l-map': LMap,
            'l-tile-layer': LTileLayer,
            //'l-marker': LMarker,
            'l-geo-json': LGeoJson,
            'l-info-control': InfoControl, 
            'l-reference-chart': ReferenceChart, 
            'l-choropleth-layer': ChoroplethLayer,
            'l-control-layers': LControlLayers,
            'l-layer-group': LLayerGroup,
            'l-control-scale': LControlScale
        },

        //delete: L.Icon.Default.prototype._getIconUrl,

        //L: L.Icon.Default.mergeOptions({
        //    iconRetinaUrl: require('leaflet/dist/images/marker-icon-2x.png'),
        //    iconUrl: require('leaflet/dist/images/marker-icon.png'),
        //    shadowUrl: require('leaflet/dist/images/marker-shadow.png')
        //}),

        data() {
            return {
                geoJson_reach: null,
                geoJson_subbasin: null,
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
                fillColor: "rgba(76, 175, 80, 0.44)",
                

                tileProviders: [
                    {
                        name: "Street Map",
                        visible: false,
                        attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
                        url: "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                    },
                    {
                        name: "Satellite",
                        visible: false,
                        attribution: 'Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community',
                        url: "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}.png"
                    },
                    {
                        name: "Terrain Map",
                        visible: true,
                        attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
                        url: "https://stamen-tiles-{s}.a.ssl.fastly.net/terrain/{z}/{x}/{y}{r}.png"
                    }
                ]


            }
        },

        computed: {
            options() {
                return {
                    onEachFeature: this.onEachFeatureFunction
                };
            },
            styleFunction_reach() {
                const fillColor = this.fillColor; // important! need touch fillColor in computed for re-calculate when change fillColor
                return () => {
                    return {
                        weight: 2.5,
                        color: "#3386ff",
                        opacity: 1,
                        fillColor: fillColor,
                        fillOpacity: 1
                    };
                };
            },
            styleFunction_subbasin() {
                const fillColor = this.fillColor; // important! need touch fillColor in computed for re-calculate when change fillColor
                return () => {
                    return {
                        weight: 1.5,
                        color: "#7c7c7c",
                        opacity: 1,
                        fillColor: "#e3dddd",
                        dashArray: '5, 5',
                        dashOffset: '10',
                        fillOpacity: 0.5
                    };
                };
            },
            
            onEachFeatureFunction() {
                var prevLayerClicked = null;
                if (!this.enableTooltip) {
                    return () => {
                    };
                }
                return (feature, layer) => {
                    layer.bindTooltip(
                        //"<div>Subbasin: "+ feature.properties.Name + "</div>",
                        "<div><strong>Click and explore!</strong></div>",
                        {permanent: false, sticky: true}
                    );
                    
                    layer.on('click', function(e){ 
    
                        var layer = e.target;
                        console.log(prevLayerClicked);
                        console.log(e.target)
                        if (prevLayerClicked !== null || prevLayerClicked == layer) {
                            prevLayerClicked.setStyle({weight: 1.5,
                            color: "#7c7c7c",
                            opacity: 1,
                            fillColor: "#e3dddd",
                            dashArray: '5, 5',
                            dashOffset: '10',
                            fillOpacity: 0.5});
                        }
                        if (prevLayerClicked !== layer) {
                            layer.setStyle({fillColor :'blue'});
                            prevLayerClicked = layer;
                        }else{
                           prevLayerClicked = null; 
                        }

                        //{click: this.layerClicked
                    });
                    
                };
            }
        },

        created() {
            this.loading = true;
            axios.get("/reaches.geojson")
                .then(response => {
                    this.geoJson_reach = response.data;
                    this.loading = true;
                    })

            axios.get("/subbasins.geojson")
                .then(response => {
                    this.geoJson_subbasin = response.data;
                    this.loading = true;
                });

        },
        methods: {
            layerClicked() {
                alert("clicked me");
                
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

    .leaflet-touch .leaflet-control-layers-toggle {
    width: 60px;
    height: 60px;
    }

    .leaflet-control-scale-line{
        font-size: 14px;
        font-weight: bold;
    }

    .modal-backdrop {
    position: fixed;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    background-color: rgba(0, 0, 0, 0.3);
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .modal {
    background: #FFFFFF;
    box-shadow: 2px 2px 20px 1px;
    max-height: 450px;
    overflow: visible;
    position: fixed;
    top: 50%;
    left: 50%;
    /* bring your own prefixes */
    transform: translate(-50%, -50%);
    max-width: 800px;
    /*overflow-x: auto;*/
    display: flex;
    flex-direction: column;
  }

  .modal-header,
  .modal-footer {
    padding: 15px;
    display: flex;
  }

  .modal-header {
    border-bottom: 1px solid #eeeeee;
    color: #4AAE9B;
    justify-content: space-between;
    font-size: 25px;
    font-weight: bold;
  }

  .modal-footer {
    
    justify-content: flex-end;
  }

  .modal-body {
    position: relative;
    padding: 30px 40px;
    font-size: 18px;

  }

  .btn-close {
    border: none;
    font-size: 20px;
    padding: 20px;
    cursor: pointer;
    font-weight: bold;
    color: #4AAE9B;
    background: transparent;
  }

  .btn-green {
    border: none;
    font-size: 20px;
    cursor: pointer;
    font-weight: bold;
    color: #4AAE9B;
    background: transparent;
  }

</style>