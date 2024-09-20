import json

from django.shortcuts import render,HttpResponse
from .models import *


# Create your views here.
# 书籍首页
def book_index(request):
    return render(request, 'book/book_index.html')

def book_list(request):
    list = Book.objects.all();
    print(list)
    json = {'books': list}
    return render(request, 'book/book_list.html',json)

def book_detail(request,book_id):
    if book_id is None:
        return HttpResponse('书籍ID为空')
    try:
        book = Book.objects.get(id=book_id)
    except Exception as e:
        return HttpResponse('未查询到相关数据')
    json = {'book':book}
    print(book)
    return render(request, 'book/book_detail.html',json)

def book_detail2(request):
    book_id = request.POST.get('book_id')

    # django rest framework

    byte_str = request.body
    string = byte_str.decode('utf-8')
    type_data = json.loads(string)
    print(type_data)
    if book_id is None:
        return HttpResponse('书籍ID为空')
    return HttpResponse("成功")