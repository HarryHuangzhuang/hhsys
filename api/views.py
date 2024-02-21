from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from . import views

def info(request):
    return HttpResponse("Hello world")

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
