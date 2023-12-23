$(document).ready(function () {
  var navbar = $(".navbar");

  $(window).scroll(function () {
      if ($(window).scrollTop() > 56) { /* Ajustez la hauteur ici si nécessaire */
          navbar.addClass("fixed-top");
      } else {
          navbar.removeClass("fixed-top");
      }
  });
});
