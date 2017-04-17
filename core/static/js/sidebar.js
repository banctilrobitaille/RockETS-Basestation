/**
 * Created by Benoit on 2017-04-04.
 */
$(document).ready(function () {
    $(".menu-tab").on('click', function (e) {
        $(e.target).addClass("active");
        localStorage.setItem('activeTab', e.target.id);
        console.log(e.target.id);
    });
    var activeTab = localStorage.getItem('activeTab');
    console.log(activeTab);
    if (activeTab) {
        $("#" + activeTab).addClass("active");
    }
});