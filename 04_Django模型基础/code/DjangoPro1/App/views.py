import math

from django.db.models import Max, Min, Sum, Avg, Count
from django.shortcuts import render, HttpResponse
from django.db.models import Q

# 导入models
from .models import *




# 增加数据
def add_person(request):
    # 方式1
    # try:
    #     p = PersonModel()
    #     p.name = '李四'
    #     p.age = 44
    #     p.save()  # 同步到数据库表中
    # except Exception as e:
    #     return HttpResponse('添加失败')
    #
    # return HttpResponse('添加成功!')

    # 方式2
    # try:
    #     p = PersonModel(name='王五', age=55)
    #     p.save()  # 同步到数据库表中
    # except Exception as e:
    #     return HttpResponse('添加失败')
    #
    # return HttpResponse('添加成功!')

    # 方式3
    # try:
    #     PersonModel.objects.create(name='赵六', age=66)
    # except Exception as e:
    #     return HttpResponse('添加失败')
    #
    # return HttpResponse('添加成功!')

    # 方式4
    # try:
    #     ret = PersonModel.objects.get_or_create(name='钱七', age=77)
    #     print('ret:', ret)
    #     # ret: (<PersonModel: PersonModel object (5)>, True)
    #     # 如果是第一次创建：则是True，如果已经存在则是False
    #
    # except Exception as e:
    #     return HttpResponse('添加失败')

    # 添加多条数据
    for i in range(21, 100):
        PersonModel.objects.create(name=f'武{i}范', age=i)

    return HttpResponse()


# 删除数据
def del_person(request):
    # 删除数据:
    #  1. 先找到要删除的数据
    #  2. 然后删除
    try:
        # 删除一条数据
        # p = PersonModel.objects.first()  # 第一条数据
        # p.delete()

        # 删除多条数据
        #int1 = PersonModel.objects.filter(age__gt=15).delete()  # age>15的多条数据
        int2 = PersonModel.objects.filter(id=161).delete()
        #print(int1)
        print(int2)

    except Exception as e:
        return HttpResponse('删除失败!')

    return HttpResponse('删除成功!')


# 修改数据
def update_person(request):
    # 修改数据
    #  1. 先找到要修改的数据
    #  2. 然后修改
    try:
        # 修改一条数据
        # p = PersonModel.objects.first()
        # p.age = 666
        # # p.save()  # 同步到数据库表中
        # p.save(update_fields=['age'])  # 指定更新的字段，提高更新效率
        p = PersonModel.objects.get(id=7)
        print(p)
        p.name = "hahaha"
        p.age = 30
        p.save()

        # 修改多条数据
        # PersonModel.objects.all().update(age=100)

    except Exception as e:
        return HttpResponse('修改失败！')

    return HttpResponse('修改成功！')


# 查询数据
def get_person(request):
    # p = PersonModel.objects.get(id=162)
    # print(p, type(p))  # PersonModel对象
    #persons = PersonModel.objects.all()
    #persons = PersonModel.objects.filter()
    #print("persons:", persons)
    #print("list(persons):", list(persons))  # 将查询集强制转换成列表
    query = Q(name="hahaha") & Q(age=30)
    p = PersonModel.objects.filter(query)
    if not p:
        return HttpResponse('没有查询到')
    print(p)

    persons = PersonModel.objects.filter(age__in=[100, 200, 666, 777, 888])  # in
    # exclude(): 排除，取反的意思
    persons = PersonModel.objects.exclude(age__in=[100, 200, 666, 777, 888])  # not in
    persons = PersonModel.objects.filter(age__contains='6')  # 包含, 模糊查找，类似like
    persons = PersonModel.objects.filter(name__contains='3')  # 包含, 模糊查找，类似like
    persons = PersonModel.objects.filter(name__icontains='3')  # 包含, 模糊查找，类似like
    persons = PersonModel.objects.filter(name__regex='^wu')  # 正则匹配，姓武的
    persons = PersonModel.objects.filter(name__iregex='^wu')  # 正则匹配，忽略大小写
    # persons = PersonModel.objects.filter(age__range=[200, 400])  # 200-400之间，两边都包含

    persons = PersonModel.objects.filter(name__startswith='wu')  # 以wu开头，忽略大小写
    persons = PersonModel.objects.filter(name__istartswith='wu')  # 以wu开头，忽略大小写
    persons = PersonModel.objects.filter(name__endswith='wu')  # 以wu结尾，忽略大小写
    persons = PersonModel.objects.filter(name__iendswith='wu')  # 以wu结尾，忽略大小写
    print(persons)

    # 聚合函数：max,min,sum
    result = PersonModel.objects.aggregate(Max('age'))  # 最大值  {'age__max': 666}
    result = PersonModel.objects.aggregate(Min('age'))  # 最小值  {'age__min': 100}
    result = PersonModel.objects.aggregate(Sum('age'))  # 求和  {'age__sum': 1666}
    result = PersonModel.objects.aggregate(Avg('age'))  # 平均值  {'age__avg': 333.2}
    result = PersonModel.objects.aggregate(Count('age'))  # 计数  {'age__count': 5}
    print(result)

    # 排序
    persons = PersonModel.objects.all().order_by('age')  # 升序
    persons = PersonModel.objects.all().order_by('age', '-id')  # 先按照age升序，如果age相同则按id降序排列
    persons = PersonModel.objects.all().order_by('-age')  # 降序
    print(persons)

    return HttpResponse(p)


# 分页功能
# 手动分页
def paginate(request, page=1):
    # 页码：page
    # 每页数量：per_page
    per_page = 10

    # 分页功能：
    #  数据 =【1,2,3,4,5,...,100】
    #   第几页       数据范围       数据下标范围      切片
    #   page=1        1 ~ 10      0 ~ 9        [0 : 10]
    #   page=2       11 ~ 20     10 ~ 19       [10 : 20]
    #   page=3       21 ~ 30     20 ~ 29       [20 : 30]
    #   page=4       31 ~ 40     30 ~ 39       [30 : 40]
    #   ...
    #   page=n                        [(n-1) * 10  :  n * 10]
    #   page=page                     [(page-1) * per_page  :  page * per_page]

    # 实现分页功能
    persons = PersonModel.objects.all()
    persons = persons[(page-1) * per_page  :  page * per_page]

    # 总页数
    total = PersonModel.objects.count()  # 总数据量
    total_page = math.ceil(total / per_page)  # 总页数
    pages = range(1, total_page+1)  # 1,2,3,4,5,6,7...

    data = {'persons': persons,'pages': pages}
    return render(request, 'paginate.html', data)


# 分页器：自动分页
from django.core.paginator import Paginator

def paginate2(request, page=1):
    per_page = 10
    all_data = PersonModel.objects.all()

    #分页器
    paginator = Paginator(all_data, per_page)
    persons = paginator.page(page)
    pages = paginator.page_range
    data = {'persons':persons,'pages':pages}
    return render(request,'paginate2.html',data)




