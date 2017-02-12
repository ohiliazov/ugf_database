function playerFilter() {
    var input1, input2, filter1, filter2, tables, tr, td1, td2, i;

    input1 = document.getElementById('full_name_search');
    input2 = document.getElementById('city_search');

    filter1 = input1.value.toUpperCase();
    filter2 = input2.value.toUpperCase();

    tables = document.getElementsByClassName('ugd_table');
    for (j = 0; j < 6; j++) {
        tr = tables[j].getElementsByTagName("tr");

        for (i = 0; i < tr.length; i++) {
            td1 = tr[i].getElementsByTagName("td")[1];
            td2 = tr[i].getElementsByTagName("td")[2];
            if (td1) {
                if (td1.innerHTML.toUpperCase().indexOf(filter1) > -1 && td2.innerHTML.toUpperCase().indexOf(filter2) > -1) {
                        tr[i].style.display = "";
                }
                else {
                        tr[i].style.display = "none";
                }
            }
        }
    }
};