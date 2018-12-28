from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hirer(request):
    return HttpResponse('欢迎雇佣者')