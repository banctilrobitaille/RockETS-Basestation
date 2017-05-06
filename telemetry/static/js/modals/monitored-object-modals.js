/**
 * Created by Benoit on 2017-05-02.
 */
$(document).ready(function () {
    $(".monitored-object-modal-configuration").hide();

    $(".modal-sensor-select").select2({
        placeholder: "Select sensors"
    });

    $('#createMonitoredObjectButton').on('click', function (event) {
        var monitoredObjectName = $("#monitoredObjectName").val();
        var monitoredObjectDescription = $("#monitoredObjectDescription").val();
        var monitoredObjectId = $("#monitoredObjectId").val();
        var monitoredObjectType = $("#monitoredObjectType").val();
        var queryParams = "?name=" + monitoredObjectName + "&description=" + monitoredObjectDescription + "&id=" + monitoredObjectId + "&type=" + monitoredObjectType;

        jQuery.ajax({
            url: "http://localhost:8000/telemetry/monitored-object" + queryParams,
            type: "POST",
            success: function (resultData) {
                swal({
                    title: "Created",
                    text: "Monitored object has been successfully created",
                    type: "success"
                }, function () {
                    location.reload();
                });
            },
            error: function (jqXHR, textStatus, errorThrown) {
                sweetAlert("Oops...", "An error has occurred while creating the monitored object", "error");
            },

            timeout: 12000000
        });
        $("#monitored-object-creation-modal").modal('toggle');
    });
    $("#monitoredObjectType").on("change", function () {
        $(".monitored-object-modal-configuration-configuration").slideUp();
        showMonitoredObjectConfigurationFrom($("#monitoredObjectType").val())
    });

    $("#monitored-object-creation-modal").on("shown.bs.modal", function () {
        showMonitoredObjectConfigurationFrom($("#monitoredObjectType").val())
    });
});

function showMonitoredObjectConfigurationFrom(monitoredObjectType) {
    const ROCKET = "rocket";

    if (monitoredObjectType == ROCKET) {
        $("#rocketMonitoredObjectConfiguration").slideDown();
    }
}