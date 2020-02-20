from django.shortcuts import render
from django.shortcuts import redirect
from django.db import IntegrityError
from . import models
from . import forms
import hashlib          #使用hashlib对密码进行加密


def hash_code(s, salt='macbook'):      # 加点盐
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())  # update方法只接收bytes类型
    return h.hexdigest()

# Create your views here.


def index(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    return render(request, 'login/index.html')


def login(request):
    if request.session.get('is_login', None):  # 不允许重复登录
        return redirect('/index/')
    if request.method == "POST":
        login_form = forms.UserForm(request.POST)
        message = '请检查填写的内容! '
        if login_form.is_valid():    #确保用户名和密码都不为空
            username = login_form.cleaned_data.get('username')     #这里应该是填写账号或者用户名都可
            password = login_form.cleaned_data.get('password')
            try:
                user = models.User.objects.get(username=username)
            except:
                try:
                    user = models.User.objects.get(phonenumber=username)
                except:
                    message = '用户不存在！'
                    return render(request, 'login/login.html', locals())

            if user.password == hash_code(password):
                request.session['is_login'] = True         #向session字典中写入用户状态和数据
                request.session['user_id'] = user.id
                request.session['user_name'] = user.username
                print(username, password)
                return redirect('/index/')
            else:
                message = '密码不正确!'
                return render(request, 'login/login.html', locals())
        else:
            return render(request, 'login/login.html', locals())

    login_form = forms.UserForm()
    return render(request, 'login/login.html',locals())


def register(request):
    if request.session.get('is_login', None):
        return redirect('/index/')

    if request.method == 'POST':
        register_form = forms.RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():
            phonenumber = register_form.cleaned_data.get('phonenumber')
            password1 = register_form.cleaned_data.get('password1')
            password2 = register_form.cleaned_data.get('password2')

            if password1 != password2:
                message = '两次输入的密码不同！'
                return render(request, 'login/register.html', locals())
            else:
                same_phone_user = models.User.objects.filter(phonenumber=phonenumber)
                if same_phone_user:
                    message = '手机号已被注册'
                    return render(request, 'login/register.html', locals())

                new_user = models.User()
                new_user.phonenumber = phonenumber
                new_user.password = hash_code(password1)
                new_user.save()


                return redirect('/login/')
        else:
            return render(request, 'login/register.html', locals())
    register_form = forms.RegisterForm()
    return render(request, 'login/register.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/login/")
    request.session.flush()
    # 或者使用下面的方法
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect("/login/")

