<template>
    <ul class="nav nav-pills nav-justified thumbnail setup-panel step-progress-bar">
        <li v-bind:class="fromparent">
            <div href="#step-1">
            <div class="step-no">1</div>
            <h4 class="list-group-item-heading">Goals</h4>
            <p class="list-group-item-text">2 golas selected</p>
        </div></li>
        <li v-bind:class="fromparent"><div href="#step-2">
            <div class="step-no">2</div>
            <h4 class="list-group-item-heading">Actors</h4>
            <p class="list-group-item-text">Choose actors</p>
        </div></li>
        <li class=""><div href="#step-3">
            <div class="step-no">3</div>
            <h4 class="list-group-item-heading">Actions</h4>
            <p class="list-group-item-text">Choose Actions</p>
        </div></li>
        <li class=""><div href="#step-4">
            <div class="step-no">4</div>
            <h4 class="list-group-item-heading">Plans</h4>
            <p class="list-group-item-text">Visualize adaptation plans</p>
        </div></li>
        <li class=""><div href="#step-5">
            <div class="step-no">5</div>
            <h4 class="list-group-item-heading">Evaluate</h4>
            <p class="list-group-item-text">Give Feedback</p>
        </div></li>
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

    export default {
        name: 'ProgressBar',

        props: ['fromparent'],

        methods: {

            active(){
                alert('active')
            }

        }

    }


</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
    .step-progress-bar li::after{
        display: none;
        position: absolute;
        z-index: 2;
        content: '';
        top: 50%;
        right: 0;
        border: medium none;
        border-top-color: currentcolor;
        border-top-style: none;
        border-top-width: medium;
        border-right-color: currentcolor;
        border-right-style: none;
        border-right-width: medium;
        border-bottom-color: currentcolor;
        border-bottom-style: none;
        border-bottom-width: medium;
        border-left-color: currentcolor;
        border-left-style: none;
        border-left-width: medium;
        background-color: #fff;
        width: 1.14285714em;
        height: 1.14285714em;
        border-style: solid;
        border-color: rgba(34,36,38,.15);
        border-width: 0 1px 1px 0;
        -webkit-transition: background-color .1s ease,opacity .1s ease,color .1s ease,-webkit-box-shadow .1s ease;
        transition: background-color .1s ease,opacity .1s ease,color .1s ease,-webkit-box-shadow .1s ease;
        transition: background-color .1s ease,opacity .1s ease,color .1s ease,box-shadow .1s ease;
        transition: background-color .1s ease,opacity .1s ease,color .1s ease,box-shadow .1s ease,-webkit-box-shadow .1s ease;
        -webkit-transform: translateY(-50%) translateX(50%) rotate(-45deg);
        transform: translateY(-50%) translateX(50%) rotate(-45deg);
    }

    .step-progress-bar li{
        padding: 1rem 1rem 1rem 2rem;
        width:20%;
    background-color: #f5f8fa;
        border-right:1px solid #B0BEC5;
}

    .step-progress-bar h4{
        font-size: 1.14285714em;
        font-weight: 700;
        color:#5f6c73;
        margin-bottom: .05rem;
    }

    .step-progress-bar p{
        font-weight: 400;
        font-size: .82857143em;
        color: #5f6c73;
        margin-bottom: 0;
    }

    .step-progress-bar .step-no{
        float: left;
        font-size:30px;
        font-weight:700;
        color: #5f6c73;
        width:30px;
    }

    .step-progress-bar .active{
        background: #DCEDC8;
    }
</style>