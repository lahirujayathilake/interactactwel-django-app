<template>
    <div>
        <b-card no-body>
            <b-tabs pills card vertical nav-wrapper-class="w-25">
                <b-tab title="My Projects">
                    <div class="card map-container">
                        <l-map :zoom="zoom" :center="center">
                            <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>
                            <l-marker :lat-lng="marker"></l-marker>
                        </l-map>
                    </div>
                </b-tab>
                <b-tab title="Umatilla">
                    <b-card-body title="Umatilla Region Adapts To Changes In Allocation Of Water For irrigation">
                        <b-card-text>
                            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque luctus purus sit amet massa hendrerit semper at eu dui. Sed eget hendrerit tortor. Vestibulum ultrices augue eu ante elementum, eget gravida lacus semper. Sed sed lectus augue. Duis ac ex quis magna tristique ullamcorper vel in nisl. Aliquam molestie nibh non orci fringilla gravida. Curabitur id est eu mauris facilisis consectetur a quis felis. Vivamus egestas ex nisl, et viverra sem placerat vitae.
                        </b-card-text>
                        <div class="card map-container">
                            <l-map :zoom="zoom" :center="center">
                                <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>
                                <l-marker :lat-lng="marker"></l-marker>
                            </l-map>
                        </div>
                        <div class="mt-3">
                            <b-button class="mr-2 btn-sm" disabled>Status</b-button>
                            <b-button class="mr-2 btn-sm" disabled>Send Email</b-button>
                            <b-button class="mr-2 btn-sm" disabled>Unjoin</b-button>
                            <b-button class="mr-2 btn-sm" disabled>Invite</b-button>
                            <b-button class="mr-2 btn-sm"><router-link to="/visualize/1">Visualize</router-link></b-button>
                            <b-button class="mr-2 btn-sm"><router-link to="/adaptation-plans/1">Adaptation Plans</router-link></b-button>
                        </div>
                    </b-card-body>
                </b-tab>
                <b-tab title="Colarado">
                    <b-card-text>
                        <b-card-body title="Colarado Region Adapts To Changes In Allocation Of Water For irrigation">
                            <b-card-text>
                                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque luctus purus sit amet massa hendrerit semper at eu dui. Sed eget hendrerit tortor. Vestibulum ultrices augue eu ante elementum, eget gravida lacus semper. Sed sed lectus augue. Duis ac ex quis magna tristique ullamcorper vel in nisl. Aliquam molestie nibh non orci fringilla gravida. Curabitur id est eu mauris facilisis consectetur a quis felis. Vivamus egestas ex nisl, et viverra sem placerat vitae.
                            </b-card-text>
                            <div class="card map-container">
                                <l-map :zoom="zoom" :center="center">
                                    <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>
                                    <l-marker :lat-lng="marker"></l-marker>
                                </l-map>
                            </div>
                            <div class="mt-3">
                                <b-button class="mr-2 btn-sm" disabled>Status</b-button>
                                <b-button class="mr-2 btn-sm" disabled>Send Email</b-button>
                                <b-button class="mr-2 btn-sm" disabled>Unjoin</b-button>
                                <b-button class="mr-2 btn-sm" disabled>Invite</b-button>
                                <b-button class="mr-2 btn-sm"><router-link to="/visualize/2">Visualize</router-link></b-button>
                                <b-button class="mr-2 btn-sm"><router-link to="/adaptation-plans/2">Adaptation Plans</router-link></b-button>
                            </div>
                        </b-card-body>
                    </b-card-text>
                </b-tab>
                <b-tab title="Texas">
                    <b-card-text>
                        <b-card-body title="Texas Region Adapts To Changes In Allocation Of Water For irrigation">
                            <b-card-text>
                                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque luctus purus sit amet massa hendrerit semper at eu dui. Sed eget hendrerit tortor. Vestibulum ultrices augue eu ante elementum, eget gravida lacus semper. Sed sed lectus augue. Duis ac ex quis magna tristique ullamcorper vel in nisl. Aliquam molestie nibh non orci fringilla gravida. Curabitur id est eu mauris facilisis consectetur a quis felis. Vivamus egestas ex nisl, et viverra sem placerat vitae.
                            </b-card-text>
                            <div class="card map-container">
                                <l-map :zoom="zoom" :center="center">
                                    <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>
                                    <l-marker :lat-lng="marker"></l-marker>
                                </l-map>
                            </div>
                            <div class="mt-3">
                                <b-button class="mr-2 btn-sm" disabled>Status</b-button>
                                <b-button class="mr-2 btn-sm" disabled>Send Email</b-button>
                                <b-button class="mr-2 btn-sm" disabled>Unjoin</b-button>
                                <b-button class="mr-2 btn-sm" disabled>Invite</b-button>
                                <b-button class="mr-2 btn-sm"><router-link to="/visualize/3">Visualize</router-link></b-button>
                                <b-button class="mr-2 btn-sm"><router-link to="/adaptation-plans/3">Adaptation Plans</router-link></b-button>
                            </div>
                        </b-card-body>
                    </b-card-text>
                </b-tab>
            </b-tabs>
        </b-card>
        <b-card v-show="">
        <b-card-body title="You don't have access to any projects">
            <b-card-text>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque luctus purus sit amet massa hendrerit semper at eu dui.
            </b-card-text>
        </b-card-body>
        </b-card>
    </div>
</template>

<script>
    import L from 'leaflet';
    import {LMap, LTileLayer, LMarker} from 'vue2-leaflet';

    export default {
        components: {
            LMap, LTileLayer, LMarker

        },
        name: 'MyProjects',

        data() {
            return {
                zoom:13,
                center: L.latLng(47.413220, -1.219482),
                url:'http://{s}.tile.osm.org/{z}/{x}/{y}.png',
                attribution:'&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
                marker: L.latLng(47.413220, -1.219482),
            }

        },

        mounted() {

        },


        methods: {}

    }

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
    @import '../../../assets/vendor/Vue2Leaflet/leaflet.css';
    .map-container{
        height: 400px;
        overflow:auto;
    }
</style>

