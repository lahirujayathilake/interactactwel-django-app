<template>
    <b-card footer-tag="footer">
        <div class="step-header" slot="header">Overview
        </div>
        <b-card-text>
            <b-row>
                <b-col lg="6">
                    <h6><strong>Selected Goals</strong></h6>
                    <b-list-group class="no-padding">
                        <b-list-group-item>Improve surface water quality</b-list-group-item>
                        <b-list-group-item>Increase recharge to shallow aquifer</b-list-group-item>
                        <b-list-group-item>Increase agriculture productivity</b-list-group-item>
                        <b-list-group-item>Improve ecological habitat</b-list-group-item>
                    </b-list-group>

                </b-col>
                <b-col lg="6">
                    <h6><strong>Selected Actors</strong></h6>
                    <b-list-group class="no-padding">
                        <b-list-group-item>Farmer with Columbia river water rights</b-list-group-item>
                        <b-list-group-item>Farmer with other surface water rights</b-list-group-item>
                        <b-list-group-item>Farmer with groundwater rights</b-list-group-item>
                    </b-list-group>
                </b-col>
            </b-row>
            <b-row style="margin-top:20px;">
                <b-col lg="12">
                    <h6><strong>Selected Actions for Actors</strong></h6>
                    <b-tabs vertical>
                        <b-tab title="Farmers with GW" active>
                            <b-list-group>
                                <b-list-group-item class="no-border">
                                    <small> No changes to current water right allocations</small>
                                </b-list-group-item>
                                <b-list-group-item class="no-border">
                                    <small> Decrease the volume of non-Columbia surface water</small>
                                </b-list-group-item>
                            </b-list-group>
                        </b-tab>
                        <b-tab title="Farmers with SW" active>
                            <b-list-group>
                                <b-list-group-item class="no-border">
                                    <small> Decrease the volume of non-Columbia surface water</small>
                                </b-list-group-item>
                                <b-list-group-item class="no-border">
                                    <small> Increase the volume of Columbia surface water</small>
                                </b-list-group-item>
                                <b-list-group-item class="no-border">
                                    <small> Increase the volume of groundwater</small>
                                </b-list-group-item>
                            </b-list-group>
                        </b-tab>
                    </b-tabs>
                </b-col>
            </b-row>
        </b-card-text>
    </b-card>
</template>

<script>
    import EventBus from './../../../event-bus';

    export default {
        components: {

        },
        name: 'PlansOverview',

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
.top-fixed-nav a, button a{
    color: #fff;
}
    .router-link-exact-active{
        color: #4cae4c;
    }
</style>

