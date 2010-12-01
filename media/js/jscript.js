$(document).ready(function(){
	var message_count = 0, show_text = $('#show_text'), temp;
//  фнкция отправки сообщения
	function sendMessage(){
		if ($('#send_text').val() != "") {
			message_count ++;
			$.get('/send-message/', {'message': $('#send_text').val(), 'user_name': $('#user_name > a').text(), 'message_count' :message_count} , function(data){
					temp = show_text.html() + '<tr><td id = "user_name">' + data.user_name + ':</td><td> ' + data.message + '</td><td>' + data.send_time +'</td><td></td></tr>';
					show_text.html(temp);
			});
			$('#send_text').val('');
		};
	};
	
	// Ожидание сообщения
	function wait_message(){
		var split_text;
		$.ajax({
			type: 'POST',
			url: '/update-message/',
			data: {'message_count': message_count, 'user_name': $('#user_name > a').text()},
			success: function(data){
				/*
				$.each(data.new_mass, function(){
					$('#temp_message').html('' + $(this));
				})*/
				message_count = data.messge_count;
				split_text = data.mass[0].split(',');
				temp = show_text.html() + '<tr><td id = "user_name">' + split_text[0] + ':</td><td> ' + split_text[1] + '</td><td>' + split_text[2] +'</td><td></td></tr>';
				show_text.html(temp);
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
