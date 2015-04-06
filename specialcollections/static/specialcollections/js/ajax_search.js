$(function() {
	$('#collection_item_search').keypress(function() {
		$.ajax({
			type: "POST",
			url: "/collections/searchitem/",
			data: {
				"q": $('#collection_item_search_text').val(),

			},
			success: searchSuccess,
			dataType: 'html'
		});
	});
});