from django.shortcuts import render
from rest_framework.generics import ListAPIView
from API.serializers import ArticleSerializer ,StudentSerializer, StudentArticleSerializer 
from API.models import Article , StudentRegister, StudentArticle
from rest_framework.response import Response




# Create your views here.

class ArticleListView(ListAPIView):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        article = Article.objects.all()
        return article

    # def get(self, request):
    #     queryset = self.get_queryset()
    #     serializer = ArticleSerializer(queryset, many=True)
    #     return Response(serializer.data)


class StudentListView(ListAPIView):
    serializer_class = StudentSerializer
    def get_queryset(self):
        student = StudentRegister.objects.all()
        return student 
    


class StudentArticleAPIView(ListAPIView):
    serializer_class = StudentArticleSerializer

    def get_queryset(self):
        data = StudentArticle.objects.all()
        return data
    
# class HostelArticleAPIView(ListAPIView):
#     serializer_class = HostelSerializer


