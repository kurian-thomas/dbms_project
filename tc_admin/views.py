# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

# Create your views here.
def dashboard(request):
	return render(request, 'tc_admin/dashboard.html')

def login(request): 
	return render(request, 'tc_admin/login.html')
