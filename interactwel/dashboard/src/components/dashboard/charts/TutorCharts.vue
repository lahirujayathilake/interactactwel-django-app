<template>
    <div id="graph" class="card">
        
            <div class="card-header"><span v-on:click="dismiss" class="close"><font-awesome-icon
                icon="times-circle"/> Close</span>
                <strong>What are Adaptation Plans?</strong>
            </div>
            <div class="card-body">
            <p align="justify" style="font-size: 17px;">In this section you will be able to view multiple adaptation plans that incorporate the actors <strong>(Step 2)</strong> and actions <strong>(Step 3)</strong> that you selected.  You can compare how each adaptation plan meets the goals you selected in <strong>Step 1</strong> for the entire basin, sub-basins, and individual streams.  You can also compare the actions and their timeframes included within each plan.</p>
            <p aling="justify">Remember that you can click the map to visualize the data. </p>
            </div>
        
            <footer class="tutor-footer">
          <slot name="footer">
            <button type="button" class="btn-close" @click="dismiss">Continue</button>
            
          </slot>
        </footer>
    </div>
</template>

<script>

    import EventBus from './../../../event-bus';

    export default {
        name: 'TutorGraph',

        methods: {
            dismiss() {
                EventBus.$emit('CLOSE');
            },
            close() {
                this.$emit('close');
            },
        },
        //props: ["jsonData"]
    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
