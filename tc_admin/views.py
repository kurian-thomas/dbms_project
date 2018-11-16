# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, HttpResponse
import sqlite3
from django.http import HttpResponse,JsonResponse

# Create your views here.
def dashboard(request):
	return render(request, 'tc_admin/dashboard.html')

def login(request):
    return render(request,'tc_admin/login.html')    

@csrf_exempt
def auth(name,passd):
    conn=sqlite3.connect('SQL/Main.db')
    c=conn.cursor()
    c.execute("SELECT * FROM ADMIN WHERE ADMIN.Name=:name AND ADMIN.password=:passd",{'name':name,'passd':passd})
    l=len(c.fetchall())
    conn.close()
    return(l)

@csrf_exempt    
def adlogin(request): 
    admin_name=request.POST.get("name","")
    admin_pass=request.POST.get("pass","")
    print(str(admin_name)+" "+str(admin_pass))  #to see the form fiels results
    l=auth(admin_name,admin_pass)
    print(l);
    return JsonResponse({"l":l})

def createtest(request):
    return render(request,'tc_admin/create_test.html')

@csrf_exempt
def create_test_form(request):
    print(request.POST)
    questions = request.POST.getlist('question')
    options_a = request.POST.getlist('A')
    options_b = request.POST.getlist('B')
    options_c = request.POST.getlist('C')
    options_d = request.POST.getlist('D')
    answers = request.POST.getlist('answer')
    test_title = request.POST.get('test_title')
    test_desc = request.POST.get('test_desc')
    test_date = request.POST.get('test_date')
    test_duration = request.POST.get('test_duration')
    test_tags = request.POST.get('test_tags')
    print(questions)
    print(options_a)
    print(options_b)
    print(options_c)
    print(options_d)
    print(answers)
    print(test_title, test_desc, test_date, test_duration, test_tags)

    return HttpResponse("hi")