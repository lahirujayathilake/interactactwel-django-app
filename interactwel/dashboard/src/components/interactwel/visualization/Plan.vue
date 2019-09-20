<template>
    <div>
                    <h2>Project {{$route.params.projectId}}</h2>
                    <h2>Plan {{$route.params.planId}}</h2>
    </div>
</template>

<script>

    export default {
        components: {

        },
        name: 'Plan',

        props: {
            adaptationPlan: {
                type: String,
                default: ""
            },
        },

        data() {
            return {
            }
        },

        mounted() {
        },


        methods: {
            showFeedback(currentComponent, planId) {
                    this.adaptationPlan = 'Adaptation Plan '+planId;
                    this.currentComponent = currentComponent;
                    //EventBus.$emit('PLAN_FEEDBACK', this.currentComponent);

            },
        }

    }

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>

    .main{
        background-color: #efefef;
        padding: 1rem;
        min-height: 90vh;
    }

    .map-container {
        -webkit-box-flex: 1;
        -ms-flex: 1;
        flex: 1;
        height: calc(92vh - 20px);
    }
</style>

