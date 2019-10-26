<template>
    <div>
        <component v-bind:is="component='Header'"></component>
        <b-container fluid class="main">
            <b-container>
                <b-breadcrumb :items="breadcrumb"></b-breadcrumb>
                <b-row>
                    <b-col>
                        <b-card no-body class="main-wrapper">
                            <b-tabs pills card vertical>
                                <b-tab title="Members" active class="main-wrapper">
                                    <b-card-text>
                                        <b-container>
                                            <b-row>
                                                <b-col lg="8">
                                                    <h4 class="card-title">Current Members</h4>
                                                    <b-container>
                                                        <b-row>
                                                            <b-col>
                                                                <b-button size="sm">See All Members</b-button>
                                                                <b-button class="mr-2" size="sm">Create List</b-button>
                                                            </b-col>
                                                        </b-row>
                                                    </b-container>
                                                    <b-container class="mt-3">
                                                        <b-row>
                                                            <b-col>
                                                                <b-list-group>
                                                                    <b-list-group-item>Andrew Smith</b-list-group-item>
                                                                    <b-list-group-item>John Doe</b-list-group-item>
                                                                    <b-list-group-item>Nick Harrison</b-list-group-item>
                                                                    <b-list-group-item>Justin Watson</b-list-group-item>
                                                                    <!--<b-list-group-item>Vestibulum at eros
                                                                    </b-list-group-item>-->
                                                                </b-list-group>
                                                            </b-col>
                                                        </b-row>
                                                    </b-container>
                                                </b-col>
                                                <b-col lg="4">
                                                    <b-container>
                                                        <b-row>
                                                            <b-col class="widget">
                                                                <div class="widget-title">Invite Members</div>
                                                                <b-list-group class="mt-2">
                                                                    <b-list-group-item>Andrew Smith
                                                                        <b-button size="sm">Invite</b-button>
                                                                    </b-list-group-item>
                                                                    <b-list-group-item>John Doe
                                                                        <b-button size="sm">Invite</b-button>
                                                                    </b-list-group-item>
                                                                    <b-list-group-item>Nick Harrison
                                                                        <b-button size="sm">Invite</b-button>
                                                                    </b-list-group-item>
                                                                    <b-list-group-item>Justin Watson
                                                                        <b-button size="sm">Invite</b-button>
                                                                    </b-list-group-item>
                                                                    <!--<b-list-group-item>Vestibulum at eros
                                                                        <b-button size="sm">Invite</b-button>
                                                                    </b-list-group-item> -->
                                                                </b-list-group>
                                                            </b-col>
                                                        </b-row>
                                                        <b-row>
                                                            <b-col class="widget">
                                                                <div class="widget-title">
                                                                    Members you may connected with
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
                                                                    <!--<b-list-group-item>Vestibulum at eros
                                                                        <b-button size="sm">Connect</b-button>
                                                                    </b-list-group-item> -->
                                                                </b-list-group>
                                                            </b-col>
                                                        </b-row>
                                                    </b-container>
                                                </b-col>
                                            </b-row>
                                        </b-container>
                                    </b-card-text>
                                </b-tab>
                                <b-tab title="Events" class="main-wrapper">
                                    <b-card-text>
                                        <b-container>
                                            <b-row>
                                                <b-col lg="8">
                                                    <h4 class="card-title">Events</h4>
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
                                        </b-container>
                                    </b-card-text>
                                </b-tab>
                                <b-tab title="Groups" class="main-wrapper">
                                    <b-card-text>
                                        <b-container>
                                            <b-row>
                                                <b-col lg="8">
                                                    <h4 class="card-title">Groups</h4>
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
                                        </b-container>
                                    </b-card-text>
                                </b-tab>
                            </b-tabs>
                        </b-card>
                    </b-col>
                </b-row>
            </b-container>
        </b-container>
        <component v-bind:is="component='Footer'"></component>
    </div>
</template>

<script>
    import EventBus from './../../event-bus';
    import Header from './Header.vue';
    import Footer from './Footer.vue';

    export default {
        components: {
            Header, Footer
        },
        name: 'Community',

        data() {
            return {
                breadcrumb: [
                    {
                        text: 'Home',
                        to: { name: 'Home' }
                    },
                    {
                        text: 'Community',
                        to: { name: 'Community' },
                        active: true
                    }
                ]
            }
        },

        mounted() {
        },


        methods: {}

    }

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
    .main-wrapper {
        min-height: 60vh;
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

