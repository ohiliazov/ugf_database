/*
 * Module Suggest
 */
// Keep all suggest function as jQuery plugin
;$.fn.suggest  = function(option) {
	// add default options to new option
	var opts = $.extend( {}, $.fn.suggest.default, option );

	// Take access to the element (before .suggest()) 
	var parent = $( this );

	var data_type = 'input[data-type="' + opts.data_type +'"]';

	// Add handlers
	$(parent).on('keyup', data_type, suggestOn) /* if input has focus, every time when you press key call function suggestOn() */  
		.on('change',$(data_type).parent(), suggestLost)	/* if input lost focus delete suggest block */
		.on('click','#' + opts.suggest_block + ' div',complete); /* click inside suggest block will call function complete */

	/* Create Suggest Block */
	function suggestOn(event) {
		suggestOff();
		/* Take input current value */
		var request = $(this).val();
		if (request !== '') { /* if value is not emplty */
			//Create new suggest block
			$('<div id="' + opts.suggest_block + '"></div>')
				.attr(opts.target_by, $(this).attr(opts.target_by)) // copy attributes 
				.appendTo($(this).parent()); // add suggest block after input
			getPlayersList(request); 
		}
	}
	/* add delay. Now Click event will be first than destroy suggest block */
	function suggestLost (event) {
		setTimeout(suggestOff, 300);
	}

	/* Destroy suggest Block */
	function suggestOff() {
		$('#' + opts.suggest_block).remove();
	}

	/* Write rating in target input */
	function complete (event) {
		// this = clicked string in suggest block
		var text = $(this).text();

		// attribute data-target give input to write result
		var target = $('#' + opts.suggest_block).attr(opts.target_by);

		// data-rating attribute = rating as a number
		var rating = $(this).attr(opts.attribute);

		// write clicked string to input
		$('#' + opts.suggest_block).parent().find(data_type).val(text);

		// write rating to rating input
		$('#' + target).val(rating);
		suggestOff(); // destroy suggest block
	}

	/* Fill Suggest block */
	function suggestRender(data) {
		/*
		 * data = {
		 *	id:	['String Player Name', 'Rating']
		 * }
		 */
		for(var item in data) {
			var suggestString = data[item][0] + " (" + data[item][1] + ")";

			// result: <div data-rating="rating">Player Name (Rating)</div>
			$('<div></div>').attr(opts.attribute, data[item][1])
						.html(suggestString)
						.appendTo('#' + opts.suggest_block);// add result DOM element to suggest block
		}
	}

	/* Get players from server */
	function getPlayersList (query) {
		// AJAX request
		$.getJSON('/api/json/player_list/?full_name=' + query)
			.done(suggestRender) 
			.fail(showErrorMessage); 
	}

	// Ensure jQuery chaining
	return this;
};

/*
 * Suggest plugin defaults
 */
$.fn.suggest.default = {
	data_type: "suggest",	// suggest input has this data-type 
	suggest_block: 'suggest', // id for suggest block
	target_by: 'data-target', // if suggest has another target
	attribute: 'data-rating', // value of this attribute will be written  to target 
	link: '/' // ajax link
};

/*
 * if page loaded and ready to use
 * Standard jQuery string
 */
$(document).ready(function () {
	/* take form, add handler for suggest */
	$('#rating_form').suggest({
		link: '/api/json/player_list/?full_name=' 
		})
		.on('submit', submitRating); // and submit event

		// Show suggest input if javascript on and jQuery library loaded
		$('.suggest-input').show();

	function submitRating ( event) {
		/* Do not send GET request as browser */
		event.preventDefault();

		// Get form data, and save as request string
		var form_data = $(this).serialize();
		// AJAX send GET request
		$.getJSON('/api/json/calculated_rating/' + '?' + form_data)
			.done(drawResult)
			.fail(showErrorMessage);
	}

	function drawResult (data) {
		/*
		 * read Handlebars temlate from #ratind_output
		 * Compile it
		 */
		var template = Handlebars.compile( $('#rating_output').html() );
		// Write response data to #calculator_output 
		$('#calculator_output').html(template(data));
	}
});

function showErrorMessage (jqxhr, textStatus, error) {
	var template = Handlebars.compile( $('#rating_error').html() );
	$('#calculator_output').html(template(jqxhr.responseJSON));
}

