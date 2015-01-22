from django.shortcuts import render
import logging
# Create your views here.
from sopromat_stretch.models import stretch_tasks as db_tasks, stretch_attempts as db_attempts
from django.http import HttpResponse
from django.template import RequestContext
from sopromat_python.classes import StretchTask, Drawing
from django.conf.urls.static import static
from django.conf import settings
from datetime import datetime
from django.db import models
import sys
import os, os.path

from decimal import *
getcontext().prec = 4
log = logging.getLogger(__name__)


def index(request):
    context = {'adminuser': checkadmin()}
    return render(request, 'main.html', context)


def stretch(request):
    context = {'adminuser': checkadmin()}
    return render(request, 'stretch_main.html', context)


def stretch_tester(request):
    context = {'adminuser': checkadmin()}
    # if request.method == 'POST':
    if db_tasks.objects.all().count() > 0:
        context['stretch_usertasks'] = [i for i in range(1, db_tasks.objects.latest('id').id + 1)]
    if request.method == 'GET':
        if request.GET.get('task'):
            if request.GET.get('task') == 'new':
                print("stretch_tester(): new task get request")
                while True:
                    try:
                        stretch_task = StretchTask()
                        print("stretch_tester(): creating task")
                        stretch_task.generate()
                        print("stretch_tester(): task created")
                        print(stretch_task.text)
                        print("stretch_tester(): solving")
                        stretch_task.solve()
                        break
                    except:
                        print("stretch_tester(): smth went wrong when creating task")
                        print("stretch_tester(): Unexpected error:", sys.exc_info()[0])
                context['stretch_tasktext'] = stretch_task.text
                context['stretch_taskgiven'] = True
                print("stretch_tester(): taskgiven=", context['stretch_taskgiven'])
                print("stretch_tester(): getting last id in db")
                unique_id = 0
                if db_tasks.objects.all().count() == 0:
                    unique_id = 1
                else:
                    unique_id = db_tasks.objects.latest('id').id + 1
                context['stretch_taskid'] = unique_id
                print("stretch_tester(): id=", unique_id)
                print("stretch_tester(): getting image")
                getStretchImg(stretch_task.beam, unique_id)
                request.session['taskid'] = unique_id
                context['stretch_image'] = 'stretch_' + str(unique_id) + ".png"
                context['stretch_imagelink'] = context['stretch_image']
                print("stretch_tester(): inserting in database")
                tsk = db_tasks()
                tsk.id = unique_id
                tsk.date = datetime.now()
                tsk.text = str(stretch_task.text)
                tsk.answerN = stretch_task.answerN
                tsk.answerL = stretch_task.answerL
                tsk.answerS = stretch_task.answerS
                tsk.user = str(request.user.username or "AnonymousUser")
                tsk.imagelink = context['stretch_imagelink']
                context['stretch_N'] = stretch_task.answerN
                context['stretch_L'] = stretch_task.answerL
                context['stretch_S'] = stretch_task.answerS
                tsk.save()
                print("stretch_tester(): done inserting")
            elif request.GET.get('task').isdigit():
                print("stretch_tester(): old task get request")
                context['stretch_taskgiven'] = True
                context['stretch_taskid'] = int(request.GET.get('task'))
                print("stretch_tester(): id =", context['stretch_taskid'])
                print("stretch_tester(): getting task from db")
                tsk = db_tasks.objects.get(id=context['stretch_taskid'])
                request.session['taskid'] = tsk.id
                context['stretch_tasktext'] = tsk.text
                print('stretch_tester(): taskgiven=', str(context['stretch_taskgiven']))
                # print("stretch_tester(): text =",tsk.text)
                print("stretch_tester(): N =", tsk.answerN)
                print("stretch_tester(): L =", tsk.answerL)
                print("stretch_tester(): S =", tsk.answerS)
                context['stretch_N'] = tsk.answerN
                context['stretch_L'] = tsk.answerL
                context['stretch_S'] = tsk.answerS
        if request.GET.get('answer'):
            print("stretch_tester(): answers request")
            print(type(request.session['taskid']))
            task = db_tasks.objects.get(id=request.session['taskid'])
            context['stretch_tasktext'] = task.text
            if request.GET.get('N').isdigit() and (abs(float(request.GET.get('N')) - float(task.answerN)) <= 0.1):
                context['stretch_answerN'] = 'correct'
            else:
                context['stretch_answerN'] = 'wrong'
            if request.GET.get('L').isdigit() and (abs(float(request.GET.get('L')) - float(task.answerL)) < 0.1):
                context['stretch_answerL'] = 'correct'
            else:
                context['stretch_answerL'] = 'wrong'
            if request.GET.get('S').isdigit() and (abs(float(request.GET.get('S')) - float(task.answerS)) < 0.1):
                context['stretch_answerS'] = 'correct'
            else:
                context['stretch_answerS'] = 'wrong'
            context['sub_n'] = request.GET.get('N')
            context['sub_l'] = request.GET.get('L')
            context['sub_s'] = request.GET.get('S')
            print("stretch_tester(): inserting solve attempt")
            print("stretch_tester(): getting last id in db")
            unique_id = 0
            if db_attempts.objects.all().count() == 0:
                unique_id = 1
            else:
                unique_id = db_attempts.objects.latest('id').id + 1
            if request.session['taskid']:
                context['stretch_taskgiven'] = True
                context['stretch_taskid'] = request.session['taskid']
            tsk = db_attempts()
            tsk.id = unique_id
            tsk.date = datetime.now()
            tsk.answerN = context['stretch_answerN']
            tsk.answerL = context['stretch_answerL']
            tsk.taskid = task.id
            tsk.answerS = context['stretch_answerS']
            tsk.user = str(request.user.username or "AnonymousUser")
            tsk.save()
            print("stretch_tester(): done inserting")

    return render(request, 'stretch_tester.html', context)


def getStretchImg(stretch, taskid):
    d = Drawing()
    img = d.drawBeam2(stretch, taskid)

    BASE_DIR = settings.BASE_DIR
    print("getStretchImg(): saving image")
    img.save(os.path.join(BASE_DIR, "static/") + "stretch_" + str(taskid) + ".png", "PNG")
    print("getStretchImg(): image saved to", os.path.join(BASE_DIR, "static") + "/images/stretch_" + str(taskid) + ".png")


def stretch_stats_student(request):
    context = {'adminuser': checkadmin()}
    print("stretch_stats_student(): call")
    print("stretch_stats_student(): geting attempts for current user:",request.user)
    tasks=[]
    attempts=[]
    try:
        attempts = db_attempts.objects.filter(user=request.user)
        print("stretch_stats_student(): geting tasks for current user: ",request.user)
        tasks = db_tasks.objects.filter(user=request.user)
        context['stretch_usertasks'] = tasks
        context['stretch_attempts'] = attempts
    except db_attempts.DoesNotExist:
        print("stretch_stats_student(): user has no appempts at solving")
        try:
            tasks = db_tasks.objects.filter(user=request.user)
        except db_tasks.DoesNotExist:
            print("stretch_stats_student(): user has no tasks")
    context['stretch_usertasks'] = tasks
    context['stretch_attempts'] = attempts
    return render(request, 'stretch_stats_student.html', context)


def stretch_stats_teacher(request):
    context = {'adminuser': checkadmin()}
    print("stretch_stats_teacher(): call")
    print("stretch_stats_teacher(): geting a list of users")
    users = db_tasks.objects.values('user').distinct()

    tasks=[]
    attempts=[]
    if request.GET.get('user'):
        print("stretch_stats_teacher(): selected user: ",request.GET.get('user'))
        context['stretch_userselected'] = True
        context['stretch_selecteduser'] = request.GET.get('user')
        try:
            attempts = db_attempts.objects.filter(user=context['stretch_selecteduser'])
            print("stretch_stats_teacher(): geting tasks for current user: ",context['stretch_selecteduser'])
            tasks = db_tasks.objects.filter(user=context['stretch_selecteduser'])
            context['stretch_usertasks'] = tasks
            context['stretch_attempts'] = attempts
        except db_attempts.DoesNotExist:
            print("stretch_stats_teacher(): user has no appempts at solving")
            try:
                tasks = db_tasks.objects.filter(user=context['stretch_selecteduser'])
            except db_tasks.DoesNotExist:
                print("stretch_stats_teacher(): user has no tasks")
    context['stretch_usertasks'] = tasks
    context['stretch_attempts'] = attempts
    context['users'] = users
    return render(request, 'stretch_stats_teacher.html', context)


def stretch_tasks(request):
    context = {'adminuser': checkadmin()}
    print("stretch_tasks(): call")
    print("stretch_tasks(): geting a list of tasks")
    context['stretch_tasks'] = db_tasks.objects.values('id').distinct()
    if request.GET.get('task'):
        print("stretch_tasks(): selected task: ",request.GET.get('task'))
        context['stretch_taskselected'] = True
        context['stretch_task'] = db_tasks.objects.get(id=request.GET.get('task'))
    return render(request, 'stretch_tasks.html', context)




def checkadmin():
    return True

