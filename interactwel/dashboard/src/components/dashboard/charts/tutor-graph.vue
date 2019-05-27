<template>
    <div id="graph" class="card">
        <b-card no-body>
            <div class="card-header"><span v-on:click="dismiss" class="close"><font-awesome-icon
                icon="times-circle"/> Close</span>
                <strong>What are Actions Plans?</strong>
            </div>
            <div class="card-body">

            </div>
        </b-card>
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
</style>
