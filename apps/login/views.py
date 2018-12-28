
from django.shortcuts import render,reverse,redirect

from django.http import HttpResponse

from modelfile import tools

# Create your views here.



def login(request):
    if request.method == 'GET':
        return render(request,'login/login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        login = tools.Login(username=username, password=password)()
        return redirect(reverse(login))
        if login == 'hirer' :
            return red
        if login == 'employer' :
            return HttpResponse('欢迎被雇佣者')

        return HttpResponse('用户名或密码错误')

