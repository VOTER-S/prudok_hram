document.addEventListener('DOMContentLoaded', function () {
    var TrandingSlider = new Swiper('.tranding-slider', {
        effect: 'coverflow',
        centeredSlides: true,
        loop: true,
        slidesPerView: 'auto',
        coverflowEffect: {
          rotate: 0,
          stretch: 0,
          depth: 100,
          modifier: 2.5,
        },
        pagination: {
          el: '.swiper-pagination',
          clickable: true,
        },
        navigation: {
          nextEl: '.swiper-button-next',
          prevEl: '.swiper-button-prev',
        },
        allowTouchMove: false, // Отключаем прокрутку свайпами
    });
});


  window.addEventListener("load", function() {
    const preloader = document.getElementById("preloader");
    preloader.style.opacity = "0";
    preloader.style.pointerEvents = "none";
    setTimeout(() => {
      preloader.remove();
    }, 500); // Мягкое исчезновение
  });

