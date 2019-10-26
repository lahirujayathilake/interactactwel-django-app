<template>
    <b-container fluid class="footer">
        <b-container>
        <b-row>
            <b-col></b-col>
        </b-row>
        </b-container>
    </b-container>
</template>

<script>
    import EventBus from './../../event-bus';

    export default {
        components: {

        },
        name: 'Footer',

        data() {
            return {
            }
        },

        mounted() {
        },


        methods: {

        }

    }

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
    .footer{
        background-color: #d3d6dc;
        height: 100px;
        padding: 1rem
    }
</style>

