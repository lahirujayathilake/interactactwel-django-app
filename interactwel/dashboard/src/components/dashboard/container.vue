<template>
    <div id="main">
        <nav v-show="!sidebarLeftVisibility" id="sidebar-left">
            <component v-bind:is="component='sidebar'"></component>
        </nav>
        <article id="map">
            <component v-show="!stepsVisibility" v-bind:is="component='step1content'"
                       v-on:finish-wizard="afterWizardFinished"></component>
            <component v-show="!chartsVisibility" v-bind:is="component='charts'"></component>
            <leaflet-map></leaflet-map>
            <component v-show="!regionalSummaryVisibility" v-bind:is="component='regional-summary'"></component>
        </article>
        <aside v-show="!sidebarRightVisibility" id="sidebar-right">
            <component v-bind:is="component='feedback'"></component>
        </aside>
    </div>
</template>

<script>

    import Sidebar from './sidebar/Sidebar.vue'
    import Feedback from './feedback/feedback.vue'
    import Charts from './charts/charts.vue'
    import ActionsGraph from './charts/actions-graph.vue'
    import ProgressBar from './progressBar/ProgressBar.vue'
    import Step1Content from './../steps/Step1Content.vue'
    import LeafletMap from './map/LeafletMap.vue'
    import RegionalSummary from './map/regional_summary_chartjs.vue'
    import Container from './container.vue'

    import EventBus from './../../event-bus';

    export default {
        components: {
            'progress-bar': ProgressBar,
            'feedback': Feedback,
            'charts': Charts,
            'actions-graph': ActionsGraph,
            'sidebar': Sidebar,
            'step1content': Step1Content,
            'leafletMap': LeafletMap,
            'regionalSummary': RegionalSummary,
            'container': Container
        },
        name: 'Container',

        data() {
            return {
                stepComponent: null,
                sidebarLeftVisibility: true,
                sidebarRightVisibility: true,
                chartsVisibility: true,
                regionalSummaryVisibility: true,
                stepsVisibility: true,
                component: null,
            }
        },

        mounted() {

            let $this = this;
            EventBus.$on('START_WIZARD', function () {
                $this.stepsVisibility = false
            }),
            EventBus.$on('SELECTED_BASIN', function (selectedBasinID) {
                $this.createRegionSummary(selectedBasinID)
                $this.regionalSummaryVisibility = false
            }),
            EventBus.$on('CLOSE', function () {
                $this.regionalSummaryVisibility = true
            })
        },

        methods: {

            afterWizardFinished() {
                this.sidebarLeftVisibility = false,
                this.sidebarRightVisibility = false
                this.progressBarVisibility = false
                this.chartsVisibility = false
                this.regionalSummaryVisibility = false
            },

            createRegionSummary(subbasinID){
                EventBus.$emit('CREATE_REGION_SUMMARY', subbasinID);
            },
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
        padding: 1rem;
        background-color: #FFF;
    }

    #sidebar-left a {
        color: #fff;
    }
</style>
