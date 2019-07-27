"""DietRegimen_master URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from app01 import views
urlpatterns = [

    path('login/', views.login),
    # path('register/', views.register),
    # path('find-password/', views.find_password),
    # path('search/', views.search),
    # path('photo/', views.photo),
    # path('home/', views.home),
    # path('changefood/', views.changefood),
    # path('single/', views.single),
    # path('recipe/', views.recipe),
    # path('recipe-detail/', views.recipe_detail),
    # path('mine/', views.mine),
    # path('history/', views.history),
    # path('collection/', views.collection),
    # path('quit/', views.quit)
]
