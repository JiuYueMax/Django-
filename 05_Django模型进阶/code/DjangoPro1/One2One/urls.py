from django.urls import path
from .views import *

urlpatterns = [
    path('get/', get),
    path('addUser/', addUser),
]
