<template>
    <b-card-group>
        <b-card footer-tag="footer">
            <div class="step-header" slot="header">Members
            </div>
            <b-card-text>
                <b-row>
                    <b-col lg="8">
                        <b-container>
                            <b-row>
                                <b-col>
                                    <b-button class="mr-2" size="sm">Create Event</b-button>
                                </b-col>
                            </b-row>
                        </b-container>
                        <b-container class="mt-3">
                            <b-row>
                                <b-col>
                                    <b-list-group>
                                        <b-list-group-item>Event 1</b-list-group-item>
                                        <b-list-group-item>Event 2</b-list-group-item>
                                        <b-list-group-item>Event 3</b-list-group-item>
                                        <b-list-group-item>Event 4</b-list-group-item>
                                        <b-list-group-item>Event 5
                                        </b-list-group-item>
                                    </b-list-group>
                                </b-col>
                            </b-row>
                        </b-container>
                    </b-col>
                    <b-col lg="4">
                        <b-container>
                            <b-row>
                                <b-col class="widget">
                                    <div class="widget-title">
                                        Events you may like
                                    </div>
                                    <b-list-group class="mt-2">
                                        <b-list-group-item>Andrew Smith
                                            <b-button size="sm">Connect</b-button>
                                        </b-list-group-item>
                                        <b-list-group-item>John Doe
                                            <b-button size="sm">Connect</b-button>
                                        </b-list-group-item>
                                        <b-list-group-item>Nick Harrison
                                            <b-button size="sm">Connect</b-button>
                                        </b-list-group-item>
                                        <b-list-group-item>Justin Watson
                                            <b-button size="sm">Connect</b-button>
                                        </b-list-group-item>
                                        <b-list-group-item>Vestibulum at eros
                                            <b-button size="sm">Connect</b-button>
                                        </b-list-group-item>
                                    </b-list-group>
                                </b-col>
                            </b-row>
                            <b-row>
                                <b-col class="widget">
                                    <div class="widget-title">Calender</div>

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
        name: 'Events',

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

