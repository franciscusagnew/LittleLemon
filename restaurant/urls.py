from django.urls import path
# from .views import sayHello, index
from .views import *

urlpatterns = [
    # http://127.0.0.1:8000/restaurant/
    # path('', sayHello, name='sayHello')
    # http://127.0.0.1:8000/restaurant
    path('', index, name='home'),
]