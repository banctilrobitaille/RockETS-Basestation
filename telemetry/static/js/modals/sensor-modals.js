/**
 * Created by Benoit on 2017-05-03.
 */
$(document).ready(function () {
    const REMOTE_SENSOR = "remote";

    $("#sensorMeasures").select2({
        tags: true
    });

    $('#createSensorButton').on('click', function (event) {
        var sensorName = $("#sensorName").val();
        var sensorDescription = $("#sensorDescription").val();
        var sensorType = $("#sensorType").val();
        var sensorLocation = $("#sensorLocation").val();
        var sensorMeasures = $("#sensorMeasures").val();
        var sensorNode = "";

        try {
            if (isRemoteSensor(sensorLocation)) {
                sensorNode = $("#sensorNode").val();
                validateRemoteSensorParameters(sensorName, sensorNode);
            } else {
                validateLocalSensorParameters(sensorName);
            }

            var queryParams = "?name=" + sensorName + "&description=" + sensorDescription + "&type=" + sensorType +
                "&location=" + sensorLocation + "&node=" + sensorNode + "&measures=" + sensorMeasures;

            jQuery.ajax({
                url: "http://localhost:8000/telemetry/sensor" + queryParams,
                type: "POST",
                success: function (resultData) {
                    swal({
                        title: "Created",
                        text: "Sensor has been successfully created",
                        type: "success"
                    }, function () {
                        location.reload();
                    });
                },
                error: function (jqXHR, textStatus, errorThrown) {
                    sweetAlert("Oops...", "An error has occurred while creating the sensor", "error");
                },

                timeout: 12000000
            });
            $("#dashboard-creation-modal").modal('toggle');
        } catch (exception) {
            console.log(exception.message);
        }
    });

    function isRemoteSensor(sensorLocation) {
        return (sensorLocation == REMOTE_SENSOR)
    }
});
