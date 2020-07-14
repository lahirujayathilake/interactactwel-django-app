<template>
    <b-row>

        <b-col cols="12">
            <b-card-group deck>
            <b-card no-body class="overflow-hidden">
                <b-row no-gutters>
                    <b-col md="12">
                        <b-card-body title="Story 1">
                            <b-card-text>
                                This is a wider card with supporting text as a natural lead-in to additional content.
                                This content is a little bit longer.
                            </b-card-text>
                            <b-button href="#" variant="primary">Read More</b-button>
                        </b-card-body>
                    </b-col>
                </b-row>
            </b-card>
                <b-card no-body class="overflow-hidden">
                    <b-row no-gutters>
                        <b-col md="12">
                            <b-card-body title="Story 2">
                                <b-card-text>
                                    This is a wider card with supporting text as a natural lead-in to additional content.
                                    This content is a little bit longer.
                                </b-card-text>
                                <b-button href="#" variant="primary">Read More</b-button>
                            </b-card-body>
                        </b-col>
                    </b-row>
                </b-card>
                <b-card no-body class="overflow-hidden">
                    <b-row no-gutters>
                        <b-col md="12">
                            <b-card-body title="Story 3">
                                <b-card-text>
                                    This is a wider card with supporting text as a natural lead-in to additional content.
                                    This content is a little bit longer.
                                </b-card-text>
                                <b-button href="#" variant="primary">Read More</b-button>
                            </b-card-body>
                        </b-col>
                    </b-row>
                </b-card>
            </b-card-group>
        </b-col>
    </b-row>
</template>

<script>
    import Header from './../../Header.vue';
    import Footer from './../../Footer.vue';

    export default {
        components: {
            Header, Footer
        },
        name: 'Stories',

        data() {
            return {
            }
        },

        mounted() {
        }
        ,


        methods: {}

    }

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>

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
