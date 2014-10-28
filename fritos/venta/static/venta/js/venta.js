$(document).ready(function(){
	productos();
});

function productos () {
	$.ajax({
		url:'/venta/productos/',
		type:'post',
		data:{ csrfmiddlewaretoken:$('input[name="csrfmiddlewaretoken"]').val()},
		dataType: 'json',
		success: function(response){
			if(response.length == 0){
				alert("No hay ningun producto");
			}else{
				console.table(response);
				$("#productos li ul").html("");
				var n = 1
				$.each(response, function (index, value) {
					console.log(n)
					$("#productos li:nth-child(" + n + ") ul").append("<li>"+
	                "<i>"+value.nombre+"</i>"+
	                "<table>"+
	                    "<tr>"+
	                        "<td><i class='font1'></i></td>"+
	                        "<td class='br'><i class='font2'></i>#</td>"+
	                    "</tr>"+
	                    "<tr>"+
	                        "<td class='br'><i class='font1'></i>-</td>"+
	                       "<td class='br'><i class='font2'></i>+</td>"+
	                    "</tr>"+
	                "</table></li>");
	                n = n==3?1:n+1;
				});
				productos_venta();
			}
		}
	});
}
function productos_venta(){
	$.ajax({
		url:'/venta/'+$("#ventaid").val()+'/',
		type:'post',
		data:{ csrfmiddlewaretoken:$('input[name="csrfmiddlewaretoken"]').val()},
		dataType: 'json',
		success: function(response){
			if(response.length == 0){
				alert("No hay ningun producto");
			}else{
				console.log(response);
				for(var i = 0; i<response.length;i++){
					
				}
			}
		}
	});
}