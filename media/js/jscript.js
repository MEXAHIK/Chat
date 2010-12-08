$(document).ready(function(){
	var message_count = 0, show_text = $('#show_text'), temp;
	wait_message();
//  фнкция отправки сообщения
	function sendMessage(){
		if ($('#send_text').val() != "") {
			message_count ++;
			$.ajax({
				type: 'GET',
				url: '/send-message/',
				data: {
					'message': $('#send_text').val(),
					'user_name': $('#user_name > a').text(),
					'message_count': message_count,
					'room_id': room_id
				},
				success: function(data){
					temp = show_text.html() + '<tr><td id = "user_name">' + data.user_name + ':</td><td> ' + data.message + '</td><td>' + data.send_time +'</td><td></td></tr>';
					show_text.html(temp);
					$('.scroll-pane').scrollTo(show_text.height(),200);
				}
			})
			$('#send_text').val('');
		};
	};
	
	// Ожидание сообщения
	function wait_message(){
		var split_text;
		$.ajax({
			type: 'POST',
			url: '/update-message/',
			data: {
				'message_count': message_count,
				'user_name': $('#user_name > a').text(),
				'room_id': room_id
			},
			success: function(data){
				message_count = data.messge_count;
				for (var i = data.mass.length - 1; i >= 0; i--) {
					split_text = data.mass[i].split('###');
					temp = show_text.html() + '<tr><td id = "user_name">' + split_text[0] + ':</td><td> ' + split_text[1] + '</td><td>' + split_text[2] + '</td><td></td></tr>';
					show_text.html(temp);
					$('.scroll-pane').scrollTo(show_text.height(),1);
				};
			}
		})
	};
	var id = setInterval(wait_message, 2000);
	
// отправвка по нажатию кнопки
	$('#send_button').click(function(eObject){
		
		eObject.preventDefault();
		sendMessage();
	});
	
// отправка по нажатю Enter
	$('#send_text').keypress(function(eObject){
		if (event.keyCode == 13) {
			sendMessage();
		};
		
	});

}); //finish ready
