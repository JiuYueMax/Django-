from django.urls import path
from .views import *

urlpatterns = [
    # 首页
    path('index/', index),

    # 用户列表
    path('userlist/',user_list,name='userList'),

    # 用户详情
    path('userdetail/<int:uid>',user_detail,name='userDetail'),

    # 用户详情,传递多个参数
    path('user_ab_view/<int:a>/<int:b>',user_ab_view,name='userDetail2'),

    path('user_ba_view/<int:a>/<int:b>',user_ba_view,name='userDetail2'),

    # 重定向
    path('user_cc_view/',user_cc_view),

]