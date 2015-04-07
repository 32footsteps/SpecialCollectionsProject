$(function() {
	$('#collection_item_search').click(function() {
		$.ajax({
			type: "POST",
			url: "/collections/collectionsearchitem/",
			data: {
				'q': $('#collection_item_search_text').val(),
				'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()

			},
			success: searchSuccess,
			error: searchError,
			dataType: 'html'
		});
	});
});

function searchSuccess(data, textStatus, jqXHR) {
	console.log("success")
	$('#search_results').html(data);
}

function searchError(data, textStatus, jqXHR) {
	console.log("error")

}