$(document).ready(function () {

var place = $('table tr td.place');
// console.log(cell);
place.each(function() {
        var cell_value = $(this).html();

        if (cell_value == 1) {
            $(this).css({'background-color' : '#ffd700'});
        }
        else if (cell_value == 2) {
            $(this).css({'background-color' : '#C0C0C0'});
        }
        else if (cell_value == 3) {
            $(this).css({'background-color' : '#CD7F32'});
        }
    });
var rating_delta = $('table tr td.get_rating_delta');
// console.log(get_rating_delta);
rating_delta.each(function() {

        var cell_value = $(this).html();

        if (cell_value > 0) {
            $(this).css({'color' : 'green'});
        }
        else if (cell_value < 0) {
            $(this).css({'color' : 'red'});
        }
    });
});
