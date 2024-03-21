from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from .models import Post, Like, Comment
from user.models import User
from .serializers import PostSerializer


class PostAPITestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="test@example.com", password="Test12345"
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.post_data = {"content": "Test post content"}

    def test_create_post(self):
        url = reverse("social_media:post-list")
        response = self.client.post(url, self.post_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(Post.objects.get().content, "Test post content")

    def test_like_post(self):
        post = Post.objects.create(content="Test post content", user=self.user)
        url = reverse("social_media:like-list")
        data = {"post": post.id}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Like.objects.count(), 1)
        self.assertEqual(Like.objects.get().post, post)

    def test_comment_post(self):
        post = Post.objects.create(content="Test post content", user=self.user)
        url = reverse("social_media:comment-list")
        data = {"content": "Test comment", "post": post.id}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Comment.objects.count(), 1)
        self.assertEqual(Comment.objects.get().post, post)

    def test_get_post_list(self):
        url = reverse("social_media:post-list")
        response = self.client.get(url)
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_post_detail(self):
        post = Post.objects.create(content="Test post content", user=self.user)
        url = reverse("social_media:post-detail", args=[post.id])
        response = self.client.get(url)
        serializer = PostSerializer(post)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
