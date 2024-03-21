from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from .models import User, UserFollowing
from .serializers import UserSerializer, UserFollowingSerializer


class UserAPITestCase(TestCase):
    def setUp(self):
        self.user_data = {
            "email": "test@example.com",
            "password": "testpassword",
            "bio": "Test bio",
        }
        self.client = APIClient()

    def test_create_user(self):
        url = reverse("user:create")
        response = self.client.post(url, self.user_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().email, "test@example.com")

    def test_user_login(self):
        user = User.objects.create_user(
            email="test@example.com", password="testpassword"
        )
        url = reverse("user:token_obtain_pair")
        data = {"email": "test@example.com", "password": "testpassword"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)

    def test_user_profile_update(self):
        user = User.objects.create_user(
            email="test@example.com", password="testpassword"
        )
        self.client.login(email="test@example.com", password="testpassword")
        url = reverse("user:manage")
        data = {"bio": "Updated bio"}
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.get().bio, "Updated bio")


class UserFollowingAPITestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(
            email="user1@example.com", password="testpassword"
        )
        self.user2 = User.objects.create_user(
            email="user2@example.com", password="testpassword"
        )
        self.client = APIClient()
        self.client.login(email="user1@example.com", password="testpassword")

    def test_follow_user(self):
        url = reverse("user:user-following-list")
        data = {"user_id": self.user2.id}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(UserFollowing.objects.count(), 1)
        self.assertEqual(UserFollowing.objects.get().user_id, self.user1)
        self.assertEqual(UserFollowing.objects.get().following_user_id, self.user2)

    def test_unfollow_user(self):
        UserFollowing.objects.create(user_id=self.user1, following_user_id=self.user2)
        url = reverse("user:user-following-list")
        data = {"user_id": self.user2.id}
        response = self.client.delete(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(UserFollowing.objects.count(), 0)
