from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View

from rest_framework.views import APIView
from rest_framework.response import Response

class InfoView(View):
    """
    info 相关接口
    FBV（function base views） 基于函数的视图，就是在视图里使用函数处理请求。
    CBV（class base views） 基于类的视图，就是在视图里使用类处理请求。
    
    
    """
    def get(self,request,*args,**kwargs):
        data = [
            {"id": 1, "title": "zhengjinglewodegae", "content": "......"},
            {"id": 2, "title": "zhengjinglewodegae", "content": "......"},
            {"id": 3, "title": "zhengjinglewodegae", "content": "......"},
            {"id": 4, "title": "zhengjinglewodegae", "content": "......"}
        ]
        return JsonResponse(data, safe= False)
    # def post(self,request,*args,**kwargs):
    #     pass
    # def put(self,request,*args,**kwargs):
    #     pass
    # def delect(self,request,*args,**kwargs):
    #     pass


class DrfInfoView(APIView):
    """
    info 相关接口
    FBV（function base views） 基于函数的视图，就是在视图里使用函数处理请求。
    CBV（class base views） 基于类的视图，就是在视图里使用类处理请求。
    
    
    """
    def get(self,request,*args,**kwargs):
        data = [
            {"id": 1, "title": "zhengjinglewodegae", "content": "......"},
            {"id": 2, "title": "zhengjinglewodegae", "content": "......"},
            {"id": 3, "title": "zhengjinglewodegae", "content": "......"},
            {"id": 4, "title": "zhengjinglewodegae", "content": "......"}
        ]
        return Response(data)
    # def post(self,request,*args,**kwargs):
    #     pass
    # def put(self,request,*args,**kwargs):
    #     pass
    # def delect(self,request,*args,**kwargs):
    #     pass








# def info(request):
#     if request.method == 'GET':
#         data = [
#             {"id": 1, "title": "zhengjinglewodegae", "content": "......"},
#             {"id": 2, "title": "zhengjinglewodegae", "content": "......"},
#             {"id": 3, "title": "zhengjinglewodegae", "content": "......"},
#             {"id": 4, "title": "zhengjinglewodegae", "content": "......"}
#         ]

#         return JsonResponse(data, safe= False)









# def info(request):
#     return HttpResponse("Hello world")

# def info(request):
#     # 默认只接受字典
#     if request.method == "GET":
#         data = [
#             {"id": 1, "title": "zhengjinglewodegae", "content": "......"},
#             {"id": 2, "title": "zhengjinglewodegae", "content": "......"},
#             {"id": 3, "title": "zhengjinglewodegae", "content": "......"},
#             {"id": 4, "title": "zhengjinglewodegae", "content": "......"}
#         ]
#
#         return JsonResponse(data, safe=False)
from api import models
class DrfCategoryView(APIView):
    
    def post(self,request,*args,**kwargs):
        """
        访问这个 url 就会 
        增加分类
        获取请求
        """
       
        name = request.POST.get('name')# 拿数据
        # name = 'IT'
        models.Category.objects.create(name=name)
        return Response('success')