#!/bin/bash
from django.shortcuts import render
from services import UsrService
from django.http import HttpResponse

def login(request):
	return render(request, 'usr/login.html', {})
#end def

def login_do(request):
	service = UsrService()
	if service.login(request):
		return HttpResponse(status=200)
	#end if
	return HttpResponse(status=400)
#end def

def logout(request):
	service = UsrService()
	service.logout(request)
	return HttpResponse(status=200)
#end def