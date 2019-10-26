<template>
    <b-card-group>
        <b-card footer-tag="footer">
            <div class="step-header" slot="header">Groups
            </div>
            <b-card-text>
                <b-row>
                    <b-col lg="8">
                        <b-container>
                            <b-row>
                                <b-col>
                                    <b-button class="mr-2" size="sm">Create Group</b-button>
                                </b-col>
                            </b-row>
                        </b-container>
                        <b-container class="mt-3">
                            <b-row>
                                <b-col>
                                    <b-list-group>
                                        <b-list-group-item>Group 1 <b-button size="sm">Leave</b-button><b-button size="sm" class="mr-2">Add Friend</b-button></b-list-group-item>
                                        <b-list-group-item>Group 2 <b-button size="sm">Leave</b-button><b-button size="sm" class="mr-2">Add Friend</b-button></b-list-group-item>
                                        <b-list-group-item>Group 3 <b-button size="sm">Leave</b-button><b-button size="sm" class="mr-2">Add Friend</b-button></b-list-group-item>
                                        <b-list-group-item>Group 4 <b-button size="sm">Leave</b-button><b-button size="sm" class="mr-2">Add Friend</b-button></b-list-group-item>
                                        <b-list-group-item>Group 5 <b-button size="sm">Leave</b-button><b-button size="sm" class="mr-2">Add Friend</b-button></b-list-group-item>
                                    </b-list-group>
                                </b-col>
                            </b-row>
                        </b-container>
                    </b-col>
                    <b-col lg="4">
                        <b-container>
                            <b-row>
                                <b-col class="widget">
                                    <div class="widget-title">Groups you manage</div>
                                    <b-list-group class="mt-2">
                                        <b-list-group-item>Group 1
                                            <b-button size="sm">Manage</b-button>
                                        </b-list-group-item>
                                        <b-list-group-item>Group 1
                                            <b-button size="sm">Manage</b-button>
                                        </b-list-group-item>
                                    </b-list-group>
                                </b-col>
                            </b-row>
                            <b-row>
                                <b-col class="widget">
                                    <div class="widget-title">
                                        Groups you may like
                                    </div>
                                    <b-list-group class="mt-2">
                                        <b-list-group-item>Group 1
                                            <b-button size="sm">Join</b-button>
                                        </b-list-group-item>
                                        <b-list-group-item>Group 2
                                            <b-button size="sm">Join</b-button>
                                        </b-list-group-item>
                                        <b-list-group-item>Group 3
                                            <b-button size="sm">Join</b-button>
                                        </b-list-group-item>
                                        <b-list-group-item>Group 4
                                            <b-button size="sm">Join</b-button>
                                        </b-list-group-item>
                                        <b-list-group-item>Group 5
                                            <b-button size="sm">Join</b-button>
                                        </b-list-group-item>
                                    </b-list-group>
                                </b-col>
                            </b-row>
                        </b-container>
                    </b-col>
                </b-row>
            </b-card-text>
        </b-card>
    </b-card-group>
</template>

<script>
    import Header from './../Header.vue';
    import Footer from './../Footer.vue';

    export default {
        components: {
            Header, Footer
        },
        name: 'Groups',

        data() {
            return {
            }
        },

        mounted() {
        },


        methods: {}

    }

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
    .main {
        background-color: #efefef;
        padding: 1rem;
        min-height: 90vh;
    }
    .map-wrapper {
        -webkit-box-flex: 1;
        -ms-flex: 1;
        flex: 1;
        min-height: calc(60vh);
    }

    .widget {
        background-color: #f7f7f7;
        padding: 1rem;
        border: 1px solid #efefef;
        border-radius: 5px;
        margin-bottom: 10px;
    }

    .widget-title {
        font-size: 16px;
        font-weight: 700;
    }
</style>

