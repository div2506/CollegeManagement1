from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from django.views.decorators.cache import cache_control
from databasetset.models import *
from django.utils.dateparse import parse_date
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context_processors import csrf
from django.utils.datastructures import MultiValueDictKeyError
from datetime import date
from datetime import datetime,time
from django.contrib.auth.decorators import user_passes_test

# Create your views here.
def Index(request):
    return render(request, 'myschool/index.html', context=None)


def RegisterForm(request):
    return render(request, 'myschool/registrationform.html', context=None)


def RegisterToDB(request):
    # student
    # f_name,m_name,l_name,gender,birthdate,blood_group
    # gardian
    # f_name,m_name,l_name,relation_type,occupation,annual_income
    # contact
    # addrese,city,pincode,ph_no,email
    tec=request.user.username
    t=Teacher_info.objects.get(T_ID=tec)
    s = Student_info()
    g = Gardian_info()
    c = Contact_info()
   # stdnum=request.POST.get('std')
   # std=Standard_info.objects.get(std_num=stdnum)

    c.addrese = str(request.POST.get('addrese')).upper()
    c.city = str(request.POST.get('city')).upper()
    c.ph_no = int(request.POST.get('ph_no'))
    c.pincode = int(request.POST.get('pincode'))
    c.email = request.POST.get('email')
    c.save()
    g.f_name = str(request.POST.get('g_f_name')).upper()
    g.m_name = str(request.POST.get('g_m_name')).upper()
    g.l_name = str(request.POST.get('g_l_name')).upper()
    g.relation_type = str(request.POST.get('relation_type')).upper()
    g.occupation = str(request.POST.get('occupation')).upper()
    g.annual_income = int(request.POST.get('annual_income'))
    g.save()
    s.f_name = str(request.POST.get('f_name')).upper()
    s.m_name = str(request.POST.get('m_name')).upper()
    s.l_name = str(request.POST.get('l_name')).upper()
    s.gender = str(request.POST.get('gender')).upper()
    s.birthdate = parse_date(request.POST.get('birthdate'))
    s.blood_group = str(request.POST.get('blood_group')).upper()
    s.gardian = g
    s.contact = c
    s.S_ID = "S" + str(19) + "HK" + str(g.pk)
    s.password = str(s.birthdate.strftime("%d%m")) + s.f_name[0].lower() + s.m_name[0].lower() + s.l_name[
        0].lower() + str(s.birthdate.strftime("%d"))
    s.img = request.FILES['image']
    s.std=t.standard_info
    s.class_teacher=t
    s.save()

    u = User()
    u.username = s.S_ID
    u.set_password(
        str(s.birthdate.strftime("%d%m")) + s.f_name[0].lower() + s.m_name[0].lower() + s.l_name[0].lower() + str(
            s.birthdate.strftime("%d")))
    u.first_name = s.f_name
    u.last_name = s.l_name
    u.email = c.email
    u.save()
    s.user = u
    s.save()
    return render(request, "myschool/succses_msg.html", {'stu': s})



def loginAsStu(request):

        c = {}
        c.update(csrf(request))
        return render_to_response('myschool/student_login.html', c)

def loginAsTec(request):


        c = {}
        c.update(csrf(request))
        return render_to_response('myschool/teacher_login.html', c)


def VarifyAsStu(request):
    username = request.POST.get('username')
    if username[0] == 'S':
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect('/myschool/loggedinAsStu/')
        else:
            return HttpResponseRedirect('/myschool/invalidlogin/')
    else:
        return render(request, 'myschool/error.html', {'msg': 'Invalid Credetinals @'})


def VarifyAsTec(request):
    username = request.POST.get('username')
    if username[0] == 'T':
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect('/myschool/loggedinAsTec/')
        else:
            return HttpResponseRedirect('/myschool/invalidlogin/')
    else:
        return render(request, 'myschool/error.html', {'msg': 'Invalid Credetinals @'})


@login_required
def loggedinAsStu(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/myschool/StuAc/')
    else:
        return HttpResponseRedirect('/myschool/Index/')


@login_required
def loggedinAsTec(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/myschool/TecAc/')
    else:
        return HttpResponseRedirect('/myschool/Index/')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def TecProfile(request):
    if request.user.is_authenticated:
        full_name = request.user.username
        o = Teacher_info.objects.get(T_ID=full_name)
        if o is not None:
            return render(request, 'myschool/tec_profile.html', {"stu": o})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def StuProfile(request):
    if request.user.is_authenticated:
        full_name = request.user.username
        o = Student_info.objects.get(S_ID=full_name)
        if o is not None:
            return render(request, 'myschool/stu_profile.html', {"stu": o})


def invalidlogin(request):
    err = {'msg': 'Invalid credtentisals'}
    return render(request, "myschool/error.html", err)


def logout(request):
    auth.logout(request)
    return render_to_response('myschool/logout.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def TecAc(request):

        id = request.user.username
        o = Teacher_info.objects.get(T_ID=id)
        return render(request, 'myschool/tec_acc_home.html', {'stu': o})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='/myschool/login/')
def StuEdit(request):
    id = request.user.username
    o = Student_info.objects.get(S_ID=id)
    return render(request, 'myschool/edit_student.html', {'stu': o})
@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def TecEdit(request):
    id = request.user.username
    o = Teacher_info.objects.get(T_ID=id)

    return render(request, 'myschool/edit_teacher.html', {'stu': o})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='/myschool/login/')
def ChangeToDB(request):
    id = request.user.username
    s = Student_info.objects.get(S_ID=id)
    g = s.gardian
    c = s.contact
    u = User.objects.get(username=id)
    s.f_name = str(request.POST.get('f_name')).upper()
    s.m_name = str(request.POST.get('m_name')).upper()
    s.l_name = str(request.POST.get('l_name')).upper()
    s.gender = str(request.POST.get('gender')).upper()
    s.blood_group = str(request.POST.get('blood_group')).upper()

    g.f_name = str(request.POST.get('g_f_name')).upper()
    g.m_name = str(request.POST.get('g_m_name')).upper()
    g.l_name = str(request.POST.get('g_l_name')).upper()
    g.relation_type = str(request.POST.get('relation_type')).upper()
    g.occupation = str(request.POST.get('occupation')).upper()
    g.annual_income = int(request.POST.get('annual_income'))
    g.save()
    c.addrese = str(request.POST.get('addrese')).upper()
    c.city = str(request.POST.get('city')).upper()

    c.pincode = int(request.POST.get('pincode'))
    c.ph_no = int(request.POST.get('ph_no'))
    c.email = request.POST.get('email')
    c.save()
    s.contact = c
    s.gardian = g
    try:
        s.img = request.FILES['image']
    except MultiValueDictKeyError:
        s.img = s.img

    s.save()
    u.username = s.S_ID

    u.first_name = s.f_name
    u.last_name = s.l_name
    u.email = c.email
    u.save()

    return HttpResponseRedirect('/myschool/StuProfile')


def About(request):
    return render(request, "myschool/about.html", context=None)


def Contact(request):
    return render(request, "myschool/contact.html", context=None)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def StuAc(request):
    id = request.user.username
    s = Student_info.objects.get(S_ID=id)
    t = s.class_teacher
    nowdate = datetime.now()
    ann = []

    for i in t.announcement_set.all():
        due_date = datetime.combine(i.due_date, time(0, 0))
        end_date = datetime.combine(i.end_date, time(0, 0))
        if due_date <= nowdate and end_date >= nowdate:
            ann.append(i)


    return render(request, 'myschool/stu_acc_home.html',{'stu': s, 'tec': t, 'msgs': ann})





def TecReg(request):
    return render(request, 'myschool/teacher_reg.html')


def RegTecToData(request):
    s = Teacher_info()

    c = Contact_info()
    c.addrese = str(request.POST.get('addrese')).upper()
    c.city = str(request.POST.get('city')).upper()
    c.ph_no = str(request.POST.get('ph_no'))
    c.pincode = int(request.POST.get('pincode'))
    c.email = request.POST.get('email')
    c.save()
    s.f_name = str(request.POST.get('f_name')).upper()
    s.m_name = str(request.POST.get('m_name')).upper()
    s.l_name = str(request.POST.get('l_name')).upper()
    s.gender = str(request.POST.get('gender')).upper()
    s.birthdate = parse_date(request.POST.get('birthdate'))
    s.blood_group = str(request.POST.get('blood_group')).upper()

    s.contact = c

    s.password = str(s.birthdate.strftime("%d%m")) + s.f_name[0].lower() + s.m_name[0].lower() + s.l_name[
        0].lower() + str(s.birthdate.strftime("%d"))
    s.img = request.FILES['image']
    s.T_ID = "T" + str(19) + "HK" + str(c.pk)
    s.save()

    u = User()
    u.username = s.T_ID
    u.set_password(
        str(s.birthdate.strftime("%d%m")) + s.f_name[0].lower() + s.m_name[0].lower() + s.l_name[0].lower() + str(s.birthdate.strftime("%d")))
    u.first_name = s.f_name
    u.last_name = s.l_name
    u.email = c.email
    u.save()
    s.user = u
    s.save()
    return render(request, "myschool/succses_msg.html", {'stu':s})


def TecChangeToDB(request):
    id = request.user.username
    s = Teacher_info.objects.get(T_ID=id)
    c = s.contact
    u = User.objects.get(username=id)
    s.f_name = str(request.POST.get('f_name')).upper()
    s.m_name = str(request.POST.get('m_name')).upper()
    s.l_name = str(request.POST.get('l_name')).upper()
    s.gender = str(request.POST.get('gender')).upper()
    s.blood_group = str(request.POST.get('blood_group')).upper()

    c.addrese = str(request.POST.get('addrese')).upper()
    c.city = str(request.POST.get('city')).upper()

    c.pincode = int(request.POST.get('pincode'))
    c.ph_no = int(request.POST.get('ph_no'))
    c.email = request.POST.get('email')
    c.save()
    s.contact = c

    try:
        s.img = request.FILES['image']
    except MultiValueDictKeyError:
        s.img = s.img

    s.save()
    u.username = s.T_ID

    u.first_name = s.f_name
    u.last_name = s.l_name
    u.email = c.email
    u.save()
    return HttpResponseRedirect('/myschool/TecAc')

