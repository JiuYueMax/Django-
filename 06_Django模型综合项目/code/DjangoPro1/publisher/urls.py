from .models import *
from django.urls import path
from .views import *


urlpatterns = [
    path('detail/<int:id>',detail,name='detail' ),
]