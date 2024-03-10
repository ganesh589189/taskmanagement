from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from .models import UserProfile
from django.contrib.auth import authenticate

def mainpage(request):
    return render(request, 'mainpage.html')

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Use Django's authenticate method
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)  # Use Django's login method
                return redirect('dash.html')  # Redirect to dashboard on successful login

    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            print("User registered successfully")  # Debug statement
            return redirect('login.html')  # Redirect to login page after successful registration
        else:
            print(form.errors)  # Print form errors to console for debugging

    else:
        form = RegistrationForm()

    return render(request, 'registration.html', {'form': form})
def dash(request):
    return render(request,'dash.html')
def forgot(request):
    return render(request,'forgot.html')
def addtask(request):
    return render(request,'addtask.html')
def viewtask(request):
    return render(request,'viewtask.html')
def calendar(request):
    return render(request,'calendar.html')