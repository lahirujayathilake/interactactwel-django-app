<template>
   <div>
       <h5>Adaptation Plan {{$route.params.planId}}</h5>
       <router-view></router-view>
   </div>
</template>
<script>

    export default {
        name: 'visualization',
        props: {},
        data() {
            return {}
        },
        mounted() {

        },
        watch: {},
        methods: {}
    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
