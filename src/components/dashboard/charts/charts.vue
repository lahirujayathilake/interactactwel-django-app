<template>
    <div class="chart">
        <div class="feedback-container">
            <div class="ui header">
                <div class="ui sub header">POPSWAT_0</div>
                Evaluate Adaptation Plan
            </div>
            <div id="feedback-step1" class="ui form">
                <div class="field">
                    <label>Do you think this Alternative plan is feasible?</label>
                    <div class="inline fields">
                        <div class="field">
                            <div class="ui radio checkbox">
                                <input class="" type="radio" name="feasibility" id="feasibility-yes">
                                <label>Yes</label>
                            </div>
                            <div class="ui radio checkbox">
                                <input class="" type="radio" name="feasibility" id="feasibility-no">
                                <label>No</label>
                            </div>
                            <div class="ui radio checkbox">
                                <input class="" type="radio" name="feasibility" id="feasibility-maybe">
                                <label>May be</label>
                            </div>
                        </div>
                    </div>
                </div>
                <div id="no-feasible" class="grouped fields">
                    <label>why is this plan not feasible? (Check all that apply)</label>
                    <div class="field">
                        <div class="ui checkbox">
                            <input type="checkbox" name="top-posts">
                            <label>Unlikely to be profitable / financially sustainable</label>
                        </div>
                    </div>
                    <div class="field">
                        <div class="ui checkbox">
                            <input type="checkbox" name="hot-deals">
                            <label>Infrastructure costs</label>
                        </div>
                    </div>
                    <div class="field">
                        <div class="ui checkbox">
                            <input type="checkbox" name="hot-deals">
                            <label>Permits or other regulatory approval processes and cost</label>
                        </div>
                    </div>
                    <div class="field">
                        <div class="ui checkbox">
                            <input type="checkbox" name="hot-deals">
                            <label>Reliance on other stakeholders to take action</label>
                        </div>
                    </div>
                    <div class="field">
                        <div class="ui checkbox">
                            <input type="checkbox" name="hot-deals">
                            <label>Long time period before seeing positive results</label>
                        </div>
                    </div>
                    <div class="field">
                        <div class="ui checkbox">
                            <input type="checkbox" name="hot-deals">
                            <label>Public disapproval of the actions listed in the plans</label>
                        </div>
                    </div>
                    <div class="field">
                        <div class="ui checkbox">
                            <input type="checkbox" name="hot-deals">
                            <label>Other</label>
                        </div>
                    </div>
                    <div class="field wide">
                        <label>Short Text</label>
                        <textarea placeholder="Feel free to add additional comments about your rating here:" rows="7"></textarea>
                    </div>
                </div>
                <button type="reset" class="ui small button" tabindex="0">Clear</button>
                <button id="evaluate-submit" class="ui small green button" tabindex="0">Submit</button>
            </div>

        </div>
    </div>
</template>

<script>

    export default {
        name: 'Charts'
    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>

    .chart{
        position: absolute;
        top:100px;
        left:600px;
        z-index: 1000;
    }
</style>