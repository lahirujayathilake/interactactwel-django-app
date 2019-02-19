<template>
    <div role="tablist">
            <b-nav header-tag="header" class="p-1" role="tab">
                <b-nav-item block href="#" v-b-toggle.plan1 variant="info">Adaptation Plan 1</b-nav-item>
            </b-nav>
            <b-collapse id="plan1" visible accordion="my-accordion" role="tabpanel">
                    <b-nav vertical class="w-100">
                        <b-nav-item active>Actors</b-nav-item>
                        <b-nav-item>Cost</b-nav-item>
                        <b-nav-item>Storgage</b-nav-item>
                        <b-nav-item>ETmm</b-nav-item>
                    </b-nav>
            </b-collapse>
        <b-nav header-tag="header" class="p-1" role="tab">
            <b-nav-item block href="#" v-b-toggle.plan2 variant="info">Adaptation Plan 2</b-nav-item>
        </b-nav>
        <b-collapse id="plan2" visible accordion="my-accordion" role="tabpanel">
            <b-nav vertical class="w-100">
                <b-nav-item active>Actors</b-nav-item>
                <b-nav-item>Cost</b-nav-item>
                <b-nav-item>Storgage</b-nav-item>
                <b-nav-item>ETmm</b-nav-item>
            </b-nav>
        </b-collapse>
        <b-nav header-tag="header" class="p-1" role="tab">
            <b-nav-item block href="#" v-b-toggle.plan3 variant="info">Adaptation Plan 3</b-nav-item>
        </b-nav>
        <b-collapse id="plan3" visible accordion="my-accordion" role="tabpanel">
            <b-nav vertical class="w-100">
                <b-nav-item active>Actors</b-nav-item>
                <b-nav-item>Cost</b-nav-item>
                <b-nav-item>Storgage</b-nav-item>
                <b-nav-item>ETmm</b-nav-item>
            </b-nav>
        </b-collapse>
    </div>
</template>

<script>

    export default {
        name: 'Sidebar'
    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>

    b-nav-item{
        border-bottom: 1px solid #607D8B !important;
        background-color: #263238 !important;
    }

</style>