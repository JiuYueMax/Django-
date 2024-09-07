from django.shortcuts import render, HttpResponse
from .models import *
from django.http import JsonResponse

# 一对一
# 增删改：和一对多是类似的
def addUser(request):
    list = []
    card1 = IDCard.objects.create(idcard_num="130925199304023456", address="河北省沧州市")
    card2 = IDCard.objects.create(idcard_num="130925199201023441", address="河北省黄骅市")
    user1 = User.objects.create(name="张晓明",age=20,sex=True,idcard=card1)
    user2 = User.objects.create(name="王岚",age=23,sex=True,idcard=card2)
    print(card1)
    print(card2)
    print(user1)
    print(user2)
    list.append(card1)
    list.append(card2)
    list.append(user1)
    list.append(user2)

    return HttpResponse("添加成功")

# 查询
def get(request):
    try:
        # 查找某用户的身份证信息
        user = User.objects.get(pk=1)
        print(user)  # 对象
    except User.DoesNotExist:
        # 如果用户不存在，打印消息
        print("未查询到用户")
        return HttpResponse("未查询到用户", status=404)

    # 查找身份证对应的用户
    idcard = IDCard.objects.get(pk=4)
    print(idcard.user)  # 对象

    return HttpResponse(idcard)

