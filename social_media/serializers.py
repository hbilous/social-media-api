from rest_framework import serializers

from social_media.models import Post, Like, Comment


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id", "content", "created_at", "media", "user")


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ("id", "post", "user", "created_at")


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("id", "content", "post", "user")
