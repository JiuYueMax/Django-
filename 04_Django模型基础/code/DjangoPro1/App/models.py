from datetime import datetime

from django.db import models

# Create your models here.

class User(models.Model):
    # uid 会成为主键,原来的id不会创建
    uid = models.AutoField(auto_created=True, primary_key=True)
    # db_index 索引
    name = models.CharField(max_length=30,unique=True, db_index=True)
    age = models.IntegerField(default=18)
    sex = models.BooleanField(default=True)
    # null=True 表示可以为空, blank 在Admin管理页面可以为空
    info = models.TextField(null=True, blank=True)
    # FloatField：小数
    salary = models.FloatField(default=10000.455)
    # DecimalField: 十进制小数；max_digits：最大长度;decimal_places=2;小数点后是2为
    money = models.DecimalField(max_digits=4,decimal_places=2)
    #
    birthday = models.DateField(default='2000-01-01')
    # auto_now 每一次修改后都会为最新的时间
    updateTime = models.DateTimeField(auto_now=True)
    # 第一次添加数据的时间,以后不会再修改
    createTime = models.DateTimeField(auto_now_add=True)

    #文件和图片
    icon = models.FileField(null=True, upload_to='static/uploads')
    icon2 = models.ImageField(null=True, upload_to='static/uploads')


    def __str__(self):
        return "id:%s,姓名:%s,年龄:%s" % (self.uid,self.name, self.age)


# 增删改查
class PersonModel(models.Model):
    name = models.CharField(max_length=30, unique=True)
    age = models.IntegerField(default=18)

    class Meta:
        # 表名
        db_table = 'tb_person'

    def __str__(self):
        return f'{self.id}-{self.name}-{self.age}'

    def __repr__(self):
        return f'用户ID:{self.id},姓名:{self.name},年龄:{self.age}'





# ORM: 对象关系映射
#  模型类  =>  表结构
#  类属性  =>  表字段
#  一个对象  =>  表示中的一条数据


# 数据迁移：
#    python manage.py makemigrations
#    python manage.py migrate

# python -m pip install Pillow -i https://pypi.douban.com/simple

