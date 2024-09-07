from django.urls import path
from .views import *

urlpatterns = [
    path('addUser/', add),
    path('delUser/', delelte_user),
    path('get/', get_user_movies),
]
