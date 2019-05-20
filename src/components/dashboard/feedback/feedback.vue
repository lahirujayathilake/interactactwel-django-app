<template>
    <div class="feedback-container">
        <div class="header-container">
            <!-- <h6>POPSWAT_0</h6> -->
            <h4>Evaluate Adaptation Plan</h4>
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
            <div hidden id="no-feasible" class="grouped fields">
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
                    <textarea placeholder="Feel free to add additional comments about your rating here:"
                              rows="7"></textarea>
                </div>
            </div>
            <b-button variant="success">Submit</b-button>
        </div>

    </div>
</template>

<script>

    export default {
        name: 'Feedback'
    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>

    #feedback-step1 {
        background-color: #f5f8fa;
        padding: 20px;
        border-radius: 10px;
        margin-top: 20px;
    }

    .header-container {
        padding: 0 10px;
    }

</style>