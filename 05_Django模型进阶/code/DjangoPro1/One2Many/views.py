from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q

from .models import *


# 一对多关系

# 添加数据
def add_user(request):
    # 给UserType添加数据
    # user_type = ['青铜','白银','黄金','钻石','星耀','王者']
    # for name in user_type:
    #     UserType.objects.create(name=name)

    for i in range(10,30):
        save_user = User()
        save_user.name = f'张三-{i}'
        save_user.age =i
        save_user.user_type_id = i % 6 +1
        save_user.save()
    return HttpResponse('添加成功')


# 删除数据
def delete_user(request):
    User.objects.filter(pk=1).delete()
    UserType.objects.filter(pk=5).delete()
    return HttpResponse('删除成功')


# 修改数据
def edit_user(request):
    User.objects.filter(pk=2).update(name='哈哈')
    return HttpResponse('修改成功')

# 查询数据
def get_user(request):
    # 正向查询:从User表去查找UserType
    # user = User.objects.get(id=2)
    # print(user.name,user.age,user.user_type_id)
    # print(user.user_type.name, user.user_type.id)
    # print('-' * 60)

    # 反向查询
    # utype = UserType.objects.get(pk=2)
    # print(utype.id, utype.name)  # UserType自己的属性
    # user_set: 内部自动会生成的属性，可以让你反向查询到所有User集合
    # print(type(utype.user_set))  # RelatedManager 关联的管理器对象
    # 输出:<class 'django.db.models.fields.related_descriptors.create_reverse_many_to_one_manager.<locals>.RelatedManager'>
    # print(utype.user_set.all())  # 查询集 QuerySet
    # print('-' * 60)

    # 在filter中还可以这么用
    # 比如:查找用户类型名称为’白银‘的所有用户
    # users = User.objects.filter(user_type=UserType.objects.get(name='白银'))
    # users = User.objects.filter(user_type_id=4) # 传入user_type_id
    # users = User.objects.filter(user_type__name='王者')  # 传入UserType对象的name属性作为条件
    # print("users:",users)
    # print('-' * 60)

    # related_name：关联名称
    utype = UserType.objects.get(pk=6)
    # print(utype.user_set.all())  # 报错，使用了related_name就不可以在使用带_set的属性
    print(utype.users.all())
    return HttpResponse('查询完成')











