from django.shortcuts import render
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages

def home(request):
    return render(request, 'home.html', {}) 

def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR Password is Incorrect. Remember: Both fields are case sensitive')
    
    return render(request, "login.html", {})

def logoutUser(request):
   logout(request)
   return HttpResponseRedirect('/logout/')

def logoutSuccess(request):
    return render(request, "logout.html", {})