from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
	return render(request,'tc_app/index.html')


def insert_sql(id,name,email,password,types):
    conn=sqlite3.connect('dbms_project\SQL\Main.db')
    c=conn.cursor()
    c.execute("INSERT INTO USER VALUES(:id,:email,:name,:passd,:type)",{'id':id,'email':email,'name':name,'passd':password,'type':types})
    conn.commit()
    conn.close()    

@csrf_exempt
def get_element(request):
	name=request.POST.get("name","")
	admission=request.POST.get("admission","")
	email=request.POST.get("email","")
	password=request.POST.get("pass","")
   insert_sql(admission,name,email,password,'U')
	print(str(email)+" "+str(name)+" "+str(admission)+" "+str(password))
   return render(request,'tc_app/index.html')	
				
