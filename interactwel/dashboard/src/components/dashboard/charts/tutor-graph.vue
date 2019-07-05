<template>
    <div id="graph" class="card">
        
            <div class="card-header"><span v-on:click="dismiss" class="close"><font-awesome-icon
                icon="times-circle"/> Close</span>
                <strong>What are Adaptation Plans?</strong>
            </div>
            <div class="card-body">
            <p align="justify" style="font-size: 17px;">In this section you will be able to view multiple adaptation plans that incorporate the actors <strong>(Step 2)</strong> and actions <strong>(Step 3)</strong> that you selected.  You can compare how each adaptation plan meets the goals you selected in <strong>Step 1</strong> for the entire basin, sub-basins, and individual streams.  You can also compare the actions and their timeframes included within each plan.</p>
            <p aling="justify">Remember that you can click the map to visualize the data. </p>
            </div>
        
            <footer class="tutor-footer">
          <slot name="footer">
            <button type="button" class="btn-close" @click="dismiss">Continue</button>
            
          </slot>
        </footer>
    </div>
</template>

<script>

    import EventBus from './../../../event-bus';

    export default {
        name: 'TutorGraph',

        methods: {
            dismiss() {
                EventBus.$emit('CLOSE');
            },
            close() {
                this.$emit('close');
            },
        },
        //props: ["jsonData"]
    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
    .chart-container {
        position: absolute;
        top: 30px;
        left: 30px;
        z-index: 1000;
        background-color: #4cae4c;
        height: auto;
        width: 750px;
        max-width: 750px !important;
    }

    .nav-pills .nav-link.active, .nav-pills .show > .nav-link {
        color: #fff;
        background-color: #4cae4c !important;
    }

    .chart-inner {
        position: absolute !important;
        width: 100% !important;
        bottom: 0 !important;
    }

    .filter-options-container {
        text-align: left;
    }

    .filter-options {
        padding: 10px;
        color: #FFFFFF;
        background-color: #EFEFEF;
        margin: 5px !important;
        border-radius: 5px;
    }

    #sidebar .active {
        color: #FFF !important;
        background-color: #4cae4c;
        margin: 5px !important;
        border-radius: 5px;
    }

    .active a {
        color: rgba(255, 255, 255, 0.8);
    }

    .active a:hover {
        color: #fff
    }

    .filter-options input {
        margin-left: 10px !important;
    }

    #graph {
        width: 750px;
        max-width: 750px !important;
    }

    #graph .card-body p {
        color: #3f4558;
    }

    #graph .card-title {
        font-size: 25px;
        font-weight: bold;
        padding-bottom: 5px;
    }

</style>
