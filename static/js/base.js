$(document).ready(function () {

    // hide elements on page load
    $('#sidebar-left').hide();
    $('#sidebar-right').hide();
    $('#steps-menu').hide();
    $('.step1').hide();
    $('.step2').hide();
    $('.step3').hide();
    $('#exit-viz-builder-button').hide();
    $('.plans-wrapper').hide();
    $('#adpation-plans-list').hide();
    $('#no-feasible').hide();

    //legend toggle

    if($('#toggle-legend').prop('checked')) {
        $('.legend').show(500);
    }else{
        $('.legend').hide(500);
    }

    $('#toggle-legend').change(function(){
        $('.legend').toggle(500);

    });

    //legend miniglobe

    if($('#toggle-miniglobe').prop('checked')) {
        $('.leaflet-control-minimap').show(500);
    }else{
        $('.leaflet-control-minimap').hide(500);
    }

    $('#toggle-miniglobe').change(function(){
        $('.leaflet-control-minimap').toggle(500);

    });

    //legend zoombar

    if($('#toggle-zoom').prop('checked')) {
        $('.leaflet-control-zoom').show(500);
    }else{
        $('.leaflet-control-zoom').hide(500);
    }

    $('#toggle-zoom').change(function(){
        $('.leaflet-control-zoom').toggle(500);

    });

    //legend scale

    if($('#toggle-scale').prop('checked')) {
        $('.leaflet-control-scale').show(500);
    }else{
        $('.leaflet-control-scale').hide(500);
    }

    $('#toggle-scale').change(function(){
        $('.leaflet-control-scale').toggle(500);

    });


    // start wizard
    $('#start-viz-builder-button').click(function() {
        $('#steps-menu').show(300);
        $('#step1-menu').addClass('active');
        $('#start-viz-builder-button').hide();
        $('#exit-viz-builder-button').show();
        $('.step1').show(500);
        $('#sidebar-left').show(500);


    });

    // End wizard
    $('#exit-viz-builder-button').click(function() {
        $('.ui.basic.modal')
            .modal('show')
        ;
    });

    // more info expands
    $('.checkbox-info').hide();
    $('.more-info').hide();

    $('.checkbox-info-button').click( function(){
        $(this).next('.checkbox-info').toggle(500);
    });

    $('.more-info-button').click( function(){
        $(this).next('.more-info').toggle(500);
    });


    // events on step 1 submission
    $('#step1-submit').click(function() {
        $('.step1').hide(500);
        $('.step2').show(500);
        $('#step2-menu').addClass('active');
        $('#step1-menu').addClass('completed');
        $('#step1-menu').removeClass('active');
        $('#step1-menu .description').replaceWith("2 goals selected");

        var fields = {};
        $('.step1-checkbox').each(function(){

            if($(this). prop("checked") == true){
                fields[this.id] = true;
            }else{
                fields[this.id] = false;
            }
        });

        localStorage.setItem('step1-data',JSON.stringify(fields));

        console.log(localStorage.getItem('step1-data'));               // Output: {"field-01":"on","field-02":"1234"}
        console.log(JSON.parse(localStorage.getItem('step1-data')));


    });

    $('#step2-submit').click(function() {
        $('.step2').hide(500);
        $('.step3').show(500);
        $('#step3-menu').addClass('active');
        $('#step2-menu').addClass('completed');
        $('#step2-menu').removeClass('active');
        $('#step2-menu .description').replaceWith("2 actors selected");

        var fields = {};
        $('.step2-checkbox').each(function(){

            if($(this). prop("checked") == true){
                fields[this.id] = true;
            }else{
                fields[this.id] = false;
            }
        });

        localStorage.setItem('step2-data',JSON.stringify(fields));

        console.log(localStorage.getItem('step2-data'));               // Output: {"field-01":"on","field-02":"1234"}
        console.log(JSON.parse(localStorage.getItem('step2-data')));

    });

    $('#step2-back').click(function() {
        $('.step2').hide(500);
        $('.step1').show(500);
    });

    $('#step3-submit').click(function() {
        $('.step3').hide(500);
        $('.step4').show(500);
        $('#step4-menu').addClass('active');
        $('#step3-menu').addClass('completed');
        $('#step3-menu').removeClass('active');
        $('#step3-menu .description').replaceWith("2 actions selected");
        $('#steps-menu').hide(500);
        $('#adpation-plans-list').show(500);
        $('.plans-wrapper').show(500);

    });

    $('#step3-back').click(function() {
        $('.step3').hide(500);
        $('.step2').show(500);
    });

    $('#evaluate-plan').click(function() {
        $('#sidebar-right').show(500);
    });

    // check feedback form radio button
    if(document.getElementById('feasibility-no').checked) {
        $('#no-feasible').show();
    }else{
        $('#no-feasible').hide();
    }

    $('#feasibility-no').change(function(){
        if(document.getElementById('feasibility-no').checked) {
            $('#no-feasible').show();
        }else{
            $('#no-feasible').hide();
        }

    });


});