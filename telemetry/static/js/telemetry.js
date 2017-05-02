/**
 * Created by Benoit on 2017-05-01.
 */
$(document).ready(function () {
    $(".telemetry-section-collapse-icon").on("click", function (e) {
        var telemetrySection = $(e.target).closest(".telemetry-section");
        var telemetrySectionCollapseIconSection = telemetrySection.find(".telemetry-section-collapse-icon");
        var telemetrySectionContent = telemetrySection.find(".telemetry-section-content");

        if (telemetrySectionContent.hasClass("telemetry-section-displayed")) {
            telemetrySectionContent.removeClass("telemetry-section-displayed");
            telemetrySectionCollapseIconSection.html("<a href='#'><i class='fa  fa-arrow-down fa-2x pull-right'></i></a>");
        }
        else {
            telemetrySectionContent.addClass("telemetry-section-displayed");
            telemetrySectionCollapseIconSection.html("<a href='#'><i class='fa  fa-arrow-up fa-2x pull-right'></i></a>");
        }
        telemetrySectionContent.slideToggle();
    });
});