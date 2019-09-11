$(document).ready(function() {
    



    $('.owl-2').owlCarousel({

        loop: true,
        margin: 0,
        autoplay: true,
        autoplayTimeout: 3000,
        dots: false,
        nav: true,
        navText: ['<i class="icon-back-8"></i>', '<i class="icon-next-11"></i>'],
        responsive: {
            0: {
                items: 1
            },
            600: {
                items: 2
            },
            1000: {
                items: 3
            }
        }
    });
    $('.owl-Four').owlCarousel({

        loop: true,
        margin: 0,
        autoplay: true,
        autoplayTimeout: 3000,

        nav: false,
        navText: ['<i class="icon-back-2"></i>', '<i class="icon-next-4"></i>'],
        responsive: {
            0: {
                items: 1
            },
            600: {
                items: 1
            },
            1000: {
                items: 1
            }
        }
    });







});