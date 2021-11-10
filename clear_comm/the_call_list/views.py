from typing import List
from django.forms import models
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic.edit import DeleteView
from .models import property, note, Tent, Loop
from .forms import LeadForm, UpdateLeadForm, NoteForm, LoopForm, UpdateLoopForm, UpdateTentForm

def home(request):
    return render(request, 'home.html', {}) 

class TentListView(ListView):
    model = Tent
    template_name = 'dash.html'


class UpdateTentView(UpdateView):
    model = Tent
    form_class = UpdateTentForm
    template_name = 'edit_tent.html'
    success_url = reverse_lazy('dash')

class LoopView(ListView):
    model = Loop
    template_name = 'loop_view.html'

class LoopDetailView(DetailView):
    model = Loop
    template_name = 'loop.html'

class AddLoopView(CreateView):
    model = Loop
    form_class = LoopForm
    template_name = 'add_loop.html'

class UpdateLoopView(UpdateView):
    model = Loop
    form_class = UpdateLoopForm
    template_name = 'edit_loop.html'
    success_url = reverse_lazy('loop_view')


class DeleteLoopView(DeleteView):
    model = Loop
    template_name = 'delete_loop.html' 
    success_url = reverse_lazy('loop_view')

class LeadView(ListView):
    model = property
    template_name = 'list.html'

class LeadDetails(DetailView):
    model = property
    template_name = 'lead.html'
    

class AddLeadView(CreateView):
    model = property
    form_class = LeadForm
    template_name = 'add_lead.html' 
    success_url = reverse_lazy('call_list')
    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)



class UpdateLeadView(UpdateView):
    model = property
    form_class = UpdateLeadForm
    template_name = 'edit_lead.html'
    success_url = reverse_lazy('call_list')
    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

class DeleteLeadView(DeleteView):
    model = property
    template_name = 'delete_lead.html' 
    success_url = reverse_lazy('dash')
    
class AddNoteView(CreateView):
    model = note
    form_class = NoteForm
    template_name = 'add_note.html' 
    success_url = reverse_lazy('dash')
    def form_valid(self, form):
        form.instance.Property_id = self.kwargs['pk']
        form.instance.creator = self.request.user
        return super().form_valid(form)
    



class DeleteNoteView(DeleteView):
    model = note
    template_name = 'delete_note.html' 
    success_url = reverse_lazy('call_list')
        
    



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