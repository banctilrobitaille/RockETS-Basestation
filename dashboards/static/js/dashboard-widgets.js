/**
 * Created by Benoit on 2017-03-29.
 */
$(document).ready(function () {
    $(".dashboard-widget-delete-icon").on("click", function (event) {
        var dashboardId = event.target.id;
        var queryParams = "?uuid=" + dashboardId;

        jQuery.ajax({
            url: "http://localhost:8000/dashboards" + queryParams,
            type: "DELETE",
            success: function (resultData) {
                swal({
                    title: "Deleted",
                    text: "Dashboard has been successfully deleted",
                    type: "success"
                }, function () {
                    location.reload();
                });
            },
            error: function (jqXHR, textStatus, errorThrown) {
                sweetAlert("Oops...", "An error has occurred while deleting the dashboard", "error");
            },

            timeout: 12000000
        });
    });

    $(".dashboard-widget").on("click", function (event) {
        if (!$(event.target).hasClass("fa")) {
            var dashboardId = event.currentTarget.id;
            var queryParams = "?uuid=" + dashboardId;
            window.location.href = "http://localhost:8000/dashboards" + queryParams;
        }
    });
});