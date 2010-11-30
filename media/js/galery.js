$(document).ready(function(){
	// Слайд шоу
	$('#low_img a').click(function(eObject) {
		if ($('#big_img img').attr('src') != $(this).attr('href')) {
			$('#big_img img').hide().attr('src', $(this).attr('href'));
			$('#low_img a').fadeTo(500, 1);
			$(this).fadeTo(1000, 0.6);
			$('#big_img img').load(function(){
				$(this).fadeIn(2000);
			});
		};
		eObject.preventDefault();
	})
	$('#low_img a img').click(function(){
		$('#low_img a img').css({'border': '0px solid #cc0000'});
		$(this).css({'border': '2px solid #cc0000'});
	});
});
