/**
 * Created by Benoit on 2017-04-19.
 */
$(document).ready(function () {
    $(".widget-delete-icon").on("click", function (event) {
        var dashboardUUID = $(".dashboard").attr("id");
        var widgetUUID = $(event.target).closest(".widget-holder").attr("id");
        var queryParams = "?dashboard-uuid=" + dashboardUUID + "&widget-uuid=" + widgetUUID;

        jQuery.ajax({
            url: "http://localhost:8000/dashboards/widget" + queryParams,
            type: "DELETE",
            success: function (resultData) {
                swal({
                    title: "Deleted",
                    text: "The widget has been successfully deleted",
                    type: "success"
                }, function () {
                    location.reload();
                });
            },
            error: function (jqXHR, textStatus, errorThrown) {
                sweetAlert("Oops...", "An error has occurred while deleting the widget", "error");
            },

            timeout: 12000000
        });
    });


    $('[data-toggle="tooltip"]').tooltip();
});