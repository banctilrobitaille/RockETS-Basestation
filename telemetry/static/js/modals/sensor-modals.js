/**
 * Created by Benoit on 2017-05-03.
 */
$(document).ready(function () {
    const REMOTE_SENSOR = "remote";

    $("#sensorMeasures").select2({
        tags: true
    });

    $("#localSensorMeasures").select2({
        tags: true
    });

    $('#createSensorButton').on('click', function (event) {
        var sensorName = $("#sensorName").val();
        var sensorDescription = $("#sensorDescription").val();
        var sensorType = $("#sensorType").val();
        var sensorLocation = $("#sensorLocation").val();
        var sensorMeasures = $("#sensorMeasures").val();
        var monitoredObjectUUID = $(".monitored-object-content").attr("id");
        var sensorNode = "";

        try {
            if (isRemoteSensor(sensorLocation)) {
                sensorNode = $("#sensorNode").val();
                validateRemoteSensorParameters(sensorName, sensorNode);
            } else {
                validateLocalSensorParameters(sensorName);
            }

            var queryParams = "?name=" + sensorName + "&description=" + sensorDescription + "&type=" + sensorType +
                "&location=" + sensorLocation + "&node=" + sensorNode + "&measures=" + sensorMeasures +
                "&monitored-object-uuid=" + monitoredObjectUUID;

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
            $("#sensor-creation-modal").modal('toggle');
        } catch (exception) {
            console.log(exception.message);
        }
    });

    $('#createLocalSensorButton').on('click', function (event) {
        const LOCAL_SENSOR = "local"
        var sensorName = $("#localSensorName").val();
        var sensorDescription = $("#localSensorDescription").val();
        var sensorType = $("#localSensorType").val();
        var sensorLocation = LOCAL_SENSOR;
        var sensorMeasures = $("#localSensorMeasures").val();
        var sensorInterfaceType = $("#sensorInterfaceType").val();
        var sensorInterfaceBaudrate = $("#sensorInterfaceBaudrate").val();
        var sensorInterfacePort = $("#sensorInterfacePort").val();

        try {
            validateLocalSensorParameters(sensorName);
            var queryParams = "?name=" + sensorName + "&description=" + sensorDescription + "&type=" + sensorType +
                "&location=" + sensorLocation + "&measures=" + sensorMeasures + "&interface-type=" + sensorInterfaceType +
                "&baud-rate=" + sensorInterfaceBaudrate + "&port=" + sensorInterfacePort;

            jQuery.ajax({
                url: "http://localhost:8000/telemetry/sensor" + queryParams,
                type: "POST",
                success: function (resultData) {
                    swal({
                        title: "Created",
                        text: "Local sensor has been successfully created",
                        type: "success"
                    }, function () {
                        location.reload();
                    });
                },
                error: function (jqXHR, textStatus, errorThrown) {
                    sweetAlert("Oops...", "An error has occurred while creating the local sensor", "error");
                },

                timeout: 12000
            });
            $("#local-sensor-creation-modal").modal('toggle');
        } catch (exception) {
            console.log(exception.message);
        }
    });

    function isRemoteSensor(sensorLocation) {
        return (sensorLocation == REMOTE_SENSOR)
    }
});
