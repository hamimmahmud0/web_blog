idPattern = /<%[a-zA-Z0-9]+%>/;

$(document).ready(function () {
	$.get("projectViewerCardTemplate.htm", function(data,status) {
		console.log(status);
	});
});