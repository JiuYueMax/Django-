from django.db import models

# Create your models here.
# 出版社
class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=20)
    website = models.URLField()
    def __str__ (self):
        return self.name

# 数据迁移：
#    python manage.py makemigrations
#    python manage.py migrate