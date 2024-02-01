from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 

def home(request):
    # Check to see if loggin in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Welcome! You are Logged In.")
            return redirect('home')
        else:
            messages.success(request, "Please try Again. There was an Error Logging In...")
            return redirect('home')
    else:
        return render(request, 'home.html', {})
    

def logout_user(request):
    logout(request)
    messages.success(request,"You are Logged Out. See you soon...")
    return redirect('home')

def register_user(request):
    return render(request, 'register.html', {})
    