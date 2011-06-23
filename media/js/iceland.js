function draw_iceland() {
	if( $('#country_area') )
	{
	var svg_prepend = '<svg width="200px" height="150px" xmlns="http://www.w3.org/2000/svg" version="1.1">';
	var svg_close = '</svg>';
	//var path = '/api/island/kort/merkja/Austurland/';
	var path = '/api/island/kort/merkja/'+$('#country_area').text()+'/';
	var svg_paths = '';
	$.getJSON(path, function(data) {
		$.each(data, function(item) {
			$('#print').append((this.name)+"\n");
			svg_paths += '<path d="' + this.svg_points + '" ';
			if (this.status == 'highlight') {
				svg_paths += 'style="fill:#333333;stroke:#ffffff;stroke-width:0"';
			}
			else {
				svg_paths += 'style="fill:#4b76bb;stroke:#ffffff;stroke-width:0"';
			}
			svg_paths += '/>';
		});
		canvg(document.getElementById('iceland'), svg_prepend+svg_paths+svg_close);
	});
	}
}

$(draw_iceland);
