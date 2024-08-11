
from django.urls import path
from .views import *

# 使用子路由
urlpatterns = [
    # 路由url写法: django v1.x,v2.x
    # url(r'^index/',index),

    # v2.x, v3.x, v4.x
    path('index/', index),
    path('index2/', index2),
    path('get_all_user/', get_all_user,name='users'),
]