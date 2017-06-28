/**
 * Created by Benoit on 2017-04-18.
 */
/**
 * Created by Benoit on 2017-03-26.
 */
$(document).ready(function () {
    $(".widget-creation-modal-configuration").hide();

    $('#widget-creation-modal').on("shown.bs.modal", function () {
        updateSensorMeasures($("#widgetSensor").val());
        $(".widget-creation-modal-configuration").hide();
        showWidgetConfigurationFrom($("#widgetType").val())
    });

    $("#widgetSensor").on("change", function () {
        updateSensorMeasures($("#widgetSensor").val());
    });

    $('#addWidgetModalButton').on('click', function () {
        var widgetName = $("#widgetName").val();
        var widgetDescription = $("#widgetDescription").val();
        var widgetMeasureUnits = $("#widgetMeasureUnits").val().toLowerCase();
        var widgetType = $("#widgetType").val().toLowerCase();
        var widgetWidth = $("#widgetWidth").val();
        var widgetSensor = $("#widgetSensor").val();
        var widgetSensorMeasure = $("#widgetSensorMeasure").val();
        var widgetRefreshRate = $("#widgetRefreshRate").val();
        var widgetDashboardUUID = $("#widgetDashboardUUID").val();
        var widgetMinValue = $("#widgetMinimumValue").val();
        var widgetMaxValue = $("#widgetMaximumValue").val();
        var queryParams = "?name=" + widgetName + "&description=" + widgetDescription + "&type=" + widgetType +
            "&measure-units=" + widgetMeasureUnits + "&width=" + widgetWidth + "&sensor=" + widgetSensor +
            "&sensor-measure=" + widgetSensorMeasure + "&refresh-rate=" + widgetRefreshRate +
            "&dashboard-uuid=" + widgetDashboardUUID + "&minimum-value=" + widgetMinValue + "&maximum-value=" + widgetMaxValue;

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
    $("#widgetType").on("change", function () {
        $(".widget-creation-modal-configuration").slideUp();
        showWidgetConfigurationFrom($("#widgetType").val())
    });
});

function showWidgetConfigurationFrom(widgetType) {
    const GAUGE = "gauge";

    if (widgetType == GAUGE) {
        $("#gaugeWidgetConfiguration").slideDown();
    }
}

function updateSensorMeasures(sensorUUID) {
    $("#widgetSensorMeasure").empty();
    var queryParams = "?uuid=" + sensorUUID;

    jQuery.ajax({
        url: "http://localhost:8000/telemetry/sensor" + queryParams,
        type: "GET",
        success: function (resultData) {
            var sensor = jQuery.parseJSON(resultData);
            jQuery.each(sensor.measurements, function () {
                $("#widgetSensorMeasure").append("<option value='" + this.name + "'>" + this.name + "</option>");
            });
        },
        error: function (jqXHR, textStatus, errorThrown) {
            console.log("shit");
        },
        timeout: 12000000
    });
}