<template>

    <div>
        water rights popup content
    </div>

</template>

<script>

    export default {
        name: "PopupContentWaterRights",
        components: {
        },
        props: {
            data: {
                name: String
            },
            pcpdata: {}
        },

        computed: {}
    }
</script>

<style>
#PopupContent {
    width: 450px;
    height: 300px;
    z-index: 1000;
}

.leaflet-popup-content{
    width: 450px;
}
.leaflet-popup-content-wrapper{
    width: 490px;
}
</style>
