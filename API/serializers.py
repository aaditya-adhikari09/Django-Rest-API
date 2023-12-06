from rest_framework import serializers
from API.models import Article , StudentRegister, StudentArticle

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['name','content']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentRegister
        fields =["name","student"]

class StudentArticleSerializer(serializers.ModelSerializer):
    article = ArticleSerializer()
    student = StudentSerializer()
    class Meta:
        model = StudentArticle
        fields = '__all__'


# class HostelSerializer(serializers.ModelSerializer):
#     student = ArticleSerializer()

