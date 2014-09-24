'use strict';

var Blog = (function($){
	var init = function init () {
		$.get('/api/posts', function(response) {
			var source = $('#post-template').html();
			var template = Handlebars.compile(source);

			var areaEl = $('#posts');
			for (var postID in response.posts) {
				var post = response.posts[postID];
				var author = response.authors[post.author_id];
				var category = response.categories[post.category_id];

				var context = {
					title: post.title,
					author: author.name,
					category: category.name,
					content: post.content,
					post_url: post.url,
					author_url: author.url,
					category_url: category.url
				};
				var html = template(context);

		    	areaEl.append(html);
			}
		})
		.fail(function() {
			alert('Couldn\'t get blog posts from server.');
		});
	};

    return {
        'init' : init
    };
})(jQuery);

$(document).ready(function() {
	Blog.init();
});
