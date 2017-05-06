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
});

