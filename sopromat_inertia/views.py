from django.shortcuts import render
import logging
# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
from sopromat_python.classes import InertiaTask, Drawing
from django.conf.urls.static import static
from django.conf import settings
from datetime import datetime
from django.db import models
import sys
import os, os.path
from decimal import *
getcontext().prec = 4

import traceback
def inertia_tester(request):
    context = {'adminuser': checkadmin()}
    # if request.method == 'POST':
    if request.method == 'GET':
        if request.GET.get('task'):
            if request.GET.get('task') == 'new':
                print("inertia_tester(): new task get request")
                while True:
                    try:
                        inertia_task = InertiaTask()
                        print("inertia_tester(): creating task")
                        inertia_task.generate()
                        print("inertia_tester(): task created")
                        print(inertia_task.text)
                        break
                    except:
                        print("inertia_tester(): smth went wrong when creating task")
                        print("inertia_tester(): Unexpected error:", sys.exc_info()[0])
                        print(traceback.format_exc())
                        break
                context['inertia_tasktext'] = inertia_task.text
                context['inertia_taskgiven'] = True
                print("inertia_tester(): taskgiven=", context['inertia_taskgiven'])

                print("inertia_tester(): getting image")
                request.session['tasktext'] = inertia_task.text

                context['inertia_image'] = 'inertia_' + str(inertia_task.data['type']) + ".png"
                context['inertia_imagelink'] = context['inertia_image']
                context['inertia_N'] = inertia_task.answerX
                context['inertia_L'] = inertia_task.answerY
                request.session['inertia_imagelink'] = context['inertia_image']
                request.session['inertia_answerX'] = inertia_task.answerX
                request.session['inertia_answerY'] = inertia_task.answerY
        if request.GET.get('answer'):
            print("inertia_tester(): answers request")
            context['inertia_tasktext'] = request.session['tasktext']
            if request.GET.get('X').isdigit() and (abs(float(request.GET.get('X')) - float(request.session['inertia_answerX'])) <= 0.1):
                context['inertia_answerX'] = 'correct'
            else:
                context['inertia_answerX'] = 'wrong'
            if request.GET.get('Y').isdigit() and (abs(float(request.GET.get('Y')) - float(request.session['inertia_answerY'])) < 0.1):
                context['inertia_answerY'] = 'correct'
            else:
                context['inertia_answerY'] = 'wrong'
            context['inertia_imagelink']=request.session['inertia_imagelink']
            context['inertia_taskgiven'] = True
            context['sub_m'] = request.GET.get('M')
            context['sub_t'] = request.GET.get('T')

    return render(request, 'inertia_tester.html', context)

def checkadmin():
    return True

