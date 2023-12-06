from django.urls import path
from API.views import ArticleListView , StudentListView, StudentArticleAPIView

urlpatterns = [
    path('article/',ArticleListView.as_view(), name='article_list'),
    path("student/",StudentListView.as_view(),name ="student_register"),
    # path('student/article/', StudentArticleAPIView.as_view(), name='student_articles'),
]
