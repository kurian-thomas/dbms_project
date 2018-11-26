from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
import sqlite3
from datetime import datetime

import json
import ast

from .decorators import login_required

from django.db import connection as conn

def index(request):
	return render(request,'tc_app/index.html')

def login(request):
	return render(request,'tc_app/login.html')

@login_required
def dashboard(request):

	c = conn.cursor()
	try:
		user_admission = request.session['user']
	except:
		user_admission = ''
	c.execute("SELECT username FROM USER WHERE USER.id = '{}'".format(user_admission))
	user_name = c.fetchone()[0]
	print(user_name)
	# Fetch all the tests from database
	tests = []
	c.execute("SELECT * FROM TEST")
	for row in c.fetchall():
		print(row)
		date = row[3]#datetime.strptime(row[3], "%Y-%m-%d %H:%M:%S")
		tests.append({
			'id': row[0],
			'title': row[1],
			'description': row[2],
			'date': date.strftime("%d-%B-%Y"),
			'time': date.strftime('%I:%M %p'),
			'duration': row[4]
			})

	#Fetch all the attempted test_id 
	c.execute("SELECT id, mark, title FROM TEST_REPORT a, TEST b where a.test_id = b.id AND user_id = '{}' ".format(user_admission))
	attempted_tests_obj = c.fetchall()
	attempted_tests = []
	test_report = []
	
	for i in attempted_tests_obj:
		print(i)
		attempted_tests.append(int(i[0]))
		test_report.append([i[2], i[1]])

	print(test_report)
	conn.close()
	return render(request,'tc_app/dashboard.html',{'user_name': user_name, 'tests': tests, 'attempted_tests': attempted_tests, 'test_report': test_report})

def auth(admission ,password):
    c = conn.cursor()
    c.execute("SELECT username FROM USER WHERE USER.id = '{}' AND USER.password = '{}'".format(admission, password))
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
	stream = request.POST.get("stream","")
	sem = request.POST.get("sem","")
	division = request.POST.get("division","")
	
	c = conn.cursor()
	c.execute("INSERT INTO USER VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(admission, email, name, password, stream, sem, division))
	conn.close()

	request.session['user'] = admission

	return render(request,'tc_app/index.html')

@csrf_exempt
def get_element_log(request):
	admission = request.POST.get("ad","")
	password = request.POST.get("pass","")

	request.session['user'] = admission
	l=auth(admission, password)

	return JsonResponse({"l":l})


@csrf_exempt
#@login_required
def test(request, test_id = -1):
	# User has submitted test
	if request.method == 'POST':
		c = conn.cursor()
		responses = request.POST
		user_id = request.session['user']

		c.execute("SELECT id, correct FROM QUES WHERE QUES.test_id = {}".format(test_id))
		correct = c.fetchall()

		score = 0
		total_questions = 0

		for i in correct:
			total_questions += 1
			try:
				c.execute("INSERT INTO USER_RESPONSE VALUES('{}', '{}', '{}', '{}')".format(user_id, test_id, i[0], responses[str(i[0])]))
			except KeyError:
				pass
			conn.commit()
			try:
				if(responses[str(i[0])] == i[1]):
					score += 1
			except KeyError:
				print("user has not attempted question "+ str(i[0]))


		percentage = (score/float(total_questions))*100
		print("Total score", score, "Percentage", percentage)

		# sql to store the score 
		c.execute("INSERT INTO TEST_REPORT VALUES('{}', '{}', '{}')".format(user_id, test_id, str(percentage)))
		conn.commit()
		conn.close()

		return render(request, 'tc_app/score.html', {'score': percentage})
	else:
		dict={}
		if test_id == -1:
			return HttpResponseRedirect('/tc/dashboard')
		# User is taking the test
		else:
			print(test_id)
			c = conn.cursor()
			# Get the test duration
			c.execute("SELECT duration FROM TEST WHERE id={}".format(test_id))
			test_duration = int(float(c.fetchone()[0])*60)
			#Retriving the test questions
			c.execute("SELECT id, ques, optA, optB, optC, optD, correct from QUES where test_id={}".format(test_id))
			questions_object = c.fetchall()
			questions=[]			
			for i in questions_object:
				# pass
				print(i)
				options = [i[2], i[3], i[4], i[5]]
				print(options)
				questions.append({"q_id":i[0], "question": i[1], "question_options": options})

			dict['questions'] = questions
			dict['test_id'] = test_id
			dict['test_duration'] = test_duration
			return render(request,'tc_app/test.html', dict)

@login_required
def logout(request):
    try:
        del request.session['user']
        return HttpResponseRedirect("/tc/login/")
    except:
        return HttpResponseRedirect("/tc/login/")


def previous_tests(request):
	c = conn.cursor()
	# Fetch all the tests from database
	tests = []
	c.execute("SELECT * FROM TEST")
	for row in c.fetchall():
		print(row)
		date = row[3]#datetime.strptime(row[3], "%Y-%m-%d %H:%M:%S")
		tests.append({
			'id': row[0],
			'title': row[1],
			'description': row[2],
			'date': date.strftime("%d-%B-%Y"),
			'time': date.strftime('%I:%M %p'),
			'duration': row[4]
			})
	conn.close()
	return render(request, 'tc_app/previous_tests.html', {'tests': tests})

def test_analytics(request, test_id):
	c = conn.cursor()
	#Retriving the test questions
	c.execute("SELECT Q.id, Q.ques, Q.optA, Q.optB, Q.optC, Q.optD, Q.correct, R.response, if(Q.correct = R.response, 1, 0) as correct from QUES Q, USER_RESPONSE R where Q.id = R.question_id AND Q.test_id={}".format(test_id))
	questions_object = c.fetchall()
	questions=[]			
	for i in questions_object:
		print(i)
		options = [i[2], i[3], i[4], i[5]]
		print(options)
		questions.append({"q_id":i[0], "question": i[1], "question_options": options, 'correct': i[6], 'response': i[7], 'user_correct': i[8]})
	dict={}
	dict['questions'] = questions
	dict['test_id'] = test_id
	return render(request, 'tc_app/test_analytics.html', dict)


# def index(request):
# 	return render(request,'tc_app/index.html')

# def login(request):
# 	return render(request,'tc_app/login.html')

# @login_required
# def dashboard(request):

# 	try:
# 		user_admission = request.session['user']
# 	except:
# 		user_admission=''

# 	conn = sqlite3.connect('SQL/Main.db')
# 	c = conn.cursor()

# 	try:
# 		user_name = c.execute("SELECT username FROM USER WHERE USER.id=:id",{'id':user_admission}).fetchall()[0][0]
# 	except:
# 		user_name=''
# 		print("User not registered")
# 	conn.close()

# 	# Fetch all the tests from database
# 	conn = sqlite3.connect('SQL/Main.db')
# 	c = conn.cursor()
# 	tests = []
# 	for row in c.execute("SELECT * FROM TEST"):
# 		date = datetime.strptime(row[3], "%Y-%m-%d %H:%M:%S")
# 		tests.append({
# 			'id': row[0],
# 			'title': row[1],
# 			'description': row[2],
# 			'date': date.strftime("%d-%B-%Y"),
# 			'time': date.strftime('%I:%M %p'),
# 			'duration': row[4]
# 			})
# 	conn.close()
# 	return render(request,'tc_app/dashboard.html',{'user_name': user_name, 'tests': tests})

# def insert_sql(id,name,email,password,types):
#     conn = sqlite3.connect('SQL/Main.db')
#     c = conn.cursor()
#     c.execute("INSERT INTO USER VALUES(:id,:email,:name,:passd,:type)",{'id':id,'email':email,'name':name,'passd':password,'type':types})
#     c.execute("SELECT * FROM USER ")
#     conn.commit()
#     conn.close()


# def auth(id,passd):
#     conn = sqlite3.connect('SQL/Main.db')
#     c = conn.cursor()
#     c.execute("SELECT username FROM USER WHERE USER.id=:id AND USER.password=:passd",{'id':id,'passd':passd})
#     l = c.fetchall();
#     conn.close()
#     print(l)
#     if l:
#         return [len(l),l]
#     else:
#         return [len(l),"None"]


# @csrf_exempt
# def get_element(request):
# 	name = request.POST.get("name","")
# 	admission = request.POST.get("admission","")
# 	email = request.POST.get("email","")
# 	password = request.POST.get("pass","")
# 											#new variables
# 	stream= request.POST.get("stream","")
# 	sem= request.POST.get("sem","")
# 	division=request.POST.get("division","")
# 	print(stream+sem+division)
# 	insert_sql(admission,name,email,password,'U')
# 	# print(str(email)+" "+str(name)+" "+str(admission)+" "+str(password))

# 	request.session['user'] = admission

# 	return render(request,'tc_app/index.html')

# @csrf_exempt
# def get_element_log(request):
# 	admission = request.POST.get("ad","")
# 	password = request.POST.get("pass","")

# 	request.session['user'] = admission
# 	l=auth(admission,password)
# 	print(l)

# 	print("get_element_log")
# 	# print(str(admission)+" "+str(password))  #to see the form fiels results
# 	return JsonResponse({"l":l})

# @csrf_exempt
# @login_required
# def test(request, test_number = 0):
# 	if request.method == 'POST':
# 		print(test_number)
# 		print(request.POST)
# 		responses = request.POST
# 		user_id = request.session['user']

# 		conn = sqlite3.connect('SQL/Main.db')
# 		c = conn.cursor()

# 		# correct = c.execute("SELECT * FROM QUES WHERE QUES.id = :id",{'id':test_number}).fetchall()
# 		# correct = c.execute("SELECT * FROM QUES").fetchall()

# 		correct = c.execute("SELECT * FROM TEST_Q WHERE testid = :test_number", {"test_number": test_number}).fetchall()	
# 		print(correct)

# 		for i in correct:
# 			print(i[0], i[3])

# 		mark = 0

# 		for i in request.POST:
# 			print(i)
	
# 		conn.commit()
# 		conn.close()

# 		return HttpResponseRedirect('/tc/dashboard')
# 	else:
# 		dict={}
# 		if test_number == 0:
# 			return render(request, 'tc_app/dashboard.html')
# 		else:
# 			#retrieve the questions from the table 
# 			conn=sqlite3.connect('SQL/Main.db')
# 			cur = conn.cursor()

# 			#Retriving the test questions
# 			questions_object = cur.execute("Select id, Ques, Ans_option  from QUES where id in (SELECT qid from TEST_Q where testid = :test_id)", {"test_id": test_number})
# 			questions=[]
			
# 			for i in questions_object:
# 				options = ast.literal_eval(i[2])
# 				print(options)
# 				questions.append({"q_id":i[0], "question": i[1], "question_options": options})

# 			dict['questions'] = questions
# 			dict['test_number'] = test_number
# 			return render(request,'tc_app/test.html',dict)

# @login_required
# def logout(request):
#     try:
#         del request.session['user']
#         return HttpResponseRedirect("/tc/login/")
#     except:
#         return HttpResponseRedirect("/tc/login/")
