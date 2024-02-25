from rest_framework import serializers
from api import models
class Articleserializers(serializers.ModelSerializer):
    category_text = serializers.CharField(source = 'category.name')
    x1 = serializers.SerializerMethodField()
# 当要显示status_choices 的内容时 要用 get_status_display
    status_txt = serializers.CharField(source = 'get_status_display')
    x2 = serializers.SerializerMethodField()
    class Meta:
        model = models.Article
        fields = ['id','title','summary','content','category_id','category_text','x1','status','status_txt','x2']
        # depth = 1
    def get_x1(self,obj):
        return obj.category.name 
    
    def get_x2(self,obj):
        return obj.get_status_display()