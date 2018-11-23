from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
import sqlite3
from datetime import datetime

import json
import ast

from .decorators import login_required
# Create your views here.

def index(request):
	return render(request,'tc_app/index.html')

def login(request):
	return render(request,'tc_app/login.html')

@login_required
def dashboard(request):

	try:
		user_admission = request.session['user']
	except:
		user_admission=''

	conn = sqlite3.connect('SQL/Main.db')
	c = conn.cursor()

	try:
		user_name = c.execute("SELECT username FROM USER WHERE USER.id=:id",{'id':user_admission}).fetchall()[0][0]
	except:
		user_name=''
		print("User not registered")
	conn.close()

	# Fetch all the tests from database
	conn = sqlite3.connect('SQL/Main.db')
	c = conn.cursor()
	tests = []
	for row in c.execute("SELECT * FROM TEST"):
		date = datetime.strptime(row[3], "%Y-%m-%d %H:%M:%S")
		tests.append({
			'id': row[0],
			'title': row[1],
			'description': row[2],
			'date': date.strftime("%d-%B-%Y"),
			'time': date.strftime('%I:%M %p'),
			'duration': row[4]
			})
	conn.close()
	return render(request,'tc_app/dashboard.html',{'user_name': user_name, 'tests': tests})

def insert_sql(id,name,email,password,types):
    conn = sqlite3.connect('SQL/Main.db')
    c = conn.cursor()
    c.execute("INSERT INTO USER VALUES(:id,:email,:name,:passd,:type)",{'id':id,'email':email,'name':name,'passd':password,'type':types})
    c.execute("SELECT * FROM USER ")
    conn.commit()
    conn.close()


def auth(id,passd):
    conn = sqlite3.connect('SQL/Main.db')
    c = conn.cursor()
    c.execute("SELECT username FROM USER WHERE USER.id=:id AND USER.password=:passd",{'id':id,'passd':passd})
    l = c.fetchall();
    conn.close()
    print(l)
    if l:
        return [len(l),l]
    else:
        return [len(l),"None"]


@csrf_exempt
def get_element(request):
	name = request.POST.get("name","")
	admission = request.POST.get("admission","")
	email = request.POST.get("email","")
	password = request.POST.get("pass","")
	insert_sql(admission,name,email,password,'U')
	print(str(email)+" "+str(name)+" "+str(admission)+" "+str(password))

	request.session['user'] = admission

	return render(request,'tc_app/index.html')

@csrf_exempt
def get_element_log(request):
	admission = request.POST.get("ad","")
	password = request.POST.get("pass","")

	request.session['user'] = admission
	l=auth(admission,password)
	print(l)

	print("get_element_log")
	# print(str(admission)+" "+str(password))  #to see the form fiels results
	return JsonResponse({"l":l})

@csrf_exempt
@login_required
def test(request, test_number = 0):
	if request.method == 'POST':
		print(test_number)
		print(request.POST)
		responses = request.POST
		user_id = request.session['user']

		conn = sqlite3.connect('SQL/Main.db')
		c = conn.cursor()

		# correct = c.execute("SELECT * FROM QUES WHERE QUES.id = :id",{'id':test_number}).fetchall()
		# correct = c.execute("SELECT * FROM QUES").fetchall()

		correct = c.execute("SELECT * FROM TEST_Q").fetchall()		

		for i in correct:
			print(i[0], i[3])

		mark = 0

		for i in request.POST:
			print(i)
		# print(a,b,c,d)
		return HttpResponseRedirect('/tc/dashboard')
	else:
		dict={}
		if test_number == 0:
			return render(request, 'tc_app/dashboard.html')
		else:
			#retrieve the questions from the table 
			conn=sqlite3.connect('SQL/Main.db')
			cur = conn.cursor()
			questions_object = cur.execute("Select * from QUES")
			questions=[]
			
			for i in questions_object:
				options = ast.literal_eval(i[2])
				print(options)
				questions.append({"q_id":i[0], "question": i[1], "question_options": options})

			dict['questions'] = questions
			dict['test_number'] = test_number
			return render(request,'tc_app/test.html',dict)

@login_required
def logout(request):
    try:
        del request.session['user']
        return HttpResponseRedirect("/tc/login/")
    except:
        return HttpResponseRedirect("/tc/login/")
