/**
 * Created by Benoit on 2017-05-05.
 */
$(document).ready(function () {
    $('#createTransmitterButton').on('click', function (event) {
        var transmitterName = $("#transmitterName").val();
        var transmitterDescription = $("#transmitterDescription").val();
        var transmitterInterfaceType = $("#transmitterInterfaceType").val();
        var transmitterInterfaceBaudrate = $("#transmitterInterfaceBaudrate").val();
        var transmitterInterfacePort = $("#transmitterInterfacePort").val();
        var queryParams = "?name=" + transmitterName + "&description=" + transmitterDescription +
            "&interface-type=" + transmitterInterfaceType + "&baud-rate=" + transmitterInterfaceBaudrate +
            "&port=" + transmitterInterfacePort;

        jQuery.ajax({
            url: "http://localhost:8000/telemetry/transmitter" + queryParams,
            type: "POST",
            success: function (resultData) {
                swal({
                    title: "Created",
                    text: "The transmitter has been successfully created",
                    type: "success"
                }, function () {
                    location.reload();
                });
            },
            error: function (jqXHR, textStatus, errorThrown) {
                sweetAlert("Oops...", "An error has occurred while creating the transmitter", "error");
            },

            timeout: 12000000
        });
        $("#transmitter-creation-modal").modal('toggle');
    });
});