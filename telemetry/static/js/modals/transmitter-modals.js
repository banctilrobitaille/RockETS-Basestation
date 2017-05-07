/**
 * Created by Benoit on 2017-05-05.
 */
$(document).ready(function () {
    $(".transmitter-interface-configuration").hide();

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

    $("#transmitterInterfaceType").on("change", function () {
        $(".transmitter-interface-configuration").slideUp();
        showInterfaceConfigurationFrom($("#transmitterInterfaceType").val())
    });

    $("#transmitter-creation-modal").on("shown.bs.modal", function () {
        showInterfaceConfigurationFrom($("#transmitterInterfaceType").val())
    });

    $('#editTransmitterButton').on('click', function (event) {

        jQuery.ajax({
            url: "http://localhost:8000/telemetry/transmitter" + queryParams,
            type: "PUT",
            success: function (resultData) {
                swal({
                    title: "Updated",
                    text: "The transmitter has been successfully updated",
                    type: "success"
                }, function () {
                    location.reload();
                });
            },
            error: function (jqXHR, textStatus, errorThrown) {
                sweetAlert("Oops...", "An error has occurred while updating the transmitter", "error");
            },

            timeout: 12000000,
        });
        $("#transmitter-edition-modal").modal('toggle');
    });
});

function showInterfaceConfigurationFrom(transmitterInterfaceType) {
    const SERIAL_INTERFACE_TYPE = "serial";

    if (transmitterInterfaceType == SERIAL_INTERFACE_TYPE) {
        $("#serialTransmitterInterfaceConfiguration").slideDown();
    } else {
        $("#ethernetTransmitterInterfaceConfiguration").slideDown();
    }
}