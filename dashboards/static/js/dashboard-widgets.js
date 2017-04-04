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
                swal("Great", "Dashboard deleted successfully", "success")
            },
            error: function (jqXHR, textStatus, errorThrown) {
                sweetAlert("Oops...", "An error has occurred while deleting the dashboard", "error");
            },

            timeout: 12000000
        });
    });
});