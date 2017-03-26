/**
 * Created by Benoit on 2017-03-26.
 */
$(document).ready(function () {
    $('#createDashboardButton').on('click', function (event) {
        event.preventDefault();
        var dashboardName = $("#dashboardName").val();
        var dashboardDescription = $("#dashboardDescription").val();
        var dashboardTemplate = $("#dashboardTemplate").val();
        var queryParams = "?name=" + dashboardName + "&description=" + dashboardDescription + "&template=" + dashboardTemplate;
        if (dashboardName) {
            alert(dashboardName);
            $("#dashboardNameError").hide();
            jQuery.ajax({
                url: "http://localhost:8000/dashboards" + queryParams,
                type: "POST",
                success: function (resultData) {

                },
                error: function (jqXHR, textStatus, errorThrown) {

                    console.log(errorThrown);
                },

                timeout: 12000000,
            });
            $("#dashboard-creation-modal").modal('toggle');
        } else {
            $("#dashboardNameError").show();
        }
    })
});