from django.shortcuts import render
from .models import course_detail
from.models import teacher

# Create your views here.

def hello(request):
	return render(request,'demoapp/student_support.html')


'''def insert(request):

    c_name= request.POST['t1']
    aff_uni = request.POST['t2']
    seats = request.POST['t3']
    fee = request.POST['t4']
    pattern = request.POST['t5']
    branch = request.POST['t6']'''

def sample(request):
     Tid= request.POST.get('s1')
     Tname=  request.POST.get('s2')
     Tcontact=  request.POST.get('s3')
     Tadd=  request.POST.get('s4')
     Tquali=  request.POST.get('s5')
     Tdept=  request.POST.get('s6')
     Tjoin_date=  request.POST.get('s7')
     Texp=  request.POST.get('s8')
     Tsalary=  request.POST.get('s9')
     sql=teacher(tid=Tid,tname=Tname,tcont=Tcontact,tadd=Tadd,tquali=Tquali,tdept=Tdept,tj_date=Tjoin_date,texp=Texp,tsal=Tsalary)

     sql.save()
     return render(request,'demoapp/teacher_detail.html')

