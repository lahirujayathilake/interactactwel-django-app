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

    $('.ui.accordion')
        .accordion()
    ;

// popup menu on hover
    $('.menu .settings')
        .popup({
            inline: true,
            popup: '.settings-menu-content.popup',
            on: 'click',
            position: 'bottom right',
            delay: {
                show: 300,
                hide: 300
            }
        });

    $('.menu .account')
        .popup({
            inline: true,
            popup: '.account-menu-content.popup',
            on: 'click',
            position: 'bottom right',
            delay: {
                show: 300,
                hide: 300
            }
        });

    $('#step1-menu')
        .popup({
            inline: true,
            popup: '.step1-menu-content.popup',
            hoverable: true,
            position: 'bottom left',
            variation: 'inverted small',
            delay: {
                show: 300,
                hide: 300
            }
        });

    $('#step2-menu')
        .popup({
            inline: true,
            popup: '.step2-menu-content.popup',
            hoverable: true,
            position: 'bottom left',
            variation: 'inverted small',
            delay: {
                show: 300,
                hide: 300
            }
        });

    $('#step3-menu')
        .popup({
            inline: true,
            popup: '.step3-menu-content.popup',
            hoverable: true,
            position: 'bottom left',
            variation: 'inverted small',
            delay: {
                show: 300,
                hide: 300
            }
        });

    $('#step4-menu')
        .popup({
            inline: true,
            popup: '.step4-menu-content.popup',
            hoverable: true,
            position: 'bottom left',
            variation: 'inverted small',
            delay: {
                show: 300,
                hide: 300
            }
        });

    $('#step5-menu')
        .popup({
            inline: true,
            popup: '.step5-menu-content.popup',
            hoverable: true,
            position: 'bottom left',
            variation: 'inverted small',
            delay: {
                show: 300,
                hide: 300
            }
        });

});