from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django import forms

from .models import Contact
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/index/')
    else:
        form = ContactForm()
    return render(request, 'index.html', {'form': form})

def redirect_to_index(request):
    return HttpResponseRedirect(reverse('index'))