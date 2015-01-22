from django.shortcuts import render
import logging
# Create your views here.
from sopromat_beam.models import beam_tasks as db_tasks, beam_attempts as db_attempts
from django.http import HttpResponse
from django.template import RequestContext
from sopromat_python.classes import BeamTask, Drawing
from django.conf.urls.static import static
from django.conf import settings
from datetime import datetime
from django.db import models
import sys, traceback
import os, os.path

from decimal import *
getcontext().prec = 4
log = logging.getLogger(__name__)


def index(request):
    context = {'adminuser': checkadmin()}
    return render(request, 'main.html', context)


def beam(request):
    context = {'adminuser': checkadmin()}
    return render(request, 'beam_main.html', context)


def beam_tester(request):
    context = {'adminuser': checkadmin()}
    # if request.method == 'POST':
    if db_tasks.objects.all().count() > 0:
        context['beam_usertasks'] = [i for i in range(1, db_tasks.objects.latest('id').id + 1)]
    if request.method == 'GET':
        if request.GET.get('task'):
            if request.GET.get('task') == 'new':
                print("beam_tester(): new task get request")
                while True:
                    try:
                        beam_task = BeamTask()
                        print("beam_tester(): creating task")
                        beam_task.generate()
                        print("beam_tester(): task created")
                        print(beam_task.text)
                        print("beam_tester(): solving")
                        beam_task.solve()
                        break
                    except:
                        print("beam_tester(): smth went wrong when creating task")
                        print("beam_tester(): Unexpected error:", sys.exc_info()[0])

                context['beam_tasktext'] = beam_task.text
                context['beam_taskgiven'] = True
                print("beam_tester(): taskgiven=", context['beam_taskgiven'])
                print("beam_tester(): getting last id in db")
                unique_id = 0
                if db_tasks.objects.all().count() == 0:
                    unique_id = 1
                else:
                    unique_id = db_tasks.objects.latest('id').id + 1
                context['beam_taskid'] = unique_id
                print("beam_tester(): id=", unique_id)
                print("beam_tester(): getting image")
                getBeamImg(beam_task.beam, unique_id)
                request.session['taskid'] = unique_id
                context['beam_image'] = 'beam_' + str(unique_id) + ".png"
                context['beam_imagelink'] = context['beam_image']
                print("beam_tester(): inserting in database")
                tsk = db_tasks()
                tsk.id = unique_id
                tsk.date = datetime.now()
                tsk.text = str(beam_task.text)
                tsk.answerM = beam_task.answerM
                tsk.answerQ = beam_task.answerQ
                tsk.user = str(request.user.username or "AnonymousUser")
                tsk.imagelink = context['beam_imagelink']
                context['beam_Q'] = beam_task.answerQ
                context['beam_M'] = beam_task.answerM
                tsk.save()
                print("beam_tester(): done inserting")
            elif request.GET.get('task').isdigit():
                print("beam_tester(): old task get request")
                context['beam_taskgiven'] = True
                context['beam_taskid'] = int(request.GET.get('task'))
                print("beam_tester(): id =", context['beam_taskid'])
                print("beam_tester(): getting task from db")
                tsk = db_tasks.objects.get(id=context['beam_taskid'])
                request.session['taskid'] = tsk.id
                context['beam_tasktext'] = tsk.text
                print('beam_tester(): taskgiven=', str(context['beam_taskgiven']))
                # print("beam_tester(): text =",tsk.text)
                print("beam_tester(): Q =", tsk.answerQ)
                print("beam_tester(): M =", tsk.answerM)
                context['beam_Q'] = tsk.answerQ
                context['beam_M'] = tsk.answerM
        if request.GET.get('answer'):
            print("beam_tester(): answers request")
            print(type(request.session['taskid']))
            task = db_tasks.objects.get(id=request.session['taskid'])
            context['beam_tasktext'] = task.text
            if request.GET.get('Q').isdigit() and (abs(float(request.GET.get('Q')) - float(task.answerQ)) <= 0.1):
                context['beam_answerQ'] = 'correct'
            else:
                context['beam_answerQ'] = 'wrong'
            if request.GET.get('M').isdigit() and (abs(float(request.GET.get('M')) - float(task.answerM)) < 0.1):
                context['beam_answerM'] = 'correct'
            else:
                context['beam_answerM'] = 'wrong'
            context['sub_q'] = request.GET.get('Q')
            context['sub_m'] = request.GET.get('M')
            print("beam_tester(): inserting solve attempt")
            print("beam_tester(): getting last id in db")
            unique_id = 0
            if db_attempts.objects.all().count() == 0:
                unique_id = 1
            else:
                unique_id = db_attempts.objects.latest('id').id + 1
            if request.session['taskid']:
                context['beam_taskgiven'] = True
                context['beam_taskid'] = request.session['taskid']
            tsk = db_attempts()
            tsk.id = unique_id
            tsk.date = datetime.now()
            tsk.answerM = context['beam_answerM']
            tsk.taskid = task.id
            tsk.answerQ = context['beam_answerQ']
            tsk.user = str(request.user.username or "AnonymousUser")
            tsk.save()
            print("beam_tester(): done inserting")

    return render(request, 'beam_tester.html', context)


def getBeamImg(beam, taskid):
    d = Drawing()
    img = d.drawBeam(beam, taskid)
    print("getBeamImg(): saving image")
    img.save(os.path.join(settings.BASE_DIR, "static/") + "beam_" + str(taskid) + ".png", "PNG")
    print("getBeamImg(): image saved to", os.path.join(settings.BASE_DIR, "static/") + "beam_" + str(taskid) + ".png")


def beam_stats_student(request):
    context = {'adminuser': checkadmin()}
    print("beam_stats_student(): call")
    print("beam_stats_student(): geting attempts for current user:",request.user)
    tasks=[]
    attempts=[]
    try:
        attempts = db_attempts.objects.filter(user=request.user)
        print("beam_stats_student(): geting tasks for current user: ",request.user)
        tasks = db_tasks.objects.filter(user=request.user)
        context['beam_usertasks'] = tasks
        context['beam_attempts'] = attempts
    except db_attempts.DoesNotExist:
        print("beam_stats_student(): user has no appempts at solving")
        try:
            tasks = db_tasks.objects.filter(user=request.user)
        except db_tasks.DoesNotExist:
            print("beam_stats_student(): user has no tasks")
    context['beam_usertasks'] = tasks
    context['beam_attempts'] = attempts
    return render(request, 'beam_stats_student.html', context)


def beam_stats_teacher(request):
    context = {'adminuser': checkadmin()}
    print("beam_stats_teacher(): call")
    print("beam_stats_teacher(): geting a list of users")
    users = db_tasks.objects.values('user').distinct()

    tasks=[]
    attempts=[]
    if request.GET.get('user'):
        print("beam_stats_teacher(): selected user: ",request.GET.get('user'))
        context['beam_userselected'] = True
        context['beam_selecteduser'] = request.GET.get('user')
        try:
            attempts = db_attempts.objects.filter(user=context['beam_selecteduser'])
            print("beam_stats_teacher(): geting tasks for current user: ",context['beam_selecteduser'])
            tasks = db_tasks.objects.filter(user=context['beam_selecteduser'])
            context['beam_usertasks'] = tasks
            context['beam_attempts'] = attempts
        except db_attempts.DoesNotExist:
            print("beam_stats_teacher(): user has no appempts at solving")
            try:
                tasks = db_tasks.objects.filter(user=context['beam_selecteduser'])
            except db_tasks.DoesNotExist:
                print("beam_stats_teacher(): user has no tasks")
    context['beam_usertasks'] = tasks
    context['beam_attempts'] = attempts
    context['users'] = users
    return render(request, 'beam_stats_teacher.html', context)


def beam_tasks(request):
    context = {'adminuser': checkadmin()}
    print("beam_tasks(): call")
    print("beam_tasks(): geting a list of tasks")
    context['beam_tasks'] = db_tasks.objects.values('id').distinct()
    if request.GET.get('task'):
        print("beam_tasks(): selected task: ",request.GET.get('task'))
        context['beam_taskselected'] = True
        context['beam_task'] = db_tasks.objects.get(id=request.GET.get('task'))
    return render(request, 'beam_tasks.html', context)




def checkadmin():
    return False

