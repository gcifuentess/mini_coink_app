$(document).ready(function(){

    // Check API status
    $.getJSON('http://0.0.0.0:5001/api/v1/status', (data) => {
	if (data.status === 'OK') {
	    $('DIV#api_status').addClass('available');
	} else {
	    $('DIV#api_status').removeClass('available');
	}
    });

    function convertFormToJSON(form) {
	 // Encodes the set of form elements as an array of names and values:
    	const array = $(form).serializeArray();
    	const json = {};
    	$.each(array, function () {
    	    json[this.name] = this.value || "";
    	});
    	return JSON.stringify(json);
    };

    // to register users:
    $('button#registry').click(function(){
	$('#includedContent').removeClass('show_error');
	$('#includedContent').removeClass('show_ok');
	$('#includedContent').addClass('dont_show');

    	$.ajax('http://0.0.0.0:5001/api/v1/users', {
    	    type: 'POST',
    	    contentType: 'application/json',
    	    data: convertFormToJSON($('#form1')),
	    success: function(){
		$("#includedContent").empty();
		// resets the form:
		$('#form1')[0].reset();
		$("#includedContent").append('<p>¡Registro Exitoso!</p>');
		$('#includedContent').removeClass('dont_show');
		$('#includedContent').addClass('show_ok');
	    },
	    error: function(jqXHR, textStatus, errorThrown){
		$('#includedContent').removeClass('dont_show');
		$('#includedContent').addClass('show_error');
		// reads the api response and inserts it in the html:
		$('#includedContent').html(
		    $.parseHTML(jqXHR['responseText'])[5]
		);
	    }
    	});
    });
});
