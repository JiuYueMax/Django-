from .models import *
from django.urls import path
from .views import *


urlpatterns = [
    path('index/', book_index),
    path('list/', book_list,name='list'),
    path('book_detail/<int:book_id>', book_detail,name="detail"),
]