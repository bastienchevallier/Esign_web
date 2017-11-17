"""esign URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
    
    url(r'^login/password_change$', auth_views.password_change, {'template_name': 'login/password_change.html', 'post_change_redirect' : 'auth_views.password_change_done'}),
    url(r'^login/password_change_done$', auth_views.password_change_done, {'template_name': 'login/password_change_done.html'}),
    url(r'^login/password_reset$', auth_views.password_reset, {'template_name': 'login/password_reset.html'}),
    url(r'^login/password_reset_done$', auth_views.password_reset_done, {'template_name': 'login/password_reset_done.html'}),
    url(r'^login/password_reset_confirm$', auth_views.password_reset_confirm, {'template_name': 'login/password_reset_confirm.html'}),
    url(r'^login/password_reset_complete$', auth_views.password_reset_complete, {'template_name': 'login/password_reset_complete.html'}),
"""

from django.conf.urls import url
from social_media import views
from django.contrib.auth import views as auth_views

urlpatterns = [
               url(r'^$', views.home_social, name='home_social'),
               url(r'^login/$', views.log_in, name='login'),
               url(r'^logout/$', views.log_out, name='logout'),
               url(r'^inscription/choice', views.inscription_choice, name='inscription_choice'),
               url(r'^inscription/(?P<choice>.+)$', views.inscription, name='inscription'),
               ]
