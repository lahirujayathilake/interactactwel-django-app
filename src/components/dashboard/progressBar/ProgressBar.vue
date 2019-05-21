<template>
    <ul class="nav nav-pills nav-justified thumbnail setup-panel step-progress-bar">
        <li class="active arrow_box">
            <div href="#step-1">
                <div class="step-no">1</div>
                <h4 class="list-group-item-heading">Goals</h4>
                <p class="list-group-item-text">{{step1_desc}}</p>
            </div>
        </li>
        <li v-bind:class="{active: isStep2Active}" class="arrow_box">
            <div href="#step-2">
                <div class="step-no">2</div>
                <h4 class="list-group-item-heading">Actors</h4>
                <p class="list-group-item-text">{{step2_desc}}</p>
            </div>
        </li>
        <li v-bind:class="{active: isStep3Active}" class="arrow_box">
            <div href="#step-3">
                <div class="step-no">3</div>
                <h4 class="list-group-item-heading">Actions</h4>
                <p class="list-group-item-text">{{step3_desc}}</p>
            </div>
        </li>
        <li v-bind:class="{active: isStep4Active}" class="arrow_box">
            <div href="#step-4">
                <div class="step-no">4</div>
                <h4 class="list-group-item-heading">Plans</h4>
                <p class="list-group-item-text">{{step4_desc}}</p>
            </div>
        </li>
        <li v-bind:class="{active: isStep5Active}" class="arrow_box">
            <div href="#step-5">
                <div class="step-no">5</div>
                <h4 class="list-group-item-heading">Evaluate</h4>
                <p class="list-group-item-text">{{step5_desc}}</p>
            </div>
        </li>
    </ul>
    <!--<div id="steps-menu" class="ui ordered steps fluid no-margin">
        <div id="step1-menu" class="step">
            <div class="content">
                <div class="title">Goals</div>
                <div class="description">Choose goals</div>
            </div>
        </div>
        <div id="step2-menu" class="step">
            <div class="content">
                <div class="title">Actors</div>
                <div class="description">Choose actors</div>
            </div>
        </div>
        <div id="step3-menu" class="step">
            <div class="content">
                <div class="title">Actions</div>
                <div class="description">Choose actions</div>
            </div>
        </div>
        <div id="step4-menu" class="step">
            <div class="content">
                <div class="title">Plans</div>
                <div class="description">Visualize adaptation plans</div>
            </div>
        </div>
        <div id="step6-menu" class="step">
            <div class="content">
                <div class="title">Evaluate</div>
                <div class="description">Explore Performance and Rate</div>
            </div>
        </div>
    </div>-->
</template>

<script>

    import EventBus from './../../../event-bus';

    export default {
        name: 'ProgressBar',

        props: ['fromparent'],

        data() {
            return {

                step1_desc: "Choose Goals",
                step2_desc: "Choose Actors",
                step3_desc: "Choose Actions",
                step4_desc: "Visualize Adaptation plans",
                step5_desc: "Give Feedback",

                isStep1Active: false,
                isStep2Active: false,
                isStep3Active: false,
                isStep4Active: false,
                isStep5Active: false,
            }
        },

        mounted(){
            let $this = this;
            EventBus.$on('MOVE_TO_STEP2', function (selectedGoalsCount) {
                $this.isStep2Active = true;
                $this.step1_desc = selectedGoalsCount + " GOALS SELECTED";
            })
            EventBus.$on('MOVE_TO_STEP3', function (selectedActorsCount) {
                $this.isStep3Active = true;
                $this.step2_desc = selectedActorsCount + " ACTORS SELECTED";
            })
            EventBus.$on('MOVE_TO_STEP4', function (selectedActionsCount) {
                $this.isStep4Active = true;
                $this.step3_desc = selectedActionsCount + " ACTIONS SELECTED";
            })
        },

        methods: {

            active() {
                alert('active')
            }

        }

    }


</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>

    .step-progress-bar li {
        padding: 10px 5rem 10px 30px;
        width: 20%;
        background-color: #f5f8fa;
    }

    .step-progress-bar h4 {
        font-size: 1em;
        font-weight: 700;
        color: #5f6c73;
        margin-bottom: .05rem;
    }

    .step-progress-bar p {
        font-weight: 400;
        font-size: .72857143em;
        color: #5f6c73;
        margin-bottom: 0;
    }

    .step-progress-bar .step-no {
        float: left;
        font-size: 25px;
        font-weight: 700;
        color: #28a745;
        width: 30px;
    }

    .step-progress-bar .active {
        background: #DCEDC8;
    }

    .arrow_box {
        position: relative;
        background: #DCEDC8;
        border-right: 2px solid #28a745;
        border-left: none;
    }
    .arrow_box:after, .arrow_box:before {
        left: 100%;
        top: 50%;
        border: solid transparent;
        content: " ";
        height: 0;
        width: 0;
        position: absolute;
        pointer-events: none;
    }

    .arrow_box:after {
        border-color: rgba(136, 183, 213, 0);
        border-left-color: #28a745;
        border-width: 11px;
        margin-top: -11px;
    }
    .arrow_box:before {
        border-color: rgba(95, 108, 115, 0);
        border-left-color: #28a745;
        border-width: 10px;
        margin-top: -10px;
        z-index: 1 !important;
    }
</style>