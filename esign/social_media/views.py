# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.forms import modelformset_factory
from home.models import Utilisateur
from django.contrib.auth import logout, login, authenticate
from django.core.urlresolvers import reverse
from .forms import ConnexionForm,InscriptionForm_LSF,InscriptionForm_fr, InscriptionChoiceForm

# Create your views here.


def home_social(request):
    return render(request, 'home/home_social.html')

def log_in(request):
    error = False
    if request.method == 'POST' :
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user :
                login(request, user)
                return redirect('home')
            else :
                error =True
    else :
        form = ConnexionForm()
    return render(request, 'login/log_in.html', {'form':form})

def log_out(request):
    logout(request)
    return redirect(reverse(log_in))


def inscription_choice(request):
    if request.method == 'POST' :
        form = InscriptionChoiceForm(request.POST)
        if form.is_valid():
            format = form.cleaned_data
            if format[0] == 'LSF' :
                choice = 'LSF'
                return redirect('inscription', choice=choice)
            elif format[0] == 'Fr' :
                choice = 'Fr'
                return redirect('inscription', choice=choice)
    else :
        choice = 'non'
        form = InscriptionChoiceForm()
    return render(request,'inscription/inscription_choice.html',{'form':form})


'''Inscription form'''
def inscription(request, choice):
    if choice == 'LSF' :
        InscriptionFormSet = modelformset_factory(Utilisateur, exclude = ('profil_picture','description'), formset=InscriptionForm_LSF)
        if request.method == 'POST':
            form = InscriptionFormSet(request.POST)
            if form.is_valid():
                new_user = form.save(commit=False)
                new_user.save()
                return redirect('log_in')
        else :
            form = InscriptionFormSet()
    elif choice == 'Fr' :
        InscriptionFormSet = modelformset_factory(Utilisateur, exclude = ('profil_picture_signed','description_signed'), formset=InscriptionForm_fr)
        if request.method == 'POST':
            form = InscriptionFormSet(request.POST)
            if form.is_valid():
                new_user = form.save(commit=False)
                new_user.save()
                return redirect('log_in')
        else :
            form = InscriptionFormSet()
    else :
        return redirect('home_social')
    return render(request, 'inscription/inscription_form.html', {'form': form})
