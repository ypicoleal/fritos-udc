from forms import ProductoForm, VentaForm, VentaProductoForm
from usr.models import Asistente, Cajero
from models import Venta, Producto
from django.db import connection
import simplejson

class VentaService():

	def crear_venta(self, request):
		venta = VentaForm(request.POST.copy())
		asistente = Asistente.objects.get(usr = request.user)
		venta.data['asistente'] = str(asistente.id)
		if venta.is_valid():
			v = venta.save()
			return v.pk
		#end if
		print venta.errors
		return False
	#end def

	def agregar_producto(self, request):
		vp = VentaProductoForm(request.POST)
		if vp.is_valid():
			vp.save()
			return True
		#end if
		return False
	#end def

	def confirmar_venta(self, request):
		venta = request.POST.get('venta',False)
		ventas = Venta.objects.filter(id = venta)
		cajero = Cajero.objects.get(usr = request.user)
		if len(ventas):
			venta = ventas[0]
			venta.estado = True
			venta.cajero = cajero
			venta.save()
			cursor = connection.cursor()
			cursor.execute("SELECT restar_existencias(%s)", [str(venta.id)])
			return True
		#end if
		return False
	#end def

	def anular_venta(self, request):
		venta = request.POST.get('venta',False)
		ventas = Venta.objects.filter(id = venta)
		if len(ventas):
			venta = ventas[0]
			venta.estado = False
			venta.save()
			return True
		#end if
		return False
	#end def

	def ordenes(self, request):
		cursor = connection.cursor()
		cursor.execute("SELECT ordenes()")
		row = cursor.fetchone()
		return row[0]
	#end def 

	def mostrar_venta(self, request,venta):
		cursor = connection.cursor()
		cursor.execute("SELECT mostrar_venta(%s)",[venta,])
		row = cursor.fetchone()
		return row[0]
	#end def 

	def mostrar_dia(self, request):
		cursor = connection.cursor()
		cursor.execute("SELECT mostrar_dia()")
		row = cursor.fetchone()
		return row[0]
	#end def
	def productos(self, request):
		productos = Producto.objects.values()
		return simplejson.dumps(list(productos))
	#end def
#end class