$(document).ready(function(){
  $('.owl-carousel').owlCarousel({
    thumbs: true,
    thumbsPrerendered: true,
    items:1,
    autoplay:true,
    autoplayTimeout:4000,
     nav: true,
       navText: ['<i class="icon-back-8"></i>', '<i class="icon-next-11"></i>'],
        dots: false

    

  });
});