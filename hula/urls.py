"""
URL configuration for hula project.

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
from django.urls import path
from django.contrib import admin
from api import views 
urlpatterns = [
    path("admin/", admin.site.urls),
    path(r'info/', views.InfoView.as_view()),
    # 遵循restful 规范
    path(r'drf/info/', views.DrfInfoView.as_view()),
    path(r'drf/category/', views.DrfCategoryView.as_view()),
    # get 获取
    # post 添加
    # put 更新
    # delete 删除
]
