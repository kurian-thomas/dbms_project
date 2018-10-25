# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, HttpResponse

# Create your views here.
def dashboard(request):
	return render(request, 'tc_admin/dashboard.html')
@csrf_exempt
def login(request): 
	admin_name=request.POST.get("name","")
	admin_pass=request.POST.get("pass","")
	print(str(admin_name)+" "+str(admin_pass))  #to see the form fiels results
	return render(request, 'tc_admin/login.html')
