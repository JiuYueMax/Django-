from django.urls import path
from .views import *

urlpatterns = [
    path('add/', add_person),  # 添加数据
    path('del/', del_person),  # 删除数据
    path('update/', update_person),  # 修改数据
    path('get/', get_person),  # 查询数据
    path('paginate2/<int:page>/', paginate2, name='paginate2'),
]