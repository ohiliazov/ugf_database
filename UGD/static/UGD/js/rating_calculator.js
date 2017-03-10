/**
 * Module Suggest
 *
 */
;$.fn.suggest  = function(option) {
	var opts = $.extend( {}, $.fn.suggest.default, option );
	var parent = $( this );
	var data_type = 'input[data-type="' + opts.data_type +'"]';
	/* if you in input, every time when you press key call function suggestOn() */  
	$(parent).on('keyup', data_type, suggestOn);

	/* if input lost focus delete suggest block */
	$(parent).on('change',$(data_type).parent(), suggestLost);

	/* click inside suggest block will call function complete */
	$(parent).on('click','#' + opts.suggest_block + ' div',complete);

	/* Create Suggest Block */
	function suggestOn(event) {
		suggestOff();
		var request = $(this).val();
		if (request !== '') {
			$('<div id="' + opts.suggest_block + '"></div>')
				.attr(opts.target_by, $(this).attr(opts.target_by))
				.appendTo($(this).parent());
			getPlayersList(request);
		}
	}

	function suggestLost (event) {
		setTimeout(suggestOff, 300);
	}

	/* Destroy suggest Block */
	function suggestOff() {
		$('#' + opts.suggest_block).remove();
	}

	/* Write rating in target input */
	function complete (event) {
		var text = $(this).text();
		var target = $('#' + opts.suggest_block).attr(opts.target_by);
		var rating = $(this).attr('data-rating');
		$('#' + opts.suggest_block).parent().find(data_type).val(text);
		$('#' + target).val(rating);
		suggestOff();
	}

	/* Fill Suggest block */
	function suggestRender(data) {
		for(var item in data) {
			var suggestString = data[item][0] + " (" + data[item][1] + ")";
			$('<div></div>').attr('data-rating', data[item][1])
							.html(suggestString)
							.appendTo('#' + opts.suggest_block);
		}
	}

	/* Get players from server */
	function getPlayersList (query) {
			$.getJSON('/api/json/player_list/?full_name=' + query)
				.success(suggestRender)
				.error(function(err){
					console.log(err);
					alert('Не удалось !!');
				});
	}
};

$.fn.suggest.default = {
	/*parent: form*/
	data_type: "suggest",
	suggest_block: 'suggest',
	target_by: 'data-target',
	attribute: 'data-rating',
	link: '/'
};

$(document).ready(function () {
	$('#rating_form').suggest({
		link: '/api/json/player_list/?full_name=' 
	});

	$('#rating_form').on('click','.suggest-trigger',showSuggestInput);

	function showSuggestInput () {
		var target = $(this).parent().find('.suggest-input');
		if (!this.checked) {
			target.hide();
		} else {
			target.show();
		}
	}
});

