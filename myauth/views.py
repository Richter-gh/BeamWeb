from django.shortcuts import render
import logging
# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
from django.conf.urls.static import static
from django.conf import settings
from datetime import datetime
from django.db import models
import sys
import os, os.path
from myauth.models import user as User

def register(request):
    print("register(): register function called")
    if request.method=='POST':
        user = User()
        user.username=request.POST.get('username')
        user.password=request.POST.get('password')
        user.permission=request.POST.get('permission')
        user.save()
        return render(request, 'login.html', context)
    context = {'adminuser': ""}
    return render(request, 'register.html', context)

def login(request):
    context = {'adminuser': ""}
    if request.method=='POST':
        usr = User.objects.get(name=request.POST.get('username'))
        if usr.password==request.POST.get('password'):
            return render(request, 'login.html', context)
    return render(request, 'login.html', context)

def logout(request):
    context = {'adminuser': ""}
    return render(request, 'logout.html', context)

