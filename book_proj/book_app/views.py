from django.contrib.auth import login,logout
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Visit
import datetime
# Create your views here.
def index(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method=='POST':
        login_form=Login_form(request.POST)
        if login_form.is_valid():

            email=login_form.cleaned_data.get("email")
            password=login_form.cleaned_data.get("password")
            try:
                user=User.objects.get(email=email)
                if check_password(password,encoded=user.password):
                    login(request, user)
                    return redirect('index')
                else:
                    messages.error(request,'Email or password doesn\'t match')
                    return redirect('login')
            except (User.DoesNotExist, IndexError):
                messages.error(request,'User with that email does not exist')
                return redirect('login')
        else:
            messages.error(request,'Form is not valid')
            return redirect('login')

    else:
        login_form=Login_form()

    return render(request, 'login.html', {'form':login_form})


def logout_view(request):
    logout(request)
    return redirect('index')

def register(request):
    if request.method=='POST':
        register_form=Register_form(request.POST)
        if register_form.is_valid():
            email=register_form.cleaned_data.get('email')
            password1=register_form.cleaned_data.get('password1')
            password2=register_form.cleaned_data.get('password2')
            if User.objects.filter(email=email).exists():
                messages.info(request,'there already is user with this email, please change your email')
                return redirect('register')
            if password1==password2:
                register_form.save()
                messages.success(request, 'Account has been created')
                return redirect('login')
            else:
                messages.error(request, 'passwords are not the same')
                return redirect('register')
        else:
                messages.error(request, 'form is not valid')
                return redirect('register')
    else:
        register_form=Register_form()
        return render(request, 'register.html', {'form':register_form})

@login_required(login_url='login')
def reservation(request):
    if request.method=='POST':
        form=Day_of_visit(request.POST)
        if form.is_valid():
            day=form.cleaned_data.get('Day')
            return redirect(f'reservation/{day}')
        else:
            messages.error(request, 'form is not valid, you have to choose the future date')
            return redirect('reservation')
    else:
        form=Day_of_visit()
    return render (request, 'reservation.html',{'form':form})

@login_required(login_url='login')
def reservation_2(request,day):
    visits=Visit.objects.filter(Day=day)
    if request.method=='POST':
        form=Reservation_form(request.POST)
        if form.is_valid():
            Term=form.cleaned_data.get('Term')
            Visit_length=float(form.cleaned_data.get('Visit_length'))
            reservation_visit=Visit.objects.filter(Day=day,Term=Term)
            try:
                if reservation_visit[0].User is None:
                    if Visit_length <= 1.0:
                        reservation_visit.update(User=request.user,Term=Term, Visit_length=Visit_length)
                    else:
                        reservation_visit.update(User=request.user,Term=Term, Visit_length=1.0,Combined_id=reservation_visit[0].id+1)
                        new_term=datetime.time(Term.hour+1)
                        new_visit=Visit.objects.filter(Day=day, Term=new_term)
                        new_visit.update(User=request.user,Term=new_term,Visit_length=(-1+Visit_length),Combined_id=reservation_visit[0].id)
                else:
                    messages.error(request,'This term is reserved choose other.')
            except IndexError:
                messages.error(request,'Choose right hour, for example 9:00, 10:00')
            
    elif request.method=='GET':
        form=Reservation_form()
        if not visits.exists():
            for i in range(7,15):
                time=str(i)+':00'
                Visit.objects.create(User=None,Day=day,Term=time,Visit_length=1.0)
            visits=Visit.objects.filter(Day=day)
    else:
        return redirect('index')

    return render(request,'reservation_2.html',{'visits':visits,'form':form})

def cancel(request,day,pk):
    visit=Visit.objects.filter(id=pk,User=request.user)
    if visit[0].Combined_id == None:
        visit.update(User=None,Visit_length=1.0,Combined_id=None)
    else:
        visit_2=Visit.objects.filter(id=visit[0].Combined_id)
        visit.update(User=None,Visit_length=1.0,Combined_id=None)
        visit_2.update(User=None,Visit_length=1.0,Combined_id=None)

    messages.info(request,'Visit canceled')
    return redirect(f'/reservation/{day}')