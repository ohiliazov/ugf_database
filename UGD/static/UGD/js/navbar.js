$(document).ready(function () {
    var navbar = $(document).find(".navbar-nav").children();
    var current_url = window.location.pathname;
    navbar.each(function () {
        if ($(this).children().attr("href") == current_url) {
            $(this).toggleClass("active");
        }
    })
});