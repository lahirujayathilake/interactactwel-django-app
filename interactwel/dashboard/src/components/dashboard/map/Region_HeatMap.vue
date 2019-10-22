<template>
    <l-choropleth-layer 
      :data="pyDepartmentsData" 
      titleKey="department_name" 
      idKey="department_id"
      :value="value" 
      :extraValues="extraValues" 
      geojsonIdKey="Name" 
      :geojson="paraguayGeojson" 
      :colorScale="colorScale">
        <template slot-scope="props">
          <l-info-control 
            :item="props.currentItem" 
            :unit="props.unit" 
            title="Department" 
            placeholder="Hover over a department"/>
          <l-reference-chart 
            title="Girls school enrolment" 
            :colorScale="colorScale" 
            :min="props.min" 
            :max="props.max" 
            position="topright"/>
        </template>
    </l-choropleth-layer>
</template>

<script>
    import JSONData from "../../../assets/result_action_plans.json";
    import EventBus from './../../../event-bus';

    import { InfoControl, ReferenceChart, ChoroplethLayer } from 'vue-choropleth';
    import paraguayGeojson from './../../../../public/static/subbasins.json';

    export default {
        name: 'RegionHeatMap',

        components: {

            'l-choropleth-layer': ChoroplethLayer,
            'l-info-control': InfoControl, 
            'l-reference-chart': ReferenceChart, 
        },

        data() {
            return {
                paraguayGeojson,
                colorScale: ["e7d090", "e9ae7b", "de7062"],
                value: {
                    key: "amount_w",
                    metric: "% girls"
                },
                extraValues: [{
                    key: "amount_m",
                    metric: "% boys"
                }],
                pyDepartmentsData: [
                        {
                            department_id: 0,
                            department_name: "Asunción",
                            amount_w: 91.11,
                            amount_m: 89.5
                        },
                        {
                            department_id: 17,
                            department_name: "Alto Paraguay",
                            amount_w: 91.1,
                            amount_m: 93.88
                        },
                        {
                            department_id: 10,
                            department_name: "Alto Parana",
                            amount_w: 84.57,
                            amount_m: 84.92
                        },
                        {
                            department_id: 13,
                            department_name: "Amambay",
                            amount_w: 68.97,
                            amount_m: 67.57
                        },
                        {
                            department_id: 16,
                            department_name: "Boquerón",
                            amount_w: 83.18,
                            amount_m: 85.54
                        },
                        {
                            department_id: 5,
                            department_name: "Caaguazu",
                            amount_w: 77.55,
                            amount_m: 79.49
                        },
                        {
                            department_id: 6,
                            department_name: "Caazapa",
                            amount_w: 83.51,
                            amount_m: 88.1
                        },
                        {
                            department_id: 14,
                            department_name: "Canindeyu",
                            amount_w: 88.64,
                            amount_m: 92.04
                        },
                        {
                            department_id: 11,
                            department_name: "Central",
                            amount_w: 76.12,
                            amount_m: 76.74
                        },
                        {
                            department_id: 1,
                            department_name: "Concepción",
                            amount_w: 81.72,
                            amount_m: 83.87
                        },
                        {
                            department_id: 3,
                            department_name: "Cordillera",
                            amount_w: 86.95,
                            amount_m: 88.13
                        },
                        {
                            department_id: 4,
                            department_name: "Guaira",
                            amount_w: 80.06,
                            amount_m: 81.14
                        },
                        {
                            department_id: 7,
                            department_name: "Itapua",
                            amount_w: 71.56,
                            amount_m: 73.55
                        },
                        {
                            department_id: 8,
                            department_name: "Misiones",
                            amount_w: 87.64,
                            amount_m: 88.99
                        },
                        {
                            department_id: 12,
                            department_name: "Ñeembucu",
                            amount_w: 77.35,
                            amount_m: 76.24
                        },
                        {
                            department_id: 9,
                            department_name: "Paraguari",
                            amount_w: 78.68,
                            amount_m: 83.33
                        },
                        {
                            department_id: 15,
                            department_name: "Presidente Hayes",
                            amount_w: 83.78,
                            amount_m: 83.68
                        },
                        {
                            department_id: 2,
                            department_name: "San Pedro",
                            amount_w: 90.45,
                            amount_m: 93.67
                        }
                        ],

                mapOptions: { attributionControl: false},
                currentStrokeColor: '3d3213',
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

        methods: {
            dismiss() {
                EventBus.$emit('CLOSE');
            },
        },
        //props: ["jsonData"]

    }
</script>


<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
.baseline-graph-title{
    background-color: #6c757d;
    padding: 5px;
    text-align: center;
    color: #FFF;
    font-size: 12px;
}
</style>
