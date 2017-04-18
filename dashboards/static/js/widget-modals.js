/**
 * Created by Benoit on 2017-04-18.
 */
/**
 * Created by Benoit on 2017-03-26.
 */
$(document).ready(function () {
    $('#addWidgetModalButton').on('click', function () {
        var widgetName = $("#widgetName").val();
        var widgetDescription = $("#widgetDescription").val();
        var widgetType = $("#widgetType").val().toLowerCase();
        var widgetSize = $("#widgetSize").val();
        var widgetSensor = $("#widgetSensor").val();
        var widgetRefreshRate = $("#widgetRefreshRate").val();
        var widgetDashboardUUID = $("#widgetDashboardUUID").val();
        var queryParams = "?name=" + widgetName + "&description=" + widgetDescription + "&type=" + widgetType +
            "&size=" + widgetSize + "&sensor=" + widgetSensor + "&refresh-rate=" + widgetRefreshRate +
            "&dashboard-uuid=" + widgetDashboardUUID;

        jQuery.ajax({
            url: "http://localhost:8000/dashboards/widget" + queryParams,
            type: "POST",
            success: function (resultData) {
                swal({
                    title: "Created",
                    text: "The widget has been successfully created",
                    type: "success"
                }, function () {
                    location.reload();
                });
            },
            error: function (jqXHR, textStatus, errorThrown) {
                sweetAlert("Oops...", "An error has occurred while creating the widget", "error");
            },

            timeout: 12000000,
        });
    });
});