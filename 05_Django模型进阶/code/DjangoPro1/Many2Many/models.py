from django.db import models

# 多对多
# 用户：电影 = N:M
# 一个用户可以收藏多部电影
# 一部电影可以被不同的用户收藏

# 电影
class Movie(models.Model):
    name = models.CharField(max_length=100)
    duration =models.IntegerField(default=90) #默认90min

# 用户
class User(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField(default=18)
    # 多对多关系
    movies = models.ManyToManyField(Movie)


# 数据迁移：
#    python manage.py makemigrations
#    python manage.py migrate