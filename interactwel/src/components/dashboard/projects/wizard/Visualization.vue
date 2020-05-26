<template>
   <div>
       <h6 class="mt-3">Adaptation Plan {{$route.params.planId}}</h6>
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
