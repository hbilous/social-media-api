from django.shortcuts import render
from rest_framework import viewsets

from social_media.models import Post, Like, Comment
from social_media.serializers import PostSerializer, LikeSerializer, CommentSerializer


class PostViewSet(viewsets.GenericViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class LikeViewSet(viewsets.GenericViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
