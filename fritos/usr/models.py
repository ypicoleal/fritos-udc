from django.db import models
from django.contrib.auth.models import User

class Asistente(models.Model):
	usr = models.ForeignKey(User)

	def __unicode__(self):
		return u'%s' % (self.usr.username,)
	#end def
#end class

class Cajero(models.Model):
	usr = models.ForeignKey(User)

	def __unicode__(self):
		return u'%s' % (self.usr.username,)
	#end def
#end class
