from django.shortcuts import render
from django.http import HttpResponse
# 写视图函数
def index(request):

    # 返回相应的response
    return HttpResponse('hello jiuyue')
