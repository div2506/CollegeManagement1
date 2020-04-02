from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
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
from datetime import datetime,time
from django.utils.dateparse import parse_date



def TecHome(request):
    id = request.user.username
    s = Teacher_info.objects.get(T_ID=id)
    return render(request, 'moodle/teacherhome.html', {'stu': s})

def ViewStus(request):
    id = request.user.username
    s = Teacher_info.objects.get(T_ID=id)
    stus=s.student_info_set.all()

    return render(request, 'moodle/viewstues.html', {'stu': s,'stus':stus})


def StuHome(request):
    id = request.user.username
    s = Student_info.objects.get(S_ID=id)
    t=s.class_teacher
    nowdate=datetime.now()
    ann=[]

    for i in t.announcement_set.all():
        due_date = datetime.combine(i.due_date, time(0, 0))
        end_date = datetime.combine(i.end_date , time(0, 0))
        if due_date < nowdate and end_date > nowdate:
            ann.append(i)
    return render(request,'moodle/studenthome.html',{'stu': s,'tec':t,'msgs':ann})

def StuNotes(request):
    id = request.user.username
    s = Student_info.objects.get(S_ID=id)
    t=s.class_teacher


    return render(request, 'moodle/notes.html', {'stu': t})

def TecNotes(request):
    id = request.user.username
    t= Teacher_info.objects.get(T_ID=id)



    return render(request, 'moodle/tec_notes.html', {'stu': t})

def AddNotes(request):
    id = request.user.username
    t = Teacher_info.objects.get(T_ID=id)
    n=Notes()
    n.name=str(request.POST.get('name')).upper()
    try:
        n.pdf= request.FILES['pdf']
    except MultiValueDictKeyError:
        s.img =None
    n.pdf = request.FILES['pdf']
    n.teacher=t
    n.save()
    t = Teacher_info.objects.get(T_ID=id)
    return render(request, 'moodle/tec_notes.html', {'stu': t})


def TecAnn(request):
    id = request.user.username
    t= Teacher_info.objects.get(T_ID=id)
    return render(request, 'moodle/tec_ann.html', {'stu': t})

def AddAnn(request):
    id = request.user.username
    t = Teacher_info.objects.get(T_ID=id)
    a=Announcement()
    a.msg=str(request.POST.get('msg')).upper()
    a.due_date=parse_date(request.POST.get('due_date'))
    a.end_date=parse_date(request.POST.get('end_date'))
    a.teacher=t
    a.save()
    t = Teacher_info.objects.get(T_ID=id)
    return render(request, 'moodle/tec_ann.html', {'stu': t})


def DelAnn(request):
    ann=request.POST.get('ann')
    msg=ann

    a=Announcement.objects.get(pk=ann)
    a.delete()
    id = request.user.username
    t = Teacher_info.objects.get(T_ID=id)
    return render(request, 'moodle/tec_ann.html', {'stu': t,'msg':msg})


def DelNotes(request):
    note = request.POST.get('note')
    msg = note

    a = Notes.objects.get(pk=note)
    a.delete()
    id = request.user.username
    t = Teacher_info.objects.get(T_ID=id)
    return render(request, 'moodle/tec_notes.html', {'stu': t, 'msg': msg})

def StuAnn(request):
    id = request.user.username
    s = Student_info.objects.get(S_ID=id)
    t = s.class_teacher
    nowdate = datetime.now()
    ann = []
    for i in t.announcement_set.all():
        due_date = datetime.combine(i.due_date, time(0, 0))
        end_date = datetime.combine(i.end_date , time(0, 0))
        if due_date < nowdate and end_date > nowdate:
            ann.append(i)
    return render(request, 'moodle/stu-ann.html', {'stu': t,'tec':t,'msgs':ann})
