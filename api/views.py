from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View

from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms.models import model_to_dict



from api import serializer
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

        因为遵循rest     帮助转换数据   使用了
        request 。post 不会有值
        所以
        """
        # import json
        # info_dict= json.loads(request.body)
        # 现在可以使用request.data
        # print(request.data)
        # print(request.body) # 输出原始输出 
        
        # print(request.POST)# 对原始数据进行了处理

    
        # name = request.POST.get('name')# 拿数据
        # name = 'IT'
        models.Category.objects.create(**request.data)
        return Response('success')
    def get(self,request,*args,**kwargs):
        """获取所有的文章分类"""
        pk = kwargs.get('pk')
        if not pk:
            queryset = models.Category.objects.all().values("id","name")
            data_list = list(queryset )
            return Response(data_list)
        else:
            catetgory_object = queryset = models.Category.objects.filter(id=pk).first()
            data = model_to_dict(catetgory_object)
            return Response(data)
    def delete(self,request,*args,**kwargs):
        """"delete"""
        pk = kwargs.get('pk') 
        models.Category.objects.filter(id=pk).delete()
        return Response('delete success')
    def put(self,request,*args,**kwargs):
        pk = kwargs.get('pk') 
        models.Category.objects.filter(id=pk).update(**request.data)
        return Response("更新成功")



"""  serializers 可以序列话 and 校验 """

from rest_framework import serializers
from rest_framework.generics import ListAPIView, RetrieveAPIView,CreateAPIView,DestroyAPIView

class  NewCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = "__all__"
        # fields = ['id','name'] 表示就展示 只展示 id 和 name 列

class NewCategoryView(ListAPIView, RetrieveAPIView,CreateAPIView,DestroyAPIView):
    queryset = models.Category.objects.all()
    serializer_class = NewCategorySerializer

# class NewCategoryView(APIView):
    # def get(self,request,*args,**kwargs):
    #     pk = kwargs.get('pk')
    #     if not pk:
    #         queryset = models.Category.objects.all()
    #         ser = NewCategorySerializer(instance= queryset,many = True)
    #         return Response(ser.data)
    #     else:
    #         model_object = models.Category.objects.filter(id = pk).first()
    #         ser = NewCategorySerializer(instance= queryset,many = False)
    #         return Response(ser.data)
    # def post(self,request,*args,**kwargs):
    #     ser = NewCategorySerializer(data = request.data)
    #     if ser.is_valid():
    #         ser.save()
    #         return Response(ser.data)
    #     else:
    #         return Response(ser.errors)
    # def put(self,request,*args,**kwargs):
    #     pk = kwargs.get('pk')
    #     category_object = models.Category.objects.filter(id=pk).first()
    #     ser = NewCategorySerializer(instance=category_object,data= request.data)

    #     if ser.is_valid():
    #         ser.save()
    #         return Response(ser.data)
    #     return Response(ser.errors)
    # def delete(self,request,*args,**kwargs):
    #     pk = kwargs.get('pk')
    #     models.Category.objects.filter(id = pk).delete()
    #     return Response("删除成功")




class ArticleView(APIView):
    def get(self,request,*args,**kwargs):
        queryset = models.Article.objects.all()

        ser = serializer.Articleserializers(instance=queryset,many = True)

        return Response(ser.data)
    def post(self,request,*args,**kwargs):
        ser = serializer.Articleserializers(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)
    
    

class NewArticleView(APIView):
    def get(self,request,*args,**kwargs):
        pk = kwargs.get('pk')
        if not pk:
            #实现所有数据
            queryset = models.Article.objects.all()
            ser = serializer.NewArticleserializers(instance = queryset, many = True)
            return Response(ser.data)
        #实现拿一条数据
        article_object = models.Article.objects.filter(id = pk ).first()
        ser = serializer.NewArticleserializers(instance=article_object,many = False)
        return Response(ser.data)
    
    def post(self,request,*args,**kwargs):
        ser = serializer.FormNewArticleserializers(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors) 
    def put(self,request,*args,**kwargs):
        pk = kwargs.get('pk')
     
        article_object = models.Article.objects.filter(id=pk).first()
        ser = serializer.FormNewArticleserializers(instance=article_object,data= request.data)

        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)
    def delete(self,request,*args,**kwargs):
        pk = kwargs.get('pk')
        models.Article.objects.filter(id = pk).delete()
        return Response("删除成功")
    
class PageArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Article
        fields = "__all__" 
from rest_framework.pagination import PageNumberPagination
from rest_framework.pagination import LimitOffsetPagination
class hulaLimitOffsetPagination(LimitOffsetPagination):
    # 一定要设置最大值
    max_limit =2

from rest_framework.generics import GenericAPIView
class PageArticleView(APIView):
    def get(self,request,*arg,**kargs):
        queryset = models.Article.objects.all()

        # 方式一 仅数据
        """
        page_object = PageNumberPagination()

        # 分页的的时候 要根据 request的参数 返回分野 
        result = page_object.paginate_queryset(queryset,request,self)
        # print(result) 
        ser = PageArticleSerializer(instance=result,many = True)
        return Response(ser.data)
        """

        """
        # 方式二 数据➕分页信息
        page_object = PageNumberPagination()

        # 分页的的时候 要根据 request的参数 返回分野 
        result = page_object.paginate_queryset(queryset,request,self)
        # print(result) 
        ser = PageArticleSerializer(instance=result,many = True)
        return page_object.get_paginated_response(ser.data)
        
       """
        """ 
        # 方式三  数据+部分分页信息
        page_object = PageNumberPagination()

        # 分页的的时候 要根据 request的参数 返回分野 
        result = page_object.paginate_queryset(queryset,request,self)
        # print(result) 
        ser = PageArticleSerializer(instance=result,many = True)
        return Response({'count':page_object.page.paginator.count,"result":ser.data})
        """
        page_object = LimitOffsetPagination()

        # 分页的的时候 要根据 request的参数 返回分野 
        result = page_object.paginate_queryset(queryset,request,self)
        # print(result) 
        ser = PageArticleSerializer(instance=result,many = True)
        return Response(ser.data)
    

