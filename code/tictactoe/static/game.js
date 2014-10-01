'use strict';

$(document).ready(function() {
	if (!itIsMyTurn) {
		var intervalID = window.setInterval(function() {
			$.get('/api/is_it_my_turn_yet', function(response) {
				if (response.result === 'yes') {
					window.location.reload();
				} else if (response.result === 'error') {
					window.clearInterval(intervalID);
				}
			})
			.fail(function() {
				window.clearInterval(intervalID);
			});
		}, 500);
	}
});
