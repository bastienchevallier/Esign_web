# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import itertools
from django import forms
from .models import Article
from django.utils.text import slugify

class ArticleForm(forms.BaseModelFormSet):
    class Meta :
        model = Article
        exclude = ('slug',)

    def save(self):
        instance= super(ArticleForm,self).save(commit=False)
        max_length = Article._meta.get_field('slug').max_length
        instance.slug = orig = slugify(instance.title)[:max_length]
        for x in itertools.count(1):
            if not Article.objects.filter(slug=instance.slug).exists():
                break
            instance.slug = '%s-%d' %(orig[:max_length-len(str(x))-1],x)
        instance.save()
        
        return instance
