from django.shortcuts import render,HttpResponse

from .models import *

def detail(request,id):
    if id is None:
        return HttpResponse('ID不可为空')
    try:
        publisher = Publisher.objects.get(pk=id)
    except Exception as e:
        return HttpResponse('未找到相关数据')
    json = {'publisher':publisher}
    return render(request, 'publisher/publisher_detail.html',json)
