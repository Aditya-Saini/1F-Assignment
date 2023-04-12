"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from core import views as core_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', core_views.UserRegisterationAPIView.as_view(), name='user_register'),
    path('login/', core_views.MyTokenObtainPairView.as_view(), name='user_login'),
    path('request-count/', core_views.RequestCounterAPIView.as_view(), name='request_count'),
    path('request-count/reset/', core_views.RequestCounterResetAPIView.as_view(), name='request_count_reset'),
    path('', include("movie.urls"), name="movie"),
]
