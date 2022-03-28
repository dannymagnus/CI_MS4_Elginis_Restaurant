/**
 * To rotate images in the  reasons for us carousel
 * Credit:  https://getbootstrap.com/docs/5.0/components/carousel/ ]
 */
 var myCarousel = document.querySelector('#reasons-carousel');
 var carousel = new bootstrap.Carousel(myCarousel, {
     interval: 2000,
     wrap: true,
     pause: false
 });