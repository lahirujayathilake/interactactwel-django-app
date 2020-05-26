<template>
    <b-row>
        <b-col col="4">
            <div role="tablist">
                <b-card no-body class="mb-1">
                    <b-card-header header-tag="header" class="p-1" role="tab">
                        <b-button block href="#" v-b-toggle.accordion-1 variant="success">Group 1</b-button>
                    </b-card-header>
                    <b-collapse id="accordion-1" visible accordion="my-accordion" role="tabpanel">
                        <b-card-body>
                            <b-list-group>
                                <b-list-group-item v-for="video in videos" v-bind:key="video.title">
                                    <router-link :to="{ name: 'videos', params: { videoId: 123 }}">{{video.title}}
                                    </router-link>
                                </b-list-group-item>
                            </b-list-group>
                        </b-card-body>
                    </b-collapse>
                </b-card>

                <b-card no-body class="mb-1">
                    <b-card-header header-tag="header" class="p-1" role="tab">
                        <b-button block href="#" v-b-toggle.accordion-2 variant="success">Group 2</b-button>
                    </b-card-header>
                    <b-collapse id="accordion-2" accordion="my-accordion" role="tabpanel">
                        <b-card-body>
                            <b-list-group>
                                <b-list-group-item v-for="video in videos" v-bind:key="video.title">
                                    <router-link :to="{ name: 'videos', params: { videoId: 123 }}">{{video.title}}
                                    </router-link>
                                </b-list-group-item>
                            </b-list-group>
                        </b-card-body>
                    </b-collapse>
                </b-card>

                <b-card no-body class="mb-1">
                    <b-card-header header-tag="header" class="p-1" role="tab">
                        <b-button block href="#" v-b-toggle.accordion-3 variant="success">Group 3</b-button>
                    </b-card-header>
                    <b-collapse id="accordion-3" accordion="my-accordion" role="tabpanel">
                        <b-card-body>
                            <b-list-group>
                                <b-list-group-item v-for="video in videos" v-bind:key="video.title">
                                    <router-link :to="{ name: 'videos', params: { videoId: 123 }}">{{video.title}}
                                    </router-link>
                                </b-list-group-item>
                            </b-list-group>
                        </b-card-body>
                    </b-collapse>
                </b-card>
            </div>
        </b-col>
        <b-col cols="8">
            <b-card-body title="Title of the video">
                <b-card-text>
                    <b-embed
                            type="iframe"
                            aspect="16by9"
                            src="https://www.youtube.com/embed/zpOULjyy-n8?rel=0"
                            allowfullscreen
                    ></b-embed>
                </b-card-text>
                <b-card-text>
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque luctus purus sit amet massa hendrerit semper at eu dui. Sed eget hendrerit tortor. Vestibulum ultrices augue eu ante elementum, eget gravida lacus semper. Sed sed lectus augue. Duis ac ex quis magna tristique ullamcorper vel in nisl. Aliquam molestie nibh non orci fringilla gravida. Curabitur id est eu mauris facilisis consectetur a quis felis. Vivamus egestas ex nisl, et viverra sem placerat vitae.
                </b-card-text>
            </b-card-body>
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
        name: 'Videos',

        data() {
            return {
                videoId: 1,

                videos: [
                    {title: "InterACTWEL for resilient food, energy, and water sectors in local communities\n", url: "https://www.youtube.com/watch?v=os5Id_58rf4"},
                    {title: "Open Channel Flow Concepts", url: "https://www.youtube.com/watch?v=8vmTYmt0Y8Q"},
                    {title: "Culvert Hydraulics", url: "https://www.youtube.com/watch?v=vnXmGyb_hKQ"}
                ],


                Videos: [
                    {
                        "Group 1": [
                            {
                                title: "InterACTWEL for resilient food, energy, and water sectors in local communities\n",
                                url: "https://www.youtube.com/watch?v=os5Id_58rf4"
                            },
                            {title: "Open Channel Flow Concepts", url: "https://www.youtube.com/watch?v=8vmTYmt0Y8Q"},
                            {title: "Culvert Hydraulics", url: "https://www.youtube.com/watch?v=vnXmGyb_hKQ"}
                        ],
                        "Group 2": [
                            {
                                title: "InterACTWEL for resilient food, energy, and water sectors in local communities\n",
                                url: "https://www.youtube.com/watch?v=os5Id_58rf4"
                            },
                            {title: "Open Channel Flow Concepts", url: "https://www.youtube.com/watch?v=8vmTYmt0Y8Q"},
                            {title: "Culvert Hydraulics", url: "https://www.youtube.com/watch?v=vnXmGyb_hKQ"}
                        ],
                    }
                ],
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
