"""
URL configuration for digitallibrary project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
     path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('home.html',  TemplateView.as_view(template_name = 'home.html'), name='home_html'),
    path('login.html', TemplateView.as_view(template_name='login.html'), name='login_html'),
    path('regi_login.html', TemplateView.as_view(template_name='regi_login.html'), name='regi_login_html'),
    path('OTP.html', TemplateView.as_view(template_name = 'OTP.html'), name='OTP_html'),
    path('readnow/<int:book_id>.html',  TemplateView.as_view(template_name = 'readnow.html'), name='readnow_html'),
     path('readnow.html',  TemplateView.as_view(template_name = 'readnow.html'), name='readnow_html'),
    path('contribution.html',  TemplateView.as_view(template_name = 'contribution.html'), name='contribution_html'),
    path('pageturner.html',  TemplateView.as_view(template_name = 'pageturner.html'), name='pageturner_html'),
    path('pageturner<int:book_id>.html',  TemplateView.as_view(template_name = 'pageturner.html'), name='pageturner_html'),
    path('bookpreview.html', TemplateView.as_view(template_name='bookpreview.html'), name='bookpreview_html'),
    path('myshelf.html', TemplateView.as_view(template_name='myshelf.html'), name='myshelf_html'),
    path('faq.html', TemplateView.as_view(template_name='faq.html'), name='faq_html'),
]
