/**
 * Created by Benoit on 2017-03-31.
 */
$(document).ready(function () {
    function startTime() {
        $(".dashboard-time-content").html("Local time: " + moment().format('HH:mm:ss'));
        t = setTimeout(function () {
            startTime()
        }, 500);
    }

    $("#dashboard-play-icon").on("click", function () {
        jQuery.ajax({
            url: "http://localhost:8000/telemetry/transmitter/stop" + queryParams,
            type: "GET",
            success: function (resultData) {

            },
            error: function (jqXHR, textStatus, errorThrown) {
                sweetAlert("Oops...", "An error has occurred while starting the communication", "error");
            },

            timeout: 12000000
        });
    });

    $("#dashboard-stop-icon").on("click", function () {
        jQuery.ajax({
            url: "http://localhost:8000/telemetry/transmitter/stop" + queryParams,
            type: "GET",
            success: function (resultData) {

            },
            error: function (jqXHR, textStatus, errorThrown) {
                sweetAlert("Oops...", "An error has occurred while stopping the communication", "error");
            },

            timeout: 12000000
        });
    });

    startTime();
});