"""
URL configuration for littlelemon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from restaurant.views import UserViewSet, BookingView, MenuItemsView, AuthToken
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
# http://127.0.0.1:8000/api/users/
router.register(r'users', UserViewSet, basename='user')
# http://127.0.0.1:8000/api/bookings/
router.register(r'bookings', BookingView, basename='bookings')
# http://127.0.0.1:8000/api/menu/
router.register(r'menu', MenuItemsView, basename='menu')

urlpatterns = [
    # http://127.0.0.1:8000/admin/
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    # http://127.0.0.1:8000/api-auth/login/
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # http://127.0.0.1:8000/restaurant/
    path('restaurant/', include('restaurant.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    # http://127.0.0.1:8000/api/registration/
    path('api/registration/', obtain_auth_token),
    # path('api-token-auth/', AuthToken.as_view()),
]
