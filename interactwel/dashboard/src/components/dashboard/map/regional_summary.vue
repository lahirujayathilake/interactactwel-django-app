<template>
    <GChart :resizeDebounce="500"
            type="BarChart"
            :data="chartData"
            :options="chartOptions"
    />
</template>

<script>
  import { GChart } from 'vue-google-charts'
  
  export default {
    name: 'regional_summary',

    components: {
            GChart,
        },
        
    methods: {
      close() {
        this.$emit('close');
      },
    },
  };
</script>
