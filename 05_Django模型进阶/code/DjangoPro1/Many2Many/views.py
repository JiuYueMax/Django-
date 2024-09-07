from django.shortcuts import render,HttpResponse
from .models import *

# Create your views here.

# 多对多

# 添加数据
def add(request):
    # 添加user
    # for i in range(1,10):
    #     User.objects.create(name=f'张三{i}',age = i)
    # Movie.objects.create(name="人民的名义",duration=190)
    # Movie.objects.create(name="第三十二条",duration=200)
    # Movie.objects.create(name="热辣滚烫",duration=220)
    # Movie.objects.create(name="多啦A梦",duration=190)
    # Movie.objects.create(name="迪迦奥特曼",duration=180)
    # Movie.objects.create(name="祝你幸福",duration=150)
    # Movie.objects.create(name="一雪前耻",duration=200)
    # Movie.objects.create(name="重生",duration=209)
    # Movie.objects.create(name="黑神话·悟空")
    user = User.objects.get(name='张三1')
    movie = Movie.objects.get(name='热辣滚烫')

    #第一种方式添加收藏
    #user.movies.add(movie) #用户收藏电影
    movie.user_set.add(user)

    return HttpResponse("添加成功")

# 删除数据
def delelte_user(request):
    # 删除用户,这个删除后，会吧中间表一块删掉
    # User.objects.filter(pk=6).delete()

    # 删除电影,这个删除后，会吧中间表一块删掉
    # Movie.objects.filter(pk=8).delete()

    #删除中间表
    user = User.objects.get(name='张三5')
    user.movies.remove(Movie.objects.get(name='祝你幸福'))

    return HttpResponse("删除成功")

# 查询数据
def get_user_movies(request):
    # 获取用户收藏的所有电影
    user = User.objects.get(name='张三1')
    user_movies = user.movies.all();
    print(user_movies)
    movie_list = []
    for movie in user_movies:
        movie_list.append(movie.name)
    print(movie_list)


    # 获取电影被安歇用户收藏了
    movie = Movie.objects.get(id=4)
    users = movie.user_set.all();
    print(users)

    return HttpResponse("查询完成")