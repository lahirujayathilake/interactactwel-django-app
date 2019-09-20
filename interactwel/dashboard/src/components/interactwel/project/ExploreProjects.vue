<template>
    <b-card-group>
        <b-card footer-tag="footer">
            <div class="step-header" slot="header">Explore Projects
            </div>
            <b-card-text>
            </b-card-text>
        </b-card>
    </b-card-group>
</template>

<script>
    import Header from './../Header.vue';
    import Footer from './../Footer.vue';
    import LeafletMap from './../../dashboard/map/LeafletMap.vue'

    export default {
        components: {
            Header, Footer, LeafletMap
        },
        name: 'ExploreProjects',

        data() {
            return {
            }
        },

        mounted() {
        },


        methods: {}

    }

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
    .main {
        background-color: #efefef;
        padding: 1rem;
        min-height: 90vh;
    }
    .map-wrapper {
        -webkit-box-flex: 1;
        -ms-flex: 1;
        flex: 1;
        min-height: calc(60vh);
    }

    .widget {
        background-color: #f7f7f7;
        padding: 1rem;
        border: 1px solid #efefef;
        border-radius: 5px;
        margin-bottom: 10px;
    }

    .widget-title {
        font-size: 16px;
        font-weight: 700;
    }
</style>

