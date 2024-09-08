from django.shortcuts import render

from .models import *

def author_detail(request,id):
    author = Author.objects.get(pk=id)
    json = {'author':author}
    return render(request,'author/author_detail.html',json)
