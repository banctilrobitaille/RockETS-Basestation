/**
 * Created by Benoit on 2017-06-18.
 */
$(document).ready(function () {
    $(".transmitter-widget-delete-icon").on("click", function (event) {
        var transmitterObjectId = event.target.closest(".transmitter-widget").id;
        var queryParams = "?uuid=" + transmitterObjectId;

        jQuery.ajax({
            url: "/telemetry/transmitter" + queryParams,
            type: "DELETE",
            success: function (resultData) {
                swal({
                    title: "Deleted",
                    text: "The transmitter has been successfully deleted",
                    type: "success"
                }, function () {
                    location.reload();
                });
            },
            error: function (jqXHR, textStatus, errorThrown) {
                sweetAlert("Oops...", "An error has occurred while deleting the transmitter", "error");
            },
            timeout: 1200
        });
    });
});