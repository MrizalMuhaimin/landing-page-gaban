$(function() {
    $(".list-sponsor").slick({
        dots: true,
        infinite: true,
        centerMode: true,
        centerPadding: '60px',
        speed: 300,
        focusOnSelect: true,
        // slidesToShow: 1.5,
        slidesToScroll: 1,
        variableWidth: true,
        autoplay: true,
        autoplaySpeed: 2000,
        // prevArrow : '<i class="far fa-arrow-alt-circle-left prev_program"></i>',
        prevArrow: ".prev_program",
        nextArrow : ".next_program",
        
    });
});

