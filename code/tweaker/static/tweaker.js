'use strict';

var Tweaker = (function($){
	var init = function init () {
		$.get('/api/get', function(response) {
			var areaEl = $('#tweak-area');
			for (var propertyName in response) {
			    if (response.hasOwnProperty(propertyName)) {
			    	areaEl.append('<div><span id=' + propertyName + '>' + propertyName + '&nbsp;</span><input type="number" value="' + response[propertyName] + '"></div>');
			    }
			}
			$('#tweak-area input').on('keyup input', onValueChanged);
		})
		.fail(function() {
			alert('Couldn\'t get data from server.');
		});
	}

	var onValueChanged = function onValueChanged(event) {
		var el = $(event.currentTarget),
			newValue = el.val(),
			propertyName,
			changeData;

		propertyName = el.parent().find('span').attr('id');

		changeData = {
			'propertyName': propertyName,
			'newValue': newValue
		};
		$.post('/api/set', changeData)
		.fail(function() {
			alert('Couldn\'t set data on server.');
		});
	};

    return {
        'init' : init
    };
})(jQuery);

$(document).ready(function() {
	Tweaker.init();
});
