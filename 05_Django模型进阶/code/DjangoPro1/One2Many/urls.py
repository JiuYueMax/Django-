
from django.urls import path
from .views import *


urlpatterns = [
    path('add/',add_user),
    path('delUser/',delete_user),
    path('updUser/',edit_user),
    path('getUser/',get_user),

]


