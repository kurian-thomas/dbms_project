# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, HttpResponse
import sqlite3

# Create your views here.
def dashboard(request):
	return render(request, 'tc_admin/dashboard.html')

@csrf_exempt
def auth(name,passd):
    conn=sqlite3.connect('SQL/Main.db')
    c=conn.cursor()
    c.execute("SELECT * FROM ADMIN WHERE ADMIN.Name=:name AND ADMIN.password=:passd",{'name':name,'passd':passd})
    l=len(c.fetchall())
    c.execute("SELECT * FROM ADMIN")
    print(c.fetchall())
    conn.close()
    return(l)

@csrf_exempt   
def login(request): 
	admin_name=request.POST.get("name","")
	admin_pass=request.POST.get("pass","")
	print(str(admin_name)+" "+str(admin_pass))  #to see the form fiels results
	print(auth(admin_name,admin_pass))
	return render(request, 'tc_admin/login.html')
