# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db import IntegrityError

class Categorie (models.Model):
    nom = models.CharField(max_length = 50)
    def __unicode__ (self):
        return self.nom

class Utilisateur (models.Model):
    user = models.OneToOneField(User)
    age = models.IntegerField(verbose_name="Âge")
    date = models.DateTimeField(auto_now=True, auto_now_add=False,
                                verbose_name="Date d'inscription")
    profil_picture_signed = models.FileField(upload_to='users/avatars/sign_language', null=True, blank=True,verbose_name="Photo de profil signée") #Video of the user's name in sign language
    profil_picture = models.FileField(upload_to ='users/avatars/image', null=True, blank=True, verbose_name="Photo de profil")
    newsletter = models.BooleanField(default =False,help_text = "Je souhaite recevoir l'actualité du site internet") #Inscription to the newsletter
    description_signed = models.FileField( upload_to='users/description/', null=True, blank=True, verbose_name="Description signée") #Description in sign language of the user
    description= models.TextField(null=True, verbose_name="Description", help_text = "Décrivez-vous brièvement, vos hobbies, votre expérience... si vous le souhaitez") #Description in sign language of the user
                            
    def __unicode__(self):
        return self.user.username



class Article (models.Model):
    titre = models.CharField(max_length = 100, blank = True, verbose_name="Titre" )
    slug = models.SlugField(max_length=100, unique=True, help_text ="Apparaitra dans l'adresse du site")
    auteur = models.ForeignKey(Utilisateur, blank = True, verbose_name="Auteur")
    contenu = models.TextField(null=True, verbose_name="Contenu")
    date = models.DateTimeField(auto_now_add=True, auto_now=False,
                                verbose_name="Date de modification")
    categorie = models.ForeignKey(Categorie)
                                
    def __unicode__(self):
        return self.titre
