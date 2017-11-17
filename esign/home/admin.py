# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import Categorie, Utilisateur, Article
from django.utils.text import Truncator

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('titre', ), }
    list_display   = ('titre', 'auteur', 'date', 'apercu_contenu')
    list_filter    = ('auteur','categorie',)
    date_hierarchy = 'date'
    ordering       = ('date', )
    search_fields  = ('titre', 'contenu')
    
    # Configuration du formulaire d'édition
    fieldsets = (
                 # Fieldset 1 : meta-info (titre, auteur…)
                 ('Général', {
                  'classes': ['collapse', ],
                  'fields': ('titre', 'slug', 'auteur', 'categorie')
                  }),
                 # Fieldset 2 : contenu de l'article
                 ('Contenu de l\'article', {
                  'description': 'Le formulaire accepte les balises HTML.',
                  'fields': ('contenu', )
                  }),
                 )
        
    def apercu_contenu(self, article):
        return Truncator(article.contenu).chars(40, truncate='...')
    apercu_contenu.short_description = 'Aperçu du contenu'

admin.site.register(Categorie)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Utilisateur)
