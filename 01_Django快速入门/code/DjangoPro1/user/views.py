from django.shortcuts import render
from django.http import HttpResponse

from .models import *

# 写视图函数
def index(request):

    # 返回相应的response
    # return HttpResponse('hello jiuyue')

    # 还有一种返回方式:渲染模版render,渲染html
    return render(request,'index.html')

def index2(request):
    # 返回相应的response
    return HttpResponse('hello jiuyue')

def get_all_user(request):
    users = User.objects.all();
    # 返回相应的response
    json = {'users':users}
    return render(request,'users.html',json)

