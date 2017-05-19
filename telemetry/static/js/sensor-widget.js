/**
 * Created by Benoit on 2017-05-10.
 */
$(document).ready(function () {
    $(".sensor-widget-delete-icon").on("click", function (event) {
        var monitoredObjectId = event.target.closest(".monitored-object-content").id;
        var sensorId = event.target.closest(".sensor-widget").id;
        var queryParams = "?uuid=" + sensorId + "&monitored-object-uuid=" + monitoredObjectId;

        jQuery.ajax({
            url: "http://localhost:8000/telemetry/sensor" + queryParams,
            type: "DELETE",
            success: function (resultData) {
                swal({
                    title: "Deleted",
                    text: "The sensor has been successfully deleted",
                    type: "success"
                }, function () {
                    location.reload();
                });
            },
            error: function (jqXHR, textStatus, errorThrown) {
                sweetAlert("Oops...", "An error has occurred while deleting the sensor", "error");
            },

            timeout: 12000000
        });
    });
});