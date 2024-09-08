from .models import *
from django.urls import path
from .views import *


urlpatterns = [
    path('author_detail/<int:id>', author_detail, name='author_detail'),
]