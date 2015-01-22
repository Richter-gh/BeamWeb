from django.shortcuts import render
import logging
# Create your views here.
from sopromat_twist.models import twist_tasks as db_tasks, twist_attempts as db_attempts
from django.http import HttpResponse
from django.template import RequestContext
from sopromat_python.classes import TwistTask, Drawing
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


def twist(request):
    context = {'adminuser': checkadmin()}
    return render(request, 'twist_main.html', context)


def twist_tester(request):
    context = {'adminuser': checkadmin()}
    # if request.method == 'POST':
    if db_tasks.objects.all().count() > 0:
        context['twist_usertasks'] = [i for i in range(1, db_tasks.objects.latest('id').id + 1)]
    if request.method == 'GET':
        if request.GET.get('task'):
            if request.GET.get('task') == 'new':
                print("twist_tester(): new task get request")
                while True:
                    try:
                        twist_task = TwistTask()
                        print("twist_tester(): creating task")
                        twist_task.generate()
                        print("twist_tester(): task created")
                        print(twist_task.text)
                        print("twist_tester(): solving")
                        twist_task.solve()
                        break
                    except:
                        print("twist_tester(): smth went wrong when creating task")
                        print("twist_tester(): Unexpected error:", sys.exc_info()[0])
                context['twist_tasktext'] = twist_task.text
                context['twist_taskgiven'] = True
                print("twist_tester(): taskgiven=", context['twist_taskgiven'])
                print("twist_tester(): getting last id in db")
                unique_id = 0
                if db_tasks.objects.all().count() == 0:
                    unique_id = 1
                else:
                    unique_id = db_tasks.objects.latest('id').id + 1
                context['twist_taskid'] = unique_id
                print("twist_tester(): id=", unique_id)
                print("twist_tester(): getting image")
                getTwistImg(twist_task.beam, unique_id)
                request.session['taskid'] = unique_id
                context['twist_image'] = 'twist_' + str(unique_id) + ".png"
                context['twist_imagelink'] = context['twist_image']
                print("twist_tester(): inserting in database")
                tsk = db_tasks()
                tsk.id = unique_id
                tsk.date = datetime.now()
                tsk.text = str(twist_task.text)
                tsk.answerM = twist_task.answerM
                tsk.answerT = twist_task.answerT
                tsk.user = str(request.user.username or "AnonymousUser")
                tsk.imagelink = context['twist_imagelink']
                context['twist_N'] = twist_task.answerM
                context['twist_L'] = twist_task.answerT
                tsk.save()
                print("twist_tester(): done inserting")
            elif request.GET.get('task').isdigit():
                print("twist_tester(): old task get request")
                context['twist_taskgiven'] = True
                context['twist_taskid'] = int(request.GET.get('task'))
                print("twist_tester(): id =", context['twist_taskid'])
                print("twist_tester(): getting task from db")
                tsk = db_tasks.objects.get(id=context['twist_taskid'])
                request.session['taskid'] = tsk.id
                context['twist_tasktext'] = tsk.text
                print('twist_tester(): taskgiven=', str(context['twist_taskgiven']))
                # print("twist_tester(): text =",tsk.text)
                print("twist_tester(): M =", tsk.answerM)
                print("twist_tester(): T =", tsk.answerT)
                context['twist_M'] = tsk.answerM
                context['twist_T'] = tsk.answerT
        if request.GET.get('answer'):
            print("twist_tester(): answers request")
            print(type(request.session['taskid']))
            task = db_tasks.objects.get(id=request.session['taskid'])
            context['twist_tasktext'] = task.text
            if request.GET.get('M').isdigit() and (abs(float(request.GET.get('M')) - float(task.answerM)) <= 0.1):
                context['twist_answerM'] = 'correct'
            else:
                context['twist_answerM'] = 'wrong'
            if request.GET.get('T').isdigit() and (abs(float(request.GET.get('T')) - float(task.answerT)) < 0.1):
                context['twist_answerT'] = 'correct'
            else:
                context['twist_answerT'] = 'wrong'

            context['sub_m'] = request.GET.get('M')
            context['sub_t'] = request.GET.get('T')
            print("twist_tester(): inserting solve attempt")
            print("twist_tester(): getting last id in db")
            unique_id = 0
            if db_attempts.objects.all().count() == 0:
                unique_id = 1
            else:
                unique_id = db_attempts.objects.latest('id').id + 1
            if request.session['taskid']:
                context['twist_taskgiven'] = True
                context['twist_taskid'] = request.session['taskid']
            tsk = db_attempts()
            tsk.id = unique_id
            tsk.date = datetime.now()
            tsk.answerM = context['twist_answerM']
            tsk.answerT = context['twist_answerT']
            tsk.taskid = task.id
            tsk.user = str(request.user.username or "AnonymousUser")
            tsk.save()
            print("twist_tester(): done inserting")

    return render(request, 'twist_tester.html', context)


def getTwistImg(twist, taskid):
    d = Drawing()
    img = d.drawBeam3(twist, taskid)
    BASE_DIR = settings.BASE_DIR
    print("getTwistImg(): saving image")
    img.save(os.path.join(BASE_DIR, "static/") + "twist_" + str(taskid) + ".png", "PNG")

    print("getTwistImg(): image saved to", os.path.join(BASE_DIR, "static") + "/images/twist_" + str(taskid) + ".png")


def twist_stats_student(request):
    context = {'adminuser': checkadmin()}
    print("twist_stats_student(): call")
    print("twist_stats_student(): geting attempts for current user:",request.user)
    tasks=[]
    attempts=[]
    try:
        attempts = db_attempts.objects.filter(user=request.user)
        print("twist_stats_student(): geting tasks for current user: ",request.user)
        tasks = db_tasks.objects.filter(user=request.user)
        context['twist_usertasks'] = tasks
        context['twist_attempts'] = attempts
    except db_attempts.DoesNotExist:
        print("twist_stats_student(): user has no appempts at solving")
        try:
            tasks = db_tasks.objects.filter(user=request.user)
        except db_tasks.DoesNotExist:
            print("twist_stats_student(): user has no tasks")
    context['twist_usertasks'] = tasks
    context['twist_attempts'] = attempts
    return render(request, 'twist_stats_student.html', context)


def twist_stats_teacher(request):
    context = {'adminuser': checkadmin()}
    print("twist_stats_teacher(): call")
    print("twist_stats_teacher(): geting a list of users")
    users = db_tasks.objects.values('user').distinct()

    tasks=[]
    attempts=[]
    if request.GET.get('user'):
        print("twist_stats_teacher(): selected user: ",request.GET.get('user'))
        context['twist_userselected'] = True
        context['twist_selecteduser'] = request.GET.get('user')
        try:
            attempts = db_attempts.objects.filter(user=context['twist_selecteduser'])
            print("twist_stats_teacher(): geting tasks for current user: ",context['twist_selecteduser'])
            tasks = db_tasks.objects.filter(user=context['twist_selecteduser'])
            context['twist_usertasks'] = tasks
            context['twist_attempts'] = attempts
        except db_attempts.DoesNotExist:
            print("twist_stats_teacher(): user has no appempts at solving")
            try:
                tasks = db_tasks.objects.filter(user=context['twist_selecteduser'])
            except db_tasks.DoesNotExist:
                print("twist_stats_teacher(): user has no tasks")
    context['twist_usertasks'] = tasks
    context['twist_attempts'] = attempts
    context['users'] = users
    return render(request, 'twist_stats_teacher.html', context)


def twist_tasks(request):
    context = {'adminuser': checkadmin()}
    print("twist_tasks(): call")
    print("twist_tasks(): geting a list of tasks")
    context['twist_tasks'] = db_tasks.objects.values('id').distinct()
    if request.GET.get('task'):
        print("twist_tasks(): selected task: ",request.GET.get('task'))
        context['twist_taskselected'] = True
        context['twist_task'] = db_tasks.objects.get(id=request.GET.get('task'))
    return render(request, 'twist_tasks.html', context)




def checkadmin():
    return True

