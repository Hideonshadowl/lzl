from django.db import models
from .myvalidators import *

class bloginfo(models.Model):

    title = models.CharField(max_length=32)

    content = models.TextField(max_length=2000)

    author=models.CharField(max_length=32)
    lable=models.CharField(max_length=32)
class Author(models.Model):
    username=models.CharField(unique=True,max_length=22)
    password=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)

class Comments(models.Model):
    authorname=models.ForeignKey('Author',on_delete=False)
    content=models.TextField(max_length=2000)
    blogid=models.CharField(max_length=32)



