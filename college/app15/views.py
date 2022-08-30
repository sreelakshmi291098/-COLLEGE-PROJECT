from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from app15.models import Studreg
from app15.models import Empreg
from app15.forms import Newstud
from app15.forms import Newemp
from app15.forms import SignUpForm
from app15.forms import loginForm

# Create your views here.
def index(request):
    return render(request,'index.html')

def main(request):
    return render(request,'main.html')    



def studreg(request):
    return render(request,'studreg.html')

def empreg(request):
    return render(request,'empreg.html')

def student(request):
    return render(request,'student.html')

def attendence(request):
    return render(request,'attendence.html')

def studperform(request):
    return render(request,'studperform.html')

def employee(request):
    return render(request,'employee.html')

def employeeattend(request):
    return render(request,'employeeattend.html')

def viewstud(request):
    data=Studreg.objects.all()
    return render(request,'viewstud.html',{'data':data})

def viewemp(request):
    data=Empreg.objects.all()
    return render(request,'viewemp.html',{'data':data})     

def stud(request):
    form=Newstud()
    if request.method=='POST':
        form=Newstud(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FROM INVALID')
    return render(request,'stud.html',{'fm':form})


def emp(request):
    form=Newemp()
    if request.method=='POST':
        form=Newemp(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FROM INVALID')
    return render(request,'emp.html',{'sh':form})


def register(request):
    msg=None
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            msg='user created'
            return redirect('login_view')
        else:
            msg='form is not valid'
    else:
        form=SignUpForm()
    return render(request,'registration.html',{'form':form,'msg':msg})

def login_view(request):
    form = loginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('adminpage')
            elif user is not None and user.is_customer:
                login(request, user)
                return redirect('customer')
            elif user is not None and user.is_employee:
                login(request, user)
                return redirect('empe')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'loginview.html', {'form': form, 'msg': msg})

def admin(request):
    return render(request,'main.html')


def customer(request):
    return render(request,'student.html')


def empe(request):
    return render(request,'employee.html')
     
