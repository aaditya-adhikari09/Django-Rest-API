from django.shortcuts import render
from rest_framework.generics import ListAPIView
from CompanyApi.serializeers import CompanySerializer
from CompanyApi.models import Company
from rest_framework.response import Response
# Create your views here.
from rest_framework import viewsets
from .models import Company
# 
# from .serializers import Compa nySerializer


class CompanyListView(ListAPIView):
   serializer_class  = CompanySerializer 

   def get_queryset(self):
       company = Company.objects.all()
       return company
   

   