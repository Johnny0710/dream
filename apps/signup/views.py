from django.shortcuts import render,redirect,reverse

from django.http import HttpResponse

from modelfile import tools
# Create your views here.

def signup(request):
    if request.method == 'GET':
        return render(request,'signup/signup.html')
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        re_password = request.POST.get('re_password')

        if not password == re_password:
            return '重复密码不正确'

        nickname = request.POST.get('nickname')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        identity = int(request.POST.get('identity'))

        sign = tools.SignUp(username=username,
                            password=password,
                            name=name,
                            email=email,
                            phone=phone,
                            identity=identity,
                            nickname=nickname)

        if sign():
            # 注册成功跳转到登录页面
            return redirect(reverse('login'))
        else:
            # 注册失败,跳转到注册页面
            return redirect(reverse('signup'))