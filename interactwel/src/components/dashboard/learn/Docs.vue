<template>
  <b-row>
    <b-col cols="3">
      <b-list-group>
        <b-list-group-item href="#some-link">
          Getting Started
        </b-list-group-item>
        <b-list-group-item href="#">
          What are Adaptation Plans
        </b-list-group-item>
        <b-list-group-item href="#">
          How to generate new plans
        </b-list-group-item>
        <b-list-group-item href="#foobar">
          How to save plans
        </b-list-group-item>
      </b-list-group>
    </b-col>
    <b-col cols="9">
      <b-card-body title="Getting Started">
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
  name: 'Docs',
  components: {
    Header, Footer,
  },

  data() {
    return {

    };
  },

  mounted() {
  }
  ,

  methods: {},

};

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
