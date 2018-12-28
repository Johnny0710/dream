from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def employer(request):
    return HttpResponse('欢迎被雇佣者')