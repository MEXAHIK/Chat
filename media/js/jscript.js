$(document).ready(function(){
	
// Создание обьекта XMLHttpRequest
	function CreateRequest(){
		var Request = false;
		
		if (window.XMLHttpRequest){
			//Gecko-совместимые браузеры, Safari, Konqueror
			Request = new XMLHttpRequest();
			}
		else if (window.ActiveXObject){
			//Internet explorer
			try{
				Request = new ActiveXObject("Microsoft.XMLHTTP");
				alert('IE, Microsoft.XMLHTTP');
			}
			catch (CatchException){
				Request = new ActiveXObject("Msxml2.XMLHTTP");
				alert('IE, Msxml2.XMLHTTP');
			}
		}
		
		if (!Request){
			alert("Невозможно создать XMLHttpRequest");
		}
		return Request;
	}

//  фнкция отправки сообщения
	function sendMessage(){
		Request = CreateRequest();
		var show_text = $('#show_text'), temp;
		if ($('#send_text').val() != "") {
			temp = show_text.html() + '<tr><td color="#1119CB">' + $('#user_name > a').text() + ':</td><td> ' + $('#send_text').val() + '</td><td></td></tr>';
			show_text.html(temp);
			$.post('/send-message/', {} , function(){
				alert(Request.responseText);
			});
			$('#send_text').val('');
		};
	};
	
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