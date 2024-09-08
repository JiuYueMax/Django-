from django.db import models

# Create your models here.
# 出版社
class Publisher(models.Model):
    name = models.CharField(max_length=30, verbose_name='出版社名称')
    address = models.CharField(max_length=100, verbose_name='地址')
    city = models.CharField(max_length=30, verbose_name='城市')
    state_province = models.CharField(max_length=30, verbose_name='省份')
    country = models.CharField(max_length=20, verbose_name='国家')
    website = models.URLField(verbose_name='网址')
    def __str__ (self):
        return self.name

# 数据迁移：
#    python manage.py makemigrations
#    python manage.py migrate