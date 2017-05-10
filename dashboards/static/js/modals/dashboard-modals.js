/**
 * Created by Benoit on 2017-03-26.
 */
$(document).ready(function () {
    $('#createDashboardButton').on('click', function () {
        var dashboardName = $("#dashboardName").val();
        var dashboardDescription = $("#dashboardDescription").val();
        var dashboardTemplate = $("#dashboardTemplate").val();
        var dashboardMonitoredObjectUuid = $("#dashboardMonitoredObject").val();
        var dashboardTransmitterUuid = $("#dashboardTransmitter").val();

        var queryParams = "?name=" + dashboardName + "&description=" + dashboardDescription + "&template=" +
            dashboardTemplate + "&monitored-object-uuid=" + dashboardMonitoredObjectUuid +
            "&transmitter-uuid=" + dashboardTransmitterUuid;
        if (dashboardName) {
            $("#dashboardNameError").hide();
            jQuery.ajax({
                url: "http://localhost:8000/dashboards" + queryParams,
                type: "POST",
                success: function (resultData) {
                    swal({
                        title: "Created",
                        text: "Dashboard has been successfully created",
                        type: "success"
                    }, function () {
                        location.reload();
                    });
                },
                error: function (jqXHR, textStatus, errorThrown) {
                    sweetAlert("Oops...", "An error has occurred while creating the dashboard", "error");
                },

                timeout: 12000000
            });
            $("#dashboard-creation-modal").modal('toggle');
        } else {
            $("#dashboardNameError").show();
        }
    });


    $('#editDashboardButton').on('click', function (event) {
        var dashboardName = $("#editedDashboardName").val();
        var dashboardDescription = $("#editedDashboardDescription").val();
        var uuid = $("#editedDashboardUUID").val();
        var queryParams = "?uuid=" + uuid + "&name=" + dashboardName + "&description=" + dashboardDescription;
        if (dashboardName) {
            $("#dashboardNameError").hide();
            jQuery.ajax({
                url: "http://localhost:8000/dashboards" + queryParams,
                type: "PUT",
                success: function (resultData) {
                    swal({
                        title: "Updated",
                        text: "Dashboard has been successfully updated",
                        type: "success"
                    }, function () {
                        location.reload();
                    });
                },
                error: function (jqXHR, textStatus, errorThrown) {
                    sweetAlert("Oops...", "An error has occurred while updating the dashboard", "error");
                },

                timeout: 12000000,
            });
            $("#dashboard-edition-modal").modal('toggle');
        } else {
            $("#dashboardNameError").show();
        }
    });

    $(".dashboard-widget-edit-icon").on('click', function (event) {
        var dashboardWidget = $(event.target).closest(".dashboard-widget");
        var dashboardEditionModal = $("#dashboard-edition-modal");
        dashboardEditionModal.find("#editedDashboardName").val(dashboardWidget.find(".dashboard-name").html());
        dashboardEditionModal.find("#editedDashboardDescription").val(dashboardWidget.find(".dashboard-description").html());
        dashboardEditionModal.find("#editedDashboardUUID").val(dashboardWidget.attr("id"));
    });
});