import os
import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.text import slugify


def profile_picture_image_file_path(instance, filename):
    _, extension = os.path.splitext(filename)
    filename = f"{slugify(instance.title)}-{uuid.uuid4()}{extension}"

    return os.path.join("uploads/profile_pictures/", filename)


class User(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(
        upload_to=profile_picture_image_file_path, blank=True, null=True
    )
