$(function() {
	$('#collection_item_search').keypress(function() {
		$.ajax({
			type: "POST",
			url: "/collections/searchitem/",
			data: {
				'q': $('#collection_item_search_text').val(),
				'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()

			},
			success: searchSuccess,
			dataType: 'html'
		});
	});
});

function searchSuccess(data, textStatus, jqXHR) {
	console.log("success")
	$('#search_results').html(data);
}