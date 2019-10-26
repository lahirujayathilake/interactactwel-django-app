<template>
    <div>
        <component v-bind:is="component='Header'"></component>
        <b-container fluid class="main">

                <b-breadcrumb :items="breadcrumb"></b-breadcrumb>
                <b-row>
                    <b-col lg="2">
                        <b-list-group>
                            <b-list-group-item><router-link to="/community/members">Members</router-link></b-list-group-item>
                            <b-list-group-item><router-link to="/community/events">Events</router-link></b-list-group-item>
                            <b-list-group-item><router-link to="/community/groups">Groups</router-link></b-list-group-item>
                        </b-list-group>
                    </b-col>
                    <b-col lg="10">
                        <router-view></router-view>
                    </b-col>
                </b-row>
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

