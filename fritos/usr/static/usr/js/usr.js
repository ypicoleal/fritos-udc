$(document).ready(function(){
	login();
});

function login(){
	var options = {
		//beforeSubmit:  showRequest,  // pre-submit callback 
        success:       showResponse,
        error: showError,
        type: 'post'
        // other available options: 
        //url:       url         // override for form's 'action' attribute 
        //type:      type        // 'get' or 'post', override for form's 'method' attribute 
        //dataType:  null        // 'xml', 'script', or 'json' (expected server response type) 
        //clearForm: true        // clear all form fields after successful submit 
        //resetForm: true        // reset the form after successful submit 
        // $.ajax options can be used here too, for example: 
        //timeout:   3000
	};
	$('#formLogin').ajaxForm(options); 
	function showRequest(formData, jqForm, options) { 
    	
    } 
 
	// post-submit callback 
	function showResponse(responseText, statusText, xhr, $form)  { 
	    console.log(statusText);
	    window.location = '/'
	} 
	function showError(error){
		console.log(error.status);
		if(error.status == 400){
			alert("User o Password erroneos");
			$("#formLogin").clearForm();
		}else if(error.status == 401){
			alert("Debe iniciar session");
		}else if(error.status == 0){
			alert("servidor fuera de servicio");
		}
	}
}