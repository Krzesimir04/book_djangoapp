from django.contrib.auth import login,logout
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Visit
# Create your views here.
def index(request):
    return render(request, 'index.html')

def login_view(request):
    if not request.user.is_authenticated:
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
    else:
        return redirect('index')


def logout_view(request):
    logout(request)
    return redirect('index')

def register(request):
    if not request.user.is_authenticated:
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
                    user=User.objects.get(email=email)
                    if check_password(password1,encoded=user.password):
                        login(request, user)
                        return redirect('index')
                    else:
                        messages.error(request,'try to log in')
                        return redirect('login')
            else:
                password1=request.POST['password1']
                password2=request.POST['password2']
                if password1!=password2:
                    messages.error(request, 'passwords are not the same')
                else:
                    messages.error(request, 'wrong email')
                return redirect('register')
        else:
            register_form=Register_form()
            return render(request, 'register.html', {'form':register_form})
    else:
        return redirect('index')

@login_required(login_url='login')
def reservation(request):
    if request.method=='POST':
        form=Day_of_visit(request.POST)
        if form.is_valid():
            day=form.cleaned_data.get('Day')
            return redirect(f'reservation/{day}')
        else:
            print(form.errors)
            return render (request, 'reservation.html',{'form':form})
    else:
        form=Day_of_visit()
    return render (request, 'reservation.html',{'form':form})

@login_required(login_url='login')
def reservation_2(request,day):
    visits=Visit.objects.filter(Day=day)
    if not visits.exists():
        for i in range(7,15):
            time=str(i)+':00'
            Visit.objects.create(User=None,Day=day,Term=time,Visit_length=1.0)
        visits=Visit.objects.filter(Day=day)

    return render(request,'reservation_2.html',{'visits':visits,'day':day})

@login_required(login_url='login')
def make_reservation(request,pk):
    users_visits=Visit.objects.filter(User=request.user)
    if users_visits.count()<5:
        visit=Visit.objects.filter(id=pk)
        visit.update(User=request.user)
    else:
        messages.error(request, 'You can have booked only 5 visits now')
    return redirect('reservation')

@login_required(login_url='login')
def cancel(request,pk):
    visit=Visit.objects.filter(id=pk,User=request.user)
    visit.update(User=None)
    messages.info(request,'Visit canceled')
    return redirect('reservation')