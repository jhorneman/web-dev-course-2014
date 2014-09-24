'use strict';

var Blog = (function($){
	var init = function init () {
		var blogData = localStorage["blogData"];
		if (blogData) {
			render(JSON.parse(blogData));
			$('#posts').append("<p>This content was loaded from local storage. <a id='eraseLocalStorage' href='#''>Erase local storage</a>.</p>")
			$('#eraseLocalStorage').on('click', function(event) {
				event.preventDefault();
				eraseLocalStorage();
			});
		} else {
			$.get('/api/posts', function(response) {
				localStorage["blogData"] = JSON.stringify(response);
				render(response);
				$('#posts').append("<p>This content was loaded fresh from the server.</p>")
			})
			.fail(function() {
				alert('Couldn\'t get blog posts from server.');
			});
		}
	};

	var render = function render (blogData) {
		var source = $('#post-template').html();
		var template = Handlebars.compile(source);

		var areaEl = $('#posts');
		for (var postID in blogData.posts) {
			var post = blogData.posts[postID];
			var author = blogData.authors[post.author_id];
			var category = blogData.categories[post.category_id];

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
	};

	var eraseLocalStorage = function eraseLocalStorage () {
		localStorage.removeItem("blogData");
	};

    return {
        'init' : init
    };
})(jQuery);

$(document).ready(function() {
	Blog.init();
});
