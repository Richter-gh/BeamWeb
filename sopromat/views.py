from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

def index(request):
    context = {'s': "davaidavai"}
    return render(request, 'main.html', context)
