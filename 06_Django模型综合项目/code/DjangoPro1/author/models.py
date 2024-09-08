from django.db import models

# 作 者
class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    gender = models.BooleanField(default=True)
    def __str__(self):
        return self.first_name + self.last_name
    def get_gender_display(self):
        if self.gender:
            return '男'
        else:
            return '女'
# 数据迁移：
#    python manage.py makemigrations
#    python manage.py migrate