from django.db import models
from usr.models import Asistente, Cajero
class Producto(models.Model):
	nombre = models.CharField(max_length=45)
	existencia = models.IntegerField()
	precio = models.IntegerField()
	descripcion = models.TextField()

	def __unicode__(self):
		return u'%s' % (self.nombre,)
	#end 
#end class

class Venta(models.Model):
	fecha = models.DateTimeField(auto_now_add=True)
	numero = models.CharField(max_length=45)
	estado = models.NullBooleanField(null=True, default=None)
	asistente = models.ForeignKey(Asistente)
	cajero = models.ForeignKey(Cajero, null=True, blank=True)
	
	def __unicode__(self):
		return u'%s' % (self.numero)
	#end def
#end class

class VentaProducto(models.Model):
	venta = models.ForeignKey(Venta)
	producto = models.ForeignKey(Producto)
	cantidad = models.IntegerField()
#end class