/**
 * Created by Benoit on 2017-05-05.
 */
$(document).ready(function () {
    $(".monitored-object-widget").on("click", function (event) {
        if (!$(event.target).hasClass("fa")) {
            var monitoredObjectId = event.currentTarget.id;
            var queryParams = "?uuid=" + monitoredObjectId;
            window.location.href = "http://localhost:8000/telemetry/monitored-object" + queryParams;
        }
    });

    $(".monitored-object-widget-delete-icon").on("click", function (event) {
        var monitoredObjectId = event.target.closest(".monitored-object-widget").id;
        var queryParams = "?uuid=" + monitoredObjectId;

        jQuery.ajax({
            url: "http://localhost:8000/telemetry/monitored-object" + queryParams,
            type: "DELETE",
            success: function (resultData) {
                swal({
                    title: "Deleted",
                    text: "The monitored object has been successfully deleted",
                    type: "success"
                }, function () {
                    location.reload();
                });
            },
            error: function (jqXHR, textStatus, errorThrown) {
                sweetAlert("Oops...", "An error has occurred while deleting the monitored object", "error");
            },

            timeout: 12000000
        });
    });
});

