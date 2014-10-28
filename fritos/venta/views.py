from django.shortcuts import render
from django.http import HttpResponse
from usr.decorators import asistente, cajero
from services import VentaService
	
@asistente
def crear_venta(request, venta):
	return render(request,'venta/crear_venta2.html',{'venta': venta})
#end def

@asistente
def crear_venta_do(request):
	status = 400
	service = VentaService()
	resp = service.crear_venta(request)
	if resp:
		status = 200
		return HttpResponse(str(resp), status=status)
	#end if
	return HttpResponse(status=status)
#end def

@asistente
def agregar_producto(request):
	status = 400
	service = VentaService()
	if service.agregar_producto(request):
		status = 200
	#end if
	return HttpResponse(status=status)
#end def

@cajero
def confirmar_venta(request):
	status = 400
	service = VentaService()
	if service.confirmar_venta(request):
		status = 200
	#end if
	return HttpResponse(status=status)
#end def

@asistente
def anular_venta(request):
	status = 400
	service = VentaService()
	if service.anular_venta(request):
		status = 200
	#end if
	return HttpResponse(status=status)
#end def

def ordenes(request):
	service = VentaService()
	resp = service.ordenes(request)
	if resp:
		return HttpResponse(resp,content_type="application/json")
	#end if
	return HttpResponse(status=400)
#end def

def mostrar_venta(request,venta):
	service = VentaService()
	resp = service.mostrar_venta(request,venta)
	if resp:
		return HttpResponse(resp,content_type="application/json")
	#end if
	return HttpResponse(status=400)
#end def

def mostrar_dia(request):
	service = VentaService()
	resp = service.mostrar_dia(request)
	if resp:
		return HttpResponse(resp,content_type="application/json")
	#end if
	return HttpResponse(status=400)
#end def

def productos(request):
	service = VentaService()
	resp = service.productos(request)
	if resp:
		return HttpResponse(resp,content_type="application/json")
	#end if
	return HttpResponse(status=400)
#end def