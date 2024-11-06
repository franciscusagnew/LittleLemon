from django.urls import path
from .views import *

urlpatterns = [
    # http://127.0.0.1:8000/restaurant
    path('', index, name='home'),
]