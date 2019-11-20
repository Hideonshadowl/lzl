import datetime
import hashlib
from .serializer import *
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
import re
import json
from .models import *
from django.db.models import Q


class LoginView(APIView):
    def post(self,request):
        author = request.data['phone']
        print(author)
        # print(Author.objects.filter(username=author))
        # if Author.objects.filter(username=author):
        #     return Response(data={"msg":'用户已存在'})
        # authors = AuthorModelSerializers(data=request.data)
        # if authors.is_valid():
        #     authors.save()
        #     return Response(authors.data)
        return Response(data={"msg":'用户已存在'})


class RelLoginView(APIView):
    def get(self,request):
        user = request.GET.get("username")
        pw = request.GET.get("pw")
        print(user)
        old_user = Author.objects.filter(username=user)
        if not old_user:
            return Response(data={"msg": '无该用户'})
        psd=Author.objects.filter(pw=pw)
        if not psd:
            return Response(data={"msg": '密码不一致'})
        Authors = AuthorModelSerializers(old_user, many=True)
        return Response(Authors.data)


class BlogView(APIView):
    def get(self, request):
        author = request.GET.get("author")
        blog_list = bloginfo.objects.filter(lable='public')
        blogs = bloginfoModelSerializers(blog_list, many=True)
        return Response(blogs.data)
    def post(self, request):
        blogs = bloginfoModelSerializers(data=request.data)
        if blogs.is_valid():
            blogs.save()
            return Response(blogs.data)
        return Response(blogs.errors)
    def delete(self,request):
        id = request.GET.get("id")
        bloginfo.objects.filter(id=id).delete()
        return Response()

    def put(self, request):
        pk=request.data['id']
        content=request.data['content']
        title=request.data['title']
        blog_obj = bloginfo.objects.filter(id=pk).first()
        blog_obj.title = title
        blog_obj.content=content
        blog_obj.save()
        return Response(data={"msg": '修改成功'})


class BlogView2(APIView):
    def get(self, request):
        author = request.GET.get("author")
        print(author)
        blog_list = bloginfo.objects.filter(Q(lable='private') & Q(author=author))
        blogs = bloginfoModelSerializers(blog_list, many=True)
        return Response(blogs.data)
    def delete(self,request):
        title = request.GET.get("title")
        bloginfo.objects.filter(title=title).delete()
        return Response()
