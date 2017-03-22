$(".form-control").keyup(function() {

    var input = document.getElementsByClassName("form-control");
    // Записываем значения ввода
    var full_name_value = input[0].value.toLowerCase();
    var city_value = input[1].value.toLowerCase();
    // Выбираем все строки таблиц
    var row = $('table.ugd_table tr');
    // Цикл по каждому ряду
    row.each(function() {
        // Выбираем ячейки имени и города
        var full_name = $(this).children("td.full_name");
        var city = $(this).children("td.city");
        // Проверяем есть ли в имени и городе нужные строки ввода
        if ((full_name.text().toLowerCase().indexOf(full_name_value)) > -1 && city.text().toLowerCase().indexOf(city_value) > -1) {
            // Отображаем, если оба поля содержат значение
            full_name.parent().show();
            // Отображаем таблицу если она была скрыта
            full_name.closest('div').parent().show();
        } else {
            // Скрываем строку, если не совпадает хотя бы одно из полей
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
$(document).ready(function () {
   var cell = $("table td.rank");
   cell.each(function () {
       if ($(this).text().match(/^\d про/)) {
           $(this).closest("tr").toggleClass("gold_belt");
       } else if ($(this).text().match(/^\d дан/)) {
           $(this).closest("tr").toggleClass("black_belt");
       } else if ($(this).text().match(/^(1|2|3|4) кю/)) {
           $(this).closest("tr").toggleClass("blue_belt");
       } else if ($(this).text().match(/^(5|6|7|8|9) кю/)) {
           $(this).closest("tr").toggleClass("green_belt");
       } else if ($(this).text().match(/^1(0|1|2|3|4) кю/)) {
           $(this).closest("tr").toggleClass("yellow_belt");
       } else if ($(this).text().match(/^(1(5|6|7|8|9)|20) кю/)) {
           $(this).closest("tr").toggleClass("white_belt");
       }
   });
});
