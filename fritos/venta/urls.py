from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
    # Examples:
	url(r'^crear/(?P<venta>\d+)/$', views.crear_venta, name="crear_venta"),
    url(r'^crear/do/$', views.crear_venta_do, name="crear_venta_do"),
	url(r'^agregar/producto/$', views.agregar_producto, name="agregar_producto"),
	url(r'^confirmar/$', views.confirmar_venta, name="confirmar_venta"),
	url(r'^anular/$', views.anular_venta, name="anular_venta"),
	
	url(r'^ordenes/$', views.ordenes, name='ordenes'),
	url(r'^(?P<venta>\d+)/$', views.mostrar_venta, name='mostrar_venta'),
	url(r'^dia/$', views.mostrar_dia, name='mostrar_dia'),
	url(r'^productos/$', views.productos, name='productos'),
)