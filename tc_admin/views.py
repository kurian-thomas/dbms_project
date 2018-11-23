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

def insert_test(question,a,b,c,d,val):
    print(question)

    conn=sqlite3.connect('SQL/Main.db')
    cur=conn.cursor()
    for i in range(len(question)):
        p=[]
        print(i)
        p.extend([a[i],b[i],c[i],d[i]])
        cur.execute("INSERT INTO QUES(Ques,Ans_option,Ans_correct) VALUES(:q,:o,:val)",{'q':question[i],'o':str(p),'val':val[i]})
        conn.commit()
    cur.execute("SELECT * FROM QUES")
    print(cur.fetchall())
    conn.close()              
        

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
    question=request.POST.getlist('question')
    test_title=request.POST.get('test_title')
    test_des=request.POST.get('test_des')
    test_duration=request.POST.get('test_duration')
    test_date=request.POST.get('test_date')
    test_time=request.POST.get('test_time')
    test_tags=request.POST.get('test_tags')
    a=request.POST.getlist('A')
    b=request.POST.getlist('B')
    c=request.POST.getlist('C')
    d=request.POST.getlist('D')
    # print(a,b,c,d)
    print(test_title,test_des,test_duration,test_tags)
    val=request.POST.getlist('check')
    # print(val)
    # insert_test(question,a,b,c,d,val) # insert function
    # print(question)
    # print(a)
    # print(b)
    # print(c)
    # print(d)
    print(val)

    return HttpResponse("hi")