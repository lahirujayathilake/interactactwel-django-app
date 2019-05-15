<template>
    <div id="graph" class="card">
        <div class="card-header">
            <strong>Costs</strong>
        </div>
        <div class="card-body">
            <img class="img-fluid" src="../../../assets/cost-graph.png"/>
        </div>
    </div>
</template>

<script>
    import JSONData from "../../../assets/result_action_plans.json";

    export default {
        name: 'CostGraph',

        components: {
        },

        data() {
            return {

                NFertilizer: [
                    {
                        'Data' : [
                            {
                                'CWGR': [
                                    {
                                        'data' : [
                                            {"1":7.35, "2":48.18, "3":0.0}
                                        ],
                                        'name' : "Crested Wheatgrass"
                                    }
                                ],

                                'POTA': [
                                    {
                                        'data' : [
                                            {"1":182.0, "2":134.1, "3":1691.96}
                                        ],
                                        'name' : "Potato"
                                    }
                                ],
                                'OAK': [
                                    {
                                        'data' : [
                                            {"1":0.0, "2":0.0, "3":0.0}
                                        ],
                                        'name' : "Oak"
                                    }
                                ],

                            }
                        ]
                    }

                ],

                irrigationData: [
                    {
                        1: [
                            {'y1': 23.3423, 'y2': 34.4232, 'y3': 12.3434},

                        ],
                        2: [
                            {'y1': 23.3423, 'y2': 34.4232, 'y3': 12.3434},

                        ],
                        3:[
                            {'y1':23.3423, 'y2':34.4232, 'y3':12.3434},

                        ]
                    }
                ],

                dataSet: [
                    {'val': 50, 'val2': 1900, 'name': 'Jan'},
                    {'val': 60, 'val2': 1730, 'name': 'Feb'},
                    {'val': 65, 'val2': 1800, 'name': 'Mar'},
                    {'val': 80, 'val2': 1805, 'name': 'Apr'},
                    {'val': 56, 'val2': 1750, 'name': 'May'},
                    {'val': 78, 'val2': 1777, 'name': 'Jun'},
                    {'val': 99, 'val2': 2100, 'name': 'Jul'},
                    {'val': 95, 'val2': 2089, 'name': 'Aug'},
                    {'val': 76, 'val2': 1640, 'name': 'Sept'},
                    {'val': 40, 'val2': 1790, 'name': 'Oct'},
                    {'val': 35, 'val2': 1500, 'name': 'Nov'},
                    {'val': 42, 'val2': 1800, 'name': 'Dec'}
                ],
                options: {
                    dim: 'name',
                    height: 175,
                    width: 250
                },

                legends: {
                    enabled: true,
                    height: 25,
                    width: 50,
                }



            };
        },
        computed: {
            jsonData() {
                return JSONData;
            },

            graphData() {
                var adaptationPlan = this.planName;

                return Object.keys(this.jsonData["Adaptation_plans"][adaptationPlan])
                    .map(key => {
                        return {
                            key: key,
                            value: this.jsonData["Adaptation_plans"][adaptationPlan][key]
                        };
                    })
                    .filter(d => {
                        if (this.selectedKeyList.findIndex(k => k === d.key) > -1) {
                            //console.log(this.selectedKeyList.findIndex(k => k === d.key) > -1);
                            return true;
                        } else {
                            return false;
                        }
                    });

            },
        },

        mounted() {
        },

        methods: {},

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
        width: 800px;
        max-width: 830px !important;
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

    #graph .card {
        width: 800px;
        max-width: 830px !important;
    }
</style>