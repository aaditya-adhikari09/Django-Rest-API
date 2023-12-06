from django.db import models

# Create your models here.

class Article(models.Model):
    name = models.CharField(max_length=100)
    content = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

class StudentRegister(models.Model):
    name = models.CharField(max_length=200)
    student = models.CharField(max_length = 300)
    roll_no = models.CharField(max_length=300)
    Class = models.CharField(max_length=20)
    address = models.CharField(max_length=30)

class StudentArticle(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    student = models.ForeignKey(StudentRegister, on_delete=models.CASCADE)
    other = models.CharField(max_length=100)

class Hostel(models.Model):
    student = models.ForeignKey(StudentRegister,on_delete=models.PROTECT)
    name = models.ForeignKey(Article, on_delete=models.PROTECT)
