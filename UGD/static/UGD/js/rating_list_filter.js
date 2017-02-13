$(".form-control").keyup(function() {
    var input = document.getElementsByClassName("form-control");
    var full_name_value = input[0].value.toLowerCase();
    var city_value = input[1].value.toLowerCase();
    var row = $('table.ugd_table tr');
    row.each(function() {
        var full_name = $(this).children("td.full_name");
        var city = $(this).children("td.city");
        if ((full_name.text().toLowerCase().indexOf(full_name_value)) > -1 && city.text().toLowerCase().indexOf(city_value) > -1) {
            full_name.parent().show();
            full_name.closest('div').parent().show();
        } else {
            full_name.parent().hide();
        }
    });
    var tables = $('table.ugd_table');
    tables.each(function() {
        var rows_count = ($(this).find('tr')).length;
        var hidden_rows = ($(this).find('tr:hidden')).length;
        if (hidden_rows >= (rows_count-1)) {
            $(this).closest('div').parent().hide();
        } else {
            $(this).closest('div').parent().show();
        }
    });
});