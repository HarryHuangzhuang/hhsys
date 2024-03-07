from rest_framework import serializers
from api import models
class Articleserializers(serializers.ModelSerializer):
    category_text = serializers.CharField(source = 'category.name',required = False)
    x1 = serializers.SerializerMethodField()

# 当要显示status_choices 的内容时 要用 get_status_display
    
    status_txt = serializers.CharField(source = 'get_status_display',required = False)
    x2 = serializers.SerializerMethodField()
    class Meta:
        model = models.Article
        fields = ['id','title','summary','content','category_id','category_text','x1','status','status_txt','x2']
        # depth = 1
    def get_x1(self,obj):
        return obj.category.name 
    
    def get_x2(self,obj):
        return obj.get_status_display()

class NewArticleserializers(serializers.ModelSerializer):
    tag_info = serializers.SerializerMethodField()
    class Meta:
        model = models.Article
        
        # fields = "__all__"
        fields = ['title','summary','tag_info']
        # depth = 1
    def get_tag_info(self,obj):
        return [row for row in obj.tag.all().values('id','title')]

class FormNewArticleserializers(serializers.ModelSerializer):
    class Meta:
        model = models.Article
        
        fields = "__all__"
