'use strict';

var Blog = (function($){
	var init = function init () {
		$.get('/api/posts', function(response) {
			var areaEl = $('#posts');
			for (var postID in response.posts) {
				var post = response.posts[postID];
				var author = response.authors[post.author_id];
				var category = response.categories[post.category_id];

		    	areaEl.append('<h2>' + post.title + '</h2><p>By ' + author.name + ', in the category ' + category.name + '.</p>' +
		    		'<p>' + post.content + '</p>');
			}
		})
		.fail(function() {
			alert('Couldn\'t get blog posts from server.');
		});
	}

    return {
        'init' : init
    };
})(jQuery);

$(document).ready(function() {
	Blog.init();
});
