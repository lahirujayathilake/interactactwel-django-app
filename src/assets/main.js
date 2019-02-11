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
    $('.step-progress').hide();
    $('.step1').hide();
    $('.step2').hide();
    $('.step3').hide();
    $('.step4').hide();
    $('.step5').hide();
    $('.feedback-wrapper').hide();
    $('.plan-goals').hide();
    $('#step5-submit').hide();

    // start wizard
    $('#start-viz-builder-button').click(function() {
        $('#steps-menu').show(300);
        $('#step1-menu').addClass('active');
        $('#start-viz-builder-button').hide();
        $('#exit-viz-builder-button').show();
        $('.step1').show(500);

    });

    // events on each step submissions
    $('#step1-submit').click(function() {
        $('.step1').hide(500);
        $('.step2').show(500);
        $('#step2-menu').addClass('active');
        $('#step1-menu').addClass('completed');
        $('#step1-menu').removeClass('active');
        $('#step1-menu .description').replaceWith("2 goals selected");


    });

    $('#step2-submit').click(function() {
        $('.step2').hide(500);
        $('.step3').show(500);
        $('#step3-menu').addClass('active');
        $('#step2-menu').addClass('completed');
        $('#step2-menu').removeClass('active');
        $('#step2-menu .description').replaceWith("2 actors selected");

    });

    $('#step3-submit').click(function() {
        $('.step3').hide(500);
        $('.step4').show(500);
        $('#step4-menu').addClass('active');
        $('#step3-menu').addClass('completed');
        $('#step3-menu').removeClass('active');
        $('#step3-menu .description').replaceWith("2 actions selected");

    });

    $('#step4-submit').click(function() {
        console.log("clciked");
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
        $('.feedback-wrapper').show(200);
        $('html, body').animate({
            scrollTop: $(".feedback-wrapper").offset().top
        }, 2000);

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

});


