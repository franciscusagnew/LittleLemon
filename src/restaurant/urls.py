from django.urls import path
# from .views import sayHello, index
from . import views

urlpatterns = [
    # http://127.0.0.1:8000/restaurant/
    # path('', sayHello, name='sayHello')
    path('', views.index, name='home')
]