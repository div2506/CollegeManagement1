from django.contrib import admin
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.Index, name='index'),
    url(r'^Student/$',views.loginAsStu),
    url(r'^Teacher/$', views.loginAsTec),
    url(r'^RegisterForm/$', views.RegisterForm, name='registerform'),
    url(r'^RegisterToDB/$', views.RegisterToDB, name='registertodb'),
    url(r'^StuProfile/$',views.StuProfile,name='stuprofile'),
    url(r'^TecProfile/$', views.TecProfile, name='tecprofile'),

    url(r'^VarifyAsStu/$', views.VarifyAsStu, name='varifyAsTec'),
    url(r'^VarifyAsTec/$', views.VarifyAsTec, name='varifyAsTec'),
    url(r'^StuProfile/Edit/$', views.StuEdit, name='stu_edit'),
    url(r'^TecProfile/Edit/$', views.TecEdit, name='tec_edit'),
    url(r'^StuProfile/ChangeToDB/$', views.ChangeToDB, name='stu_ch-to-db'),
    url(r'^TecProfile/ChangeToDB/$', views.TecChangeToDB, name='tec_ch-to-db'),
     url(r'^logout/$', views.logout),
    url(r'^loggedinAsStu/$', views.loggedinAsStu),
    url(r'^loggedinAsTec/$', views.loggedinAsTec),

    url(r'^invalidlogin/$', views.invalidlogin),
    url(r'^About/$',views.About),
    url(r'^Contact/$',views.Contact),
    url(r'^StuAc/$',views.StuAc,name='stu_ac'),
    url(r'^TecReg/$',views.TecReg,name='teacher_reg'),
    url(r'^RegTecToData/$',views.RegTecToData,name='tec_reg_db'),
    url(r'^TecAc/$', views.TecAc, name='tec_ac'),
]
