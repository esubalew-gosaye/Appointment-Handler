from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('fill_date/', fill_date, name='fill_date'), 
]
