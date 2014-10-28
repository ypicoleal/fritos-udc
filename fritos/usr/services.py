from models import Asistente, Cajero
from django.contrib.auth import authenticate, login, logout

class UsrService():
	def login(self, request):
		username = request.POST.get('username', False)
		password = request.POST.get('password', False)
		print username, password
		user = authenticate(username = username, password = password)
		if user is not None and user.is_active:
			login(request, user)
			return True
		#end if
		return False
	#end def

	def logout(self, request):
		logout(request)
	#end def

	def hay_sesion(self, request):
		return request.user.is_authenticated()
	#end def

	def es_asistente(self, request):
		if self.hay_sesion(request):
			asistentes = Asistente.objects.filter(usr = request.user)
			if len(asistentes):
				return asistentes[0]
			#end if
		#end if
		return False	
	#end def

	def es_cajero(self, request):
		if self.hay_sesion(request):
			cajeros = Cajero.objects.filter(usr = request.user)
			if len(cajeros):
				return cajeros[0]
			#end if
		#end if
		return False	
	#end def

#end class