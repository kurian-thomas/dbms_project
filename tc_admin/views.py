# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, HttpResponse
import sqlite3
from django.http import HttpResponse,JsonResponse
from datetime import datetime

# Create your views here.
def dashboard(request):
	return render(request, 'tc_admin/dashboard.html')

def login(request):
    return render(request,'tc_admin/login.html')    


def insert_test(question,a,b,c,d,val,test_title,test_des,test_duration,test_tags,test_time,test_date):
    print(question)

    conn=sqlite3.connect('SQL/Main.db')
    cur=conn.cursor()
    test_date_time = datetime.strptime(test_date+" "+test_time, '%Y-%d-%m %H:%M')
    # print(test_date_time)
    # print(test_title, test_des, test_duration, test_date, test_time)
   
    
    # Inserting questions into QUES Table

    for i in range(len(question)):
        p=[]
        print(i)
        p.extend([a[i],b[i],c[i],d[i]])
        cur.execute("INSERT INTO QUES(Ques,Ans_option,Ans_correct) VALUES(:q,:o,:val)",{'q':question[i],'o':str(p),'val':val[i]})
        conn.commit()
    
    # Inserting Test
    cur.execute("INSERT INTO TEST(test_title,test_duration,test_des,test_tags,Date_Time) VALUES(:t1,:t2,:t3,:t4,:t5)",{'t1':test_title[0],'t2':test_duration[0],'t3':test_des[0],'t4':test_tags[0]},'t5':test_date_time)
    conn.commit()

    # Inserting Test_Q

    test_last_id=cur.execute("SELECT test_id FROM TEST ORDER BY test_id DESC LIMIT 1").fetchone() # Fetch the last test_id
    ques_last_id=cur.execute("SELECT id FROM QUES ORDER BY id DESC LIMIT 1").fetchone() # Fetch the last qid
    
    if(test_last_id==None):
        test_last_id=(0,)

    if(ques_last_id==None):
        ques_last_id=(0,)

    ques_last_id=ques_last_id[0]
    test_last_id=test_last_id[0]

    for i in range(len(question)):
        ques_last_id+=1
        cur.execute("INSERT INTO TEST_Q(qid,testid) VALUES(:q1,:q2)",{'q1':ques_last_id,'q2':test_last_id+1})
        conn.commit()     
    
    print((cur.execute("SELECT * FROM TEST_Q")).fetchall())
    cur.execute("SELECT * FROM QUES")
    print(cur.fetchall())
    """
    conn.close()              

@csrf_exempt
def auth(name,passd):
    conn = sqlite3.connect('SQL/Main.db')
    c = conn.cursor()
    c.execute("SELECT * FROM ADMIN WHERE ADMIN.Name=:name AND ADMIN.password=:passd", {'name':name ,'passd':passd})
    l = len(c.fetchall())
    conn.close()
    return(l)

@csrf_exempt    
def adlogin(request): 
    admin_name = request.POST.get("name","")
    admin_pass = request.POST.get("pass","")
    print(str(admin_name)+" "+str(admin_pass))  #to see the form fiels results
    l = auth(admin_name,admin_pass)
    print(l);
    return JsonResponse({"l":l})

def createtest(request):
    return render(request,'tc_admin/create_test.html')

@csrf_exempt
def create_test_form(request):

    question = request.POST.getlist('question')
    test_title = request.POST.get('test_title')
    test_des = request.POST.get('test_des')
    test_duration = request.POST.get('test_duration')
    test_tags = request.POST.get('test_tags')
    test_date=request.POST.get('test_date')
    test_time=request.POST.get('test_time')

    a = request.POST.getlist('A')
    b = request.POST.getlist('B')
    c = request.POST.getlist('C')
    d = request.POST.getlist('D')
    # print(a,b,c,d)
    print(test_title,test_des,test_duration,test_tags)
    val = request.POST.getlist('check')
    # print(val)
    insert_test(question,a,b,c,d,val,test_title,test_des,test_duration,test_tags,test_time,test_date) # insert function


    return HttpResponse("hi")