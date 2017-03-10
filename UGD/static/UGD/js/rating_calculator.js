/* if you in input, every time when you press key call function suggestOn() */  
$('#suggest_form').delegate('input', 'keyup', suggestOn);

/* if input lost focus delete suggest block */
$('#suggest_form').delegate('input', 'focusoff', suggestOff);

/* click inside suggest block will call function complete */
$('#suggest_form').delegate('#suggest div', 'click', complete);


/* Create Suggest Block */
function suggestOn(event) {
	suggestOff();
	$('<div id="suggest"></div>')
		.attr('data-target', $(this).attr('data-target'))
		.appendTo($(this).parent());
	var request = $(this).val();
	getPlayersList(request);
}

/* Destroy suggest Block */
function suggestOff() {
	$('#suggest').remove();
}

/* Write rating in target input */
function complete (event) {
	var text = $(this).text();
	var target = $('#suggest').attr('data-target');
	var rating = $(this).attr('data-rating');
	$('#suggest').parent().find('input').val(text);
	$('#' + target).val(rating);
	suggestOff();
}

/* Fill Suggest block */
function suggestRender(data) {
	var i=0;
	for(var item in data) {
		var suggestString = data[item][0] + " (" + data[item][1] + ")";
		$('<div></div>').attr('data-rating', data[item][1])
						.html(suggestString)
						.appendTo('#suggest');
		i++;
		/* TODO: create suggest parameter in admin */
		if (i > 9) break;
	}
}

/* Get players from server */
function getPlayersList (query) {
	if(query.length > 1) {
		$.getJSON('/api/json/player_list/?full_name=' + query)
			.success(suggestRender)
			.error(function(err){
				console.log(err);
				alert('Не удалось !!');
			});
	}
}
