/**
 * Created by Benoit on 2017-04-04.
 */
$(document).ready(function () {
    var path = window.location.pathname;
    path = path.replace(/\/$/, "");
    path = decodeURIComponent(path);

    $(".menu-tab-link").each(function () {
        var href = $(this).attr('href');
        if (path !== "") {
            if (path === href) {
                $(this).find('li').addClass('active');
            }
        } else {
            $("#menu-tab-home").addClass("active");
        }
    });
});