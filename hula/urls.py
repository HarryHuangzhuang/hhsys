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
    path('info/', views.InfoView.as_view()),
    # 遵循restful 规范
    path('drf/info/', views.DrfInfoView.as_view()),
    path('drf/category/', views.DrfCategoryView.as_view()),
    path('drf/category/<int:pk>/', views.DrfCategoryView.as_view()),
    path('new/category/', views.NewCategoryView.as_view()),
    path('new/category/<int:pk>/', views.NewCategoryView.as_view()),

    #get 获取列表
    #post 增加数据
    path('drf/article/', views.ArticleView.as_view()),
    path('drf/article/<int:pk>/', views.ArticleView.as_view()),

    path('new/article/', views.NewArticleView.as_view()),
    path('new/article/<int:pk>/', views.NewArticleView.as_view()),
    path('page/article/', views.PageArticleView.as_view()),
    

    # get 获取
    # post 添加
    # put 更新
    # delete 删除
]
