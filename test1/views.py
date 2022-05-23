from django.shortcuts import render
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view()
def new_list(request):
    post = Post.objects.all()       # получить все новости
    serializer = PostSerializer(post, many=True)
    return Response(serializer.data)

@api_view()
def new_list(request):
    comment = Comment.objects.all()       # получить все новости
    serializer = CommentSerializer(comment, many=True)
    return Response(serializer.data)