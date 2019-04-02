<template>
    <div class="chart-container">
        <div class="card text-center">
            <div class="card-body">
                <MyChart :actions="actions" :data="data"></MyChart>
            </div>
            <div class="card-body">
                <div class="filter-options-container">
                    <div v-for="actor in actors" v-bind:key="actor.key" v-bind:class="{ active: actor.active }" class="form-check form-check-inline filter-options">
                        <input class="form-check-input"
                               type="checkbox"
                               :name="actor.value"
                               :value="actor.key"
                               :id="actor.key"
                               @change="inputChanged($event , actor)">
                        <label class="form-check-label" :for="actor.key">{{actor.value}}</label>
                    </div>
                </div>
            </div>
            <div class="card-header">
                POPSWAT_0
            </div>
        </div>
    </div>
</template>

<script>
    import JSONData from "../../../assets/result_action_plans.json";
    import MyChart from "./MyChart";
    export default {
        name: 'Charts',

        components: {
            'MyChart': MyChart
        },

        data() {
            return {
                selectedKeyList: []
            };
        },
        computed: {
            jsonData() {
                return JSONData;
            },

            actions() {
                return this.jsonData["Actions_map"];
            },
            data() {
                var adaptationPlan = "POPSWAT_0";

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
            actors() {
                return Object.keys(this.jsonData["Actors_map"]).map(key => {
                    return {
                        key: parseInt(key, 10) + 1,
                        value: this.jsonData["Actors_map"][key]
                    };
                });
            }
        },
        methods: {
            inputChanged(event , item) {
                if (event.target.checked) {
                    this.selectedKeyList.push(event.target.value);
                    item.active = !item.active;

                } else {
                    const index = this.selectedKeyList.findIndex(
                        k => k === event.target.value
                    );
                    this.selectedKeyList.splice(index, 1);

                }
            },

            /*toggleActive: function(item) {
                item.active = !item.active;
            }*/
        },
        //props: ["jsonData"]
    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>

    .chart-container{
        position: absolute;
        top:100px;
        left:30px;
        z-index: 1000;
        background-color: #4cae4c;
        height: 400px;
        width:800px;
    }

    .nav-pills .nav-link.active, .nav-pills .show > .nav-link {
        color: #fff;
        background-color: #4cae4c !important;
    }

    .chart-inner{
        position: absolute !important;
        width: 100% !important;
        bottom: 0 !important;
    }

    .filter-options-container{
        text-align: left;
    }

    .filter-options{
        padding: 10px;
        color: #222222;
        background-color: #EFEFEF;
        margin:5px !important;
        border-radius: 5px;
    }

    .active{
        padding: 10px;
        color: #FFF;
        background-color: #4cae4c;
        margin:5px !important;
        border-radius: 5px;
    }



    .filter-options  input{
        margin-left: 10px !important;
    }
</style>