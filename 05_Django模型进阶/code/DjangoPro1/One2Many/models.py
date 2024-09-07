from django.db import models

# 1对多 = 1：N
# 用户类型 ： 用户 = 1：N
#   一种用户类型：可以有多个用户
#   一个用户：只属于一个用户类型


# 用户类型
class UserType(models.Model):
    name = models.CharField(max_length=30)


# 用户
class User(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField(default=18)
    # 外键
    # user_type = models.ForeignKey(UserType, on_delete=models.CASCADE)  # 级联删除
    # user_type = models.ForeignKey(UserType, on_delete=models.PROTECT)  # 保护模式
    # user_type = models.ForeignKey(UserType, on_delete=models.SET_NULL, null=True)  # 置空模式
    # user_type = models.ForeignKey(UserType, on_delete=models.SET_DEFAULT, default=1)  # 置默认值
    # user_type = models.ForeignKey(UserType, on_delete=models.DO_NOTHING)  # 报错FOREIGN KEY constraint failed

    # related_name: 关联名称, 设置反向查找的名称，原本使用user_set改为users
    user_type = models.ForeignKey(UserType, on_delete=models.PROTECT,
                                  related_name='users',  # 建议使用
                                  )
    def __str__(self):
        return f'用户ID:{self.id},姓名:{self.name},年龄:{self.age},段位:{self.user_type.name}'
# on_delete参数主要有以下几个可选值：
#     models.CASCADE  默认值(Django1.11)，表示级联删除，即删除UserType时，相关联的User也会被删除。
#     models.PROTECT	保护模式， 阻止级联删除。
#     models.SET_NULL	置空模式，设为null，null=True参数必须具备
#     models.SET_DEFAULT 置默认值 设为默认值，default参数必须具备
#     models.SET()	删除的时候重新动态指向一个实体访问对应元素，可传函数
#     models.DO_NOTHING   什么也不做。
# 注意: 修改on_delete参数之后需要重新同步数据库，如果使用


# 数据迁移：
#    python manage.py makemigrations
#    python manage.py migrate