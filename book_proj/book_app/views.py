from django.contrib.auth import login,logout
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
    if request.method=='POST':
        login_form=Login_form(request.POST)
        if login_form.is_valid():

            email=login_form.cleaned_data.get("email")
            password=login_form.cleaned_data.get("password")
            try:
                user=User.objects.get(email=email, password=password)
                login(request, user)
                return redirect('index')
            except User.DoesNotExist:
                messages.error(request,'Email or password doesn\'t match')
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
            date=form.cleaned_data.get('Day')
            return redirect(f'reservation/{date}')
        else:
            messages.error(request, 'form is not valid')
            return redirect('reservation')
    else:
        form=Day_of_visit()
    return render (request, 'reservation.html',{'form':form})

@login_required(login_url='login')
def reservation_2(request,date):
    visits=Visit.objects.filter(Day=date)
    return render(request,'reservation_2.html',{'visits':visits})