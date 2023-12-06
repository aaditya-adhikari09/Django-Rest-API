from django.urls import path ,include
from django.contrib import admin
from .views import CompanyListView
from rest_framework import routers


urlpatterns =[
path("company/",CompanyListView.as_view(),name ="company_list"),
]