# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from home.models import Utilisateur
from django import forms

# Create your models here.

class ConnexionForm (forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget = forms.PasswordInput)

class InscriptionChoiceForm (forms.Form):
    CHOICES = (('LSF','Inscription en LSF'),
               ('Fr','Inscription en langue française'),)
    Format = forms.MultipleChoiceField(required=True,choices=CHOICES, widget=forms.CheckboxSelectMultiple)

class InscriptionForm_LSF(forms.ModelForm):
    class Meta :
        model = Utilisateur
        exclude = ('profil_picture','description')

class InscriptionForm_fr(forms.ModelForm):
    class Meta :
        model = Utilisateur
        exclude = ('profil_picture_signed','description_signed')


