from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import  render, redirect, reverse
from .models import *

# 首页
def index(request):
    return render(request, 'index.html')

# 用户列表
def user_list(request):
    # 获取所有用户
    users = User1.objects.all()
    print(users)

    return render(request,'user_list.html',{'users':users})

# 用户详情
def user_detail(request,uid):
    print('uid:', uid)
    user = User1.objects.get(pk=uid)
    print(user)
    return render(request,'user_detail.html',{'user':user})

# 多个参数
def user_ab_view(request, a, b):
    return HttpResponse(f'a:{a} - b:{b}')

# 要和路由中的参数名一致，名字对应赋值
def user_ba_view(request, b, a):
    return HttpResponse(f'a:{a} - b:{b}')


# 重定向
def user_cc_view(request):
    # return redirect('http://www.ifeng.com')
    # return redirect('/user/userlist/')
    # return redirect('/user/userdetail/2')

    # 反向解析
    # return redirect(reverse('APPX:userList'))
    # return redirect(reverse('APPX:userDetail',args=(1,))) # 位置参数传参
    return redirect(reverse('APP:userDetail', kwargs={'uid': 2}))  # 关键字传参












