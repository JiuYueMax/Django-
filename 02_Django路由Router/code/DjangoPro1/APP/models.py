from django.db import models

# Create your models here.
class User1(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    def __str__(self):
        return "姓名:%s,年龄:%s" % (self.name, self.age)


# 数据迁移：
#    python manage.py makemigrations
#    python manage.py migrate