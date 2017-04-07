/**
 * Created by Benoit on 2017-03-31.
 */
$(document).ready(function () {
    $(".dashboard-widget").on("click", function (event) {
        //event.currentTarget.preventDefault();

        var dashboardId = event.currentTarget.id;
        var queryParams = "?uuid=" + dashboardId;

        window.location.href = "http://localhost:8000/dashboards" + queryParams;
    });
});