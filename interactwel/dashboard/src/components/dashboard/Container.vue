<template>
    <div id="main">
        <article id="map">
            <component v-show="!wizardVisibility" v-bind:is="component='Wizard'"></component>
            <leaflet-map></leaflet-map>
            <component v-show="!regionalSummaryVisibility" v-bind:is="component='regional-summary'"></component>
        </article>
        <aside v-show="asideVisibility"><feedback></feedback></aside>
    </div>
</template>

<script>

    import Wizard from './wizard/Wizard.vue'
    import Feedback from './feedback/Feedback.vue'
    import LeafletMap from './map/LeafletMap.vue'
    import RegionalSummary from './map/RegionalSummary.vue'
    import EventBus from './../../event-bus';

    export default {
        name: 'Container',

        components: {
            Feedback,
            Wizard, LeafletMap, RegionalSummary,
        },

        props: {
            visibility: {
                type: Boolean,
                default: false
            },
        },

        data() {
            return {
                chartsVisibility: true,
                wizardVisibility: true,
                asideVisibility: false,
                regionalSummaryVisibility: true,

                prevLayerClicked: null,
            }
        },

        mounted() {

            let $this = this;
            EventBus.$on('START_WIZARD', function () {
                $this.wizardVisibility = false;
            }),
                EventBus.$on('EXIT_WIZARD', function () {
                    $this.wizardVisibility = true;
                }),
                EventBus.$on('SHOW_ASIDE', function () {
                    $this.asideVisibility = true;
                }),
                EventBus.$on('HIDE_ASIDE', function () {
                    $this.asideVisibility = false;
                }),
            EventBus.$on('SELECTED_BASIN', function (selectedBasinID) {

                $this.regionalSummaryVisibility = true;

                if ($this.prevLayerClicked !== null || $this.prevLayerClicked == selectedBasinID) {
                    $this.regionalSummaryVisibility = true;
                }
                if ($this.prevLayerClicked !== selectedBasinID) {
                    $this.createRegionSummary(selectedBasinID)
                    $this.regionalSummaryVisibility = false;
                    $this.prevLayerClicked = selectedBasinID;
                    }else{
                        $this.regionalSummaryVisibility = true;
                        $this.prevLayerClicked = null;
                    }
            }),
            EventBus.$on('CLOSE', function () {
                $this.regionalSummaryVisibility = true
            })
        },

        methods: {

            createRegionSummary(subbasinID){
                EventBus.$emit('CREATE_REGION_SUMMARY', subbasinID);
            }

        }
    }

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
    .bg-secondary {
        background-color: #263238 !important;
    }

    #main {
        display: flex;
        min-height: calc(100vh - 40vh);
    }

    #main > article {
        flex: 1;
        height: calc(60vh - 20px);
    }

    #main > nav {
        flex: 0 0 auto;
        min-width: 200px;
        height: calc(92vh - 20px);
        overflow: auto;
        background-color: #37474F;
    }

    #main > nav {
        order: -1;
    }

    #main > aside {
        flex: 0 0 400px;
        height: calc(92vh - 20px);
        overflow: auto;
        background-color: #ededed;
    }
</style>
