from django.db import models


# 身份证
class IDCard(models.Model):
    idcard_num = models.CharField(max_length=18, unique=True)
    address = models.CharField(max_length=200)
    def __str__(self):
        return f'身份证号:{self.idcard_num};地址:{self.address}'

# 用户
class User(models.Model):
    name = models.CharField(max_length=30, unique=True)
    age = models.IntegerField(default=18)
    sex = models.BooleanField(default=True)
    # 一对一关系
    idcard = models.OneToOneField(IDCard, on_delete=models.PROTECT)

    def get_sex_display(self):
        if self.sex:
            return '男'
        else:
            return '女'

    def __str__(self):
        return f'姓名:{self.name};年龄:{self.age},性别:{self.get_sex_display()}; 身份证号:{self.idcard.idcard_num};地址:{self.idcard.address}'

# 数据迁移：
#    python manage.py makemigrations
#    python manage.py migrate