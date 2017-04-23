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
        var widgetMeasureUnits = $("#widgetMeasureUnits").val().toLowerCase();
        var widgetType = $("#widgetType").val().toLowerCase();
        var widgetWidth = $("#widgetWidth").val();
        var widgetSensor = $("#widgetSensor").val();
        var widgetRefreshRate = $("#widgetRefreshRate").val();
        var widgetDashboardUUID = $("#widgetDashboardUUID").val();
        var queryParams = "?name=" + widgetName + "&description=" + widgetDescription + "&type=" + widgetType +
            "&measure-units=" + widgetMeasureUnits + "&width=" + widgetWidth + "&sensor=" + widgetSensor + "&refresh-rate=" + widgetRefreshRate +
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

            timeout: 12000000
        });
    });

    $(".widget-edit-icon").on('click', function (event) {
        var widget = $(event.target).closest(".widget-holder");
        var widgetEditionModal = $("#widget-edition-modal");

        widgetEditionModal.find("#editedWidgetUUID").val($(widget).attr("id"));
        widgetEditionModal.find("#editedWidgetName").val(widget.find(".widget-name").val());
        widgetEditionModal.find("#editedWidgetDescription").val(widget.find(".widget-description").val());
        widgetEditionModal.find("#editedWidgetWidth").val(widget.find(".widget-width").val());
        widgetEditionModal.find("#editedWidgetSensor").val(widget.find(".widget-sensor-id").val());
    });

    $("#updateWidgetModalButton").on('click', function () {
        var editedWidgetUUID = $("#editedWidgetUUID").val();
        var editedWidgetName = $("#editedWidgetName").val();
        var editedWidgetDescription = $("#editedWidgetDescription").val();
        var editedWidgetWidth = $("#editedWidgetWidth").val();
        var editedWidgetSensor = $("#editedWidgetSensor").val();
        var widgetDashboardUUID = $("#widgetDashboardUUID").val();
        var queryParams = "?widget-uuid=" + editedWidgetUUID + "&name=" + editedWidgetName + "&description=" + editedWidgetDescription +
            "&width=" + editedWidgetWidth + "&sensor=" + editedWidgetSensor + "&dashboard-uuid=" + widgetDashboardUUID;

        jQuery.ajax({
            url: "http://localhost:8000/dashboards/widget" + queryParams,
            type: "PUT",
            success: function (resultData) {
                swal({
                    title: "Updated",
                    text: "The widget has been successfully updated",
                    type: "success"
                }, function () {
                    location.reload();
                });
            },
            error: function (jqXHR, textStatus, errorThrown) {
                sweetAlert("Oops...", "An error has occurred while updating the widget", "error");
            },

            timeout: 12000000
        });
    });
});