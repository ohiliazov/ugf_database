$(document).ready(function () {

var cell = $('table tr td.place');
// console.log(cell);
cell.each(function() {
        var cell_value = $(this).html();

        if (cell_value == 1) {
            $(this).css({'background-color' : 'gold'});
        }
        else if (cell_value == 2) {
            $(this).css({'background-color' : 'silver'});
        }
        else if (cell_value == 3) {
            $(this).css({'background-color' : '#CD7F32'});
        }
    });
});