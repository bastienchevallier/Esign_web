# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import itertools
from django.shortcuts import render, get_object_or_404,redirect
from home.models import Article
from home.forms import ArticleForm
from django.forms import modelformset_factory
from django.utils.text import slugify

# Create your views here.

def home(request):
    articles = Article.objects.all() #Affichage de tous les articles
    return render(request,'home/home.html',{'derniers_articles':articles})

def read(request, id, slug):
    article = get_object_or_404(Article, id=id, slug=slug)
    return render( request, 'articles/read_article.html',{'article' : article})


def publish (request):
    if request.user.is_authenticated :
        ArticleFormSet = modelformset_factory(Article, exclude =('slug',), formset=ArticleForm) #Equivalent ArticleForm
        if request.method == 'POST':
            formset = ArticleFormSet(request.POST, queryset=Article.objects.none())
            for form in formset :
                if form.is_valid():
                    new_article = form.save(commit=False)
                    new_article.slug = orig = slugify(new_article.titre)
                    for x in itertools.count(1):
                        if not Article.objects.filter(slug=new_article.slug).exists():
                            break
                    new_article.slug = '%s-%d' % (orig, x)
                    new_article.save()
                    return redirect('read_article', id=new_article.id, slug=new_article.slug)
        else:
            form = ArticleFormSet(queryset=Article.objects.none())
    else:
        return redirect('home') #!!!!!!
    return render(request, 'articles/publish.html', {'formset': form})


def modify_presentation (request):
    article = Article.objects.all()
    return render(request,'articles/modify-presentation.html',{'derniers_articles':article})


def modify_article (request, slug):
    article_to_display = get_object_or_404(Article, slug=slug)
    if request.method == 'POST':
        formset = ArticleForm(request.POST, request.FILES, instance = article_to_display)
        if formset.is_valid():
            modified_article = formset.save(commit=False)
            modified_article.save()
            return redirect('read_article', id=modified_article.id, slug=modified_article.slug)
    else:
        formset = ArticleForm(instance = article_to_display)
    return render(request, 'articles/modify-article.html', locals())
