from services import UsrService
from django.http import HttpResponse

def asistente(view):
	def new(request, **kwargs):
		service = UsrService()
		if service.es_asistente(request):
			return view(request, **kwargs)
		#end if
		return HttpResponse(status=401)
	#end def
	return new
#end def

def cajero(view):
	def new(request, **kwargs):
		service = UsrService()
		if service.es_cajero(request):
			return view(request, **kwargs)
		#end if
		return HttpResponse(status=401)
	#end def
	return new
#end def
