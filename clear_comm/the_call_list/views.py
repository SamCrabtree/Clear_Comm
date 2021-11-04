from typing import List
from django.shortcuts import render
from django.urls import reverse_lazy 
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic.edit import DeleteView
from .models import property, note

def home(request):
    return render(request, 'home.html', {}) 

class LeadView(ListView):
    model = property
    template_name = 'list.html'

class LeadDetails(DetailView):
    model = property
    template_name = 'lead.html'

class AddLeadView(CreateView):
    model = property
    template_name = 'add_lead.html' 
    fields = '__all__'

class DeleteLeadView(DeleteView):
    model = property
    template_name = 'delete_lead.html' 
    
class AddNoteView(CreateView):
    model = note
    template_name = 'add_note.html' 
    #fields = '__all__'
    fields = ()

class DeleteNoteView(DeleteView):
    model = note
    template_name = 'delete_note.html' 
    



def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dash')
        else:
            messages.info(request, 'Username OR Password is Incorrect. Remember: Both fields are case sensitive')
    
    return render(request, "login.html", {})

def logoutUser(request):
   logout(request)
   return HttpResponseRedirect('/logout/')

def logoutSuccess(request):
    return render(request, "logout.html", {})