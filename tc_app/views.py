from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import sqlite3
# Create your views here.

def index(request):
	return render(request,'tc_app/index.html')

def login(request):
	return render(request,'tc_app/login.html')

def dashboard(request):
	return render(request,'tc_app/dashboard.html')

def insert_sql(id,name,email,password,types):
    conn=sqlite3.connect('SQL/Main.db')
    c=conn.cursor()
    c.execute("INSERT INTO USER VALUES(:id,:email,:name,:passd,:type)",{'id':id,'email':email,'name':name,'passd':password,'type':types})
    c.execute("SELECT * FROM USER ")
    print(c.fetchall())
    conn.commit()
    conn.close()    

def auth(id,passd):
    conn=sqlite3.connect('SQL/Main.db')
    c=conn.cursor()
    c.execute("SELECT * FROM USER WHERE USER.id=:id AND USER.password=:passd",{'id':id,'passd':passd})
    l=len(c.fetchall())
    conn.close()
    return l

@csrf_exempt
def get_element(request):
	name=request.POST.get("name","")
	admission=request.POST.get("admission","")
	email=request.POST.get("email","")
	password=request.POST.get("pass","")
	insert_sql(admission,name,email,password,'U')
	print(str(email)+" "+str(name)+" "+str(admission)+" "+str(password))
	return render(request,'tc_app/index.html')

@csrf_exempt				
def get_element_log(request):
	admission=request.POST.get("ad","")
	password=request.POST.get("pass","")
	l=auth(admission,password)
	print(l)
	# print(str(admission)+" "+str(password))  #to see the form fiels results
	return JsonResponse({"l":l})					
