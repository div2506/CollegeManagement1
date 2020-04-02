"""testwebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,include
from django.conf.urls import url

from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    url(r'^Teacher/home$',views.TecHome,name='tec_home'),
    url(r'Teacher/ViewStus$',views.ViewStus,name='view_stus'),
    url(r'^Student/home$',views.StuHome,name='stu_home'),
    url(r'Student/Notes$',views.StuNotes,name='stu_notes'),
    url(r'Teacher/Notes$',views.TecNotes,name='tec_notes'),
    url(r'Teacher/AddNotes/$', views.AddNotes, name='add_notes'),
    url(r'Teacher/Announcement$',views.TecAnn,name='tec_ann'),
    url(r'Teacher/AddAnn/$', views.AddAnn, name='add_ann'),
    url(r'Teacher/DelAnn/$', views.DelAnn, name='del_ann'),
    url(r'Teacher/DelNotes/$', views.DelNotes, name='del_notes'),
    url(r'Student/Announcement$', views.StuAnn, name='stu_ann'),
]