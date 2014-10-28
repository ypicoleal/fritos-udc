from django.forms import ModelForm
from models import Producto, Venta, VentaProducto
class ProductoForm(ModelForm):
	class Meta:
		model = Producto
	#end class
#end clas
class VentaForm(ModelForm):
	class Meta:
		model = Venta
	#end class
#end clas
class VentaProductoForm(ModelForm):
	class Meta:
		model = VentaProducto
	#end class
#end clas