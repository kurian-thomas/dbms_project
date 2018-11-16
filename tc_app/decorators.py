from django.shortcuts import render,HttpResponse
from django.http import HttpResponseRedirect,JsonResponse

def login_required(view_func):
	def login_check(request):
		if 'user' in request.session:
			return view_func(request)
		else :
			return HttpResponseRedirect('/tc/login')
	return login_check