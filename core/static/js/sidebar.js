/**
 * Created by Benoit on 2017-04-04.
 */
$(document).ready(function () {
    const ROOT_PATH = "/";
    var path = window.location.pathname;
    path = path.replace(/\/$/, "");
    path = decodeURIComponent(path);

    $(".menu-tab-link").each(function () {
        var href = $(this).attr('href');

        if (path === ROOT_PATH || path === "") {
            $("#menu-tab-home").addClass("active");
        } else if (href !== ROOT_PATH) {
            if (path.includes(href)) {
                $(this).find('li').addClass('active');
            }
        }
    });
});