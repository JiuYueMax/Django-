from django.db import models

# 模型Model <==> 表结构
# 类属性    <==> 表字段
# 对象      <==> 表的一行记录
class User(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField(default=18)   # 对应的SQL: age int defalut 18
    sex = models.CharField(max_length=20)   # 对应的SQL: sex varchar(20)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return "姓名:%s,年龄:%s,性别:%s" % (self.name, self.age, self.sex)

# 注意：
# 数据迁移：models表结构一旦改变就需要重新数据迁移
# 迁移的概念: 就是将模型映射到数据库的过程
# 生成迁移文件:  python manage.py makemigrations
# 执行迁移:  python manage.py migrate