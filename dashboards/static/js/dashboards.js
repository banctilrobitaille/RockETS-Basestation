/**
 * Created by Benoit on 2017-03-26.
 */
$(document).ready(function () {
    $('#createDashboardButton').on('click', function (event) {
        var dashboardName = $("#dashboardName").val();
        var dashboardDescription = $("#dashboardDescription").val();
        var dashboardTemplate = $("#dashboardTemplate").val();
        var queryParams = "?name=" + dashboardName + "&description=" + dashboardDescription + "&template=" + dashboardTemplate;
        if (dashboardName) {
            $("#dashboardNameError").hide();
            jQuery.ajax({
                url: "http://localhost:8000/dashboards" + queryParams,
                type: "POST",
                success: function (resultData) {
                    swal("Great", "Dashboard created successfully", "success")
                },
                error: function (jqXHR, textStatus, errorThrown) {
                    sweetAlert("Oops...", "An error has occurred while creating the dashboard", "error");
                },

                timeout: 12000000,
            });
            $("#dashboard-creation-modal").modal('toggle');
        } else {
            $("#dashboardNameError").show();
        }
    })
});