$("#login-button").click(function(event){
	event.preventDefault();
	
	

	var busca = {}
    busca.user = $('#username').val();
    busca.pass = $('#password').val();
    console.log(busca);
	$.post("http://127.0.0.1:8080/login", busca, function(data, status) {
        if(data == 'true'){
            $('form').fadeOut(500);
	        $('.wrapper').addClass('form-success');        
	        $('#label').empty();
            $('#label').append('Welcome to Prisvo ');
        }else{
            $('#label').empty();
            $('#label').append('Wrong username or password');
        }
    });
});