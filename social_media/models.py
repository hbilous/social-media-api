import os
import uuid

from django.db import models
from django.utils.text import slugify

from user.models import User


def post_image_image_file_path(instance, filename):
    _, extension = os.path.splitext(filename)
    filename = f"{slugify(instance.title)}-{uuid.uuid4()}{extension}"

    return os.path.join("uploads/post_images/", filename)


class Post(models.Model):
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    media = models.ImageField(
        upload_to=post_image_image_file_path, blank=True, null=True
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")


class Like(models.Model):
    created_at = models.DateTimeField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes")


class Comment(models.Model):
    created_at = models.DateTimeField()
    content = models.CharField(max_length=255)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
