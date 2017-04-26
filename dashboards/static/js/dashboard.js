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

    startTime();
});