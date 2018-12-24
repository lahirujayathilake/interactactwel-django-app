$(document).ready(function () {

    // tab menu
    $('.menu .item')
        .tab()
    ;

    // drop down
    $('.ui.dropdown')
        .dropdown()
    ;

    // Star rating
    $('.ui.rating')
        .rating()
    ;

    $('.checkbox-info-button')
        .popup({
            inline: true
        })
    ;


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

    // popup menu on hover
    $('.menu .settings')
        .popup({
            inline   : true,
            popup: '.settings-menu-content.popup',
            on: 'click',
            position : 'bottom right',
            delay: {
                show: 300,
                hide: 300
            }
        });

    $('.menu .account')
        .popup({
            inline   : true,
            popup: '.account-menu-content.popup',
            on: 'click',
            position : 'bottom right',
            delay: {
                show: 300,
                hide: 300
            }
        });

    $('#step1-menu')
        .popup({
            inline   : true,
            popup: '.step1-menu-content.popup',
            hoverable: true,
            position : 'bottom left',
            variation: 'inverted small',
            delay: {
                show: 300,
                hide: 300
            }
        });

    $('#step2-menu')
        .popup({
            inline   : true,
            popup: '.step2-menu-content.popup',
            hoverable: true,
            position : 'bottom left',
            variation: 'inverted small',
            delay: {
                show: 300,
                hide: 300
            }
        });

    $('#step3-menu')
        .popup({
            inline   : true,
            popup: '.step3-menu-content.popup',
            hoverable: true,
            position : 'bottom left',
            variation: 'inverted small',
            delay: {
                show: 300,
                hide: 300
            }
        });

    $('#step4-menu')
        .popup({
            inline   : true,
            popup: '.step4-menu-content.popup',
            hoverable: true,
            position : 'bottom left',
            variation: 'inverted small',
            delay: {
                show: 300,
                hide: 300
            }
        });

    $('#step5-menu')
        .popup({
            inline   : true,
            popup: '.step5-menu-content.popup',
            hoverable: true,
            position : 'bottom left',
            variation: 'inverted small',
            delay: {
                show: 300,
                hide: 300
            }
        });

    // Hide elements on page load
    $('#steps-menu').hide();
    $('#exit-viz-builder-button').hide();
    $('.step-progress').hide();
    $('.step1').hide();
    $('.step2').hide();
    $('.step3').hide();
    $('.step4').hide();
    $('.step5').hide();
    $('.feedback-wrapper').hide();
    $('.plan-goals').hide();
    $('#step5-submit').hide();
    $('.feedback-forum').hide();
    $('.feasibility-forum').hide();


    // start wizard
    $('#start-viz-builder-button').click(function() {
        $('#steps-menu').show(300);
        $('#step1-menu').addClass('active');
        $('#start-viz-builder-button').hide();
        $('#exit-viz-builder-button').show();
        $('.step1').show(500);

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

    });

    $('#step3-back').click(function() {
        $('.step3').hide(500);
        $('.step2').show(500);
    });

    $('#step4-submit').click(function() {
        $('#step4-submit').hide();
        $('.plan-goals').show(500);
        $('#step5-submit').show(500);
        $('#step5-menu').addClass('active');
        $('#step4-menu').addClass('completed');
        $('#step4-menu').removeClass('active');
        $('#step4-menu .description').replaceWith("Plan 1");

    });

    $('#step5-submit').click(function() {
        $('#step5-submit').hide();
        $('#step6-menu').addClass('active');
        $('#step5-menu').addClass('completed');
        $('#step5-menu').removeClass('active');
        $('#step5-menu .description').replaceWith("Plan 1");
        $('#evaluate').show(200);
        $('html, body').animate({
            scrollTop: $(".feedback-wrapper").offset().top
        }, 2000);

    });


    $('#evaluate-submit').click(function() {
        $('#sidebar').show(200);
        $('.feasibility-forum').hide(200);
        $('.feedback-forum').show(200);

        /*var fields = {};
        $('.step2-checkbox').each(function(){

            if($(this). prop("checked") == true){
                fields[this.id] = true;
            }else{
                fields[this.id] = false;
            }
        });

        localStorage.setItem('step2-data',JSON.stringify(fields));

        console.log(localStorage.getItem('step2-data'));               // Output: {"field-01":"on","field-02":"1234"}
        console.log(JSON.parse(localStorage.getItem('step2-data')));*/



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


    //Check and uncheck All checkboxes
    $('#step1-select-all-checkbox').change(function(){
        if($('.step1-checkbox:checkbox').prop('checked')) {
            $('.step1-checkbox:checkbox').prop("checked", false);
            $("#step1-select-all-checkbox-label").html("Select All");
        }else{
            $('.step1-checkbox:checkbox').prop("checked", true);
            $("#step1-select-all-checkbox-label").html("Clear All");
        }
    });

    $('#step2-select-all-checkbox').change(function(){
        if($('.step2-checkbox:checkbox').prop('checked')) {
            $('.step2-checkbox:checkbox').prop("checked", false);
            $("#step2-select-all-checkbox-label").html("Select All");
        }else{
            $('.step2-checkbox:checkbox').prop("checked", true);
            $("#step2-select-all-checkbox-label").html("Clear All");
        }
    });

    $('#step3-select-all-checkbox').change(function(){
        if($('.step3-checkbox:checkbox').prop('checked')) {
            $('.step3-checkbox:checkbox').prop("checked", false);
            $("#step3-select-all-checkbox-label").html("Select All");
        }else{
            $('.step3-checkbox:checkbox').prop("checked", true);
            $("#step3-select-all-checkbox-label").html("Clear All");
        }
    });

});


