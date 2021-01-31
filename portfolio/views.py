from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib import messages

from .forms import ContactForm
from .models import Contact

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent. Thank you!')
            return redirect('/index/')
    else:
        form = ContactForm()
    return render(request, 'index.html', {'form': form})

def redirect_to_index(request):
    return HttpResponseRedirect(reverse('index'))
