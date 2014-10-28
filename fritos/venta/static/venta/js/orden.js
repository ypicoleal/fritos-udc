$(document).ready(function(){
	conf = {
		autoOpen:  false,
	    draggable: false,
	    resizable: false,
	    show: {
	    	effect: "slideDown",
	        duration: 200
	    },
	    hide: {
	        effect: "slideUp",
	        duration: 200
	    },
	    buttons: {
	    	"Ok":function (){
	    		ajaxCrearVenta();
	    	},
	    	"Cancelar":function(){
	    		$("#crearVenta").dialog("close");
	    	}
	    }
	};
	ordenes();
	agregar();
});

function ordenes(){
	$.ajax({
		url:'/venta/ordenes/',
		type:'post',
		dataType: 'json',
		data:{ csrfmiddlewaretoken:$('input[name="csrfmiddlewaretoken"]').val()},
		success: function(response){
			if(response.length == 0){
				alert("No han creado ninguna Orden");
			}else{
				console.log(response);
				var ordenes = $("#ordenes").html("");
				for(var i = 0; i < response.length; i++){
					var li = $("<li></li>");
					var ul = $("<ul></ul>");

					$.each(response[i].productos,function(index,value){
						ul.append("<li><i>"+value.producto+"</i><a>"+value.cantidad+"</a></li>");
					});
					li.append(ul);
					console.log(li);
					$('#ordenes').append(li);
				}
			}
		}
	});
}

function agregar(){
		$("#crearVenta").dialog(conf);
$("li#add").click(function (){
		$("#crearVenta").dialog("open");
	});
}
function ajaxCrearVenta(){
	$.ajax({
		url:'/venta/crear/do/',
		data:{numero:$("#numero").val(), csrfmiddlewaretoken:$('input[name="csrfmiddlewaretoken"]').val()},
		type: 'post',
		success: function (response){
			window.location = "/venta/crear/" + response +"/";
		},
		error: function(response){
			alert("un error ocurrio");
		}
	});
}
function agregarOrden(){
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
	    window.location = '/venta/crear/'
	} 
	function showError(error){
		console.log(error.status);
		if(error.status == 400){
			alert("Datos Incorreptos");
			$("#formLogin").clearForm();
		}else if(error.status == 401){
			alert("Debe iniciar session");
		}else if(error.status == 0){
			alert("servidor fuera de servicio");
		}
	}
}