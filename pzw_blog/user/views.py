from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from django.contrib.auth import authenticate, login,logout
from user.forms import UserLoginForm,UserRegisterForm,ProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from user.models import Profile
import json

# Create your views here.

#用户登录
def user_login(request):
    if request.method == 'GET':
        return render(request, 'user/login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        res = {'code':0}
        user = authenticate(username=username,password=password)
        if user:
            login(request, user)
            res['next_url'] = '/article/article_list/'
            return JsonResponse(res)
        else:
            res['code'] =1
            res['err_msg'] = '密码错误'
            return JsonResponse(res)

#用户退出登录
def user_logout(request):
    logout(request)
    return redirect("article:article_list")

#用户注册
def user_register(request):
    if request.method == 'POST':
        user_register_form = UserRegisterForm(request.POST)
        if user_register_form.is_valid():
            new_user = user_register_form.save(commit=False)
            new_user.set_password(user_register_form.cleaned_data['password'])
            new_user.save()
            login(request, new_user)
            return redirect("article:article_list")
        else:
            return render(request,'user/register.html',{ 'user_register_form': user_register_form})
    else:
        user_register_form = UserRegisterForm()
        return render(request, 'user/register.html',{ 'user_register_form': user_register_form })

#用户修改个人资料
@login_required(login_url='/user/login/')
def profile_edit(request, id):
    user = User.objects.get(id=id)
    profile = Profile.objects.get(user_id=id)
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST,request.FILES)
        if profile_form.is_valid():
            profile_data = profile_form.cleaned_data
            if 'img' in request.FILES:
                profile.img = profile_data['img']
            profile.phone = profile_data['phone']
            profile.describe = profile_data['describe']
            profile.save()
            return redirect("user:edit", id=id)
    else:
        return render(request, 'user/edit.html',{ 'profile': profile, 'user': user })

#用户修改密码
@login_required(login_url='/user/login/')
def set_password(request,id):
    user = User.objects.get(id=id)
    old_err_msg = ''
    new_err_msg = ''
    repeat_err_msg = ''
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        repeat_password = request.POST.get('repeat_password')
        if user.check_password(old_password):
            if not new_password:
                new_err_msg = '新密码不能为空'
            elif new_password != repeat_password:
                repeat_err_msg = '两次输入密码不一致'
            else:
                user.set_password(new_password)
                user.save()
                login(request,user)
                return redirect("article:article_list")
        else:
            old_err_msg = '原密码输入错误'
    content = {'old_err_msg':old_err_msg,'new_err_msg':new_err_msg,'repeat_err_msg':repeat_err_msg}
    return render(request, 'user/set_password.html',content)


