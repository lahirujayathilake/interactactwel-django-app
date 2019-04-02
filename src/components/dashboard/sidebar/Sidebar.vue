<template>
    <div id="sidebar" role="tablist">
        <div v-for="(key, value) in adaptationPlans" v-bind:key="key">
            <b-nav header-tag="header" class="p-1" role="tab">
                <b-nav-item v-on:click="showChart" block href="#" v-b-toggle="value" variant="info">{{value}}</b-nav-item>
            </b-nav>
            <b-collapse :id="value" accordion="my-accordion" role="tabpanel">
                    <b-nav vertical class="w-100">
                        <b-nav-item active>Actors</b-nav-item>
                        <b-nav-item>Cost</b-nav-item>
                        <b-nav-item>Storgage</b-nav-item>
                        <b-nav-item>ETmm</b-nav-item>
                    </b-nav>
            </b-collapse>
        </div>
    </div>
</template>

<script>

    import JSONData from "../../../assets/result_action_plans.json";

    export default {
        name: 'Sidebar',

        computed: {
            jsonData() {
                return JSONData;
            },
            adaptationPlans() {
                return this.jsonData["Adaptation_plans"]
            },
        },

        methods: {
            showChart: function () {
                this.$emit('clicked')

            },
        }
    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>

    #sidebar .collapse .nav-item{
        border-bottom: 1px solid #37474f !important;
        background-color: #263238 !important;
    }

    #sidebar .p-1{
        border-bottom: 1px solid #263238 !important;
    }

</style>