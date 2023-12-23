$(document).ready(function () {
    var path = window.location.pathname;
    $("#sidebarCollapse").on("click", function () {
      $("#sidebar").toggleClass("active");
      $("#content").toggleClass("active");
        // Change l'icône en fonction de l'état de la barre latérale
        if ($("#sidebar").hasClass("active")) {
        $("#sidebarCollapse i").removeClass("fa fa-chevron-left").addClass("fa fa-chevron-right");
        $("#sidebarCollapse").toggleClass("active");
      } else {
        $("#sidebarCollapse i").removeClass("fa fa-chevron-right").addClass("fa fa-chevron-left");
         $("#sidebarCollapse").toggleClass("active");
      }
    });


// Trouver le lien correspondant au chemin de la page actuelle
$('.nav-link').each(function() {
  var href = $(this).attr('href');
  if (path==href) {
    // Ajouter une classe "active" au lien correspondant
    $(this).addClass('active');
  }
});


  });